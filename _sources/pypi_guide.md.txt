# Publishing Your Project to PyPI

> 📦 PyPI (Python Package Index) is where you publish Python packages so others can install them with `pip install yourproject`.

This guide walks you through publishing your project from `template-project` to PyPI — manually or automatically using GitHub Actions.

---

## 📁 Step 1: Prepare Your Project

To publish to PyPI, your project needs:
- A `pyproject.toml` file with metadata
- A `README.md`, `LICENSE`, and version number
- A working `__init__.py` or version file

This template already includes most of what you need.

You can also follow the official tutorial:
👉 [Packaging Projects — Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

### Choosing a Build Backend

The official Python tutorial uses `hatchling`, like this:
```toml
[build-system]
requires = ["hatchling >= 1.26"]
build-backend = "hatchling.build"
```

In this template, we use `setuptools` instead:
```toml
[build-system]
build-backend = "setuptools.build_meta"
requires = [
  "setuptools>=42",
  "setuptools-scm[toml]>=3.4",
  "wheel",
]
```
This setup works well for scientific projects that use version tagging.

---

## 📝 Step 2: Edit Your Project Metadata

Update `pyproject.toml` under the `[project]` section:

Example from this template:
```toml
[project]
name = "template-project-efw"
description = "Example template project for docs, pip install and git"
readme = "README.md"
license = { file = "LICENSE" }
maintainers = [
  { name = "Eleanor Frajka-Williams", email = "eleanorfrajka@gmail.com" },
]
requires-python = ">=3.8"
classifiers = [
  "Programming Language :: Python :: 3 :: Only",
  "Programming Language :: Python :: 3.8",
  "Programming Language :: Python :: 3.9",
  "Programming Language :: Python :: 3.10",
  "Programming Language :: Python :: 3.11",
  "Programming Language :: Python :: 3.12",
]
dynamic = [
  "dependencies",
  "version",
]

[project.urls]
documentation = "https://github.com/eleanorfrajka/template-project"
homepage = "https://github.com/eleanorfrajka/template-project"
repository = "https://github.com/eleanorfrajka/template-project"
```

> 🎯 Change the `name`, `description`, `maintainers`, and URLs to match your own project.

### Versioning with `setuptools_scm`
This template uses automatic versioning from git tags. Here's the config:
```toml
[tool.setuptools_scm]
write_to = "template_project/_version.py"
write_to_template = "__version__ = '{version}'"
tag_regex = "^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$"
local_scheme = "no-local-version"
```

---

## 🛠️ Step 3: Build Your Package

Make sure you have the latest `build` module:
```bash
python3 -m pip install --upgrade build
```

Then from the project root:
```bash
python3 -m build
```
This generates a `dist/` folder with `.whl` and `.tar.gz` files.

---

## 🧪 Step 4: Test on TestPyPI

Before publishing for real, try everything out on [TestPyPI](https://test.pypi.org).

1. Create an account at [test.pypi.org/account/register](https://test.pypi.org/account/register)
2. Create an API token and store it securely
3. Install or upgrade Twine:
```bash
python3 -m pip install --upgrade twine
```
4. Upload your package:
```bash
python3 -m twine upload --repository testpypi dist/*
```
5. Install from TestPyPI:
```bash
pip install -i https://test.pypi.org/simple/ --no-deps template-project-efw
```

> ⚠️ If you see an error like:
```
Invalid distribution metadata: unrecognized or malformed field 'license-file'
```
Update your packaging tools:
```bash
pip install --upgrade packaging setuptools
```

---

## 🚀 Step 5: Upload to PyPI

When you're ready to go live:

1. Create an account at [pypi.org](https://pypi.org/account/register)
2. Generate a separate API token
3. Upload with Twine:
```bash
python3 -m twine upload dist/*
```

---

## 🤖 Optional: Automate Publishing with GitHub Actions

This template includes `.github/workflows/pypi.yml`, which:
- Builds your package
- Publishes to PyPI when you push a release tag (e.g. `v0.1.0`)

### To use it:
1. Register GitHub as a [trusted publisher](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/)
2. Push a tag:
```bash
git tag v0.1.0
git push origin v0.1.0
```
3. GitHub will run the Action to publish your package.

### ✅ Recommended GitHub + Local Release Workflow

1. **Merge your pull requests to `main`**
   - Make sure all desired changes are merged.
   - If you're working in a fork, sync with upstream `main` on GitHub.

2. **On your local machine:**
```bash
git checkout main
git pull origin main
git log -1   # Confirm you're tagging the latest commit

git tag v0.1.0   # Follow PEP 440
git push origin v0.1.0
```
> Make sure the tag is on the tip of `main` — otherwise `setuptools_scm` may think you're ahead and bump the version (e.g. `0.1.0.dev1`).

3. **On GitHub.com:**
   - Go to the **Releases** tab
   - Click **“Draft a new release”**
   - Choose the tag you just pushed (e.g. `v0.1.0`)
   - Add changelog/release notes
   - Click **“Publish release”**

The PyPI workflow will be triggered and your package will be published.

---

## ✅ Summary

- Fill in `pyproject.toml`
- Build your distribution with `python3 -m build`
- Test on TestPyPI, then upload to PyPI
- Use `pypi.yml` to automate releases

> 📦 Now others can `pip install` your project!
