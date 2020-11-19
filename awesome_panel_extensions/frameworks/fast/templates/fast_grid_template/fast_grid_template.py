"""
React template
"""
import pathlib

import panel as pn
import param
from bokeh.themes import Theme as _BkTheme
from panel.template.theme import DarkTheme, DefaultTheme

from awesome_panel_extensions.frameworks.fast.templates import theme

from .grid_base_template import GridBaseTemplate


def _get_theme_from_query_args(default: str = "default") -> str:
    theme_arg = pn.state.session_args.get("theme", default)
    if isinstance(theme_arg, list):
        theme_arg = theme_arg[0].decode("utf-8")
        theme_arg = theme_arg.strip("'").strip('"')
    return theme_arg


class FastGridTemplate(GridBaseTemplate):
    """
    The FastTemplate is build on top of Fast.design and the React Grid Layout.
    """

    enable_theme_toggle = param.Boolean(
        default=True, doc="If True a switch is to toggle the Theme. Default is True"
    )

    def __init__(self, **params):
        if "theme" not in params:
            _theme = "dark"
            if params.get("enable_theme_toggle", self.param.enable_theme_toggle.default):
                _theme = _get_theme_from_query_args(default=_theme)
            if _theme == "default":
                params["theme"] = FastDefaultTheme
            else:
                params["theme"] = FastDarkTheme

        super().__init__(**params)

        if "header_color" not in params:
            self.header_color = self.theme.style.header_color
        if "header_background" not in params:
            self.header_background = self.theme.style.header_background
        self._update_special_render_vars()

    def _update_special_render_vars(self):
        self._render_variables["css_base"] = pathlib.Path(self._css).read_text()
        self._render_variables["css_theme"] = pathlib.Path(self.theme.css).read_text()
        self._render_variables["js"] = pathlib.Path(self._js).read_text()
        if self.theme is FastDarkTheme:
            self._render_variables["theme"] = "dark"
        else:
            self._render_variables["theme"] = "default"
        self._render_variables["style"] = self.theme.style
        self._render_variables["enable_theme_toggle"] = self.enable_theme_toggle

    _css = pathlib.Path(__file__).parent / "fast_grid_template.css"
    _js = pathlib.Path(__file__).parent / "fast_grid_template.js"

    _template = pathlib.Path(__file__).parent / "fast_grid_template.html"


class FastDefaultTheme(DefaultTheme):
    """The Default Theme of the Fast templates"""

    css = param.Filename(default=pathlib.Path(__file__).parent / "default.css")

    _template = FastGridTemplate

    style = param.ClassSelector(class_=theme.FastStyle, default=theme.DEFAULT_STYLE)

    bokeh_theme = param.ClassSelector(
        class_=(_BkTheme, str), default=_BkTheme(json=theme.DEFAULT_THEME)
    )


class FastDarkTheme(DarkTheme):
    """The Dark Theme of the Fast Templates"""

    css = param.Filename(default=pathlib.Path(__file__).parent / "dark.css")

    _template = FastGridTemplate

    style = param.ClassSelector(class_=theme.FastStyle, default=theme.DARK_STYLE)

    bokeh_theme = param.ClassSelector(
        class_=(_BkTheme, str), default=_BkTheme(json=theme.DARK_THEME)
    )
