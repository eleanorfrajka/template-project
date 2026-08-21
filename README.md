# template-project

> 🧪 A modern Python template for scientific projects — with clean code, automated tests, documentation, citation, and publication tools, ready out-of-the-box.

This repository is designed to help researchers and developers (especially in the [UHH Experimental Oceanography group](http://eleanorfrajka.com) quickly launch well-structured Python projects with consistent tooling for open science.

📘 Full documentation available at:  
👉 https://eleanorfrajka.github.io/template-project/

---

## 🚀 What's Included

- ✅ Example Python package layout: verb subpackages under `src/template_project/` (src layout)
- 📓 Jupyter notebook demo: `notebooks/demo.ipynb`
- 📄 Markdown and Sphinx-based documentation in `docs/`
- 🔍 Tests with `pytest` in `tests/`, CI with GitHub Actions
- 🎨 Code style via `ruff` (lint + format), enforced by the CI `lint` job
- 📦 Package config + dependencies via `pyproject.toml` + optional PyPI release workflow
- 🧾 Machine-readable citation: `CITATION.cff`

---

## Project Structure

```
template-project/
├── .github/workflows/          # CI/CD for tests, docs, PyPI
├── docs/                       # Sphinx documentation  
├── notebooks/                  # Example Jupyter notebooks
├── src/template_project/       # Main Python package (src layout)
│   ├── readers/                #   tp.read()   — data loading (rapid.py + dispatch)
│   ├── writers/                #   tp.write()  — NetCDF output (netcdf.py)
│   ├── plotters/               #   tp.plot()   — figures + table views
│   ├── processors/             #   tp.process()— unit conversion (units.py)
│   ├── utilities.py            #   shared helpers
│   └── logger.py               #   logging config
├── tests/                      # Pytest test suite
├── pyproject.toml              # Packaging + all dependencies (extras: test/docs/dev)
├── docs/environment.yml        # Conda environment for the docs build
└── CITATION.cff                # Academic citation
```

## Key Features

- 📦 **Modern Python packaging** with `pyproject.toml` and automated versioning
- 🧪 **Testing setup** with pytest and a ruff-based CI `lint` job for code quality  
- 📚 **Documentation** with Sphinx, supporting both Markdown and reStructuredText
- 🔄 **CI/CD workflows** for automated testing, docs building, and PyPI publishing
- 📊 **Scientific Python** integration with numpy, pandas, xarray, matplotlib
- 🌍 **Environment management** with both pip and conda/mamba support


---

## 🔧 Quickstart

Install in development mode:

```bash
git clone https://github.com/eleanorfrajka/template-project.git
cd template-project

# Option A: pip (primary)
pip install -e ".[dev]"

# Option B: conda/mamba (used by the docs build)
conda env create -f docs/environment.yml
conda activate template-project
pip install -e ".[dev]"
```

All dependencies are declared in `pyproject.toml`; the `dev` extra installs the runtime,
test, docs, and tooling dependencies in one step.

To run tests:

```bash
pytest
```

To build the documentation locally:

```bash
cd docs
make html
```

---

## 📚 Learn More

- [Setup instructions](https://eleanorfrajka.github.io/template-project/setup.html)
- [Solo Git workflow](https://eleanorfrajka.github.io/template-project/gitworkflow_solo.html)
- [Fork-based collaboration](https://eleanorfrajka.github.io/template-project/gitcollab_v2.html)
- [Building docs](https://eleanorfrajka.github.io/template-project/build_docs.html)
- [Publishing to PyPI](https://eleanorfrajka.github.io/template-project/pypi_guide.html)

---

## 🛠️ Using this template

The key files to update when adapting this template to your own project:

| File | What to change |
|------|---------------|
| `pyproject.toml` | Package name, description, author, URLs, dependencies |
| `README.md` | Title, description, GitHub URLs |
| `CITATION.cff` | Author, ORCID, project title, URL |
| `docs/environment.yml` | Conda environment name |
| `docs/source/conf.py` | Project name, author, copyright |
| `src/template_project/logger.py` | Logger name (after renaming the directory) |

The fastest approach is a global find-and-replace of `template_project` → `your_package_name`
and `template-project` → `your-project-name`, then rename the `src/template_project/` directory.

See the full [customisation checklist](customisation_checklist.md) for a complete step-by-step guide.

---

## 🤝 Contributing

Contributions are welcome!  Please also consider adding an [issue](https://github.com/eleanorfrajka/template-project/issues) when something isn't clear.

---

## Future plans

I'll also (once I know how) add instructions for how to publish the package to conda forge, so that folks who use conda or mamba for environment management can also install that way.

---

## 📣 Citation

This repository includes a `CITATION.cff` file so that users of this template can include one in their own project.  
There is no need to cite this repository directly.

---

## 🙏 Acknowledgements

Portions of this project were developed with the assistance of [Claude Code](https://claude.com/claude-code), Anthropic's agentic coding tool.
