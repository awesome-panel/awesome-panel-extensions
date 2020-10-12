# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel as pn
import param
import pytest

from awesome_panel_extensions.data_models import ParameterizedModel, create_parameter_model
from awesome_panel_extensions.data_models.attributes import BooleanAttribute
from awesome_panel_extensions.data_models.events import IntegerEvent
from awesome_panel_extensions.data_models.properties import StringProperty


@pytest.mark.parametrize(
    ["parameter", "value", "model_definition", "model_class"],
    [
        (param.String, "Hello World", {"property_": "value", "event": "change"}, StringProperty,),
        (param.Boolean, True, {"attribute": "checked"}, BooleanAttribute,),
        (param.Integer, 2, {"event": "click"}, IntegerEvent,),
    ],
)
def test_create_parameter_model(parameter, value, model_definition, model_class):
    class MyClass(param.Parameterized):
        value_ = parameter(default=value)

    instance = MyClass

    model = create_parameter_model(instance.param.value_, **model_definition, element="element-id")

    assert isinstance(model, model_class)


def test_create_parameter_model_with_invalid_definition_raise_exception():
    class MyClass(param.Parameterized):
        value_ = param.String()

    instance = MyClass

    with pytest.raises(ValueError):
        create_parameter_model(parameter=instance.param.value_, element="element-id")


def test_string_parameter():
    # When
    class MyClass(ParameterizedModel, param.Parameterized):
        _models = {"text": {"property": "value", "event": "change"}}
        text = param.String()

    instance = MyClass(text="Hello World", element="text-field-1")
    # Then
    assert isinstance(instance.model, pn.Column)
    text_model = instance.models["text"]
    assert isinstance(text_model, StringProperty)

    # When/ Then
    instance.text = "Hello Another World"
    assert text_model.value == instance.text
    # When/ Then
    text_model.value = "Hello Third World"
    assert instance.text == text_model.value
