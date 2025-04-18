import numpy as np
import xarray as xr

from template_project import tools
from template_project.tools import reformat_units_var


def test_reformat_units_var_sv_conversion():
    # Create a fake transport DataArray with units in m3/s
    ds = xr.Dataset(
        {
            "transport": xr.DataArray(
                data=np.array([1.0e6, 2.0e6]),
                dims=["time"],
                attrs={"units": "m^3/s", "long_name": "Volume transport"},
            ),
            "velocity": xr.DataArray(
                data=np.array([100.0, 200.0]),
                dims=["time"],
                attrs={"units": "cm/s", "long_name": "Flow velocity"},
            ),
        }
    )

    new_unit = reformat_units_var(ds, "transport")
    # Units should now be Sv
    assert new_unit == "Sv"

    new_unit = reformat_units_var(ds, "velocity")
    assert new_unit == "cm s-1"


def test_convert_units_var():
    var_values = 100
    current_units = "cm/s"
    new_units = "m/s"
    converted_values = tools.convert_units_var(var_values, current_units, new_units)
    assert converted_values == 1.0
