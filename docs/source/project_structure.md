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
├── template_project              # [core] Main Python package with scientific code
│   ├── __init__.py               # [core] Makes this a Python package
│   ├── plotters.py               # [core] Functions to plot data
│   ├── readers.py                # [core] Functions to read raw data into xarray datasets
│   ├── read_rapid.py             # [core] Example for a separate module for a specific dataset
│   ├── writers.py                # [core] Functions to write data (e.g., to NetCDF)
│   ├── tools.py                  # [core] Utilities for unit conversion, calculations, etc.
│   ├── logger.py                 # [core] Structured logging configuration for reproducible runs
│   ├── template_project.mplstyle # [core] Default plotting parameters
│   └── utilities.py              # [core] Helper functions (e.g., file download or parsing)
│
├── tests/                        # [test] Unit tests using pytest
│   ├── test_readers.py           # [test] Test functions in readers.py
│   ├── test_tools.py             # [test] Test functions in tools.py
│   ├── test_utilities.py         # [test] Test functions in utilities.py
│   └── ...
│
├── docs/                         # [docs]
│   ├── source/                   # [docs] Sphinx documentation source files
│   │   ├── conf.py               # [docs] Setup for documentation
│   │   ├── index.rst             # [docs] Main page with menus in *.rst
│   │   ├── setup.md              # [docs] One of the documentation pages in *.md
│   │   ├── template_project.rst  # [docs] The file to create the API based on docstrings
│   │   ├── ...                   # [docs] More *.md or *.rst linked in index.rst
│   │   └── _static               # [docs] Figures
│   │       ├── css/custom.css    # [docs, style] Custom style sheet for docs
│   │       └── logo.png          # [docs] logo for top left of docs/
│   └── Makefile                  # [docs] Build the docs
│
├── notebooks/                    # [demo] Example notebooks
│   ├── demo.ipynb                # [demo] Also run in docs.yml to appear in docs
│   └── ...
│
├── data/                         # [data]
│   └── moc_transports.nc         # [data] Example data file used for the template.
│
├── logs/                         # [core] Log output from structured logging
│   └── amocarray_*.log           # [core]
│
├── .github/                      # [ci] GitHub-specific workflows (e.g., Actions)
│   ├── workflows/
│   │   ├── docs.yml              # [ci] Test build documents on *pull-request*
│   │   ├── docs_deploy.yml       # [ci] Build and deploy documents on "merge"
│   │   ├── pypi.yml              # [ci] Package and release on GitHub.com "release"
│   │   └── test.yml              # [ci] Run pytest on tests/test_<name>.py on *pull-request*
│   ├── ISSUE_TEMPLATE.md         # [ci, meta] Template for issues on Github
│   └── PULL_REQUEST_TEMPLATE.md  # [ci, meta] Template for pull requests on Github
│
├── .gitignore                    # [meta] Exclude build files, logs, data, etc.
├── requirements.txt              # [meta] Pip requirements
├── requirements-dev.txt          # [meta] Pip requirements for development (docs, tests, linting)
├── .pre-commit-config.yaml       # [style] Instructions for pre-commits to run (linting)
├── pyproject.toml                # [ci, meta, style] Build system and config linters
├── CITATION.cff                  # [meta] So Github can populate the "cite" button
├── README.md                     # [meta] Project overview and getting started
└── LICENSE                       # [meta] Open source license (e.g., MIT as default)
```

The tags above give an indication of what parts of this template project are used for what purposes, where:
- `# [core]` – Scientific core logic or core functions used across the project.
<!--- `# [api]` – Public-facing functions or modules users are expected to import and use.-->
- `# [docs]` – Documentation sources, configs, and assets for building project docs.
- `# [test]` – Automated tests for validating functionality.
- `# [demo]` – Notebooks and minimal working examples for demos or tutorials.
- `# [data]` – Sample or test data files.
- `# [ci]` – Continuous integration setup (GitHub Actions).
- `# [style]` – Configuration for code style, linting, and formatting.
- `# [meta]` – Project metadata (e.g., citation info, license, README).

**Note:** There are also files that you may end up generating but which don't necessarily appear in the project on GitHub.com (due to being ignored by your `.gitignore`).  These may include your environment (`venv/`, if you use pip and virtual environments), distribution files `dist/` for building packages to deploy on http://pypi.org, `htmlcov/` for coverage reports for tests, `template_project_efw.egg-info` for editable installs (e.g., `pip install -e .`).

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

## 🤖 Automation Features

This template includes several automation features to streamline development:

### Dependabot (Dependency Updates)
- **File**: `.github/dependabot.yml`
- **Purpose**: Automatically creates PRs to update Python dependencies and GitHub Actions
- **Schedule**: Weekly on Mondays
- **To disable**: Delete `.github/dependabot.yml` or comment out the package ecosystems you don't want

### Towncrier (Automated Changelog)
- **Files**: `pyproject.toml` ([tool.towncrier] section), `changelog.d/`
- **Purpose**: Generates changelogs from fragment files
- **Usage**: Create `.md` files in `changelog.d/` describing changes, then run `towncrier build`
- **To disable**: 
  - Remove `towncrier` from `requirements-dev.txt`
  - Remove `[tool.towncrier]` section from `pyproject.toml`
  - Delete `changelog.d/` directory

### Pre-commit Hooks
- **File**: `.pre-commit-config.yaml`  
- **Purpose**: Runs code quality checks before each commit
- **To disable**: Remove the file or run `pre-commit uninstall`

**Note**: These automation features are optional but recommended for maintaining code quality and staying up-to-date with dependencies.

---

## ✅ Summary

This template is a starting point for research or open-source Python projects. It supports:
- Clean project structure
- Reproducible environments
- Easy testing
- Auto-publishing documentation
- Optional packaging for PyPI

> 💡 Use what you need. Delete what you don’t. This is your scaffold for doing good, shareable science/code.
