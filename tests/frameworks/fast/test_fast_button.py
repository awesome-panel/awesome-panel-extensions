# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest
from awesome_panel_extensions.frameworks.fast import FastButton
from awesome_panel_extensions.frameworks.fast.fast_button import BUTTON_TYPE_TO_APPEARANCE


def test_constructor():
    FastButton(
        appearance="lightweight", autofocus=False,
    )


@pytest.mark.parametrize("button_type", BUTTON_TYPE_TO_APPEARANCE.keys())
def test_button_type_on_constructor(button_type):
    # When
    button = FastButton(button_type=button_type)
    # Then
    assert button.appearance == BUTTON_TYPE_TO_APPEARANCE[button_type]


@pytest.mark.parametrize("button_type", BUTTON_TYPE_TO_APPEARANCE.keys())
def test_button_type_on_change(button_type):
    # When
    button_type = "primary"
    button = FastButton(button_type=button_type)
    # Then
    assert button.appearance == BUTTON_TYPE_TO_APPEARANCE[button_type]

if __name__=="__main__":
    import panel as pn
    from awesome_panel_extensions.frameworks.fast import config
    pn.Column(
        FastButton(name="Hello World"),
        pn.Param(FastButton, parameters=["button_type", "clicks", "autofocus", "appearance"]),
        config.get_fast_js_panel(),
        ).show(port=5007)