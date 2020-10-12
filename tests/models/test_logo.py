# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel as pn

from awesome_panel_extensions.models import Logo
from awesome_panel_extensions.models.logo import (
    PANEL_LOGO_RECTANGULAR_DARK_BACKGROUND,
    PANEL_LOGO_SQUARE_LIGHT_BACKGROUND,
)


def test_can_construct(logo):
    assert isinstance(logo, Logo)
    assert isinstance(logo.name, str)
    assert isinstance(logo.url, str)
    assert isinstance(logo._repr_html_(), str)


def test_contains_panel_logos():
    assert isinstance(PANEL_LOGO_RECTANGULAR_DARK_BACKGROUND, Logo)
    assert isinstance(PANEL_LOGO_SQUARE_LIGHT_BACKGROUND, Logo)


def test_can_create_application():
    return pn.Column(
        pn.Row(
            PANEL_LOGO_RECTANGULAR_DARK_BACKGROUND, background="black", margin=0, align="center"
        ),
        PANEL_LOGO_SQUARE_LIGHT_BACKGROUND,
    )


if __name__.startswith("bokeh"):
    test_can_create_application().servable()
elif __name__ == "__main__":
    test_can_create_application().show(port=5007)
