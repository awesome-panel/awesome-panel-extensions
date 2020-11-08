# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.frameworks.fast import FastCheckbox
from tests.frameworks.fast.fast_test_app import create_fast_test_app


def test_constructor():
    # When
    checkbox = FastCheckbox(name="Check Me")
    # Then
    assert checkbox.disabled is False
    assert checkbox.name == "Check Me"
    assert checkbox.value is False


if __name__ == "__main__":
    checkbox = FastCheckbox(name="Hello Fast Design World")
    app = create_fast_test_app(component=checkbox, parameters=["disabled", "readonly", "value", ""])
    app.show(port=5007)
