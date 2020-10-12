# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.data_models.attributes import BooleanAttribute, StringAttribute


def test_string_attribute():
    # Given
    element = "element-id"
    attr = "href"
    value = "https://panel.holoviz.org"
    # When
    attribute = StringAttribute(element=element, attribute=attr, value=value)
    # Then
    assert attribute.element == element
    assert attribute.attribute == attr
    assert attribute.value == value


def test_boolean_attribute_link():
    # Given
    element = "element-id"
    attr = "visible"
    value = True
    # When
    attribute = BooleanAttribute(element=element, attribute=attr, value=value)
    # Then
    assert attribute.element == element
    assert attribute.attribute == attr
    assert attribute.value == value
