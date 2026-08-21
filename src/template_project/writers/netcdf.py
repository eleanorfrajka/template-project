"""Functions for saving xarray Datasets to NetCDF files."""

from numbers import Number
from pathlib import Path

import numpy as np
import xarray as xr

from template_project.logger import log_error, log_info, log_warning
from template_project.utilities import cast_output_dtypes, get_default_data_dir


def save_dataset(
    ds: xr.Dataset,
    output_file: str | Path | None = None,
    *,
    compress: bool = True,
    complevel: int = 4,
    optimise_dtype: bool = True,
    keep_dtype: list[str] | None = None,
    delete_existing: bool = False,
    prompt_user: bool = False,
) -> bool:
    """Save a Dataset to NetCDF with optional compression and dtype optimisation.

    Dask-backed datasets stream to disk chunk-by-chunk (the data is never loaded
    into memory here), so this works for datasets larger than RAM.

    Parameters
    ----------
    ds : xarray.Dataset
        The dataset to be saved.
    output_file : str or Path, optional
        The path to the output NetCDF file. Defaults to ``<cwd>/data/test.nc``
        (via :func:`~template_project.utilities.get_default_data_dir`).
    compress : bool
        Apply lossless zlib compression to every data variable (writes NETCDF4).
        Defaults to True. When False, writes uncompressed NETCDF4_CLASSIC.
    complevel : int
        zlib compression level 1-9 (higher = smaller/slower). Defaults to 4.
    optimise_dtype : bool
        Downcast data variables to a smaller storage dtype via
        :func:`~template_project.utilities.cast_output_dtypes` (e.g. float64->float32)
        before writing. Defaults to True. Coordinates and datetime/``*time*`` variables
        are always preserved; float32 is lossy (~7 significant digits), so set this
        False — or list precision-critical variables in *keep_dtype* — when full
        precision matters.
    keep_dtype : list of str, optional
        Data-variable names to keep at full precision when ``optimise_dtype`` is True.
    delete_existing : bool
        Whether to delete the file if it already exists. Defaults to False.
    prompt_user : bool
        Whether to prompt interactively before deleting an existing file. Defaults to
        False (safe for notebooks, scripts, and CI); set True for interactive use.

    Returns
    -------
    bool
        True if the dataset was saved successfully, False otherwise.

    Based on: https://github.com/pydata/xarray/issues/3743
    """
    if output_file is None:
        output_file = get_default_data_dir() / "test.nc"
    output_path = Path(output_file)
    if output_path.exists():
        if prompt_user:
            user_input = (
                input(f"File '{output_file}' already exists. Delete it? (y/n): ")
                .strip()
                .lower()
            )
            if user_input != "y":
                log_info("File not deleted. Aborting save operation.")
                return False
            output_path.unlink()
            log_info("File '%s' deleted. Re-saving.", output_file)
        elif delete_existing:
            output_path.unlink()
            log_info("File '%s' deleted. Re-saving.", output_file)
        else:
            log_warning(
                "File '%s' already exists and delete_existing is False. "
                "Aborting save operation.",
                output_file,
            )
            return False

    # Ensure the target directory exists (mirrors the reader's data-dir handling);
    # otherwise to_netcdf fails when writing into a not-yet-created folder.
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if optimise_dtype:
        ds = cast_output_dtypes(ds, keep_dtype=keep_dtype)

    if compress:
        # zlib compression requires the NETCDF4 format (not NETCDF4_CLASSIC).
        nc_format = "NETCDF4"
        # Shallow copy: shares data buffers (no duplication of large arrays) but
        # gives independent attrs dicts, so the coord-attr edits below don't mutate
        # the caller's dataset.
        ds = ds.copy(deep=False)
        # Strip coord attributes that clash with xarray's automatic CF encoding.
        for coord in ds.coords:
            for key in ("units", "calendar"):
                ds[coord].attrs.pop(key, None)
        encoding = {var: {"zlib": True, "complevel": complevel} for var in ds.data_vars}
    else:
        nc_format = "NETCDF4_CLASSIC"
        encoding = None

    return _write_netcdf(ds, output_file, nc_format, encoding)


def _write_netcdf(
    ds: xr.Dataset,
    output_file: str | Path,
    nc_format: str,
    encoding: dict | None,
) -> bool:
    """Write *ds* to NetCDF, coercing invalid attributes to strings on TypeError."""
    valid_types = (str, Number, np.ndarray, np.number, list, tuple)
    try:
        ds.to_netcdf(output_file, format=nc_format, encoding=encoding)
    except TypeError as e:
        log_warning("%s: %s", e.__class__.__name__, e)
        for varname, variable in ds.variables.items():
            for k, v in variable.attrs.items():
                if not isinstance(v, valid_types) or isinstance(v, bool):
                    log_info(
                        "variable '%s': converting attribute '%s' (value '%s') to string.",
                        varname,
                        k,
                        v,
                    )
                    variable.attrs[k] = str(v)
        try:
            ds.to_netcdf(output_file, format=nc_format, encoding=encoding)
        except (TypeError, ValueError, OSError) as e2:
            log_error("Failed to save dataset: %s", e2)
            datetime_vars = [
                var for var in ds.variables if ds[var].dtype == "datetime64[ns]"
            ]
            log_error("Variables with dtype datetime64[ns]: %s", datetime_vars)
            float_attrs = [
                attr for attr in ds.attrs if isinstance(ds.attrs[attr], float)
            ]
            log_error("Attributes with dtype float64: %s", float_attrs)
            return False
        else:
            return True
    else:
        return True
