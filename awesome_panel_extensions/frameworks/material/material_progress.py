import param

from awesome_panel_extensions.frameworks._base.progress import Progress as _BaseProgress
from awesome_panel_extensions.frameworks._base.config import PROGRESS_TYPES
from awesome_panel_extensions.web_component import WebComponent

_ATTRIBUTES_TO_WATCH_BASE = {"class": "bar_color"}
_PROPERTIES_TO_WATCH_BASE = {
    "indeterminate": "active",
    "progress": "_progress",
    "closed": "closed",
}

DENSITY_RATIO = 4

class _MaterialProgress(_BaseProgress):
    closed = param.Boolean(
        default=False,
        doc="""Sets the progress indicator to the closed state. Sets content opacity to 0.
        Typically should be set to true when loading has finished.""",
    )
    _progress = param.Number(default=None, bounds=(0, 1), allow_None=True)

    attributes_to_watch = param.Dict(_ATTRIBUTES_TO_WATCH_BASE)
    properties_to_watch = param.Dict(_PROPERTIES_TO_WATCH_BASE)

    def __init__(self, **params):
        # Hack: to make sure that value is shown on construction
        if "value" in params and not "active" in params:
            params["active"] = False

        super().__init__(**params)

        self._update_progress()

    @param.depends("value", "max", watch=True)
    def _update_progress(self, *events):
        if self.value is None or self.value == 0 or self.max is None or self.max == 0:
            self._progress = None
        else:
            self._progress = self.value / self.max


class LinearProgress(_MaterialProgress):
    html = param.String(
        "<mwc-linear-progress style='width:100%' progress='0.0'></mwc-linear-progress"
    )

    buffer = param.Integer(
        default=None,
        bounds=(0, 100),
        allow_None=True,
        doc="""Sets the buffer progress bar's value. Value should be between [0, 1].
            Setting this value to be less than max will reveal moving, buffering dots.""",
    )

    _buffer = param.Number(default=None, allow_None=True,)
    reverse = param.Boolean(
        default=False, doc="Reverses the direction of the linear progress indicator."
    )

    properties_to_watch = param.Dict(
        {**_PROPERTIES_TO_WATCH_BASE, "buffer": "_buffer", "reverse": "reverse"}
    )

    @param.depends("max", watch=True)
    def _update_buffer_bounds(self):
        self.param.buffer.bounds = (0, self.max)

    @param.depends("buffer", "max", watch=True)
    def _update_buffer(self, *events):
        if self.buffer is None or self.buffer == 0 or self.max is None or self.max == 0:
            self._buffer = None
        else:
            self._buffer = self.buffer / self.max


class CircularProgress(_MaterialProgress):
    html = param.String("<mwc-circular-progress style='width:51px'></mwc-circular-progress")

    density = param.Integer(
        default=0,
        bounds=(-8, 2000),
        doc="""Sets the progress indicator's sizing based on density scale. Minimum value is -8.
        Each unit change in density scale corresponds to 4px change in side dimensions. The stroke
        width adjusts automatically.""",
    )
    # _style = param.String()

    # attributes_to_watch = param.Dict(dict(**_ATTRIBUTES_TO_WATCH_BASE, style="_style"))
    properties_to_watch = param.Dict(dict(**_PROPERTIES_TO_WATCH_BASE, density="density"))

    def __init__(self, **params):
        if "density" in params and not "html" in params:
            density = params["density"]
            diameter = round((density+8)*DENSITY_RATIO+17)
            html = f"<mwc-circular-progress style='height:{diameter}px;width:{diameter}px' density={density}></mwc-circular-progress"
            params["html"]=html

        super().__init__(**params)

        self._update_diameter()

    @param.depends("density", watch=True)
    def _update_diameter(self, *events):
        diameter = round((self.density+8)*DENSITY_RATIO+17)
        self.min_height=diameter
        self.min_width=diameter
        # Cannot get the style updating programmatically. Starts an infinite loop.
        # self._style = f"height:{diameter}px;width:{diameter}px;"
