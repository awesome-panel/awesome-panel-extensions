# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
# pylint: disable=too-many-statements, not-callable, too-complex, too-many-instance-attributes
# pylint: disable=too-many-branches
import inspect
import math
from datetime import date, datetime

import holoviews as hv
import numpy as np
import pandas as pd
import panel as pn
import param
from holoviews import opts
from panel import widgets as pnw

from awesome_panel_extensions.frameworks.fast import styles
from awesome_panel_extensions.frameworks.fast.templates.fast_list_template import FastListTemplate
from awesome_panel_extensions.widgets.dataframe import get_default_formatters

pn.extension("echarts", "ace")
hv.extension("bokeh")
ACCENT_REST = "#DF3874"


def get_dataframe():
    return pd.DataFrame(np.random.randint(0, 100, size=(25, 4)), columns=list("ABCD"))


PANES = [
    pn.pane.HoloViews,
    pn.pane.ECharts,
]
WIDGETS = [
    pnw.Ace,
    pnw.AutocompleteInput,
    pnw.Button,
    pnw.Checkbox,
    pnw.CheckBoxGroup,
    pnw.CheckButtonGroup,
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
    pnw.FileInput,
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
    pnw.RadioBoxGroup,
    pnw.RadioButtonGroup,
    pnw.RangeSlider,
    pnw.Select,
    pnw.StaticText,
    pnw.TextAreaInput,
    pnw.TextInput,
    pnw.Toggle,
    # pnw.VideoStream,
]
LAYOUTS = [pn.layout.Divider]

COMPONENTS = {"Layout": LAYOUTS, "Pane": PANES, "Widget": WIDGETS}
DEFAULT_COMPONENT_TYPE = "Pane"
DEFAULT_COMPONENT = {
    "Layout": pn.layout.Divider,
    "Pane": pn.pane.HoloViews,
    "Widget": pn.widgets.DataFrame,
}


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
    ).opts(opts.Points(tools=["hover"]))
    plot = (
        clusters
        * hv.Ellipse(2, 2, 2).opts(line_width=3, color=ACCENT_REST)
        * hv.Ellipse(-2, -2, (4, 2)).opts(line_width=3, color=ACCENT_REST)
    )
    return plot


def _create_echarts_plot():
    echart = {
        "tooltip": {},
        "legend": {"data": ["Sales"]},
        "xAxis": {
            "data": ["shirt", "cardign", "chiffon shirt", "pants", "heels", "socks"],
            "axisLine": {"lineStyle": {"color": "#ccc"}},
        },
        "yAxis": {
            "axisLine": {"lineStyle": {"color": "#ccc"}},
        },
        "series": [
            {
                "name": "Sales",
                "type": "bar",
                "data": [
                    1.0,
                    1.2,
                    1.4,
                    1.6,
                    1.8,
                    2.0,
                ],
                "itemStyle": {"color": "#DF3874"},
            }
        ],
        "responsive": True,
    }
    text_style = {"color": "#ccc"}
    update = ["legend", "xAxis", "yAxis"]
    for upd in update:
        echart[upd]["textStyle"] = text_style
    return echart


