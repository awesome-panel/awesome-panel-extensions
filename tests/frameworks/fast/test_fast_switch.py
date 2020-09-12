# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.frameworks.fast import FastSwitch
from tests.frameworks.fast.fast_test_app import create_fast_test_app


def test_constructor():
    # When
    switch = FastSwitch(name="Notify by Email", value=False, checked_message="On", unchecked_message="Off")
    # Then
    assert switch.name=="Notify by Email"
    assert switch.value is False
    assert switch.checked_message=="On"
    assert switch.unchecked_message=="Off"

    assert switch.disabled is False
    assert switch.readonly is False


if __name__.startswith("bokeh"):
    switch = FastSwitch(
        name="Notify by Email",
        value=False,
        checked_message="On",
        unchecked_message="Off",
    )
    app = create_fast_test_app(
        component=switch,
        parameters=[
            "name",
            "value",
            "checked_message",
            "unchecked_message",
            "required",
            "disabled",
            "readonly"
        ],
    )
    app.servable()