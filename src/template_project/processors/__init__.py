"""Data processing and unit-conversion utilities.

Public API
----------
- :func:`reformat_units_var`, :func:`convert_units_var` — unit helpers (in :mod:`.units`).
- :func:`process` — the package-level ``process`` verb; a small example that normalises
  unit strings across a Dataset. This is the extension point for a real processing
  pipeline (compare ``oceanarray.processors``).
"""

import xarray as xr

from template_project.processors.units import (
    convert_units_var,
    reformat_units_var,
    unit_conversion,
    unit_str_format,
)

__all__ = [
    "convert_units_var",
    "process",
    "reformat_units_var",
    "unit_conversion",
    "unit_str_format",
]


def process(ds: xr.Dataset) -> xr.Dataset:
    """Normalise unit strings on every variable in a Dataset (example processor).

    For each variable carrying a ``units`` attribute, rewrite it to the preferred
    string form via :func:`reformat_units_var`. Returns a copy; the input is unchanged.

    Parameters
    ----------
    ds : xr.Dataset
        Dataset whose variable ``units`` attributes should be normalised.

    Returns
    -------
    xr.Dataset
        A copy of *ds* with normalised unit strings.

    """
    ds = ds.copy()
    for var in ds.variables:
        if "units" in ds[var].attrs:
            ds[var].attrs["units"] = reformat_units_var(ds, var)
    return ds
