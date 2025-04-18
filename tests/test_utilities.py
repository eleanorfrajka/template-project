import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

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
        assert Path(downloaded).exists()
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
    assert utilities._is_valid_url(url) == expected


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

    with caplog.at_level("DEBUG", logger="amocarray"):
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
