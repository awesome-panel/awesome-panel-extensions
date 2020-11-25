from datetime import date, datetime
import pathlib

import holoviews as hv
import numpy as np
from numpy.lib.arraysetops import isin
import panel as pn
import param
from holoviews import opts
from panel import widgets as pnw
import pandas as pd
from awesome_panel_extensions.frameworks.fast import FastGridTemplate
from awesome_panel_extensions.widgets.dataframe import get_default_formatters

hv.extension("bokeh")


def get_dataframe():
    return pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list("ABCD"))


ROOT = pathlib.Path.cwd() / "awesome_panel_extensions/frameworks/fast/templates/assets"

CSS_FILES = [
    "fast_root.css",
    "bokeh.css",
    "bokeh_tabs.css",
    "widgets.css",
    "slickgrid.css",
    "bokeh_slider.css",
    "bokeh_multichoice.css",
    "bokeh_inputrange.css",
]
COMPONENTS = [
    pnw.Button,
    pnw.Checkbox,
    pnw.ColorPicker,
    pnw.CrossSelector,
    pnw.DataFrame,
    pnw.DatePicker,
    pnw.DateRangeSlider,
    pnw.DateSlider,
    pnw.DatetimeInput,
    pnw.DatetimeRangeInput,
    pnw.DiscretePlayer,
    pnw.DiscreteSlider,
    pnw.FileDownload,
    pnw.FileSelector,
    pnw.FloatInput,
    pnw.FloatSlider,
    pnw.IntInput,
    pnw.IntRangeSlider,
    pnw.IntSlider,
    pnw.LiteralInput,
    pnw.MenuButton,
    pnw.MultiChoice,
    pnw.MultiSelect,
    pnw.PasswordInput,
    pnw.Player,
    pnw.Progress,
]
DEFAULT_COMPONENT = pnw.Progress

opts.defaults(opts.Ellipse(line_width=3, color="#DF3874"))
opts.defaults(opts.Points(tools=["hover"]))


def _create_hvplot():
    # Generate some data
    cl1 = np.random.normal(loc=2, scale=0.2, size=(200, 200))
    cl2x = np.random.normal(loc=-2, scale=0.6, size=200)
    cl2y = np.random.normal(loc=-2, scale=0.1, size=200)
    cl3 = np.random.normal(loc=0, scale=1.5, size=(400, 400))
    # Create an overlay of points and ellipses
    clusters = (
        hv.Points(cl1).opts(color="blue")
        * hv.Points((cl2x, cl2y)).opts(color="green")
        * hv.Points(cl3).opts(color="#FDDC22")
    )
    plot = clusters * hv.Ellipse(2, 2, 2) * hv.Ellipse(-2, -2, (4, 2))
    return plot


