FAQ / Troubleshooting
======================


#### I get an error when doing `from projectName import plotters`

This is because your code can't find the project `projectName`.

**Option 1:** Install the package `projectName` locally

Activate your environment.

```
micromamba activate glidertest_env
```

then install your project from the terminal window in, e.g., `/Users/eddifying/github/projectName` as
```
pip install -e .
```
This will set it up so that you are installing the package in "editable" mode.  Then any changes you make to the scripts will be taken into account (though you may need to restart your kernel).  

**Option 2:** Add the path to the `projectName` to the code

Alternatively, you could add to your notebook some lines so that your code can "find" the package.  This might look like
```
import sys
sys.path.append('/Users/eddifying/github/projectName')
```
before the line where you try `from projectName import plotters`.  The secon

