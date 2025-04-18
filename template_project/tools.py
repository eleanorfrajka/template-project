import logging

# Initialize logging
_log = logging.getLogger(__name__)
# Various conversions from the key to units_name with the multiplicative conversion factor
unit_conversion = {
    "cm/s": {"units_name": "m/s", "factor": 0.01},
    "cm s-1": {"units_name": "m s-1", "factor": 0.01},
    "m/s": {"units_name": "cm/s", "factor": 100},
    "m s-1": {"units_name": "cm s-1", "factor": 100},
    "S/m": {"units_name": "mS/cm", "factor": 0.1},
    "S m-1": {"units_name": "mS cm-1", "factor": 0.1},
    "mS/cm": {"units_name": "S/m", "factor": 10},
    "mS cm-1": {"units_name": "S m-1", "factor": 10},
    "dbar": {"units_name": "Pa", "factor": 10000},
    "Pa": {"units_name": "dbar", "factor": 0.0001},
    "degrees_Celsius": {"units_name": "Celsius", "factor": 1},
    "Celsius": {"units_name": "degrees_Celsius", "factor": 1},
    "m": {"units_name": "cm", "factor": 100},
    "cm": {"units_name": "m", "factor": 0.01},
    "km": {"units_name": "m", "factor": 1000},
    "g m-3": {"units_name": "kg m-3", "factor": 0.001},
    "kg m-3": {"units_name": "g m-3", "factor": 1000},
}

# Specify the preferred units, and it will convert if the conversion is available in unit_conversion
preferred_units = ["m s-1", "dbar", "S m-1"]

# String formats for units.  The key is the original, the value is the desired format
unit_str_format = {
    "m/s": "m s-1",
    "cm/s": "cm s-1",
    "S/m": "S m-1",
    "meters": "m",
    "degrees_Celsius": "Celsius",
    "g/m^3": "g m-3",
    "m^3/s": "Sv",
}


def reformat_units_var(ds, var_name, unit_format=unit_str_format):
    """
    Renames units in the dataset based on the provided dictionary for OG1.

    Parameters
    ----------
    ds (xarray.Dataset): The input dataset containing variables with units to be renamed.
    unit_format (dict): A dictionary mapping old unit strings to new formatted unit strings.

    Returns
    -------
    xarray.Dataset: The dataset with renamed units.
    """
    old_unit = ds[var_name].attrs["units"]
    if old_unit in unit_format:
        new_unit = unit_format[old_unit]
    else:
        new_unit = old_unit
    return new_unit


def convert_units_var(
    var_values, current_unit, new_unit, unit_conversion=unit_conversion
):
    """
    Convert the units of variables in an xarray Dataset to preferred units.  This is useful, for instance, to convert cm/s to m/s.

    Parameters
    ----------
    ds (xarray.Dataset): The dataset containing variables to convert.
    preferred_units (list): A list of strings representing the preferred units.
    unit_conversion (dict): A dictionary mapping current units to conversion information.
    Each key is a unit string, and each value is a dictionary with:
        - 'factor': The factor to multiply the variable by to convert it.
        - 'units_name': The new unit name after conversion.

    Returns
    -------
    xarray.Dataset: The dataset with converted units.
    """
    if (
        current_unit in unit_conversion
        and new_unit in unit_conversion[current_unit]["units_name"]
    ):
        conversion_factor = unit_conversion[current_unit]["factor"]
        new_values = var_values * conversion_factor
    else:
        new_values = var_values
        print(f"No conversion information found for {current_unit} to {new_unit}")
    #        raise ValueError(f"No conversion information found for {current_unit} to {new_unit}")
    return new_values
