# Writing and Running Tests

> 🧪 This guide explains how to write and run tests using `pytest`, following the structure used in the template-project.

Writing good tests helps you avoid bugs, refactor safely, and ensure your code does what you expect — even weeks or months later.

---

## 📁 Where Tests Go

All test code lives in the `tests/` directory at the root of the project.

- Each Python file in this folder starts with `test_`
- Each test function inside starts with `test_`
- You can organize tests by topic or module: `test_utils.py`, `test_readers.py`, etc.

---

## ✍️ Writing Your First Test

Tests are written as plain Python functions and typically use assertions to check behavior:

```python
# tests/test_math.py

def test_addition():
    assert 1 + 1 == 2
```

To test your own project modules, just import them like normal:

```python
# tests/test_tools.py
from template_project.tools import convert_units

def test_convert_units_basic():
    result = convert_units(10, "m", "km")
    assert result == 0.01
```

> 💡 All test functions must start with `test_` so `pytest` can discover them.

---

## ▶️ Running Tests Locally

Make sure you’ve installed the dev dependencies:
```bash
pip install -r requirements-dev.txt
```
Then run:
```bash
pytest
```

This will automatically find and run any `test_*.py` files under the `tests/` folder.

To run a specific test file:
```bash
pytest tests/test_tools.py
```

To run a specific test function:
```bash
pytest tests/test_tools.py::test_convert_units_basic
```

---

## 🛠 Recommended Conventions

- Group related tests by file (e.g. `test_utilities.py`, `test_standardise.py`)
- Name test functions to reflect what they check (e.g. `test_raises_on_invalid_units`)
- Use fixtures or test classes to share setup code when needed
- Keep each test focused on one thing

---

## 📊 Checking Test Coverage

Test coverage shows which lines of code are executed during testing. Higher coverage generally means better testing, but 100% coverage doesn't guarantee perfect tests.

### Quick Coverage Check
```bash
# Basic coverage report in terminal
pytest --cov=template_project --cov-report=term-missing
```

This shows:
- **Percentage covered** for each file
- **Missing lines** that aren't tested

### Detailed Coverage Analysis

For a comprehensive view, generate an HTML report:
```bash
pytest --cov=template_project --cov-report=html
```
Then open `htmlcov/index.html` in your browser.

### Reading Coverage Reports

**Terminal output example:**
```
Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
template_project/tools.py    20      3    85%   63, 96-97
template_project/utils.py    78     24    69%   79-80, 113-120
-----------------------------------------------------
TOTAL                       354     76    79%
```

**What this means:**
- **Stmts**: Total executable statements
- **Miss**: Statements not covered by tests  
- **Cover**: Percentage covered
- **Missing**: Specific line numbers not tested

**HTML report shows:**
- 🟢 **Green lines**: Covered by tests
- 🔴 **Red lines**: Not covered by tests
- 🟡 **Yellow lines**: Partially covered (e.g., branches)

### Coverage Guidelines

**Target coverage levels:**
- **80%+**: Good coverage for most projects
- **90%+**: Excellent coverage 
- **100%**: Often impractical (includes error handling, edge cases)

**Focus on:**
- Core business logic functions
- Complex algorithms and calculations
- Error handling paths
- Public API functions

**Less critical to test:**
- Simple getters/setters
- Third-party library integration
- Configuration/setup code


If you're using [pre-commit hooks](precommit_guide.md), you can configure them to run `pytest` before each commit. This helps you catch test failures early.

---

## Summary Cheatsheet

| Task                    | Command                                    |
|-------------------------|---------------------------------------------|
| Run all tests           | `pytest`                                   |
| Run specific test file  | `pytest tests/test_xyz.py`                 |
| Run specific test       | `pytest tests/test_xyz.py::test_name`      |
| Coverage report (terminal) | `pytest --cov=template_project --cov-report=term-missing` |
| Coverage report (HTML) | `pytest --cov=template_project --cov-report=html` |
| Install test tools      | `pip install -r requirements-dev.txt`     |

> ✅ Tests help you make confident changes. Use them early, and use them often!
