from bokeh.core.properties import Int, String

from awesome_panel_extensions.bokeh_extensions.data_models.parameter_model import ParameterModel


class IntegerEvent(ParameterModel):
    event = String()
    value = Int()
