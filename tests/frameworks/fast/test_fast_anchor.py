# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.frameworks.fast import FastAnchor
from tests.frameworks.fast.fast_test_app import create_fast_test_app


def test_constructor():
    # When
    anchor = FastAnchor(name="Anchor")
    # Then
    assert anchor.value is None
    assert anchor.appearance is None
    assert anchor.download is None
    assert anchor.hreflang is None
    assert anchor.ping is None
    assert anchor.referrerpolicy is None
    assert anchor.rel is None
    assert anchor.target is None
    assert anchor.mimetype is None
    assert anchor.height == 40


def test_constructor_with_hypertext():
    # When
    anchor = FastAnchor(name="Anchor", appearance="hypertext")
    # Then
    assert anchor.height == 20


def test_change_appearance_to_hypertext():
    # Given
    anchor = FastAnchor(name="Anchor")
    # When
    anchor.appearance = "hypertext"
    # Then
    assert anchor.height == 20


if __name__.startswith("bokeh"):
    anchor = FastAnchor(
        name="Be Fast!",
        value="https://fast.design",
        appearance="neutral",
        rel="help",
        target="_blank",
    )
    app = create_fast_test_app(
        component=anchor,
        parameters=[
            "name",
            "value",
            "appearance",
            "download",
            "href",
            "hreflang",
            "ping",
            "referrerpolicy",
            "referrer",
            "rel",
            "target",
            "mimetype",
        ],
    )
    app.servable()
