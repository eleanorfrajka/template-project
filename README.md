# template-project
Template for a Python project for oceanography.  It is designed to be used as a template for your own specific project, where you can then change the name of the project (here `template_project`), update the code (`template_project/*.py`), and use the example code to build a project with documentation, citation information, etc.

Functionality currently includes:
- Sample code with naming conventions in `template_project/*.py`
- Demo notebook in `notebooks/demo.ipynb`
- Initial example for documentation using sphinx and a read-the-docs theme in `docs/` (see build at [https://eleanorfrajka.github.io/template-project/](https://eleanorfrajka.github.io/template-project/))
- Examples of test code in `tests/test_tools.py`
- Workflows for testing the build of documentation on pull request (`.github/workflows/docs.yml`) and for running the tests using `pytest` (`.github/workflows/tests.yml`)
- Both a `requirements.txt` file for the python packages to run the code, and a `requirements-dev.txt` file for packages needed to develop the code.  The additions are there for running tests (`pytest` and `pytest-cov`) and building documentation (`nbsphinx`, `nbconvert`, etc).
- Examples of a `CONTRIBUTING.md` file generated initially using [https://github.com/bttger/contributing-gen](https://github.com/bttger/contributing-gen) and then edited.
- Examples of a `CITATION.cff` file which provides citation information for your software package on Github.
- Necessary files to enable installing the package locally using pip (`pyproject.toml`) and [instructions](https://eleanorfrajka.github.io/template-project/pypi-publish.html) and a github workflow (`.github/workflows/pypi.yml`) for publishing a release to [https://pypi.org](https://pypi.org) so that others can install your package using pip.

Future plans for template project include adding instructions for how to test your build locally, and run your tests (and generate a report) locally are pending.

I'll also (once I know how) add instructions for how to publish the package to conda forge, so that folks who use conda or mamba for environment management can also install that way.


### Install

Install locally using
```sh
pip install -e .
```

### Documentation

Documentation is available at [https://eleanorfrajka.github.io/template-project](https://eleanorfrajka.github.io/template-project/).

Check out the demo notebook `notebooks/demo.ipynb` for example functionality.

### Contributing

All contributions are welcome!  See [contributing](CONTRIBUTING.md) for more details.

To install a local, development version of template-project, clone the repository, open a terminal in teh root directory (next to this readme file) and run these commands:

```sh 
git clone https://github.com/eleanorfrajka/template-project.git
cd template-project
pip install -r requirements-dev.txt
pip install -e .
```
This installs template-project locally.  The `-e` ensures that any edits you make in the files will be picked up by scripts that impport functions from glidertest.

You can run the example jupyter notebook by launching jupyterlab with `jupyter-lab` and navigating to the `notebooks` directory, or in VS Code or another python GUI.

All new functions should include tests.  You can run tests locally and generate a coverage reporrt with:
```sh
pytest --cov=template-project --cov-report term-missing tests/
```

Try to ensure that all the lines of your contribution are covered in the tests.

