"""
React template
"""
import pathlib

import param
from bokeh.themes import Theme as _BkTheme
from panel.depends import depends
from panel.layout import Card, GridSpec
from panel.template.base import BasicTemplate
from panel.template.theme import DarkTheme, DefaultTheme

from awesome_panel_extensions.frameworks.fast.templates import theme


class FastTemplate(BasicTemplate):
    """
    The FastTemplate is build on top of Fast.design and the React Grid Layout.
    """

    compact = param.ObjectSelector(default=None, objects=[None, "vertical", "horizontal", "both"])

    cols = param.Dict(default={"lg": 12, "md": 10, "sm": 6, "xs": 4, "xxs": 2})

    breakpoints = param.Dict(default={"lg": 1200, "md": 996, "sm": 768, "xs": 480, "xxs": 0})

    main = param.ClassSelector(
        class_=GridSpec,
        constant=True,
        doc="""
        A list-like container which populates the main area.""",
    )

    row_height = param.Integer(default=150)

    enable_theme_selection = param.Boolean(
        default=True,
        doc="""If True it will be possible for the
    user to toggle between the 'default' and 'dark' theme. Default""",
    )

    _css = pathlib.Path(__file__).parent / "fast_grid.css"

    _js = pathlib.Path(__file__).parent / "fast_grid.js"

    _template = pathlib.Path(__file__).parent / "fast_grid.html"

    _modifiers = {Card: {"children": {"margin": (20, 20)}, "margin": (10, 5)}}

    _resources = {
        "js": {
            "react": "https://unpkg.com/react@16/umd/react.development.js",
            "react-dom": "https://unpkg.com/react-dom@16/umd/react-dom.development.js",
            "babel": "https://unpkg.com/babel-standalone@latest/babel.min.js",
            "react-grid": "https://cdnjs.cloudflare.com/ajax/libs/react-grid-layout/1.1.1/react-grid-layout.min.js",
        },
        "css": {},
    }

    def __init__(self, **params):
        if "main" not in params:
            params["main"] = GridSpec(ncols=12, mode="override")
        super().__init__(**params)
        self._update_render_vars()
        self._update_special_render_vars()

    def _update_special_render_vars(self):
        self._render_variables["css_base"] = pathlib.Path(self._css).read_text()
        self._render_variables["css_theme"] = pathlib.Path(self.theme.css).read_text()
        if self.theme is FastDarkTheme:
            self._render_variables["theme"] = "dark"
        else:
            self._render_variables["theme"] = "default"
        self._render_variables["style"]=self.theme.style

    def _update_render_items(self, event):
        super()._update_render_items(event)
        if event.obj is not self.main:
            return
        layouts = []
        for i, ((y0, x0, y1, x1), v) in enumerate(self.main.objects.items()):
            if x0 is None:
                x0 = 0
            if x1 is None:
                x1 = 12
            if y0 is None:
                y0 = 0
            if y1 is None:
                y1 = self.main.nrows
            layouts.append({"x": x0, "y": y0, "w": x1 - x0, "h": y1 - y0, "i": str(i + 1)})
        self._render_variables["layouts"] = {"lg": layouts, "md": layouts}

    @depends("cols", "breakpoints", "row_height", "compact", watch=True)
    def _update_render_vars(self):
        self._render_variables["breakpoints"] = self.breakpoints
        self._render_variables["cols"] = self.cols
        self._render_variables["rowHeight"] = self.row_height
        self._render_variables["compact"] = self.compact


class FastDefaultTheme(DefaultTheme):

    css = param.Filename(default=pathlib.Path(__file__).parent / "default.css")

    _template = FastTemplate

    style = param.ClassSelector(class_=theme.FastStyle, default=theme.DEFAULT_STYLE)

    bokeh_theme = param.ClassSelector(
        class_=(_BkTheme, str), default=_BkTheme(json=theme.DEFAULT_THEME)
    )


class FastDarkTheme(DarkTheme):

    css = param.Filename(default=pathlib.Path(__file__).parent / "dark.css")

    _template = FastTemplate

    style = param.ClassSelector(class_=theme.FastStyle, default=theme.DARK_STYLE)

    bokeh_theme = param.ClassSelector(
        class_=(_BkTheme, str), default=_BkTheme(json=theme.DARK_THEME)
    )
