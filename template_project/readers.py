from pathlib import Path
from typing import Union

import pandas as pd
import xarray as xr

from template_project import logger
from template_project.logger import log_info
from template_project.read_rapid import read_rapid

log = logger.log


def _get_reader(array_name: str):
    """Return the reader function for the given array name.

    Parameters
    ----------
    array_name : str
        The name of the observing array.

    Returns
    -------
    function
        Reader function corresponding to the given array name.

    Raises
    ------
    ValueError
        If an unknown array name is provided.

    """
    readers = {
        "rapid": read_rapid,
    }
    try:
        return readers[array_name.lower()]
    except KeyError:
        raise ValueError(
            f"Unknown array name: {array_name}. Valid options are: {list(readers.keys())}",
        )


def load_sample_dataset(array_name: str = "rapid") -> xr.Dataset:
    """Load a sample dataset for quick testing.

    Currently supports:
    - 'rapid' : loads the 'RAPID_26N_TRANSPORT.nc' file

    Parameters
    ----------
    array_name : str, optional
        The name of the observing array to load. Default is 'rapid'.

    Returns
    -------
    xr.Dataset
        A single xarray Dataset from the sample file.

    Raises
    ------
    ValueError
        If the array_name is not recognised.

    """
    if array_name.lower() == "rapid":
        sample_file = "moc_transports.nc"
        datasets = load_dataset(
            array_name=array_name,
            file_list=sample_file,
            transport_only=True,
        )
        if not datasets:
            raise FileNotFoundError(
                f"No datasets were loaded for sample file: {sample_file}",
            )
        return datasets[0]

    raise ValueError(
        f"Sample dataset for array '{array_name}' is not defined. "
        "Currently only 'rapid' is supported.",
    )


def load_dataset(
    array_name: str,
    source: str = None,
    file_list: Union[str | list[str]] = None,
    transport_only: bool = True,
    data_dir: Union[str, Path, None] = None,
    redownload: bool = False,
) -> list[xr.Dataset]:
    """Load raw datasets from a selected AMOC observing array.

    Parameters
    ----------
    array_name : str
        The name of the observing array to load. Options are:
        - 'rapid' : RAPID 26N array
    source : str, optional
        URL or local path to the data source.
        If None, the reader-specific default source will be used.
    file_list : str or list of str, optional
        Filename or list of filenames to process.
        If None, the reader-specific default files will be used.
    transport_only : bool, optional
        If True, restrict to transport files only.
    data_dir : str, optional
        Local directory for downloaded files.
    redownload : bool, optional
        If True, force redownload of the data.

    Returns
    -------
    list of xarray.Dataset
        List of datasets loaded from the specified array.

    Raises
    ------
    ValueError
        If an unknown array name is provided.

    """
    if logger.LOGGING_ENABLED:
        logger.setup_logger(array_name=array_name)

    # Use logger globally
    log = logger.log
    log_info(f"Loading dataset for array: {array_name}")

    reader = _get_reader(array_name)
    datasets = reader(
        source=source,
        file_list=file_list,
        transport_only=transport_only,
        data_dir=data_dir,
        redownload=redownload,
    )

    log_info(f"Successfully loaded {len(datasets)} dataset(s) for array: {array_name}")
    _summarise_datasets(datasets, array_name)

    return datasets


def _summarise_datasets(datasets: list, array_name: str):
    """Print and log a summary of loaded datasets."""
    summary_lines = []
    summary_lines.append(f"Summary for array '{array_name}':")
    summary_lines.append(f"Total datasets loaded: {len(datasets)}\n")

    for idx, ds in enumerate(datasets, start=1):
        summary_lines.append(f"Dataset {idx}:")

        # Filename from metadata
        source_file = ds.attrs.get("source_file", "Unknown")
        summary_lines.append(f"  Source file: {source_file}")

        # Time coverage
        time_var = ds.get("TIME")
        if time_var is not None:
            time_start = pd.to_datetime(time_var.values[0]).strftime("%Y-%m-%d")
            time_end = pd.to_datetime(time_var.values[-1]).strftime("%Y-%m-%d")
            summary_lines.append(f"  Time coverage: {time_start} to {time_end}")
        else:
            summary_lines.append("  Time coverage: TIME variable not found")

        # Dimensions
        summary_lines.append("  Dimensions:")
        for dim, size in ds.sizes.items():
            summary_lines.append(f"    - {dim}: {size}")

        # Variables
        summary_lines.append("  Variables:")
        for var in ds.data_vars:
            shape = ds[var].shape
            summary_lines.append(f"    - {var}: shape {shape}")

        summary_lines.append("")  # empty line between datasets

    summary = "\n".join(summary_lines)

    # Print to console
    print(summary)

    # Write to log
    log_info("\n" + summary)
