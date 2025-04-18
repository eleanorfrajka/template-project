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

## Project structure

template-project/
├── .github/
│   └── workflows/              # GitHub Actions for tests, docs, PyPI
├── docs/                       # Sphinx-based documentation
│   ├── source/                 # reStructuredText + MyST Markdown + _static
│   └── Makefile                # for building HTML docs
├── notebooks/                  # Example notebooks
├── template_project/           # Main Python package
│   ├── __init__.py
│   ├── _version.py
│   ├── tools.py
│   ├── readers.py
│   ├── writers.py
│   ├── utilities.py
│   ├── plotters.py
│   └── template_project.mplstyle  # Optional: matplotlib style file
├── tests/                      # Pytest test suite
│   ├── test_tools.py
│   └── test_utilities.py
├── .gitignore
├── .pre-commit-config.yaml
├── CITATION.cff                # Sample file for citable software
├── CONTRIBUTING.md             # Sample file for inviting contributions
├── LICENSE                     # Sample MIT license
├── README.md
├── pyproject.toml              # Modern packaging config
├── requirements.txt            # Package requirements
├── customisation_checklist.md  # Development requirements
└── requirements-dev.txt        # Linting, testing, docs tools


---

## 🔧 Quickstart

Install in development mode:

```bash
git clone https://github.com/eleanorfrajka/template-project.git
cd template-project
pip install -r requirements-dev.txt
pip install -e .
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

---

## Future plans

I'll also (once I know how) add instructions for how to publish the package to conda forge, so that folks who use conda or mamba for environment management can also install that way.

---

## 📣 Citation

This repository includes a `CITATION.cff` file so that users of this template can include one in their own project.  
There is no need to cite this repository directly.
