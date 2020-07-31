"""Implementation of MWC Material Slider"""
import panel as pn
import param

from awesome_panel_extensions.web_component import WebComponent

# pylint: disable=abstract-method

MWC_SLIDER_HTML = """
<mwc-slider
    step="5"
    pin
    markers
    max="50"
    value="10">
</mwc-slider>
"""

class MWCSlider(WebComponent):
    """Implementation of mwc-slider

    You can change the behaviour by changing the `bounds` and `step` value.
    """

    html = param.String(MWC_SLIDER_HTML)
    properties_to_watch = param.Dict({"value": "value"})

    value = param.Integer(default=10, bounds=(0, 50), step=5)
    height = param.Integer(default=50)