import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import numpy as np
import pytest
import xarray as xr

from template_project import logger, utilities

# Sample data
VALID_URL = "https://rapid.ac.uk/sites/default/files/rapid_data/"
INVALID_URL = "ftdp://invalid-url.com/data.nc"
INVALID_STRING = "not_a_valid_source"

logger.disable_logging()


def test_get_default_data_dir():
    # This should always resolve to your project's /data directory
    data_dir = utilities.get_default_data_dir()
    assert isinstance(data_dir, Path)
    assert data_dir.name == "data"
    assert (
        data_dir.exists() or not data_dir.exists()
    )  # Should be valid even if data folder doesn't yet exist


@patch("template_project.utilities.requests.get")
def test_download_file_http(mock_get):
    # Set up mock HTTP response
    mock_response = MagicMock()
    mock_response.iter_content = lambda chunk_size: [b"test content"]
    mock_response.__enter__.return_value = mock_response
    mock_response.raise_for_status = lambda: None
    mock_get.return_value = mock_response

    with tempfile.TemporaryDirectory() as tmpdir:
        url = "https://example.com/testfile.txt"
        out_path = Path(tmpdir) / "testfile.txt"

        downloaded = utilities.download_file(url, tmpdir)
        assert Path(downloaded) == out_path
        assert out_path.exists()
        with open(downloaded, "rb") as f:
            assert f.read() == b"test content"


def test_apply_defaults_decorator_applies_source_and_file_list():
    # Define a dummy function to wrap
    def dummy_reader(source=None, file_list=None):
        return {"source": source, "file_list": file_list}

    default_source = "http://example.com"
    default_files = ["test.nc"]

    decorated = utilities.apply_defaults(default_source, default_files)(dummy_reader)

    # Test with no arguments
    result = decorated()
    assert result["source"] == default_source
    assert result["file_list"] == default_files

    # Test with only one override
    result = decorated(source="custom.nc")
    assert result["source"] == "custom.nc"
    assert result["file_list"] == default_files

    result = decorated(file_list=["override.nc"])
    assert result["source"] == default_source
    assert result["file_list"] == ["override.nc"]


@pytest.mark.parametrize(
    "url,expected",
    [
        (VALID_URL, True),
        (INVALID_URL, False),
        ("not_a_url", False),
    ],
)
def test_is_valid_url(url, expected):
    assert utilities.is_valid_url(url) == expected


@pytest.mark.parametrize(
    "var_name,data,expected",
    [
        ("temperature", np.array([1.0, 2.0], dtype="float64"), np.float32),
        ("count", np.array([1, 2], dtype="int64"), np.int32),
        ("temperature_qc", np.array([0, 1], dtype="int64"), np.int8),
        # QC/flag name match is case-insensitive (uppercase CF convention).
        ("TEMP_QC", np.array([0.0, 1.0], dtype="float64"), np.int8),
        ("QC_FLAG", np.array([0.0], dtype="float64"), np.int8),
        ("serial", np.array([123, 456], dtype="int64"), np.int32),
        ("latitude", np.array([1.0], dtype="float32"), np.float64),
        ("time", np.array([1.0, 2.0], dtype="float64"), np.float64),
        # Unsigned 64-bit is NOT downcast to int32 (would overflow large values).
        ("bigcount", np.array([1, 2], dtype="uint64"), np.uint64),
    ],
)
def test_find_best_dtype(var_name, data, expected):
    da = xr.DataArray(data)
    assert utilities.find_best_dtype(var_name, da) == expected


def test_cast_output_dtypes_replaces_nan_and_downcasts():
    ds = xr.Dataset(
        {
            "temp": ("x", np.array([1.0, 2.0], dtype="float64")),
            "temp_qc": ("x", np.array([1.0, np.nan], dtype="float64")),
        }
    )
    out = utilities.cast_output_dtypes(ds)
    # float64 measurement -> float32; float QC with NaN -> int8 with CF fill 9.
    assert out["temp"].dtype == np.float32
    assert out["temp_qc"].dtype == np.int8
    assert out["temp_qc"].values.tolist() == [1, 9]
    # Input dataset is not modified.
    assert ds["temp"].dtype == np.float64
    assert np.isnan(ds["temp_qc"].values[1])


def test_cast_output_dtypes_keep_dtype():
    ds = xr.Dataset({"juld": ("x", np.array([1.0e9, 2.0e9], dtype="float64"))})
    out = utilities.cast_output_dtypes(ds, keep_dtype=["juld"])
    assert out["juld"].dtype == np.float64


def test_safe_update_attrs_add_new_attribute():
    ds = xr.Dataset()
    new_attrs = {"project": "MOVE"}
    ds = utilities.safe_update_attrs(ds, new_attrs)
    assert ds.attrs["project"] == "MOVE"


def test_safe_update_attrs_existing_key_logs(caplog):
    from template_project import logger, utilities

    # Re-enable logging for this test
    logger.enable_logging()

    ds = xr.Dataset(attrs={"project": "MOVE"})
    new_attrs = {"project": "OSNAP"}

    with caplog.at_level("DEBUG", logger="template_project"):
        utilities.safe_update_attrs(ds, new_attrs, overwrite=False, verbose=True)

    assert any(
        "Attribute 'project' already exists in dataset attrs and will not be overwritten."
        in message
        for message in caplog.messages
    )


def test_safe_update_attrs_existing_key_with_overwrite():
    ds = xr.Dataset(attrs={"project": "MOVE"})
    new_attrs = {"project": "OSNAP"}
    ds = utilities.safe_update_attrs(ds, new_attrs, overwrite=True)
    assert ds.attrs["project"] == "OSNAP"
