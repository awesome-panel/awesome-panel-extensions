# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from awesome_panel_extensions.widgets.link_buttons import (
    BinderLinkButton,
    ImageLinkButton,
    NBViewerLinkButton,
    PanelLinkButton,
)
from awesome_panel_extensions.widgets.link_buttons.image_link_button import (
    _STYLE,
    DerivedImageLinkButton,
)


@pytest.fixture
def style():
    return _STYLE


@pytest.fixture
def style_str(style):
    return ";".join([key + ":" + value for key, value in style.items()])


@pytest.fixture
def image_url():
    return "https://panel.holoviz.org/_static/logo_stacked.png"


@pytest.fixture
def link_url():
    return "https://panel.holoviz.org"


@pytest.fixture
def sizing_mode():
    return "fixed"


@pytest.fixture
def image_button(link_url, image_url):
    return ImageLinkButton(
        link_url=link_url,
        image_url=image_url,
    )


@pytest.fixture
def image_button_object(link_url, image_url):
    return (
        f'<a href="{link_url}" target="_blank">'
        f'<img src="{image_url}" style="height:100%;max-width:100%;display:block;margin-left:auto'
        ';margin-right:auto"></a>'
    )


def test_image_link_button():
    assert ImageLinkButton.param.object.constant  # pylint: disable=no-member


def test_image_link_button_constructor(image_button, style, image_button_object):
    """We use the ImageLinkButton to test the ImageLinkButton"""
    # When
    button = image_button
    # Then
    assert isinstance(button, ImageLinkButton)
    assert button._rename == {"object": "text", "image_url": None, "link_url": None}
    assert button.style == style
    assert button.object == image_button_object


def test_image_link_button_change(image_button):
    # Given
    button = ImageLinkButton(
        link_url="a",
        image_url="b",
    )
    assert button.object != image_button.object
    # When
    button.link_url = image_button.link_url
    button.image_url = image_button.image_url
    # Then
    assert button.object == image_button.object


def test_derived_image_link_button():
    """We use the binder_button as an example"""
    assert isinstance(DerivedImageLinkButton(), ImageLinkButton)
    assert DerivedImageLinkButton.param.link_url.constant  # pylint: disable=no-member
    assert DerivedImageLinkButton.param.image_url.constant  # pylint: disable=no-member


def test_binder_button():
    # When
    button = BinderLinkButton(
        repository="MarcSkovMadsen/awesome-panel-extensions",
        branch="master",
        folder="examples/reference/panes",
        notebook="WebComponent.ipynb",
    )
    # Then
    assert isinstance(button, DerivedImageLinkButton)
    assert button.image_url == "https://mybinder.org/badge_logo.svg"
    assert button.style == {}
    assert button.link_url == (
        "https://mybinder.org/v2/gh/MarcSkovMadsen/awesome-panel-extensions/master"
        "?filepath=examples%2Freference%2Fpanes%2FWebComponent.ipynb"
    )


def test_nbviewer_button():
    # When
    button = NBViewerLinkButton(
        repository="MarcSkovMadsen/awesome-panel-extensions",
        branch="master",
        folder="examples/reference/panes",
        notebook="WebComponent.ipynb",
    )
    # Then
    assert isinstance(button, DerivedImageLinkButton)
    assert (
        button.image_url
        == "https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg"
    )
    assert button.style == {}
    assert button.link_url == (
        "https://nbviewer.jupyter.org/github/MarcSkovMadsen/awesome-panel-extensions/blob/"
        "master/examples/reference/panes/WebComponent.ipynb"
    )


def test_panel_button():
    # When
    button = PanelLinkButton(theme="light")
    # Then
    assert isinstance(button, DerivedImageLinkButton)
    assert button.image_url == "https://panel.holoviz.org/_static/logo_stacked.png"
    assert button.link_url == "https://panel.holoviz.org"
    assert button.style == _STYLE

    # When
    button.theme = "dark"
    # Then
    assert button.image_url == "https://panel.holoviz.org/_static/logo_horizontal.png"
