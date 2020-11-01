import panel as pn
import param
from panel.widgets import Button

FAST_BUTTON_APPEARENCES = [
    "accent",
    "lightweight",
    "neutral",
    "outline",
    "light",
]
DEFAULT_FAST_BUTTON_APPEARANCE = "neutral"
BUTTON_TYPE_TO_APPEARANCE = {
    "default": "neutral",
    "primary": "accent",
    "success": "outline",
    "warning": "accent",
    "danger": "accent",
}


class FastButton(Button):
    appearance = param.ObjectSelector(
        default=DEFAULT_FAST_BUTTON_APPEARANCE,
        objects=FAST_BUTTON_APPEARENCES,
        doc="The appearance attribute",
        allow_None=True,
    )
    _rename = {
        **pn.widgets.Button._rename,
        "appearance": None,
    }

    # def __init__(self, **params):
    #     if "button_type" in params and "appearance" not in params:
    #         params["appearance"] = BUTTON_TYPE_TO_APPEARANCE[params["button_type"]]
    #     super().__init__(**params)

    # @param.depends("button_type", watch=True)
    # def _update_accent(self, *_):
    #     self.appearance = BUTTON_TYPE_TO_APPEARANCE[self.button_type]


button = Button(name="Hello World")

pn.Column(
    button,
    pn.Param(button, parameters=["button_type", "clicks", "appearance"]),
).show(port=5007)
