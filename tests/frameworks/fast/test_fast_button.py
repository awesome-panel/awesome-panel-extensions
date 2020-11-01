# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel as pn
import pytest

from awesome_panel_extensions.frameworks import fast
from awesome_panel_extensions.frameworks.fast import FastButton
from awesome_panel_extensions.frameworks.fast.fast_button import BUTTON_TYPE_TO_APPEARANCE


def test_constructor():
    FastButton(
        appearance="lightweight",
        autofocus=False,
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


if __name__ == "__main__":
    button = FastButton(name="Hello Fast Design World")
    app = pn.Column(
        pn.Column(
            pn.pane.SVG(
                "https://explore.fast.design/e1e15bd85334e4346744078af2f52308.svg", height=100
            ),
            pn.Spacer(height=25),
            pn.pane.PNG("https://panel.holoviz.org/_static/logo_horizontal.png", height=100),
        ),
        pn.Spacer(height=10),
        pn.pane.HTML("<fast-divider></fast-divider>", sizing_mode="stretch_width", height=25),
        button,
        pn.Spacer(height=10),
        pn.pane.HTML("<fast-divider></fast-divider>", sizing_mode="stretch_width", height=25),
        pn.Param(
            button,
            parameters=[
                # Old
                "name",
                "disabled",
                "button_type",
                "clicks",
                "height",
                "width",
                "margin",
                "sizing_mode",
                # New
                "autofocus",
                "appearance",
            ],
            show_name=False,
        ),
        fast.config.get_fast_js_panel(),
    )

    fast.FastTemplate(main=[app]).show(port=5007)
