# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel as pn
import pytest

from awesome_panel_extensions.frameworks.material.style.stylesheet import _STYLE_PARAMETERS
from awesome_panel_extensions.frameworks.material import Stylesheet


@pytest.fixture
def stylesheet():
    return Stylesheet()


def test_can_construct(stylesheet):
    assert isinstance(stylesheet, Stylesheet)


def test_can_change_style_parameters(stylesheet):
    for parameter in _STYLE_PARAMETERS:
        assert parameter in stylesheet.param


def test_has_editor(stylesheet):
    assert isinstance(stylesheet.editor, pn.layout.Reactive)


def test_can_reset_to_defaults(stylesheet):
    # Given:
    stylesheet.param.set_param(**{p: "#cccccc" for p in _STYLE_PARAMETERS})
    # When:
    stylesheet.reset_to_defaults()
    # Then:
    for parameter in _STYLE_PARAMETERS:
        assert getattr(stylesheet, parameter) == stylesheet.param[parameter].default
