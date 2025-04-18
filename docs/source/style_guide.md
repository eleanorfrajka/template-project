# Project Style Guide

> 🎨 This guide explains the coding and formatting conventions used in the project, and how to keep things consistent when adding or editing code.

It combines Python code conventions, documentation standards, and metadata formatting guidelines.

---

## 🧑‍💻 Python Coding Conventions

### ✅ Function Definitions
- Use **type hints** for all parameters and return types.
```python
def convert_units(
    values: xr.DataArray,
    current: str,
    target: str,
) -> xr.DataArray:
    ...
```

### 🐍 Naming
- Functions and variables: `snake_case`
- Constants (e.g., in xarray datasets): `ALL_CAPS`

### 📝 Docstrings
- Use **NumPy-style** docstrings
- Required for all functions.
- Sections include: `Parameters`, `Returns`, `Notes`, (optionally `Examples`, `References`)

Example:
```python
def convert_units_var(
    var_values: xr.DataArray,
    current_unit: str,
    new_unit: str,
    unit_conversion: dict = unit_conversion,
) -> xr.DataArray:
    """
    Convert variable values from one unit to another.

    Parameters
    ----------
    var_values : xr.DataArray
        The numerical values to convert.
    current_unit : str
        Unit of the original values.
    new_unit : str
        Desired unit for the output values.
    unit_conversion : dict, optional
        Dictionary containing conversion factors between units.

    Returns
    -------
    xr.DataArray
        Converted values in the desired unit.

    Notes
    -----
    If no valid conversion is found, the original values are returned unchanged.
    """
```

> 📚 NumPy-style docstrings render cleanly in Sphinx documentation (e.g. on Read the Docs). See [NumPy docstring style](https://numpydoc.readthedocs.io/en/latest/format.html).
> 
> 💡 Alternatives like [Google-style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) and [reST-style](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#info-field-lists) docstrings are also valid with Sphinx if configured properly.

---

## 🗂 Dataset & Metadata Conventions

### 🧬 Variable Names
- **ALL CAPITALS** for variables and dimensions: `TRANSPORT`, `DEPTH`, `TIME`
- Keep short and unambiguous

### 🧾 Attributes
- Follow [OceanGliders OG1 format](https://oceangliderscommunity.github.io/OG-format-user-manual/OG_Format.html)
- Use `units`, `long_name`, `comment`
- Avoid placing units in variable names — use attributes instead

### 📐 Consistency
- Units are checked and converted using helper functions
- Time is standardized using utility functions across the project

---

## 🔁 Automating Formatting (Optional)

The project uses tools like `black`, `ruff`, and `pytest` to enforce style, linting, and test consistency. These are integrated into the workflow using [pre-commit hooks](precommit_guide.md).

You don’t need to run them manually, but setting up pre-commit ensures your code follows project standards automatically.

---

## 🛠 Optional: VSCode Setup for Auto-formatting

To automatically format code when you save a file, add this to your **Workspace Settings** (`.vscode/settings.json`):
```json
{
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  }
}
```

You can also add a VSCode task to format manually:
```json
{
  "label": "Format Code",
  "type": "shell",
  "command": "black . && ruff check . --fix",
  ...
}
```
- Then bind it to a keyboard shortcut (e.g. `Cmd+Shift+R`) or run it from the command palette.

---

## 💡 Future Considerations

- Add `mypy` for static type checking
- Use Sphinx for auto-generating documentation (already partially configured)

---

> ✅ By following these conventions, your code will integrate smoothly with the rest of the project — clean, consistent, and ready for collaboration.
