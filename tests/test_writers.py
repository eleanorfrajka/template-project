import numpy as np
import pandas as pd
import xarray as xr

from template_project.writers import save_dataset


def create_dummy_dataset():
    return xr.Dataset(
        {
            "mock_variable": (
                ["x"],
                np.array([1.0, 2.0, 3.0]),
                {"units": "Sv", "comment": "Mock transport"},
            )
        },
        coords={"x": [0, 1, 2]},
    )


def test_save_dataset_creates_file(tmp_path):
    ds = create_dummy_dataset()
    outfile = tmp_path / "test.nc"

    success = save_dataset(
        ds, output_file=outfile, delete_existing=True, prompt_user=False
    )
    assert success
    assert outfile.exists()


def test_save_dataset_skips_when_file_exists_and_no_delete(tmp_path):
    ds = create_dummy_dataset()
    outfile = tmp_path / "test_exists.nc"

    # First save
    save_dataset(ds, output_file=outfile, delete_existing=False, prompt_user=False)

    # Try again without delete or prompt
    success = save_dataset(
        ds, output_file=outfile, delete_existing=False, prompt_user=False
    )

    assert not success
    assert outfile.exists()


def test_save_dataset_overwrites_if_delete_existing(tmp_path):
    ds = create_dummy_dataset()
    outfile = tmp_path / "overwrite.nc"

    save_dataset(ds, output_file=outfile, delete_existing=False, prompt_user=False)
    assert outfile.exists()

    # Should overwrite without asking
    success = save_dataset(
        ds, output_file=outfile, delete_existing=True, prompt_user=False
    )
    assert success
    assert outfile.exists()


def test_save_dataset_compresses_data_vars(tmp_path):
    ds = create_dummy_dataset()
    outfile = tmp_path / "compressed.nc"

    assert save_dataset(ds, output_file=outfile, delete_existing=True)
    reopened = xr.open_dataset(outfile)
    # zlib compression is recorded in the variable's on-disk encoding.
    assert reopened["mock_variable"].encoding.get("zlib") is True


def test_save_dataset_creates_missing_parent_dir(tmp_path):
    ds = create_dummy_dataset()
    outfile = tmp_path / "nested" / "sub" / "out.nc"  # parent dirs don't exist yet

    assert save_dataset(ds, output_file=outfile)
    assert outfile.exists()


def test_compress_does_not_mutate_caller_coord_attrs(tmp_path):
    ds = create_dummy_dataset()
    ds["x"].attrs["units"] = "count"  # a coord attr the writer strips before writing
    outfile = tmp_path / "nomutate.nc"

    assert save_dataset(ds, output_file=outfile, delete_existing=True)
    # The shallow copy must leave the caller's dataset untouched.
    assert ds["x"].attrs.get("units") == "count"


def test_optimise_dtype_downcasts_float64_by_default(tmp_path):
    ds = create_dummy_dataset()  # mock_variable is float64
    outfile = tmp_path / "optimised.nc"

    assert save_dataset(ds, output_file=outfile, delete_existing=True)
    assert xr.open_dataset(outfile)["mock_variable"].dtype == np.float32


def test_optimise_dtype_can_be_disabled(tmp_path):
    ds = create_dummy_dataset()
    outfile = tmp_path / "full_precision.nc"

    assert save_dataset(
        ds, output_file=outfile, optimise_dtype=False, delete_existing=True
    )
    assert xr.open_dataset(outfile)["mock_variable"].dtype == np.float64


def test_time_and_coords_keep_full_precision(tmp_path):
    # A float TIME coordinate + a data var named "juld" that must not be downcast.
    times = pd.date_range("2020-01-01", periods=3)
    ds = xr.Dataset(
        {
            "temperature": (["TIME"], np.array([1.0, 2.0, 3.0])),
            "juld": (["TIME"], np.array([1.0e9, 2.0e9, 3.0e9])),  # seconds-since-epoch
        },
        coords={"TIME": times, "depth": np.array([10.0])},
    )
    outfile = tmp_path / "time.nc"

    assert save_dataset(
        ds, output_file=outfile, keep_dtype=["juld"], delete_existing=True
    )
    reopened = xr.open_dataset(outfile)
    # TIME stays datetime64; a coordinate stays float64; kept var stays float64;
    # the ordinary measurement is downcast.
    assert np.issubdtype(reopened["TIME"].dtype, np.datetime64)
    assert reopened["depth"].dtype == np.float64
    assert reopened["juld"].dtype == np.float64
    assert reopened["temperature"].dtype == np.float32
