# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.frameworks.material import Button

def test_constructor():
    Button(
        unelevated = False,
        raised = True,
        icon = "shopping_cart"
    )