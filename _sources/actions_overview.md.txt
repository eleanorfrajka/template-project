# GitHub Actions: Automating Your Project

> ⚙️ GitHub Actions are tools that run automatically when certain things happen in your repository. They can test your code, build your docs, publish your package, and more.

In `template-project`, GitHub Actions live in the `.github/workflows/` folder.

---

## 🤖 What Is a GitHub Action?

A GitHub Action is a set of instructions that GitHub runs in response to events like:
- Opening a pull request
- Pushing new code
- Creating a release tag

Each Action is defined in a `.yml` file inside `.github/workflows/`.

---

## 🧪 `tests.yml`: Run Your Tests Automatically

**When it runs:**
- Every time you open or update a pull request

**What it does:**
- Sets up Python
- Installs your dependencies
- Runs `pytest` to check your code

**Why it matters:**
- Makes sure new code doesn’t break old code
- Helps catch bugs early

---

## 🧱 `docs.yml`: Test Your Documentation Build

**When it runs:**
- On every pull request to `main`

**What it does:**
- Builds your documentation using Sphinx
- Ensures you haven’t broken the docs accidentally

**Why it matters:**
- Keeps your docs up to date with your code
- Warns you if a bad docstring or config breaks the build

---

## 🚀 `docs_deploy.yml`: Publish to GitHub Pages

**When it runs:**
- After a pull request is merged into `main`

**What it does:**
- Rebuilds the documentation
- Publishes the result to the `gh-pages` branch

**Why it matters:**
- You get a public documentation site (e.g., `https://yourusername.github.io/your-repo`)

---

## 📦 `pypi.yml`: Publish a Package to PyPI

**When it runs:**
- When you push a GitHub release tag (e.g., `v0.1.0`)

**What it does:**
- Builds your Python package
- Uploads it to [PyPI](https://pypi.org) using secure GitHub credentials

**Why it matters:**
- Makes your code `pip install`-able by others

---

## 🛠️ How to Customize These Workflows

Look in `.github/workflows/*.yml` files. You’ll see sections like:
- `on:` — what triggers the workflow
- `jobs:` — what steps to run

Each step can run shell commands or call existing actions (e.g., `actions/setup-python`).

If you want to:
- **Add coverage reports** → modify `tests.yml`
- **Deploy to a different site** → update `docs_deploy.yml`
- **Use conda** instead of pip → swap the environment setup steps

---

## ✅ Summary

GitHub Actions in this template help you:
- Test every pull request
- Keep documentation working
- Publish code to the web or to PyPI automatically

> 💡 You don’t have to do anything to use them — they just work when you push code to GitHub!
