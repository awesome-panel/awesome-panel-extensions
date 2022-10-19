"""The Icon can be used to add SVG based icons to buttons, menus etc."""
# See https://github.com/holoviz/panel/issues/1586 for motivation, possibilities and requirements.

from bokeh.core import properties
from bokeh.models.widgets import AbstractIcon


class Icon(AbstractIcon):
    """The Icon can be used to add SVG based icons to buttons, menus etc."""

    label = properties.String()
    text = properties.String(default="", help="""The text or HTML contents of the widget.""")
    size = properties.Float()
    fill_color = properties.String()
    spin_duration = properties.Int()
