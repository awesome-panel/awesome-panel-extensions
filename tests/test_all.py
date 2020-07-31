"""This module contains common tests across all extensions"""
import pytest

import awesome_panel_extensions.pane as pane
from awesome_panel_extensions import pane as pane

EXTENSIONS = [pane.PandasProfileReport]
_EXTENSIONS = [(extension,) for extension in EXTENSIONS]


@pytest.mark.parametrize(["extension"], _EXTENSIONS)
def test_repr(extension):
    # When
    actual = extension().__repr__(depth=1)
    # Then
    assert isinstance(actual, str)
