# What’s in This Template Project?

> 🐍 This project is designed for a **Python-based code repository**. It includes features to help you manage, test, document, and share your code.

Below is an overview of the files and folders you’ll find in the `template-project`, along with what they do and why they’re useful. If you're new to GitHub or Python packaging, this is your orientation.

---

## 🔍 Project Structure Overview

📷 *This is what the template looks like when you clone or fork it:*

![Project directory screenshot](Screenshot%202025-04-18%20at%2010.33.52.png)

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
