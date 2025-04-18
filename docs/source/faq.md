# FAQ / Troubleshooting

> 🧩 Common issues and how to fix them when working with this project template.

---

## 🐍 Import Error: `from template_project import plotters`

**Problem:** Python can’t find the `template_project` module.

### ✅ Option 1: Install the package locally (recommended)

Activate your environment:
```bash
micromamba activate template_env  # or conda activate template_env
```

Then install your project in “editable” mode:
```bash
pip install -e .
```
This lets Python find your package and reflects changes without needing to reinstall. Restart your kernel to apply changes.

📚 See also: [setup.md](setup.md)

### 🛠 Option 2: Add the path manually (in a notebook)
If you're working in a Jupyter notebook and haven't installed the package, insert this before importing:
```python
import sys
sys.path.append("/path/to/your/template-project")
```
Then you can run:
```python
from template_project import plotters
```
This is useful for testing during development, but installation is preferred.

---

## 💥 Pip install error in GitHub Actions

**Error message:**
```
× Getting requirements to build editable did not run successfully.
│ exit code: 1
╰─> See above for output.
```

This usually means something is wrong with the local installation process. Try the following locally in a clean environment:

```bash
virtualenv venv
source venv/bin/activate && micromamba deactivate
pip install -r requirements.txt
pip install -e .
```

If this works locally, your GitHub Actions will likely succeed too.

📁 GitHub workflows live in `.github/workflows/*.yml`

---

## 🤔 What's the difference between `template-project` and `template_project`?

- **`template-project`** is the name of the repository — it's fine to use hyphens in GitHub repo names.
- **`template_project`** is the name of the Python package (i.e., the importable module) — dashes are not allowed in Python package names.

| Term               | Use For                          |
|--------------------|-----------------------------------|
| `template-project` | GitHub repository name            |
| `template_project` | Python package (`import` syntax)  |

### Could they be the same name?
- ✅ Yes: Both could be `template_project`
- 🚫 No: Avoid `template-project` for the Python module

### Why this setup?
- Originally accidental, but it reinforces the distinction between repo and code module.
- Helps clarify which name to use in each context, especially when editing docs, imports, or packaging configs.

---

## 😬 I accidentally committed to `main` instead of a branch

It happens! If you haven't pushed yet:

### 🧼 Option 1: Create a new branch from the current commit
```bash
git branch new-feature-branch
```
Then switch to it:
```bash
git checkout new-feature-branch
```
You’re now safe to push your changes and create a pull request.

### 🗑 Option 2: Move the commit off `main` (before push)
```bash
git branch temp-fix

git reset --hard origin/main  # resets main to the last pushed commit

git checkout temp-fix
```
Now your `main` is clean and you can cherry-pick or merge your changes onto a feature branch properly.

> ⚠️ Only use `reset --hard` if you're sure you haven’t pushed yet and don’t need to keep local-only changes.

---

## 🚨 Continuous Integration (CI) is failing

### 🧪 If the failure is in tests:
Run tests locally to reproduce the issue:
```bash
pytest
```
Try running an individual test:
```bash
pytest tests/test_tools.py::test_my_function
```

📚 See: [writing_tests.md](writing_tests.md)

### 📚 If the failure is in documentation:
Try rebuilding the docs locally:
```bash
cd docs
make html
```
Then open `_build/html/index.html` in a browser.

📚 See: [build_docs.md](build_docs.md)

If your changes involve docstrings or `.md` files, a local preview will help catch errors before pushing.

> 💡 The GitHub Actions logs show exactly which step failed — start there!

---

## 🧭 How do I check which branch I'm on?

**In the terminal:**
```bash
git branch
```
The active branch is marked with an asterisk.

**In VSCode:**
- Look at the lower-left corner — your current branch name is shown there.

---

## 🔄 I cloned the repo but don’t see the latest updates

Make sure you're on the `main` branch and that it’s up to date:
```bash
git checkout main
git pull origin main
```

If you forked the repo, check out [gitcollab.md](gitcollab.md) for syncing instructions.

---

## ✍️ I made changes but GitHub doesn’t show them

You need to commit and push your work:
```bash
git add .
git commit -m "Describe your changes"
git push origin your-branch-name
```
> 💡 Pushing updates your branch on GitHub. Committing saves changes locally.

---

## 📋 I opened a pull request — what happens now?

- Your changes will be reviewed.
- GitHub Actions (CI) will check that tests and docs pass.
- You might be asked to tweak something.
- Once all is approved, your changes will be merged.

---

## 🙋 Still stuck?

Check [setup.md](setup.md), or ask a question by opening an issue at [github.com/eleanorfrajka/template-project](https://github.com/eleanorfrajka/template-project/issues).

> ✅ This FAQ is a living document — feel free to suggest improvements!
