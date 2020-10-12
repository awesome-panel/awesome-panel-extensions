# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pandas as pd
import param
import pytest

from awesome_panel_extensions.data_models.properties import (
    DataFrameProperty,
    DictProperty,
    IntegerProperty,
    ListProperty,
    NumberProperty,
    PropertyModel,
    StringProperty,
    create_property_model,
)


@pytest.fixture
def element():
    return "element-id"


@pytest.fixture
def prop():
    return "value"


@pytest.fixture
def event():
    return "change"


@pytest.mark.parametrize(
    ["property_class", "value"],
    [
        (StringProperty, "Hello World"),
        (IntegerProperty, 1),
        (NumberProperty, 2.2),
        (ListProperty, ["a", "b"]),
        (DictProperty, {"a": 1, "b": 2}),
    ],
)
def test_can_construct(property_class, value, element, prop, event):
    # Given
    # When
    item = property_class(element=element, prop=prop, event=event, value=value)
    # Then
    assert item.element == element
    assert item.prop == prop
    assert item.event == event
    assert item.value == value


def test_can_construct_dataframe(element, prop):
    # Given
    value = pd.DataFrame({"x": [1, 2]})
    orient = "records"
    # When
    item = DataFrameProperty(element=element, prop=prop, value=value, orient=orient)
    # Then
    assert item.element == element
    assert item.prop == prop
    pd.testing.assert_frame_equal(item.value, value)
    assert item.orient == orient


@pytest.mark.parametrize(
    ["parameter", "value", "model_definition", "model_class", "value2"],
    [
        (
            param.String,
            "Hello World",
            {"property_": "value", "event": "change"},
            StringProperty,
            "Hello World 2",
        ),
    ],
)
def test_create_linked_model_from_parameter(
    parameter, value, model_definition, model_class, value2
) -> PropertyModel:
    class MyClass(param.Parameterized):
        value_ = parameter(default=value)

    instance = MyClass(value_=value)

    model = create_property_model(instance.param.value_, element="element-id", **model_definition)

    assert model.value == instance.value_
    assert isinstance(model, model_class)
    # When/ Then
    instance.value_ = value2
    assert model.value == instance.value_
    # When/ Then
    model.value = value
    assert model.value == instance.value_
