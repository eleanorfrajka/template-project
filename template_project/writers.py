from pathlib import Path
from numbers import Number

import numpy as np


def save_dataset(
    ds, output_file="../data/test.nc", delete_existing=False, prompt_user=True
):
    """
    Attempts to save the dataset to a NetCDF file. If a TypeError occurs due to invalid attribute values,
    it converts the invalid attributes to strings and retries the save operation.

    Parameters
    ----------
    ds (xarray.Dataset): The dataset to be saved.
    output_file (str): The path to the output NetCDF file. Defaults to 'test.nc'.
    delete_existing (bool): Whether to delete the file if it already exists. Defaults to False.
    prompt_user (bool): Whether to prompt the user before deleting an existing file. Defaults to True.

    Returns
    -------
    bool: True if the dataset was saved successfully, False otherwise.

    Based on: https://github.com/pydata/xarray/issues/3743
    """
    output_path = Path(output_file)
    if output_path.exists():
        if prompt_user:
            user_input = (
                input(f"File '{output_file}' already exists. Delete it? (y/n): ")
                .strip()
                .lower()
            )
            if user_input != "y":
                print("File not deleted. Aborting save operation.")
                return False
            output_path.unlink()
            print(f"File '{output_file}' deleted. Re-saving.")
        elif delete_existing:
            output_path.unlink()
            print(f"File '{output_file}' deleted. Re-saving.")
        else:
            print(
                f"File '{output_file}' already exists and delete_existing is False. Aborting save operation."
            )
            return False

    valid_types = (str, int, float, np.float32, np.float64, np.int32, np.int64)
    # More general
    valid_types = (str, Number, np.ndarray, np.number, list, tuple)
    try:
        ds.to_netcdf(output_file, format="NETCDF4_CLASSIC")
        return True
    except TypeError as e:
        print(e.__class__.__name__, e)
        for varname, variable in ds.variables.items():
            for k, v in variable.attrs.items():
                if not isinstance(v, valid_types) or isinstance(v, bool):
                    print(
                        f"variable '{varname}': Converting attribute '{k}' with value '{v}' to string."
                    )
                    variable.attrs[k] = str(v)
        try:
            ds.to_netcdf(output_file, format="NETCDF4_CLASSIC")
            return True
        except Exception as e:
            print("Failed to save dataset:", e)
            datetime_vars = [
                var for var in ds.variables if ds[var].dtype == "datetime64[ns]"
            ]
            print("Variables with dtype datetime64[ns]:", datetime_vars)
            float_attrs = [
                attr for attr in ds.attrs if isinstance(ds.attrs[attr], float)
            ]
            print("Attributes with dtype float64:", float_attrs)
            return False
