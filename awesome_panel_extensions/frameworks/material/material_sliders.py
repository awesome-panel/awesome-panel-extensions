"""Implementation of MWC Material Slider"""
import panel as pn
import param

from awesome_panel_extensions.web_component import WebComponent

# pylint: disable=abstract-method

MWC_SLIDER_HTML = """
<mwc-slider style="width:100%"></mwc-slider>
"""

class IntSlider(WebComponent):
    """Implementation of mwc-slider for Integers

    You can change the behaviour by changing the `bounds` and `step` value.
    """

    value = param.Integer(
        default=0,
        doc="Current value of the slider."
    )
    start = param.Integer(
        default=0,
        doc="Minimum value of the slider."
        )
    end = param.Integer(
        default=1,
        doc="Maximum value of the slider."
    )
    step = param.Integer(
        default=1,
        bounds=(0,None),
        doc="""When defined, the slider will quantize (round to the nearest multiple) all values
        to match that step value, except for the minimum and maximum values, which can always be
        set. When 0, quantization is disabled. NOTE: Throws when <0."""
    )

    pin = param.Boolean(
        doc="Shows the thumb pin on a discrete slider."
    )
    markers = param.Boolean(
        doc="Shows the tick marks for each step on the track when the slider is discrete."
    )

    # height = param.Integer(default=50)

    html = param.String(MWC_SLIDER_HTML)
    attributes_to_watch = param.Dict({"min": "start", "max": "end", "step": "step", "pin": "pin", "markers": "markers"})
    properties_to_watch = param.Dict({"value": "value"})
    events_to_watch = param.Dict({"change": None})

    def __init__(self, **params):
        super().__init__(**params)

        if self.pin:
            self._update_margin()

    @param.depends("pin", watch=True)
    def _update_margin(self, *events):
        if self.pin:
            self.margin=(25,5,10,5)
        else:
            self.margin=(5, 10)

class FloatSlider(WebComponent):
    """Implementation of mwc-slider for Integers

    You can change the behaviour by changing the `bounds` and `step` value.
    """

    value = param.Number(
        default=0.0,
        doc="Current value of the slider."
    )
    start = param.Number(
        default=0.0,
        doc="Minimum value of the slider."
        )
    end = param.Number(
        default=1.0,
        doc="Maximum value of the slider."
    )
    step = param.Number(
        default=0.1,
        bounds=(0,None),
        doc="""When defined, the slider will quantize (round to the nearest multiple) all values
        to match that step value, except for the minimum and maximum values, which can always be
        set. When 0, quantization is disabled. NOTE: Throws when <0."""
    )

    height = param.Integer(default=50)

    html = param.String(MWC_SLIDER_HTML)
    properties_to_watch = param.Dict({"value": "value", "min": "start", "max": "end", "step": "step"})