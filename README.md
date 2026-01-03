# template-project

> 🧪 A modern Python template for scientific projects — with clean code, automated tests, documentation, citation, and publication tools, ready out-of-the-box.

This repository is designed to help researchers and developers (especially in the [UHH Experimental Oceanography group](http://eleanorfrajka.com) quickly launch well-structured Python projects with consistent tooling for open science.

📘 Full documentation available at:  
👉 https://eleanorfrajka.github.io/template-project/

---

## 🚀 What's Included

- ✅ Example Python package layout: `template_project/*.py`
- 📓 Jupyter notebook demo: `notebooks/demo.ipynb`
- 📄 Markdown and Sphinx-based documentation in `docs/`
- 🔍 Tests with `pytest` in `tests/`, CI with GitHub Actions
- 🎨 Code style via `black`, `ruff`, `pre-commit`
- 📦 Package config via `pyproject.toml` + optional PyPI release workflow
- 🧾 Machine-readable citation: `CITATION.cff`

---

## Project Structure

```
template-project/
├── .github/workflows/          # CI/CD for tests, docs, PyPI
├── docs/                       # Sphinx documentation  
├── notebooks/                  # Example Jupyter notebooks
├── template_project/           # Main Python package
│   ├── tools.py
│   ├── readers.py  
│   ├── plotters.py
│   └── utilities.py
├── tests/                      # Pytest test suite
├── pyproject.toml              # Modern packaging config
├── environment.yml             # Conda environment
├── requirements.txt            # Core dependencies
├── requirements-dev.txt        # Development dependencies
└── CITATION.cff                # Academic citation
```

## Key Features

- 📦 **Modern Python packaging** with `pyproject.toml` and automated versioning
- 🧪 **Testing setup** with pytest and pre-commit hooks for code quality  
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

# Option A: Using conda/mamba (recommended)
conda env create -f environment.yml
conda activate template-project
pip install -e .

# Option B: Using pip
pip install -e ".[dev]"
```

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

## 🤝 Contributing

Contributions are welcome!  Please also consider adding an [issue](https://github.com/eleanorfrajka/template-project/issues) when something isn't clear.

See the [customisation checklist](customisation_checklist.md) to adapt this template to your own project.

For information about planned improvements and the development roadmap, see [MODERNIZATION_PLAN.md](MODERNIZATION_PLAN.md).

---

## Future plans

I'll also (once I know how) add instructions for how to publish the package to conda forge, so that folks who use conda or mamba for environment management can also install that way.

---

## 📣 Citation

This repository includes a `CITATION.cff` file so that users of this template can include one in their own project.  
There is no need to cite this repository directly.
