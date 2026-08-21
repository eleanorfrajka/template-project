"""General-purpose utilities for data handling and downloading."""

from collections.abc import Callable
from ftplib import FTP
from functools import wraps
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import numpy as np
import requests
import xarray as xr

from template_project import logger
from template_project.logger import log_debug, log_error, log_info

log = logger.log

# Byte width of a 64-bit integer; float64/int64 storage is downcast in find_best_dtype.
_INT64_NBYTES = 8


def get_default_data_dir() -> Path:
    """Return the default data directory (``./data`` under the current working directory).

    Resolved relative to the working directory rather than the installed package
    location, so downloads never land inside ``site-packages`` and the result is
    independent of the source layout (flat vs ``src/``).
    """
    return Path.cwd() / "data"


def find_best_dtype(var_name: str, da: xr.DataArray) -> type:
    """Determine the optimal storage dtype for a variable.

    Parameters
    ----------
    var_name : str
        Variable name.
    da : xr.DataArray
        Data array to inspect.

    Returns
    -------
    type
        Recommended numpy dtype.

    Notes
    -----
    Rules applied in order:

    - String / datetime / object variables: unchanged.
    - ``time`` in name: unchanged (preserve datetime64 / float encoding).
    - ``*_qc`` suffix or ``flag`` in name: ``int8`` (name match is case-insensitive).
    - ``serial_number`` or ``serial``: ``int32``.
    - ``latitude`` / ``longitude`` in name: ``float64``.
    - Signed 64-bit integer input: downsize to ``int32``; unsigned integers are left
      unchanged (``uint64`` values can exceed the ``int32`` range).
    - ``float64`` input: ``float32``.
    - Anything else: unchanged.

    """
    input_dtype = da.dtype.type
    name = var_name.lower()
    if da.dtype.kind in ("U", "S", "O", "M"):
        return input_dtype
    if "time" in name:
        return input_dtype
    if name.endswith("_qc") or "flag" in name:
        return np.int8
    if name in ("serial_number", "serial"):
        return np.int32
    if "latitude" in name or "longitude" in name:
        return np.float64
    # Only downcast *signed* int64 -> int32; uint64 values can exceed int32 range.
    if da.dtype.kind == "i" and da.dtype.itemsize == _INT64_NBYTES:
        return np.int32
    if input_dtype == np.float64:
        return np.float32
    return input_dtype


def cast_output_dtypes(
    ds: xr.Dataset, keep_dtype: list[str] | None = None
) -> xr.Dataset:
    """Cast each data variable to its optimal storage dtype for NetCDF output.

    Calls :func:`find_best_dtype` per data variable and rebuilds only those whose
    dtype changes; attributes are preserved and the input dataset is not modified.
    **Coordinates are never touched** (so a ``TIME`` coordinate keeps full precision),
    and ``find_best_dtype`` already preserves datetime and ``*time*``-named variables.

    ``float64`` -> ``float32`` is lossy (~7 significant digits). That is fine for most
    geophysical measurements but wrong for high-dynamic-range quantities where error
    accumulates (e.g. a float time axis such as "seconds since 1970"). Pass such
    variable names in *keep_dtype* to preserve their dtype.

    Parameters
    ----------
    ds : xr.Dataset
        Dataset to cast.
    keep_dtype : list of str, optional
        Data-variable names to leave at their original dtype.

    Returns
    -------
    xr.Dataset
        New dataset with optimised dtypes (or the same object if nothing changed).

    """
    keep = set(keep_dtype or ())
    updates: dict[str, xr.DataArray] = {}
    for vname in ds.data_vars:
        if vname in keep:
            continue
        var = ds[vname]
        target = find_best_dtype(vname, var)
        if np.dtype(target) == var.dtype:
            continue
        if np.issubdtype(np.dtype(target), np.integer) and np.issubdtype(
            var.dtype, np.floating
        ):
            # NaN cannot be represented as an integer; replace before casting.
            # QC/flag variables use 9 (CF "missing value"); other integer vars use 0.
            name = vname.lower() if isinstance(vname, str) else str(vname)
            fill_val = 9 if (name.endswith("_qc") or "flag" in name) else 0
            # xr.where keeps dask arrays lazy, so a larger-than-RAM dataset still
            # streams to disk chunk-by-chunk instead of being computed into memory.
            new = xr.where(np.isfinite(var), var, fill_val).astype(target)
        else:
            new = var.astype(target)
        new.attrs = dict(var.attrs)
        updates[vname] = new
    if not updates:
        return ds
    return ds.assign(updates)


