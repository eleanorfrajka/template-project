import xarray as xr
import numpy as np
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
