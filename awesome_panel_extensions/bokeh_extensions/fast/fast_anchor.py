"""The FastAnchor wraps the fast-anchor component"""
from bokeh.core import properties
from bokeh.models import Widget


class FastAnchor(Widget):
    """Bokeh model wrapping the fast-anchor component"""

    appearance = properties.String()
    download = properties.String()
    href = properties.String()
    hreflang = properties.String()
    ping = properties.String()
    referrerpolicy = properties.String()
    referrer = properties.String()  # cannot call this ref
    rel = properties.String()
    target = properties.String()
    mimetype = properties.String()
