"""The FastButton enables using the `fast-button` with Bokeh."""
from bokeh.core import properties
from bokeh.models import Button as _BkButton


class FastButton(_BkButton):
    """The FastButton enables using the `fast-button` with Bokeh."""

    appearance = properties.String(
        default="neutral",
        help="The appearance attribute",
    )
    autofocus = properties.Bool(
        default=False,
        help="The autofocus attribute",
    )
