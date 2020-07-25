"""Implementation of MWC Material Button"""
import panel as pn
import param

from awesome_panel_extensions.pane import WebComponent

from .config import MWC_ICONS

# pylint: disable=abstract-method

class Button(WebComponent):
    """Implementation of mwc-button

    Set the `name` to set the text shown to the user
    Set the `icon` to set the icon shown to the user

    Set `unelevated` or `raised` to change the style
    """

    html = param.String("<mwc-button style='width:100%;></mwc-button")
    attributes_to_watch = param.Dict(
        {"label": "name", "icon": "icon", "raised": "raised", "unelevated": "unelevated"}
    )
    events_to_watch = param.Dict({"click": "clicks"})

    icon = param.ObjectSelector(default=None, objects=MWC_ICONS, allow_None=True)
    raised = param.Boolean(default=False)
    unelevated = param.Boolean(default=True)

    clicks = param.Integer()

    height = param.Integer(default=30)

    # NEW IN THIS EXAMPLE

