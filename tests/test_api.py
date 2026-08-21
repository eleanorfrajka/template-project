import numpy as np
import xarray as xr

import template_project as tp


def test_verbs_exist():
    for verb in ("read", "write", "plot", "process"):
        assert callable(getattr(tp, verb))


def test_version_is_a_string():
    assert isinstance(tp.__version__, str)


def test_process_verb_delegates_to_processors():
    ds = xr.Dataset(
        {
            "velocity": xr.DataArray(
                data=np.array([1.0, 2.0]),
                dims=["time"],
                attrs={"units": "cm/s"},
            ),
        }
    )
    out = tp.process(ds)
    assert out["velocity"].attrs["units"] == "cm s-1"
