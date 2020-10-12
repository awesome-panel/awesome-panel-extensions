from typing import Dict, Optional, Union

import panel as pn
import param

from . import attributes, events, properties


def create_parameter_model(
    parameter: param.Parameter,
    element: str,
    property_: Optional[str] = None,
    attribute: Optional[str] = None,
    event: Optional[str] = None,
):
    if property_:
        if not event:
            event = "change"
        return properties.create_property_model(
            parameter=parameter, element=element, property_=property_, event=event
        )
    if attribute:
        return attributes.create_attribute_model(
            parameter=parameter, element=element, attribute=attribute
        )
    if event:
        return events.create_event_model(parameter=parameter, element=element, event=event)

    raise ValueError(
        "Value Error. The arguments provided do not define a property, attribute or event!"
    )


def create_parameter_models(
    parameterized: param.Parameterized,
    parameterized_model_definition: Dict,
    element: Optional[Union[str, Dict]] = None,
):
    models = {}
    for parameter_name, parameter_model_definition in parameterized_model_definition.items():
        parameter_model_definition = parameter_model_definition.copy()

        if "element" in parameter_model_definition:
            _element = parameter_model_definition.pop("element")
        else:
            _element = ""

        if isinstance(element, str):
            _element = element
        elif isinstance(element, dict) and parameter_name in element:
            _element = element.pop(parameter_name)

        if "property" in parameter_model_definition:
            parameter_model_definition["property_"] = parameter_model_definition.pop("property")

        models[parameter_name] = create_parameter_model(
            parameter=parameterized.param[parameter_name],
            element=_element,
            **parameter_model_definition
        )
    return models


class ParameterizedModel:
    _models: Dict[str, Dict[str, str]] = {}

    def __init__(self, element: Optional[str] = None, **params):
        super().__init__(**params)

        self.models = create_parameter_models(
            self, parameterized_model_definition=self._models, element=element
        )
        self.model = pn.Column(
            *self.models.values(),
            width=0,
            height=0,
            margin=0,
            sizing_mode="fixed",
            css_classes=["parameterized-model"]
        )
