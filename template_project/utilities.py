from functools import wraps
from pathlib import Path
from typing import Callable, Dict, List, Optional, Union
from urllib.parse import urlparse

import xarray as xr
import requests

from template_project import logger
from template_project.logger import log_debug, log_error, log_info

log = logger.log


def get_default_data_dir() -> Path:
    return Path(__file__).resolve().parent.parent / "data"


def apply_defaults(default_source: str, default_files: List[str]) -> Callable:
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
            source: Optional[str] = None,
            file_list: Optional[List[str]] = None,
            *args,
            **kwargs,
        ) -> Callable:
            if source is None:
                source = default_source
            if file_list is None:
                file_list = default_files
            return func(source=source, file_list=file_list, *args, **kwargs)

        return wrapper

    return decorator


def _is_valid_url(url: str) -> bool:
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
    except Exception:
        return False


def resolve_file_path(
    file_name: str,
    source: Union[str, Path, None],
    download_url: Optional[str],
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
    if source and not _is_valid_url(source):
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
            raise FileNotFoundError(f"Failed to download {download_url}: {e}")

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
    new_attrs: Dict[str, str],
    overwrite: bool = False,
    verbose: bool = True,
) -> xr.Dataset:
    """Safely update attributes of an xarray Dataset without overwriting existing keys,
    unless explicitly allowed.

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
        if key in ds.attrs:
            if not overwrite:
                if verbose:
                    log_debug(
                        f"Attribute '{key}' already exists in dataset attrs and will not be overwritten.",
                    )
                continue  # Skip assignment
        ds.attrs[key] = value

    return ds
