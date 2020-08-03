"""This module contains common tests across all extensions"""
# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from awesome_panel_extensions import pane

EXTENSIONS = [pane.PandasProfileReport]
_EXTENSIONS = [(extension,) for extension in EXTENSIONS]


@pytest.mark.parametrize(["extension"], _EXTENSIONS)
def test_repr(extension):
    # When
    actual = extension().__repr__(depth=1)
    # Then
    assert isinstance(actual, str)
