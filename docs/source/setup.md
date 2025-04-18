# Getting Started: Setup and Installation

This guide walks you through the setup process when starting a new project using this template, or contributing to one based on it. It includes instructions for both terminal users and those using GitHub Desktop.

---

## Step 1: Get the Repository

You have two choices, depending on whether you're making a copy for your own use or contributing to someone else's.

### Option A: Use this template for your own project

You're making a fresh project based on this template.

#### a. Clone the repository to your computer
From a **terminal**:
```bash
git clone https://github.com/eleanorfrajka/template-project
```

Or in your **browser**:
1. Navigate to [https://github.com/eleanorfrajka/template-project](https://github.com/eleanorfrajka/template-project)
2. Click the green `<> Code` button.
3. Choose **Open with GitHub Desktop**.

> 💡 You can rename the folder after cloning.

#### b. (Optional) Change the remote origin
If you want to push to your own GitHub repository, create a new repo on [GitHub.com](https://github.com) and set it as the remote:
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/new-repo-name.git
git push -u origin main
```

### Option B: Contribute to someone else's project
See [Git Collaboration](gitcollab_v2.md) for full instructions on forking and branching when contributing to another repository.

---

## Step 2: Set Up a Python Environment

We recommend using a clean Python environment with `micromamba`, `conda`, `venv`, or similar. Below is the example using `venv`.

<!---
### Option A: Use `micromamba` (recommended for reproducibility)
If you're using `micromamba`, create an environment from the included YAML file:
```bash
micromamba create -f environment.yml
micromamba activate template_env
```
--->

### Option A: Use `venv` and `pip`
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
pip install -r requirements-dev.txt  # For development tools and testing
```

> 🔁 These install all runtime and development dependencies.

---

## Step 3: Install the Package (Editable Mode)

To use the code as an importable package:
```bash
pip install -e .
```
This sets up the local repository in *editable* mode, so changes you make to `.py` files will immediately be reflected when imported.

---

## Step 4: Test That It Works

Try running the tests:
```bash
pytest
```
If all goes well, this runs the unit tests in the `tests/` folder.

---

## Optional: Use GitHub Desktop Instead of Terminal

If you prefer not to use the terminal:
- Clone the repo using GitHub Desktop.
- Set up your Python environment using a tool like Anaconda or venv.
- Open the project folder in VSCode.
- Install the Python extension and interpreter.
- Run test scripts in the terminal panel or from notebooks.

See also [faq.md](faq.md) for troubleshooting installation problems.


---

## Git Workflows

Depending on how you’re working:

- If you are **working on your own project** using this template, see: [Solo Git](gitworkflow_solo.md)
- If you are **contributing to someone else’s project**, see: [Git Collaboration](gitcollab_v2.md)

Both guides include step-by-step workflows with examples using Terminal, VSCode, and GitHub Desktop.

---

## You're All Set!

From here, you can start editing code, writing documentation, or adding tests.
