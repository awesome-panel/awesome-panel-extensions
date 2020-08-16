"""Implementation of MWC Material Button"""
import param

from awesome_panel_extensions.frameworks._base.config import BUTTON_TYPES
from awesome_panel_extensions.frameworks.material.config import MWC_ICONS
from awesome_panel_extensions.web_component import WebComponent

# pylint: disable=abstract-method


class Button(WebComponent):
    """Implementation of mwc-button

    Set the `name` to set the text shown to the user
    Set the `icon` to set the icon shown to the user

    Set `unelevated` or `raised` to change the style
    """

    html = param.String("<mwc-button style='width:100%'></mwc-button")
    attributes_to_watch = param.Dict(
        {
            "label": "name",
            "icon": "icon",
            "raised": "raised",
            "unelevated": "unelevated",
            "disabled": "disabled",
            "trailingIcon": "trailing_icon",
            "class": "_button_css_class",
        }
    )
    events_to_watch = param.Dict({"click": "clicks"})

    button_type = param.ObjectSelector(default="default", objects=BUTTON_TYPES)
    disabled = param.Boolean(default=False)

    icon = param.ObjectSelector(default=None, objects=MWC_ICONS, allow_None=True)
    trailing_icon = param.Boolean(default=False)
    raised = param.Boolean(default=False)
    unelevated = param.Boolean(default=False)

    clicks = param.Integer()

    _button_css_class = param.String()

    height = param.Integer(default=30)

    def __init__(self, **params):
        super().__init__(**params)

        if self.button_type != "default":
            self._handle_button_type_change()

    @param.depends("button_type", watch=True)
    def _handle_button_type_change(self, *_):
        if self.button_type in ["primary", "success", "warning", "danger"]:
            self.param.set_param(raised=True, unelevated=False, _button_css_class=self.button_type)
        else:
            self.param.set_param(
                raised=self.param.raised.default,
                unelevated=self.param.unelevated.default,
                _button_css_class=self.button_type,
            )
