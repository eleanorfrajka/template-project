from pathlib import Path

from pandas import DataFrame
import matplotlib.pyplot as plt
import xarray as xr


def plot_monthly_transport(ds: xr.Dataset, var: str = "moc_mar_hc10") -> None:
    """Plot original and monthly averaged transport time series.

    Parameters
    ----------
    ds : xr.Dataset
        Dataset with a time dimension and a transport variable.
    var : str, optional
        Name of the variable to plot. Default is "moc_mar_hc10".
    """
    here = Path(__file__).resolve().parent
    plt.style.use(here / "template_project.mplstyle")

    da = ds[var]
    ds_monthly = ds.resample(TIME="ME").mean()

    fig, ax = plt.subplots()
    ax.plot(ds.TIME, da, color="grey", alpha=0.5, linewidth=0.5, label="Original")
    ax.plot(
        ds_monthly.TIME,
        ds_monthly[var],
        color="red",
        linewidth=1.0,
        label="Monthly Avg",
    )
    ax.axhline(0, color="black", linestyle="--", linewidth=0.5)

    ax.set_title("RAPID 26°N - AMOC")

    # Use variable attributes if present
    label = da.attrs.get("long_name", var)
    units = da.attrs.get("units", "")
    ax.set_ylabel(f"{label} [{units}]" if units else label)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend()
    plt.tight_layout()

    return fig, ax


def show_variables(data):
    """
    Processes an xarray Dataset or a netCDF file, extracts variable information,
    and returns a styled DataFrame with details about the variables.

    Parameters:
    data (str or xr.Dataset): The input data, either a file path to a netCDF file or an xarray Dataset.

    Returns:
    pandas.io.formats.style.Styler: A styled DataFrame containing the following columns:
        - dims: The dimension of the variable (or "string" if it is a string type).
        - name: The name of the variable.
        - units: The units of the variable (if available).
        - comment: Any additional comments about the variable (if available).
    """

    if isinstance(data, str):
        print("information is based on file: {}".format(data))
        dataset = xr.Dataset(data)
        variables = dataset.variables
    elif isinstance(data, xr.Dataset):
        print("information is based on xarray Dataset")
        variables = data.variables
    else:
        raise TypeError("Input data must be a file path (str) or an xarray Dataset")

    info = {}
    for i, key in enumerate(variables):
        var = variables[key]
        if isinstance(data, str):
            dims = var.dimensions[0] if len(var.dimensions) == 1 else "string"
            units = "" if not hasattr(var, "units") else var.units
            comment = "" if not hasattr(var, "comment") else var.comment
        else:
            dims = var.dims[0] if len(var.dims) == 1 else "string"
            units = var.attrs.get("units", "")
            comment = var.attrs.get("comment", "")

        info[i] = {
            "name": key,
            "dims": dims,
            "units": units,
            "comment": comment,
            "standard_name": var.attrs.get("standard_name", ""),
            "dtype": str(var.dtype) if isinstance(data, str) else str(var.data.dtype),
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


def show_attributes(data):
    """
    Processes an xarray Dataset or a netCDF file, extracts attribute information,
    and returns a DataFrame with details about the attributes.

    Parameters:
    data (str or xr.Dataset): The input data, either a file path to a netCDF file or an xarray Dataset.

    Returns:
    pandas.DataFrame: A DataFrame containing the following columns:
        - Attribute: The name of the attribute.
        - Value: The value of the attribute.
    """
    from netCDF4 import Dataset

    if isinstance(data, str):
        print("information is based on file: {}".format(data))
        rootgrp = Dataset(data, "r", format="NETCDF4")
        attributes = rootgrp.ncattrs()
        get_attr = lambda key: getattr(rootgrp, key)
    elif isinstance(data, xr.Dataset):
        print("information is based on xarray Dataset")
        attributes = data.attrs.keys()
        get_attr = lambda key: data.attrs[key]
    else:
        raise TypeError("Input data must be a file path (str) or an xarray Dataset")

    info = {}
    for i, key in enumerate(attributes):
        dtype = type(get_attr(key)).__name__
        info[i] = {"Attribute": key, "Value": get_attr(key), "DType": dtype}

    attrs = DataFrame(info).T

    return attrs
