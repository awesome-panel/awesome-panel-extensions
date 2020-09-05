from bokeh.models import Button as _BkButton
from bokeh.core import properties

class FastButton(_BkButton):
    appearance = properties.String(
        default="neutral",
        help="The appearance attribute",
    )
    autofocus = properties.Bool(
        default=False,
        help="The autofocus attribute",
    )