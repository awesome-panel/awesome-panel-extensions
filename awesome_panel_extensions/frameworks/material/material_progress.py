import param

from awesome_panel_extensions.frameworks._base.progress import Progress as _BaseProgress
from awesome_panel_extensions.frameworks._base.config import PROGRESS_TYPES
from awesome_panel_extensions.web_component import WebComponent

class _MaterialProgress(_BaseProgress):
    density = param.Integer(
        default=0,
        bounds=(-8,10),
        doc="""Sets the progress indicator's sizing based on density scale. Minimum value is -8.
        Each unit change in density scale corresponds to 4px change in side dimensions. The stroke
        width adjusts automatically."""
        )
    closed = param.Boolean(
        default=False,
        doc="""Sets the progress indicator to the closed state. Sets content opacity to 0.
        Typically should be set to true when loading has finished."""
    )
    _value = param.Number(default=None, bounds=(0,1), allow_None=True)
    _class = param.String()

    attributes_to_watch = param.Dict(
        {
            "indeterminate": "active",
            "progress": "_value",

            "density": "density",
            "closed": "closed",

            "class": "_class",
        }
    )

    def __init__(self, **params):
        super().__init__(**params)

        self._update_value()
        self._update_css_classes()

    @param.depends("bar_color", watch=True)
    def _update_css_classes(self, *events):
        if self.css_classes is None:
            css_classes = []
        else:
            css_classes = [
                item for item in self.css_classes if item not in self.param.bar_color.objects
            ]
        css_classes.append(self.bar_color)
        self.css_classes = css_classes

    @param.depends("value", "max", watch=True)
    def _update_value(self, *events):
        if self.value is None or self.max is None or self.max==0:
            self._value = None
        else:
            self._value = self.value/self.max



class LinearProgress(_MaterialProgress):
    html = param.String("<mwc-linear-progress style='width:100%'></mwc-linear-progress")

class CircularProgress(_MaterialProgress):
    html = param.String("<mwc-circular-progress style='width:100%'></mwc-circular-progress")