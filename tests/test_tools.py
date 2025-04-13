import pathlib
import sys
from template_project import tools

script_dir = pathlib.Path(__file__).parent.absolute()
parent_dir = script_dir.parents[0]
sys.path.append(str(parent_dir))


def test_convert_units_var():
    var_values = 100
    current_units = "cm/s"
    new_units = "m/s"
    converted_values = tools.convert_units_var(var_values, current_units, new_units)
    assert converted_values == 1.0
