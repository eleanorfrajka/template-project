# Building Documentation Locally

> 🧱 This guide walks you through building and previewing your project documentation using Sphinx — the same way it will appear on Read the Docs.

This is useful for checking formatting, linking, and rendering before publishing.

---

## 📦 Step 1: Install Documentation Dependencies

The required tools are listed in `requirements-dev.txt`. These are included **because the project uses Sphinx-based documentation** and may include Jupyter notebooks or Markdown-based pages.

To install them:
```bash
pip install -r requirements-dev.txt
```
This installs:
- `sphinx`
- `sphinx_rtd_theme`
- `myst-parser` for Markdown support
- `numpydoc` for parsing NumPy-style docstrings
- `nbsphinx` and `nbconvert` for integrating Jupyter notebooks
- `pypandoc` for converting between Markdown and reStructuredText formats


## 🏗 Step 2: Build the Docs

From the root of your project (where `docs/` lives), run:
```bash
cd docs
make html
```
This generates the documentation site in `docs/_build/html/`.

To preview:
```bash
open _build/html/index.html  # or use your browser
```

> 💡 On Windows, use `start _build/html/index.html`

---

## 🖋 Writing in Markdown or reStructuredText

You can write documentation pages in either:
- `.md` Markdown (using `myst-parser`)
- `.rst` reStructuredText (Sphinx’s default)

Markdown is supported for all new pages — just list them in your `index.rst` using the `.md` extension.

---

## 🧠 Tips for Clean Docs

- Keep filenames and headings consistent
- Use relative links when referring to other files
- Use backticks for inline code: `like_this()`
- Add `.. toctree::` blocks to structure your site

---

## 🧪 Rebuild After Changes

Sphinx doesn't auto-rebuild on save, so re-run `make html` each time you:
- Add or rename a `.md` or `.rst` file
- Edit cross-references or links
- Change docstrings if you're auto-documenting code

---

> 🧰 The `make html` command is defined in the project's `docs/Makefile`. You can inspect or modify it if needed.
> 
> 📁 The `docs/_build/` folder is ignored from version control via `.gitignore`.
> 
> 🖼 Static files like images, logos, or custom CSS should go in `docs/source/_static`. A default `logo.jpg` is included there.
> 
> ⚙️ The `docs/source/conf.py` controls your Sphinx build settings. Edit project metadata like `project`, `author`, and `release` to match your repo.


## 📚 Learn More

- [MyST Markdown Reference](https://myst-parser.readthedocs.io/en/latest/syntax/intro.html)
- [Sphinx reStructuredText Guide](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html)

These explain the syntax and tools supported when writing `.md` or `.rst` pages for your docs.

---

## Summary Cheatsheet

| Task                       | Command                |
|----------------------------|------------------------|
| Install dependencies       | `pip install -r requirements-dev.txt` |
| Build the docs             | `make html` (from inside `docs/`)     |
| Preview locally            | `open _build/html/index.html`        |

> ✅ Local docs previewing helps you spot problems early and polish your project site before publishing!
