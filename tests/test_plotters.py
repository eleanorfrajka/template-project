import matplotlib
import numpy as np
import xarray as xr
from pandas.io.formats.style import Styler
from pandas import DataFrame

from template_project import plotters


def test_plot_monthly_transport_runs():
    # Use non-interactive backend for headless test environments
    matplotlib.use("Agg")

    time = np.arange("2000-01", "2000-04", dtype="datetime64[D]")
    data = np.random.rand(len(time))

    ds = xr.Dataset(
        {
            "moc_mar_hc10": (
                ["TIME"],
                data,
                {"units": "Sv", "long_name": "MOC strength"},
            )
        },
        coords={"TIME": time},
    )

    fig, ax = plotters.plot_monthly_transport(ds)

    assert fig is not None
    assert ax is not None
    assert ax.get_ylabel() == "MOC strength [Sv]"
    assert ax.get_title() == "RAPID 26°N - AMOC"


def test_show_variables_returns_styler():
    # Create a dummy dataset
    ds = xr.Dataset(
        {
            "moc_mar_hc10": (
                ["TIME"],
                [1.0, 2.0, 3.0],
                {
                    "units": "Sv",
                    "comment": "Test variable",
                    "standard_name": "ocean_mass_transport",
                },
            )
        },
        coords={"TIME": ["2000-01-01", "2000-01-02", "2000-01-03"]},
    )

    styled = plotters.show_variables(ds)

    assert isinstance(styled, Styler)


def test_show_attributes_returns_styler():
    # Create a dummy dataset
    ds = xr.Dataset(
        {
            "moc_mar_hc10": (
                ["TIME"],
                [1.0, 2.0, 3.0],
                {
                    "units": "Sv",
                    "comment": "Test variable",
                    "standard_name": "ocean_mass_transport",
                },
            )
        },
        coords={"TIME": ["2000-01-01", "2000-01-02", "2000-01-03"]},
    )

    # Add global attributes
    ds.attrs["title"] = "Test Dataset"
    ds.attrs["institution"] = "Example Institute"

    df = plotters.show_attributes(ds)

    assert isinstance(df, DataFrame)
