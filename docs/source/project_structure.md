# What’s in This Template Project?

> 🐍 This project is designed for a **Python-based code repository**. It includes features to help you manage, test, document, and share your code.

Below is an overview of the files and folders you’ll find in the `template-project`, along with what they do and why they’re useful. If you're new to GitHub or Python packaging, this is your orientation.

---

## 🔍 Project Structure Overview

📷 *This is what the template looks like when you clone or fork it:*
# 📁 `template-project` File Structure

A minimal, modular Python project structure for collaborative research and reproducible workflows.

```
template-project/
├── template_project              # Main Python package with scientific code
│   ├── __init__.py               # Makes this a Python package
│   ├── plotters.py               # Functions to plot data
│   ├── readers.py                # Functions to read raw data into xarray datasets
│   ├── read_rapid.py             # Example for a separate module for a specific dataset
│   ├── writers.py                # Functions to write data (e.g., to NetCDF)
│   ├── tools.py                  # Utilities for unit conversion, calculations, etc.
│   ├── logger.py                 # Structured logging configuration for reproducible runs
│   ├── template_project.mplstyle # Default plotting parameters
│   └── utilities.py              # Helper functions (e.g., file download, header parsing)
│
├── tests/                        # Unit tests using pytest
│   ├── test_readers.py
│   ├── test_tools.py
│   ├── test_utilities.py
│   └── ...
│
├── docs/                         # Sphinx documentation source files
│   ├── source/
│   |   ├── conf.py               # Setup for documentation
│   |   ├── index.rst             # Main page with menus in *.rst
│   |   ├── setup.md              # One of the documention pages in *.md
│   |   ├── template_project.rst  # The file to create the API based on docstrings
│   |   ├── ...                   # More *.md or *.rst linked in index.rst
│   |   └── _static               # Figures
|   |       ├── css/custom.css    # Custom style sheet
|   |       └── logo.png          # logo for top left of docs/
│   └── Makefile
│
├── notebooks/                    # Example notebooks
│   ├── demo.ipynb                # Note - this is run in .github/workflows/docs.yml to appear in index.rst as demo-output.ipynb
│   └── ...
│
├── data/                         # (Optional) Example input data or placeholder
│   └── moc_transports.nc         # Example data file used for the template.
│
├── logs/                         # Log output from structured logging
│   └── amocarray_*.log
│
├── .github/                      # GitHub-specific workflows (e.g., Actions)
│   └── workflows/
|       ├── docs.yml              # Test build documents on *pull-request*
|       ├── docs_deploy.yml       # Build and deploy documents on "merge"
|       ├── pypi.yml              # Package and release on GitHub.com "release"
│       └── test.yml              # Run pytest on tests/test_<name>.py on *pull-request*
│
├── .gitignore                    # Exclude build files, logs, data, etc.
├── requirements.txt              # Pip requirements
├── requirements-dev.txt          # Pip requirements for development (docs, tests, linting)
├── .pre-commit-config.yaml       # Instructions for pre-commits to run (linting)
├── pyproject.toml                # Build system and tool config (e.g., black, isort)
├── CITATION.cff                  # Citation info so Github can populate the "cite" button
├── README.md                     # Project overview and getting started
└── LICENSE                       # Open source license (e.g., MIT as default)
```

## 🔍 Notes

- **Modularity**: Code is split by function (reading, writing, tools).
- **Logging**: All major functions support structured logging to `logs/`.
- **Tests**: Pytest-compatible tests are in `tests/`, with one file per module.
- **Docs**: Sphinx documentation is in `docs/`.


---

## 🔰 The Basics (Always Included)

- **`README.md`** – The first thing people see when they visit your GitHub repo. Use this to explain what your project is, how to install it, and how to get started.
- **`LICENSE`** – Explains what others are allowed to do with your code. This template uses the **MIT License**:
  - ✅ Very permissive — allows commercial and private use, modification, and distribution.
  - 🔗 More license info: [choosealicense.com](https://choosealicense.com/)
- **`.gitignore`** – Tells Git which files/folders to ignore (e.g., system files, data outputs).
- **`requirements.txt`** – Lists the Python packages your project needs to run.

---

## 🧰 Python Packaging and Development

- **`pyproject.toml`** – A modern configuration file for building, installing, and describing your package (e.g. name, author, dependencies).
- **`requirements-dev.txt`** – Additional tools for developers (testing, linting, formatting, etc.).
- **`template_project/`** – Your main code lives here. Python will treat this as an importable module.
- **`pip install -e .`** – Lets you install your project locally in a way that updates as you edit files.

---

## 🧪 Testing and Continuous Integration

- **`tests/`** – Folder for test files. Use these to make sure your code works as expected.
- **`.github/workflows/`** – GitHub Actions automation:
  - `tests.yml` – Runs your tests automatically when you push changes.
  - `docs.yml` – Builds your documentation to check for errors.
  - `docs_deploy.yml` – Publishes documentation to GitHub Pages.
  - `pypi.yml` – Builds and uploads a release to PyPI when you tag a new version.

---

## 📝 Documentation

- **`docs/`** – Contains Sphinx and Markdown files to build your documentation site.
  - Run `make html` or use GitHub Actions to generate a website.
- **`.vscode/`** – Optional settings for Visual Studio Code (e.g., interpreter paths).
- **`notebooks/`** – A place to keep example Jupyter notebooks.

---

## 🧾 Metadata and Community

- **`CITATION.cff`** – Machine-readable citation info. Lets GitHub generate a "Cite this repository" button.
- **`CONTRIBUTING.md`** – Guidelines for contributing to the project. Useful if you welcome outside help.
- **`.pre-commit-config.yaml`** – Configuration for running automated checks (e.g., code formatting) before each commit.

---

## ✅ Summary

This template is a starting point for research or open-source Python projects. It supports:
- Clean project structure
- Reproducible environments
- Easy testing
- Auto-publishing documentation
- Optional packaging for PyPI

> 💡 Use what you need. Delete what you don’t. This is your scaffold for doing good, shareable science/code.
