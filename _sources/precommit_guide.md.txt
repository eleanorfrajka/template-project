# Linting & Formatting

> 🧹 Consistent linting and formatting keep the codebase clean and reduce review time. This project uses [`ruff`](https://docs.astral.sh/ruff/) for both — it is fast, requires almost no configuration, and replaces the older `black` + `pre-commit` setup.

> ℹ️ **Note:** This project no longer uses `pre-commit`. Its checks were removed in favour of a CI-side `lint` job that runs `ruff` on every pull request. The filename of this page is kept for backward-compatible links.

---

## 🛠 The Tools

- **`ruff`** — linting, formatting, *and* type-annotation checks for Python. One tool covers all three jobs.

---

## ⚙️ Everyday Commands

Run these from the root of the project.

### Lint

```bash
ruff check .
```

### Lint and autofix

```bash
ruff check --fix .
```

### Format

```bash
ruff format .
```

### Verify formatting (what CI runs)

```bash
ruff format --check .
```

`ruff format --check .` does not modify any files — it exits non-zero if anything is not already formatted, which is exactly what the CI `lint` job does.

---

## 🤖 Enforcement in CI

Every pull request triggers a `lint` job in GitHub Actions that runs:

```bash
ruff check .
ruff format --check .
```

If either command fails, the job fails. To fix issues before pushing, run `ruff check --fix .` and `ruff format .` locally, then commit the result.

---

## 📋 Cheatsheet

| Task                        | Command                     |
|-----------------------------|-----------------------------|
| Lint                        | `ruff check .`              |
| Lint and autofix            | `ruff check --fix .`        |
| Format                      | `ruff format .`             |
| Verify formatting (CI)      | `ruff format --check .`     |

---

## 🔗 Learn More

- [Ruff](https://docs.astral.sh/ruff/) — a fast Python linter and formatter written in Rust
- [Pytest](https://docs.pytest.org/) — a framework for testing Python code
