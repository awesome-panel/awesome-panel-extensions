import param

from awesome_panel_extensions.bokeh_extensions.data_models.attributes import (
    BooleanAttribute as _BkBooleanAttribute,
)
from awesome_panel_extensions.bokeh_extensions.data_models.attributes import (
    StringAttribute as _BkStringAttribute,
)

from .parameter_model import ParameterModel


class AttributeModel(ParameterModel):
    attribute = param.String(doc="The name of the attribute to link")


class StringAttribute(AttributeModel):
    _widget_type = _BkStringAttribute

    value = param.String(doc="The current value of the attribute")


class BooleanAttribute(AttributeModel):
    _widget_type = _BkBooleanAttribute

    value = param.Boolean(doc="The current value of the attribute")


PARAMETER_TO_ATTRIBUTE = {
    param.String: StringAttribute,
    param.Boolean: BooleanAttribute,
}


def create_attribute_model(parameter: param.Parameter, element: str, attribute: str):
    parameter_type = type(parameter)
    if not parameter_type in PARAMETER_TO_ATTRIBUTE:
        raise ValueError(f"Parameter {parameter.name} is not a valid Parameter type!")
    return PARAMETER_TO_ATTRIBUTE[parameter_type](
        element=element, attribute=attribute, value=getattr(parameter.owner, parameter.name)
    )
