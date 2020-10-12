from awesome_panel_extensions import awesome_panel
import param
import awesome_panel_extensions

from awesome_panel_extensions.bokeh_extensions.data_models.events import (
    IntegerEvent as _BkIntegerEvent,
)
from awesome_panel_extensions.data_models.parameter_model import ParameterModel
from awesome_panel_extensions.param import link


class IntegerEvent(ParameterModel):
    _widget_type = _BkIntegerEvent

    event = param.String(doc="The name of the event to watch")
    value = param.Integer(doc="The number of times the event has been triggered")


def create_event_model(parameter: param.Parameter, element: str, event: str):
    if not isinstance(parameter, param.Integer):
        raise ValueError(f"Error. The parameter {parameter.name} is not of type Integer!")
    model = IntegerEvent(
        element=element, event=event, value=getattr(parameter.owner, parameter.name)
    )
    link(parameter, model.param.value)
    return model