class PanelComponentExplorer(param.Parameterized):
    component_type = param.ObjectSelector(
        DEFAULT_COMPONENT_TYPE, objects=list(COMPONENTS.keys()), label="Type"
    )
    component = param.ObjectSelector(
        DEFAULT_COMPONENT[DEFAULT_COMPONENT_TYPE], COMPONENTS[DEFAULT_COMPONENT_TYPE]
    )
    update = param.Action()

    def __init__(self, **params):
        super().__init__(**params)
        self._default_component = DEFAULT_COMPONENT.copy()

        self.update = self._update_css_panel
        self.view = self._create_view()
        self.update()
        self._update_css_panel()
        self._update_widgets_panel()

    def _create_view(self):
        self._css_panel = pn.pane.HTML(height=0, width=0, margin=0, sizing_mode="fixed")
        self._settings_panel = pn.Column(
            pn.pane.Markdown("## Selections"),
            pn.Param(
                self,
                parameters=["component_type", "component"],
                expand_button=False,
                show_name=False,
            ),
            self._css_panel,
        )
        self._component_panel = pn.Column()

        self._template = FastListTemplate(
            site="Awesome Panel",
            title="Component Explorer",
            sidebar=[self._settings_panel],
            main=[self._component_panel],
            main_max_width="1024px",
        )
        self._bokeh_theme = self._template.theme.bokeh_theme
        if "Dark" in str(self._template.theme):
            self._theme = "dark"
            self._ace_theme = "tomorrow_night"
        else:
            self._theme = "default"
            self._ace_theme = "tomorrow"
        return self._template

    def _update_css_panel(self, *_):
        if self._theme == "dark":
            style = styles.DARK_CSS
        else:
            style = styles.DEFAULT_CSS
        self._css_panel.object = "<style>" + style + "</style>"

    @pn.depends("component_type", watch=True)
    def _update_component_list(self):
        self.param.component.objects = COMPONENTS[self.component_type]
        self.component = self._default_component[self.component_type]

    @pn.depends("component", watch=True)
    def _update_widgets_panel(self):
        self._default_component[self.component_type] = self.component

        component = None
        controls = None
        if self.component is pn.pane.HoloViews:
            component = pn.pane.HoloViews(_create_hvplot(), theme=self._bokeh_theme)
        if self.component is pn.pane.ECharts:
            # Issue https://github.com/holoviz/panel/issues/1817
            component = pn.pane.ECharts(
                _create_echarts_plot(), min_height=400, min_width=200, sizing_mode="stretch_both"
            )
        if self.component is pnw.Ace:
            py_code = inspect.getsource(_create_hvplot)
            component = pnw.Ace(
                value=py_code,
                sizing_mode="stretch_width",
                language="python",
                height=400,
                theme=self._ace_theme,
            )
        elif self.component is pnw.AutocompleteInput:
            component = pnw.AutocompleteInput(
                name="Autocomplete Input",
                options=["Biology", "Chemistry", "Physics"],
                placeholder="Write something here",
            )
        elif self.component is pnw.Button:
            component = pnw.Button(name="Click me", button_type="primary")
        elif self.component is pnw.CheckBoxGroup:
            component = pnw.CheckBoxGroup(
                name="Checkbox Group",
                value=["Apple", "Pear"],
                options=["Apple", "Banana", "Pear", "Strawberry"],
                inline=True,
            )
        elif self.component is pnw.CheckButtonGroup:
            component = pnw.CheckButtonGroup(
                name="Check Button Group",
                value=["Apple", "Pear"],
                options=["Apple", "Banana", "Pear", "Strawberry"],
                button_type="success",
            )
        elif self.component is pnw.Checkbox:
            component = pnw.Checkbox(name="Checkbox")
        elif self.component is pnw.ColorPicker:
            component = pnw.ColorPicker(name="Color Picker", value="#DF3874")
        elif self.component is pnw.CrossSelector:
            component = pnw.CrossSelector(
                name="Fruits",
                value=["Apple", "Pear"],
                options=["Apple", "Banana", "Pear", "Strawberry"],
                height=300,
            )
        elif self.component is pnw.DataFrame:
            component = self.component(name="Hello")
            component.value = get_dataframe()
            component.formatters = get_default_formatters(component.value)
            controls = pn.Spacer()
        elif self.component is pnw.DatePicker:
            component = pnw.DatePicker(name="Date Picker")
            # Issue: https://github.com/holoviz/panel/issues/1810
            # component.start = date(2020, 1, 20)
            # component.end = date(2020, 2, 20)
            # component.value = date(2020, 2, 18)
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
        elif self.component is pnw.DiscretePlayer:
            component = pnw.DiscretePlayer(
                name="Discrete Player",
                options=[2, 4, 8, 16, 32, 64, 128],
                value=32,
                loop_policy="loop",
            )
        elif self.component is pnw.DiscreteSlider:
            component = pnw.DiscreteSlider(
                name="Discrete Slider", options=[2, 4, 8, 16, 32, 64, 128], value=32
            )
        elif self.component is pnw.FileDownload:
            component = pnw.FileDownload(file="README.md", filename="README.md")
        elif self.component is pnw.FileInput:
            component = pnw.FileInput(accept=".csv,.json")
        elif self.component is pnw.FileSelector:
            component = pnw.FileSelector(name="Hello", max_height=400)
        elif self.component is pnw.FloatInput:
            component = pnw.FloatInput(name="FloatInput", value=5.0, step=1e-1, start=0, end=1000)
        elif self.component is pnw.FloatSlider:
            component = pnw.FloatSlider(
                name="Float Slider", start=0, end=3.141, step=0.01, value=1.57
            )
        elif self.component is pnw.IntInput:
            component = pnw.IntInput(name="IntInput", value=5, step=2, start=0, end=1000)
        elif self.component is pnw.IntRangeSlider:
            component = pnw.IntRangeSlider(
                name="Integer Range Slider", start=0, end=100, value=(8, 40), step=2
            )
        elif self.component is pnw.IntSlider:
            component = pnw.IntSlider(name="Integer Slider", start=0, end=20, step=2, value=4)
        elif self.component is pnw.LiteralInput:
            component = pnw.LiteralInput(
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
            component = pnw.MenuButton(name="Dropdown", items=menu_items, button_type="primary")
        elif self.component is pnw.MultiChoice:
            component = pnw.MultiChoice(
                name="MultiSelect",
                value=["Apple", "Pear"],
                options=["Apple", "Banana", "Pear", "Strawberry"],
            )
        elif self.component is pnw.MultiSelect:
            component = pnw.MultiSelect(
                name="MultiSelect",
                value=["Apple", "Pear"],
                options=["Apple", "Banana", "Pear", "Strawberry"],
                size=8,
            )
        elif self.component is pnw.PasswordInput:
            component = pnw.PasswordInput(
                name="Password Input", placeholder="Enter a string here..."
            )
        elif self.component is pnw.Player:
            component = pnw.Player(name="Player", start=0, end=100, value=32, loop_policy="loop")
        elif self.component is pnw.Progress:
            component = pnw.Progress(name="Progress", value=20, width=200)
        elif self.component is pnw.RadioBoxGroup:
            component = pnw.RadioBoxGroup(
                name="RadioBoxGroup", options=["Biology", "Chemistry", "Physics"], inline=True
            )
        elif self.component is pnw.RadioButtonGroup:
            component = pnw.RadioButtonGroup(
                name="Radio Button Group",
                options=["Biology", "Chemistry", "Physics"],
                button_type="success",
            )
        elif self.component is pnw.RangeSlider:
            component = pnw.RangeSlider(
                name="Range Slider",
                start=0,
                end=math.pi,
                value=(math.pi / 4.0, math.pi / 2.0),
                step=0.01,
            )
        elif self.component is pnw.Select:
            component = pnw.Select(name="Select", options=["Biology", "Chemistry", "Physics"])
        elif self.component is pnw.StaticText:
            component = pnw.StaticText(name="Static Text", value="A string")
        elif self.component is pnw.TextAreaInput:
            component = pnw.input.TextAreaInput(
                name="Text Area Input", placeholder="Enter a string here..."
            )
        elif self.component is pnw.TextInput:
            component = pnw.TextInput(name="Text Input", placeholder="Enter a string here...")
        elif self.component == pnw.Toggle:
            component = pnw.Toggle(name="Toggle", button_type="success")
        elif self.component == pnw.VideoStream:
            component = pnw.VideoStream(
                name="Video Stream", sizing_mode="stretch_width", height=300
            )
        if not component:
            component = self.component(name="Hello")
        if not controls:
            controls = component.controls()
        controls.margin = 0
        self._component_panel[:] = [
            pn.pane.Markdown("## " + component.__class__.name + " " + self.component_type),
            component,
            pn.layout.Divider(),
            pn.pane.Markdown("## Parameters"),
            controls,
        ]


def view():
    """Returns a small app for testing"""
    pn.config.sizing_mode = "stretch_width"
    return PanelComponentExplorer().view


if __name__.startswith("bokeh"):
    pn.config.sizing_mode = "stretch_width"
    app = PanelComponentExplorer()
    pn.state.add_periodic_callback(app._update_css_panel, period=1000)
    app.view.servable()
