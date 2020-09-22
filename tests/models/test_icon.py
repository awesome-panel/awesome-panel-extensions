# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.bokeh_extensions.icon import Icon as _BkIcon
from awesome_panel_extensions.models.icon import Icon
import pytest

# pylint: disable=line-too-long
def _icon():
    return Icon(
        name="Github",
        value="""<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-github" viewBox="0 0 19 20"><path d="M6.71154 17.0776C2.09615 18.4906 2.09615 14.7226 0.25 14.2517L6.71154 17.0776ZM13.1731 19.9036V16.2581C13.2077 15.8089 13.1482 15.3574 12.9986 14.9335C12.849 14.5096 12.6127 14.123 12.3054 13.7995C15.2038 13.4698 18.25 12.3489 18.25 7.20563C18.2498 5.89046 17.754 4.62572 16.8654 3.67319C17.2862 2.52257 17.2564 1.25074 16.7823 0.121918C16.7823 0.121918 15.6931 -0.207776 13.1731 1.51605C11.0574 0.930913 8.82722 0.930913 6.71154 1.51605C4.19154 -0.207776 3.10231 0.121918 3.10231 0.121918C2.62819 1.25074 2.59844 2.52257 3.01923 3.67319C2.12396 4.63279 1.62771 5.90895 1.63462 7.23389C1.63462 12.3394 4.68077 13.4604 7.57923 13.8278C7.27554 14.148 7.04132 14.5299 6.89182 14.9486C6.74233 15.3674 6.6809 15.8135 6.71154 16.2581V19.9036"></path></svg>""",
        fill_color="#E1477E",
        spin_duration=2000,
    )

@pytest.fixture
def icon():
    return _icon()


# pylint: enable=line-too-long

def test_can_construct(icon):
    assert isinstance(icon._bk_icon, _BkIcon)
    assert icon._bk_icon.label==icon.name
    assert icon._bk_icon.text==icon.value
    assert icon._bk_icon.size==icon.size
    assert icon._bk_icon.fill_color==icon.fill_color
    assert icon._bk_icon.spin_duration==icon.spin_duration

def test_can_change_name(icon):
    # When
    icon.name = "a"
    # Then
    assert icon._bk_icon.label == icon.name

def test_can_change_value(icon):
    # When
    icon.value = "<svg></svg>"
    # Then
    assert icon._bk_icon.text == icon.value
def test_can_change_size(icon):
    # When
    icon.size = 3.1
    # Then
    assert icon._bk_icon.size == icon.size
def test_can_change_fill_color(icon):
    # When
    icon.fill_color = "red"
    # Then
    assert icon._bk_icon.fill_color == icon.fill_color
def test_can_change_spin_duration(icon):
    # When
    icon.spin_duration = 201
    # Then
    assert icon._bk_icon.spin_duration == icon.spin_duration