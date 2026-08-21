"""Tabular inspection of Dataset variables and attributes."""

from typing import Any

import xarray as xr
from pandas import DataFrame
from pandas.io.formats.style import Styler

from template_project.logger import log_info


def show_variables(data: str | xr.Dataset) -> Styler:
    """Extract variable information from a Dataset or netCDF file as a styled DataFrame.

    Parameters
    ----------
    data (str or xr.Dataset): The input data, either a file path to a netCDF file or an xarray Dataset.

    Returns
    -------
    pandas.io.formats.style.Styler: A styled DataFrame containing the following columns:
        - dims: The dimension of the variable (or "string" if it is a string type).
        - name: The name of the variable.
        - units: The units of the variable (if available).
        - comment: Any additional comments about the variable (if available).
    """
    if isinstance(data, str):
        # A file path: open with netCDF4 (the per-variable branch below reads the
        # netCDF4.Variable API — .dimensions/.units/.comment). xr.Dataset(str) would
        # try to build a dataset from the string as a mapping and raise.
        from netCDF4 import Dataset

        log_info("information is based on file: %s", data)
        dataset = Dataset(data, "r", format="NETCDF4")
        variables = dataset.variables
    elif isinstance(data, xr.Dataset):
        log_info("information is based on xarray Dataset")
        variables = data.variables
    else:
        raise TypeError("Input data must be a file path (str) or an xarray Dataset")

    info = {}
    for i, key in enumerate(variables):
        var = variables[key]
        if isinstance(data, str):
            # netCDF4.Variable: attributes via getattr, dims via .dimensions.
            dims = var.dimensions[0] if len(var.dimensions) == 1 else "string"
            units = getattr(var, "units", "")
            comment = getattr(var, "comment", "")
            standard_name = getattr(var, "standard_name", "")
            dtype = str(var.dtype)
        else:
            # xarray Variable: attributes via .attrs, dims via .dims.
            dims = var.dims[0] if len(var.dims) == 1 else "string"
            units = var.attrs.get("units", "")
            comment = var.attrs.get("comment", "")
            standard_name = var.attrs.get("standard_name", "")
            dtype = str(var.data.dtype)

        info[i] = {
            "name": key,
            "dims": dims,
            "units": units,
            "comment": comment,
            "standard_name": standard_name,
            "dtype": dtype,
        }

    vars = DataFrame(info).T

    dim = vars.dims
    dim[dim.str.startswith("str")] = "string"
    vars["dims"] = dim

    vars = (
        vars.sort_values(["dims", "name"])
        .reset_index(drop=True)
        .loc[:, ["dims", "name", "units", "comment", "standard_name", "dtype"]]
        .set_index("name")
        .style
    )

    return vars


def show_attributes(data: str | xr.Dataset) -> DataFrame:
    """Extract attribute information from a Dataset or netCDF file as a DataFrame.

    Parameters
    ----------
    data (str or xr.Dataset): The input data, either a file path to a netCDF file or an xarray Dataset.

    Returns
    -------
    pandas.DataFrame: A DataFrame containing the following columns:
        - Attribute: The name of the attribute.
        - Value: The value of the attribute.
    """
    from netCDF4 import Dataset

    if isinstance(data, str):
        log_info("information is based on file: %s", data)
        rootgrp = Dataset(data, "r", format="NETCDF4")
        attributes = rootgrp.ncattrs()

        def get_attr(key: str) -> Any:
            return getattr(rootgrp, key)
    elif isinstance(data, xr.Dataset):
        log_info("information is based on xarray Dataset")
        attributes = data.attrs.keys()

        def get_attr(key: str) -> Any:
            return data.attrs[key]
    else:
        raise TypeError("Input data must be a file path (str) or an xarray Dataset")

    info = {}
    for i, key in enumerate(attributes):
        dtype = type(get_attr(key)).__name__
        info[i] = {"Attribute": key, "Value": get_attr(key), "DType": dtype}

    attrs = DataFrame(info).T

    return attrs
