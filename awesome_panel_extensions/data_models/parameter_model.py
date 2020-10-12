import panel as pn
import param
from param import Boolean


class ParameterModel(pn.widgets.Widget):
    _rename = {
        "title": None,
        "parameter": None,
    }

    height = param.Integer(default=0, constant=True)
    width = param.Integer(default=0, constant=True)
    margin = param.Parameter(default=0, constant=True)
    sizing_mode = param.String(default="fixed", constant=True)

    parameter = param.ClassSelector(class_=param.Parameter, doc="The parameter")
    element = param.String(
        doc="The id, query selection string or similar identifying target object"
    )
    value = param.Parameter()
