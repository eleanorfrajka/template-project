import numpy as np
import xarray as xr

from template_project import processors
from template_project.processors import reformat_units_var


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
    converted_values = processors.convert_units_var(
        var_values, current_units, new_units
    )
    assert converted_values == 1.0


def test_process_normalises_units():
    ds = xr.Dataset(
        {
            "velocity": xr.DataArray(
                data=np.array([100.0, 200.0]),
                dims=["time"],
                attrs={"units": "cm/s"},
            ),
        }
    )
    out = processors.process(ds)
    # process() normalises the unit string; the input dataset is untouched.
    assert out["velocity"].attrs["units"] == "cm s-1"
    assert ds["velocity"].attrs["units"] == "cm/s"
