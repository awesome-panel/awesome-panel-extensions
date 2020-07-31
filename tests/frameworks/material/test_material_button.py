# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from awesome_panel_extensions.frameworks.material import Button


def test_constructor():
    Button(unelevated=False, raised=True, icon="shopping_cart")


@pytest.mark.parametrize(["button_type"], [("primary",), ("success",), ("warning",), ("danger",)])
def test_button_type_on_construction(button_type):
    # When
    button = Button(button_type=button_type)
    # Then
    assert button.raised
    assert not button.unelevated


@pytest.mark.parametrize(["button_type"], [("primary",), ("success",), ("warning",), ("danger",)])
def test_button_type_on_change(button_type):
    # Given
    button = Button()
    button.raised = False
    button.unulevated = True
    # When
    button.button_type = button_type
    # Then
    assert button.raised
    assert not button.unelevated
