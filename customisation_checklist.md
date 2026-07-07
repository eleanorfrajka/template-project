# Customisation Checklist

Use this checklist when adapting `template-project` to your own project.
The simplest approach is a global find-and-replace of `template_project` → `your_package_name`
and `template-project` → `your-project-name`, then work through the file-specific items below.

---

## 1. Rename the package directory

```bash
mv template_project/ your_package_name/
```

---

## 2. File-by-file changes

### `pyproject.toml`
- `[project] name` — PyPI package name (e.g. `"my-ocean-package"`)
- `[project] description` — one-line description of your project
- `[project] authors` / `maintainers` — your name and email
- `[project.urls]` — homepage, repository, documentation URLs
- `[tool.setuptools.packages.find] include` — change `"template_project"` → your package name
- `[tool.setuptools.package-data]` — same package name change
- `[tool.setuptools_scm] write_to` — path inside your renamed package directory
- `[tool.towncrier] package` / `package_dir` — your package name
- `[tool.towncrier] issue_format` — replace `[OWNER]/[REPO]` with your GitHub org/repo

### `README.md`
- Title, description, and badges
- GitHub URLs (clone URL, issues link, Actions badge)
- Documentation URL

### `CITATION.cff`
- `authors` — your name, ORCID, affiliation
- `title` — your project name
- `version` and `date-released`
- `url` — your repository URL

### `environment.yml`
- `name:` — conda environment name (currently `template-project`)

### `docs/source/conf.py`
- `project`, `author`, `copyright` variables
- `html_theme_options` — GitHub repository links

### `docs/source/index.md` (or `index.rst`)
- Project title and introductory text

### `template_project/logger.py` (after renaming)
- `logging.getLogger("template_project")` → `logging.getLogger("your_package_name")`

### `tests/test_utilities.py`
- `caplog.at_level("DEBUG", logger="template_project")` → your logger name

### `.github/workflows/`
- Check any hardcoded package names or environment names in CI workflow files

### `CHANGELOG.md`
- Reset to an empty changelog for your project's history

---

## 3. Remove template-specific content

- `data/moc_transports.nc` — replace with your own example data, or remove
- `notebooks/demo.ipynb` — replace with a notebook relevant to your project
- `template_project/read_rapid.py` — RAPID-specific reader; remove if not needed
- `CLAUDE-*.md` files — planning notes from this template's development; safe to delete
- `MODERNIZATION_PLAN.md` — if present, remove (template development notes)

---

## 4. Quick check — search for remaining template references

```bash
grep -rE 'template[-_.]project|eleanorfrajka|Frajka-Williams' \
     --include='*.py' --include='*.md' --include='*.toml' \
     --include='*.yml' --include='*.cff' --include='*.rst' .
```

Any hits outside of this checklist file itself should be reviewed.
