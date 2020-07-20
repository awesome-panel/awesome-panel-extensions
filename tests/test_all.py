"""This module contains common tests across all extensions"""
from awesome_panel_extensions import panes
import awesome_panel_extensions.panes as panes
import pytest

EXTENSIONS = [panes.PandasProfileReport]
_EXTENSIONS = [(extension,) for extension in EXTENSIONS]

@pytest.mark.parametrize(["extension"], _EXTENSIONS)
def test_repr(extension):
    # When
    actual = extension().__repr__(depth=1)
    # Then
    assert isinstance(actual, str)
