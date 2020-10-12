import param

from awesome_panel_extensions.bokeh_extensions.data_models.attributes import (
    BooleanAttribute as _BkBooleanAttribute,
)
from awesome_panel_extensions.bokeh_extensions.data_models.attributes import (
    StringAttribute as _BkStringAttribute,
)
from awesome_panel_extensions.param import link

from .parameter_model import ParameterModel


class AttributeModel(ParameterModel):
    attribute = param.String(doc="The name of the attribute to link")


class StringAttribute(AttributeModel):
    _widget_type = _BkStringAttribute

    value = param.String(doc="The current value of the attribute")


class BooleanAttribute(AttributeModel):
    _widget_type = _BkBooleanAttribute

    value = param.Boolean(doc="The current value of the attribute")

class _DerivedAttribute(AttributeModel):
    _rename = {**AttributeModel._rename, "value": None, "_value": "value"}
    _widget_type = _BkStringAttribute
    _convert_func=str

    value = param.String(doc="The current value of the attribute")
    _value = param.String(doc="The current value of the attribute as a String")

    def __init__(self, **params):
        super().__init__(**params)

        self._set__value()

    @param.depends("value", watch=True)
    def _set__value(self, *events):
        old_value = self._value
        new_value = str(self.value)
        if old_value!=new_value:
            self._value = new_value

    @param.depends("_value", watch=True)
    def _set_value(self, *events):
        old_value = str(self.value)
        new_value = self._convert_func(self._value)
        print("_set_value", new_value)
        if old_value!=new_value:
            self.value = new_value

class IntegerAttribute(_DerivedAttribute):
    _convert_func=int

    value = param.Integer(doc="The current value of the attribute")

class NumberAttribute(_DerivedAttribute):
    _convert_func=float

    value = param.Number(doc="The current value of the attribute")


PARAMETER_TO_ATTRIBUTE = {
    param.String: StringAttribute,
    param.Boolean: BooleanAttribute,
    param.Integer: IntegerAttribute,
    param.Number: NumberAttribute,
}


def create_attribute_model(parameter: param.Parameter, element: str, attribute: str):
    parameter_type = type(parameter)
    if not parameter_type in PARAMETER_TO_ATTRIBUTE:
        raise ValueError(f"Parameter {parameter.name} is not a valid Parameter type!")
    model = PARAMETER_TO_ATTRIBUTE[parameter_type](
        element=element, attribute=attribute, value=getattr(parameter.owner, parameter.name)
    )
    link(parameter, model.param.value)
    print("HelloModel", model)
    return model
