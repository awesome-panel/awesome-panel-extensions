"""The SVGIcon can be used to add SVG based icons to buttons, menus etc."""
# See https://github.com/holoviz/panel/issues/1586 for motivation, possibilities and requirements.

from bokeh.core import properties
from bokeh.models.widgets import AbstractIcon

class SVGIcon(AbstractIcon):
    """The SVGIcon can be used to add SVG based icons to buttons, menus etc."""

    icon_name = properties.String()
    svg = properties.String()
    size = properties.Float()
    fill_color = properties.String()
    spin_duration = properties.Int()
