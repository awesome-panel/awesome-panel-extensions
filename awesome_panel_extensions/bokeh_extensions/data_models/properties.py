from bokeh.core.properties import Any, Bool, Dict, Float, Int, List, String
from bokeh.core.property.instance import Instance
from bokeh.models.sources import ColumnDataSource

from awesome_panel_extensions.bokeh_extensions.data_models.parameter_model import ParameterModel


class PropertyModel(ParameterModel):
    event = String()
    property_ = String()


class StringProperty(PropertyModel):
    value = String()


class BooleanProperty(PropertyModel):
    value = Bool()


class IntegerProperty(PropertyModel):
    value = Int()


class FloatProperty(PropertyModel):
    value = Float()


class ListProperty(PropertyModel):
    value = List(Any)


class DictProperty(PropertyModel):
    value = Dict(Any, Any)


class CDSProperty(PropertyModel):
    value = Instance(ColumnDataSource)