class CSSDesigner(param.Parameterized):
    css_files = param.List(CSS_FILES)
    component = param.ObjectSelector(DEFAULT_COMPONENT, COMPONENTS)
    update = param.Action()

    def __init__(self, **params):
        super().__init__(**params)

        self.update = self._update_css_panel
        self.view = self._create_view()
        self.update()
        self._update_css_panel()
        self._update_widgets_panel()
        pn.state.add_periodic_callback(self._update_css_panel, period=1000)

    def _create_view(self):
        self._css_panel = pn.pane.HTML(height=0, width=0, margin=0, sizing_mode="fixed")
        self._settings_panel = pn.Column(
            pn.Param(self, parameters=["component", "update"], expand_button=False),
            self._css_panel,
        )
        self._widgets_panel = pn.Column()

        template = FastGridTemplate(title="Designer", sidebar=[self._settings_panel])
        template.main[0:20, 0:12] = self._widgets_panel
        template.main[20:30, 0:12] = pn.pane.HoloViews(_create_hvplot())
        return template

    def _update_css_panel(self, *_):
        css = [(ROOT / file).read_text() for file in self.css_files]
        self._css_panel.object = "<style>" + "".join(css) + "</style>"

    @pn.depends("component", watch=True)
    def _update_widgets_panel(self):
        component = None
        controls = None
        if self.component is pnw.DataFrame:
            component = self.component(name="Hello")
            component.value = get_dataframe()
            component.formatters = get_default_formatters(component.value)
            controls = pn.Spacer()
        elif self.component is pnw.DateRangeSlider:
            component = self.component(name="Hello")
            component.start = date(2020, 1, 20)
            component.end = date(2020, 2, 20)
            component.value = (date(2020, 2, 18), date(2020, 2, 20))
        elif self.component is pnw.DateSlider:
            component = self.component(name="Hello")
            component.start = date(2020, 1, 20)
            component.end = date(2020, 2, 20)
            component.value = date(2020, 2, 18)
        elif self.component is pnw.DatetimeInput:
            component = self.component(name="Hello")
            component.value = datetime(2020, 2, 18, 1, 2, 3)
        elif self.component is pnw.DatetimeRangeInput:
            component = self.component(
                name="Hello",
                start=datetime(2020, 1, 20),
                end=datetime(2020, 2, 20),
                value=(datetime(2020, 2, 18), datetime(2020, 2, 20)),
            )
        elif self.component is pnw.DiscreteSlider:
            component = pnw.DiscreteSlider(
                name="Discrete Slider", options=[2, 4, 8, 16, 32, 64, 128], value=32
            )
        elif self.component is pnw.FloatInput:
            component = pn.widgets.FloatInput(
                name="FloatInput", value=5.0, step=1e-1, start=0, end=1000
            )
        elif self.component is pnw.FloatSlider:
            component = pn.widgets.FloatSlider(
                name="Float Slider", start=0, end=3.141, step=0.01, value=1.57
            )
        elif self.component is pnw.IntInput:
            component = pn.widgets.IntInput(name="IntInput", value=5, step=2, start=0, end=1000)
        elif self.component is pnw.IntRangeSlider:
            component = pn.widgets.IntRangeSlider(
                name="Integer Range Slider", start=0, end=100, value=(8, 40), step=2
            )
        elif self.component is pnw.IntSlider:
            component = pn.widgets.IntSlider(
                name="Integer Slider", start=0, end=20, step=2, value=4
            )
        elif self.component is pnw.LiteralInput:
            component = pn.widgets.LiteralInput(
                name="Literal Input (dict)", value={"key": [1, 2, 3]}, type=dict
            )
        elif self.component is pnw.MenuButton:
            menu_items = [
                ("Option A", "a"),
                ("Option B", "b"),
                ("Option C", "c"),
                None,
                ("Help", "help"),
            ]
            component = pn.widgets.MenuButton(
                name="Dropdown", items=menu_items, button_type="primary"
            )
        elif self.component is pnw.MultiChoice:
            component = pn.widgets.MultiChoice(
                name="MultiSelect",
                value=["Apple", "Pear"],
                options=["Apple", "Banana", "Pear", "Strawberry"],
            )
        elif self.component is pnw.MultiSelect:
            component = pn.widgets.MultiSelect(
                name="MultiSelect",
                value=["Apple", "Pear"],
                options=["Apple", "Banana", "Pear", "Strawberry"],
                size=8,
            )
        elif self.component is pnw.PasswordInput:
            component = pn.widgets.PasswordInput(
                name="Password Input", placeholder="Enter a string here..."
            )
        elif self.component is pnw.Player:
            component = pn.widgets.Player(name='Player', start=0, end=100, value=32, loop_policy='loop')
        elif self.component is pnw.Progress:
            component = pn.widgets.Progress(name='Progress', value=20, width=200)
        if not component:
            component = self.component(name="Hello")
        if not controls:
            controls = component.controls()
        self._widgets_panel[:] = [
            pn.pane.Markdown("## Panel " + component.__class__.name),
            component,
            pn.layout.HSpacer(height=25),
            controls,
        ]


def view():
    pn.config.sizing_mode = "stretch_width"
    return CSSDesigner().view


if __name__.startswith("bokeh"):
    view().servable()
