import param
from bokeh.models.sources import ColumnDataSource

from awesome_panel_extensions.bokeh_extensions.data_models.properties import (
    BooleanProperty as _BkBoolProperty,
)
from awesome_panel_extensions.bokeh_extensions.data_models.properties import (
    CDSProperty as _BkCDSProperty,
)
from awesome_panel_extensions.bokeh_extensions.data_models.properties import (
    DictProperty as _BkDictProperty,
)
from awesome_panel_extensions.bokeh_extensions.data_models.properties import (
    FloatProperty as _BkFloatProperty,
)
from awesome_panel_extensions.bokeh_extensions.data_models.properties import (
    IntegerProperty as _BkIntProperty,
)
from awesome_panel_extensions.bokeh_extensions.data_models.properties import (
    ListProperty as _BkListProperty,
)
from awesome_panel_extensions.bokeh_extensions.data_models.properties import (
    StringProperty as _BkStringProperty,
)
from awesome_panel_extensions.param import link

from .parameter_model import ParameterModel


class PropertyModel(ParameterModel):
    event = param.String(doc="The name of the event that signals the property has changed")
    property_ = param.String(doc="The name of the property to link")


class StringProperty(PropertyModel):
    _widget_type = _BkStringProperty

    value = param.String(doc="The current value of the property")


class BooleanProperty(PropertyModel):
    _widget_type = _BkBoolProperty

    value = param.Boolean(doc="The current value of the property")


class IntegerProperty(PropertyModel):
    _widget_type = _BkIntProperty

    value = param.Integer(doc="The current value of the property")


class NumberProperty(PropertyModel):
    _widget_type = _BkFloatProperty

    value = param.Number(doc="The current value of the property")


class ListProperty(PropertyModel):
    _widget_type = _BkListProperty

    value = param.List(doc="The current value of the property")


class DictProperty(PropertyModel):
    _widget_type = _BkDictProperty

    value = param.Dict(doc="The current value of the property")


class DataFrameProperty(PropertyModel):
    _rename = {**ParameterModel._rename, "value": None, "_value": "value"}

    _widget_type = _BkCDSProperty

    value = param.DataFrame(doc="The current value of the property")
    _value = param.ClassSelector(class_=ColumnDataSource)
    orient = param.ObjectSelector(default="list", objects=["list", "records"])


PARAMETER_TO_PROPERTY = {
    param.String: StringProperty,
    param.Boolean: BooleanProperty,
    param.Integer: IntegerProperty,
    param.Number: NumberProperty,
    param.List: ListProperty,
    param.Dict: DictProperty,
    param.DataFrame: DataFrameProperty,
}


def create_property_model(
    parameter: param.Parameter, element: str, property_: str, event: str, **args
):
    parameter_type = type(parameter)
    if not parameter_type in PARAMETER_TO_PROPERTY:
        raise ValueError(f"Parameter {parameter.name} is not a valid Parameter type!")
    model = PARAMETER_TO_PROPERTY[parameter_type](
        element=element,
        property_=property_,
        event=event,
        **args,
        value=getattr(parameter.owner, parameter.name),
    )
    link(parameter, model.param.value)
    return model
