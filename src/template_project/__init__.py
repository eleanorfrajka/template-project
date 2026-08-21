"""Template project for oceanographic Python packages.

Public API
----------
Verb-style convenience functions delegate to the subpackages:

    import template_project as tp
    ds = tp.read("rapid")        # -> readers.load_dataset
    tp.write(ds, "out.nc")       # -> writers.save_dataset
    tp.plot(ds)                  # -> plotters.plot_monthly_transport
    tp.process(ds)               # -> processors.process

The subpackages remain importable directly, e.g.
``from template_project.readers import load_dataset``.
"""

try:
    # Written by setuptools-scm at build time (gitignored); the live version.
    from template_project._version import __version__
except ImportError:  # pragma: no cover - source tree with no build artefact
    try:
        from importlib.metadata import PackageNotFoundError as _PNF
        from importlib.metadata import version as _v

        __version__ = _v("template-project-efw")
    except _PNF:  # pragma: no cover
        __version__ = "0.0.0"

from pathlib import Path
from typing import Any

import xarray as xr

from template_project import plotters, processors, readers, writers

__all__ = [
    "__version__",
    "plot",
    "plotters",
    "process",
    "processors",
    "read",
    "readers",
    "write",
    "writers",
]


def read(array_name: str = "rapid", **kwargs: Any) -> list[xr.Dataset]:
    """Load dataset(s) for an observing array (delegates to ``readers.load_dataset``)."""
    return readers.load_dataset(array_name, **kwargs)


def write(ds: xr.Dataset, output_file: str | Path | None = None, **kwargs: Any) -> bool:
    """Save a Dataset to NetCDF (delegates to ``writers.save_dataset``).

    ``output_file`` defaults to ``<cwd>/data/test.nc`` when omitted.
    """
    return writers.save_dataset(ds, output_file, **kwargs)


def plot(ds: xr.Dataset, **kwargs: Any) -> tuple[Any, Any]:
    """Plot monthly transport (delegates to ``plotters.plot_monthly_transport``)."""
    return plotters.plot_monthly_transport(ds, **kwargs)


def process(ds: xr.Dataset, **kwargs: Any) -> xr.Dataset:
    """Process a Dataset (delegates to ``processors.process``)."""
    return processors.process(ds, **kwargs)