def apply_defaults(default_source: str, default_files: list[str]) -> Callable:
    """Decorator to apply default values for 'source' and 'file_list' parameters if they are None.

    Parameters
    ----------
    default_source : str
        Default source URL or path.
    default_files : list of str
        Default list of filenames.

    Returns
    -------
    Callable
        A wrapped function with defaults applied.

    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(
            source: str | None = None,
            file_list: list[str] | None = None,
            *args: Any,
            **kwargs: Any,
        ) -> Callable:
            if source is None:
                source = default_source
            if file_list is None:
                file_list = default_files
            return func(*args, source=source, file_list=file_list, **kwargs)

        return wrapper

    return decorator


def is_valid_url(url: str) -> bool:
    """Validate if a given string is a valid URL with supported schemes.

    Parameters
    ----------
    url : str
        The URL string to validate.

    Returns
    -------
    bool
        True if the URL is valid and uses a supported scheme ('http', 'https', 'ftp'),
        otherwise False.

    """
    try:
        result = urlparse(url)
        return all(
            [
                result.scheme in ("http", "https", "ftp"),
                result.netloc,
                result.path,  # Ensure there's a path, not necessarily its format
            ],
        )
    except (ValueError, AttributeError):
        return False


def resolve_file_path(
    file_name: str,
    source: str | Path | None,
    download_url: str | None,
    local_data_dir: Path,
    redownload: bool = False,
) -> Path:
    """Resolve the path to a data file, using local source, cache, or downloading if necessary.

    Parameters
    ----------
    file_name : str
        The name of the file to resolve.
    source : str or Path or None
        Optional local source directory.
    download_url : str or None
        URL to download the file if needed.
    local_data_dir : Path
        Directory where downloaded files are stored.
    redownload : bool, optional
        If True, force redownload even if cached file exists.

    Returns
    -------
    Path
        Path to the resolved file.

    """
    # Use local source if provided
    if source and not is_valid_url(str(source)):
        source_path = Path(source)
        candidate_file = source_path / file_name
        if candidate_file.exists():
            log_info("Using local file: %s", candidate_file)
            return candidate_file
        else:
            log_error("Local file not found: %s", candidate_file)
            raise FileNotFoundError(f"Local file not found: {candidate_file}")

    # Use cached file if available and redownload is False
    cached_file = local_data_dir / file_name
    if cached_file.exists() and not redownload:
        log_info("Using cached file: %s", cached_file)
        return cached_file

    # Download if URL is provided
    if download_url:
        try:
            log_info("Downloading file from %s to %s", download_url, local_data_dir)
            return download_file(download_url, local_data_dir, redownload=redownload)
        except Exception as e:
            log_error("Failed to download %s: %s", download_url, e)
            raise FileNotFoundError(f"Failed to download {download_url}: {e}") from e

    # If no options succeeded
    raise FileNotFoundError(
        f"File {file_name} could not be resolved from local source, cache, or remote URL.",
    )


def download_file(url: str, dest_folder: str, redownload: bool = False) -> str:
    """Download a file from HTTP(S) or FTP to the specified destination folder.

    Parameters
    ----------
    url : str
        The URL of the file to download.
    dest_folder : str
        Local folder to save the downloaded file.
    redownload : bool, optional
        If True, force re-download of the file even if it exists.

    Returns
    -------
    str
        The full path to the downloaded file.

    Raises
    ------
    ValueError
        If the URL scheme is unsupported.

    """
    dest_folder_path = Path(dest_folder)
    dest_folder_path.mkdir(parents=True, exist_ok=True)

    local_filename = dest_folder_path / Path(url).name
    if local_filename.exists() and not redownload:
        # File exists and redownload not requested
        return str(local_filename)

    parsed_url = urlparse(url)

    if parsed_url.scheme in ("http", "https"):
        # HTTP(S) download
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(local_filename, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

    elif parsed_url.scheme == "ftp":
        # FTP download
        with FTP(parsed_url.netloc) as ftp:
            ftp.login()  # anonymous login
            with open(local_filename, "wb") as f:
                ftp.retrbinary(f"RETR {parsed_url.path}", f.write)

    else:
        raise ValueError(f"Unsupported URL scheme in {url}")

    return str(local_filename)


def safe_update_attrs(
    ds: xr.Dataset,
    new_attrs: dict[str, str],
    overwrite: bool = False,
    verbose: bool = True,
) -> xr.Dataset:
    """Safely update Dataset attributes without overwriting existing keys.

    Parameters
    ----------
    ds : xr.Dataset
        The xarray Dataset whose attributes will be updated.
    new_attrs : dict of str
        Dictionary of new attributes to add.
    overwrite : bool, optional
        If True, allow overwriting existing attributes. Defaults to False.
    verbose : bool, optional
        If True, emit a warning when skipping existing attributes. Defaults to True.

    Returns
    -------
    xr.Dataset
        The dataset with updated attributes.

    """
    for key, value in new_attrs.items():
        if key in ds.attrs and not overwrite:
            if verbose:
                log_debug(
                    f"Attribute '{key}' already exists in dataset attrs and will not be overwritten.",
                )
            continue  # Skip assignment
        ds.attrs[key] = value

    return ds
