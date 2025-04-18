# Code Formatting with Black and isort

This document captures the setup and workflow for automatic code formatting in this project, using **Black** and **isort**. Pre-commit hooks and testing are described in a separate document.

---

## Purpose of Tools

### **Black**
> *"The uncompromising Python code formatter."*

- **What it does:** Automatically formats Python code (including `.py` and `.ipynb` notebooks) to a consistent, opinionated style.
- **Why it's useful:** Saves time on manual formatting and keeps the codebase clean and readable. Focus on code, not style decisions!

### **isort**
> *"A Python utility to sort imports alphabetically, and automatically separate them into sections."*

- **What it does:** Auto-sorts import statements in Python files and notebooks.
- **Why it's useful:** Keeps imports clean and consistent, prevents duplication, and improves readability.

---

## Installation and Setup

### 1. Add to `requirements-dev.txt`
Make sure these lines are included:

```
black[jupyter]
isort
```

Then install dev requirements:

```bash
pip install -r requirements-dev.txt
```

### 2. Manual use (optional)
You can manually run these tools at any time:

```bash
black .
isort .
```

This will format all Python and notebook files in the current directory and subdirectories.

### 3. Notes on Data Files

We intentionally avoid running formatting tools on the `data/` directory because:
- These files may have meaningful whitespace (e.g., for alignment in `.txt`, `.csv`, or raw data formats).
- These files are considered **read-only** within the project.
- We want to preserve raw scientific data exactly as received or produced.

---

## Workflow Notes

### For **terminal users**:
- Run formatting manually before committing:

```bash
black .
isort .
```

### For **VSCode users**:
- Use VSCode for editing as usual.
- Format files automatically on save by setting up VSCode settings (see below).

#### Recommended VSCode Settings:

1. Open **Command Palette** (`Cmd+Shift+P`).
2. Type **Preferences: Open Workspace Settings (JSON)** (make sure you choose *Workspace* if prompted).
3. Add the following to your settings:

```json
{
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
}
```

### Optional VSCode Task and Shortcut

If you prefer, you can also set up a VSCode task and keyboard shortcut to run both tools manually inside VSCode.

#### Add the VSCode Task:
1. Create `.vscode/tasks.json` with the following content:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Format Code",
            "type": "shell",
            "command": "black . && isort .",
            "problemMatcher": [],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "presentation": {
                "reveal": "always",
                "panel": "dedicated"
                // Optional: Auto-close terminal when successful
                // "close": true
            }
        }
    ]
}
```

2. Open **Command Palette** (`Cmd+Shift+P`).
3. Type **Tasks: Run Task**.
4. Select **Format Code** from the list to test that it works!

#### Install the Tasks Extension:
1. Open **Extensions Panel** (`Cmd+Shift+X`).
2. In the search bar, type **Tasks**.
3. Find the extension by **actboy168** and click **Install**.
4. Reload VSCode if needed.

#### Add a keyboard shortcut:
1. Open **Command Palette** (`Cmd+Shift+P`).
2. Type **Preferences: Open Keyboard Shortcuts (JSON)**.
3. Add the following inside the square brackets:

```json
{
    "key": "cmd+shift+r",
    "command": "workbench.action.tasks.runTask",
    "args": "Format Code",
    "when": "editorTextFocus"
}
```

#### Add the status bar button:
1. After installing the **Tasks** extension by `actboy168`, you'll see a status bar item at the bottom of the window, showing your task name (e.g., "Format Code").
2. Click the button to run your task!

---

## Summary Cheatsheet

| Step | Command |
|------|----------|
| Install tools | `pip install -r requirements-dev.txt` |
| Format manually (terminal) | `black . && isort .` |
| VSCode auto-format | On save (with workspace settings.json) |
| VSCode task | `Cmd+Shift+R` or status bar click |

---

> ✅ Your project now has a clean, automated workflow for code formatting using Black and isort!

For details about pre-commit hooks and test automation, see the separate documentation file.

