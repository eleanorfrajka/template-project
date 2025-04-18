# Setting Up Pre-commit Hooks

> 🔄 Pre-commit hooks help keep your code clean. They automatically format, lint, and check your files *before* a commit is made — reducing review time and improving consistency.

This guide walks you through setting up `pre-commit` in your project using the configuration in `template-project`.

---

## 🧠 What Are Pre-commit Hooks?

- Pre-commit hooks run **automatically** when you try to commit code.
- They check or fix things like formatting, linting, or large file commits.
- They help prevent messy code or accidental mistakes before it reaches your repository.

This project includes hooks for:
- `black` — autoformatting Python code and notebooks
- `codespell` — catch common misspellings in comments and strings
- `ruff` — fast linting and optional autofixing
- `pytest` — run tests before committing
- Cleanup tools: end-of-file fixer, trailing whitespace, YAML syntax checks

---

## ⚙️ Step-by-step Setup

### 1. Add `pre-commit` to your dev requirements
Make sure your `requirements-dev.txt` includes:
```txt
pre-commit
```
Then install:
```bash
pip install -r requirements-dev.txt
```

### 2. Create `.pre-commit-config.yaml`
At the root of your project, use:
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black
        language_version: python3
        files: \.(py|ipynb)$
        exclude: ^data/

  - repo: https://github.com/codespell-project/codespell
    rev: v2.2.6
    hooks:
      - id: codespell
        args: ["--ignore-words-list", "nd"]

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

  - repo: local
    hooks:
      - id: pytest
        name: pytest
        entry: pytest -q
        language: system
        types: [python]
        exclude: ^data/

  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.3.0
    hooks:
      - id: ruff
        args: ["--fix", "--exit-zero", "--select", "E,F,W,C90,ANN,B,BLE,TRY,ARG,SLF"]
        exclude: ^data/
```

> 💡 Files in `data/` are excluded to avoid disrupting raw or structured data.

### 3. Install the hooks
Once per project:
```bash
pre-commit install
```
This enables hooks to run automatically when you commit.

### 4. Test the setup
You can manually run all hooks like this:
```bash
pre-commit run --all-files
```

To test safely:
```bash
git checkout -b test/pre-commit-check
pre-commit run --all-files
```
And to discard:
```bash
git branch -D test/pre-commit-check
```

---

## 💻 Using Pre-commit in Your Workflow

### 🧑‍💻 Terminal workflow:
```bash
git add .
git commit -m "msg"
```
Hooks run automatically on commit. If a hook modifies files, stage the changes again and re-commit.

### 🧑‍🎨 VSCode workflow:
- Save your files
- Use `Cmd+Shift+R` or your custom VSCode task
- Stage and commit via Source Control panel

> 🧠 Tip: If a hook modifies your file, VSCode may show it as changed again — just stage and commit once more.

---

## 📋 Cheatsheet

| Step                    | Command                                 |
|-------------------------|-----------------------------------------|
| Install tools           | `pip install -r requirements-dev.txt`  |
| Install hooks           | `pre-commit install`                    |
| Run hooks manually      | `pre-commit run --all-files`           |
| Test safely in branch   | `git checkout -b test/pre-commit-check` + run + delete |
| Run tests via hook      | Add pytest to `.pre-commit-config.yaml` |

---

## 🔗 Learn More

- [Black](https://black.readthedocs.io/) — the uncompromising Python code formatter
- [Codespell](https://github.com/codespell-project/codespell) — a simple spellchecker for code
- [Ruff](https://docs.astral.sh/ruff/) — a fast Python linter written in Rust
- [Pytest](https://docs.pytest.org/) — a framework for testing Python code

> ✅ Your commits are now cleaner, safer, and tested — before they even leave your machine!
