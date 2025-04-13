# Pre-commit Hook Setup

This document captures the setup and workflow for using **pre-commit hooks** in this project. Pre-commit hooks automate code formatting and quality checks before every commit, keeping the repository clean and consistent.

There is also a separate document for code formatting tools specifically: *see "Code Formatting with Black and isort" for details on those tools.*

---

## Purpose of Pre-commit Hooks

- **What it does:** Automatically runs code formatters and linters (Black, isort, and more) every time you commit code.
- **Why it's useful:** Ensures consistency, catches formatting issues early, and automates tedious tasks.
- **Current hooks include:**
  - **Black** — Format Python and Jupyter notebooks.
  - **isort** — Sort Python imports.
  - **End of file fixer** — Ensure files end with a newline.
  - **Trailing whitespace remover** — Clean up accidental trailing spaces.
  - **YAML checks** — Validate YAML syntax.
  - **Large file check** — Prevent accidental commits of large files.

Later, you can also add test runners (like pytest) and linters!

---

## Installation and Setup

### 1. Add to `requirements-dev.txt`

Add **pre-commit** to your dev requirements:

```
pre-commit
```

Then install:

```bash
pip install -r requirements-dev.txt
```

### 2. Create `.pre-commit-config.yaml`

Create this file at the root of your project with the following content:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black
        language_version: python3
        files: \.(py|ipynb)$
        exclude: ^data/|\.txt$

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort
        language_version: python3
        files: \.(py|ipynb)$
        exclude: ^data/

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: end-of-file-fixer
        files: \.(py|yaml|yml|ipynb)$
        exclude: ^data/
      - id: trailing-whitespace
        files: \.(py|yaml|yml|ipynb)$
        exclude: ^data/
      - id: check-yaml
        files: \.(yaml|yml)$
        exclude: ^data/
      - id: check-added-large-files
```

**Why exclude `.txt` files from Black?**
> `.txt` files often contain data or formatted text where whitespace is meaningful (e.g., aligned tables, scientific data dumps). Black aggressively reformats whitespace, so we explicitly exclude `.txt` files to avoid corrupting data formatting.

### 3. Install pre-commit hooks

Run this once to install hooks into your Git configuration:

```bash
pre-commit install
```

### 4. Test pre-commit before committing

Before making real commits, you can safely test:

```bash
pre-commit run --all-files
```

You can also create a test branch for safety:

```bash
git checkout -b test/pre-commit-check
pre-commit run --all-files
```

If you're not happy with the changes, simply discard the branch:

```bash
git branch -D test/pre-commit-check
```

---

## Workflow Notes

### For **terminal users**:
1. Make your code changes.
2. Stage changes:
   ```bash
   git add .
   ```
3. Commit:
   ```bash
   git commit -m "Your message"
   ```
4. Pre-commit hooks will run automatically. If hooks modify files, you will need to re-stage and re-commit.

5. Optional: run pre-commit manually at any time:

```bash
pre-commit run --all-files
```

### For **VSCode users**:
- Do your editing as normal.
- **Before staging/committing**, run your pre-commit task:
  - Use your keyboard shortcut (e.g., `Cmd+Shift+R`) **or**
  - Click the status bar task button (if you’ve set this up).
- After running the task, stage changes and commit in the VSCode Git panel.

Optional reminder: if you try to commit in VSCode and pre-commit modifies files, you’ll need to stage the changes again before the commit goes through!

---

## Adding Pytest to Pre-commit (Optional)

You can also add automated test runs to your pre-commit hooks.

1. Install pytest if you haven’t already:

```bash
pip install pytest
```

2. Add this to your `.pre-commit-config.yaml`:

```yaml
  - repo: local
    hooks:
      - id: pytest
        name: pytest
        entry: pytest
        language: system
        types: [python]
```

3. Now, tests will automatically run before every commit!

---

## Notes

- **Data files and `.txt` files are excluded from pre-commit hooks.**
  - Files in `data/` and any `.txt` files are considered read-only and are intentionally excluded from automatic formatting or cleanup.
  - These files often contain meaningful whitespace (e.g., alignment in scientific data or structured text formats) that should not be changed automatically.

- **Manual pre-commit runs are safe.**
  - You can run `pre-commit run --all-files` anytime to pre-clean your repository.

- **Pre-commit helps enforce consistency.**
  - Even if one contributor forgets to format their code, pre-commit ensures everything stays clean before merging.

---

## Summary Cheatsheet

| Step | Command |
|------|----------|
| Install tools | `pip install -r requirements-dev.txt` |
| Install hooks | `pre-commit install` |
| Run hooks manually | `pre-commit run --all-files` |
| Test safely in a branch | `git checkout -b test/pre-commit-check` + `pre-commit run --all-files` |
| Add pytest (optional) | Add local hook to `.pre-commit-config.yaml` |

---

> ✅ Your project now has a clean, automated workflow for code quality and pre-commit hooks!

See "Code Formatting with Black and isort" for details on formatting tools and VSCode integration.

---

*This documentation was generated with the help of ChatGPT, in collaboration with the project developer.*

