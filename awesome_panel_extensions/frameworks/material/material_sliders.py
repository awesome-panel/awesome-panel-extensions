"""Implementation of MWC Material Slider"""
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

    value = param.Integer(default=0, doc="Current value of the slider.")
    start = param.Integer(default=0, doc="Minimum value of the slider.")
    end = param.Integer(default=1, doc="Maximum value of the slider.")
    step = param.Integer(
        default=1,
        bounds=(0, None),
        doc="""When defined, the slider will quantize (round to the nearest multiple) all values
        to match that step value, except for the minimum and maximum values, which can always be
        set. When 0, quantization is disabled. NOTE: Throws when <0.""",
    )

    pin = param.Boolean(doc="Shows the thumb pin on a discrete slider.")
    markers = param.Boolean(
        doc="Shows the tick marks for each step on the track when the slider is discrete."
    )

    # height = param.Integer(default=50)

    html = param.String(MWC_SLIDER_HTML)
    attributes_to_watch = param.Dict(
        {"min": "start", "max": "end", "step": "step", "pin": "pin", "markers": "markers"}
    )
    properties_to_watch = param.Dict({"value": "value"})
    events_to_watch = param.Dict({"change": None})

    height = param.Integer(default=50)

    def __init__(self, **params):
        super().__init__(**params)

        if self.pin:
            self._update_margin()

    @param.depends("pin", watch=True)
    def _update_margin(self, *_):
        if self.pin:
            self.margin = (25, 5, 10, 5)
        else:
            self.margin = (5, 10)


class FloatSlider(WebComponent):
    """Implementation of mwc-slider for Integers

    You can change the behaviour by changing the `bounds` and `step` value.
    """

    value = param.Number(default=0.0, doc="Current value of the slider.")
    start = param.Number(default=0.0, doc="Minimum value of the slider.")
    end = param.Number(default=1.0, doc="Maximum value of the slider.")
    step = param.Number(
        default=0.1,
        bounds=(0.0, None),
        doc="""When defined, the slider will quantize (round to the nearest multiple) all values
        to match that step value, except for the minimum and maximum values, which can always be
        set. When 0, quantization is disabled. NOTE: Throws when <0.""",
    )

    pin = param.Boolean(doc="Shows the thumb pin on a discrete slider.")
    markers = param.Boolean(
        doc="Shows the tick marks for each step on the track when the slider is discrete."
    )

    # height = param.Integer(default=50)

    html = param.String(MWC_SLIDER_HTML)
    attributes_to_watch = param.Dict(
        {"min": "_start", "max": "_end", "step": "_step", "pin": "pin", "markers": "markers"}
    )
    properties_to_watch = param.Dict({"value": "value"})
    events_to_watch = param.Dict({"change": None})

    height = param.Integer(default=50)

    _value = param.Number(default=0)
    _start = param.Number(default=0)
    _end = param.Number(default=10)
    _step = param.Number(default=1)

    def __init__(self, **params):
        super().__init__(**params)

        if self.pin:
            self._update_margin()

    @param.depends("pin", watch=True)
    def _update_margin(self, *_):
        if self.pin:
            self.margin = (25, 5, 10, 5)
        else:
            self.margin = (5, 10)

    @param.depends("value", "start", "end", "step", watch=True)
    def _update_parameters(self, *_):
        value = self.value
        start = self.start
        end = self.end
        step = self.step

        _value = round(value / step)
        _start = round(start / step)
        _end = round(end / step)
        _step = round(step / step)

        self.param.set_param(_value=_value, _start=_start, _end=_end, _step=_step)
