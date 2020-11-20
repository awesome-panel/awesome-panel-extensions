# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pathlib

import holoviews as hv
import numpy as np
import panel as pn
from holoviews import opts

from awesome_panel_extensions.frameworks.fast import (
    FastButton,
    FastCheckbox,
    FastSwitch,
    FastTextAreaInput,
    FastTextInput,
)
from awesome_panel_extensions.frameworks.fast.templates.fast_grid_template import FastGridTemplate

hv.extension("bokeh")
opts.defaults(opts.Ellipse(line_width=3, color="#DF3874"))

ROOT = pathlib.Path(__file__).parent
COLLAPSED_SVG_ICON = """
<svg style="stroke: #E62F63" width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" slot="collapsed-icon">
            <path d="M15.2222 1H2.77778C1.79594 1 1 1.79594 1 2.77778V15.2222C1 16.2041 1.79594 17 2.77778 17H15.2222C16.2041 17 17 16.2041 17 15.2222V2.77778C17 1.79594 16.2041 1 15.2222 1Z" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M9 5.44446V12.5556" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M5.44446 9H12.5556" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
"""

EXPANDED_SVG_ICON = """
<svg style="stroke: #E62F63" width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" slot="expanded-icon">
    <path d="M15.2222 1H2.77778C1.79594 1 1 1.79594 1 2.77778V15.2222C1 16.2041 1.79594 17 2.77778 17H15.2222C16.2041 17 17 16.2041 17 15.2222V2.77778C17 1.79594 16.2041 1 15.2222 1Z" stroke-linecap="round" stroke-linejoin="round"></path>
    <path d="M5.44446 9H12.5556" stroke-linecap="round" stroke-linejoin="round"></path>
</svg>
"""
LINKS = ROOT / "fixtures/links.html"


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
    return plot.opts(title="HoloViews Plot")


def _navigation_menu():
    links = (
        LINKS.read_text()
        .replace("{{ collapsed_icon }}", COLLAPSED_SVG_ICON)
        .replace("{{ expanded_icon }}", EXPANDED_SVG_ICON)
    )

    return pn.pane.HTML(links)


def _sidebar_items():
    return [
        pn.pane.Markdown("## Settings"),
        FastButton(name="Click Me"),
        FastCheckbox(name="Check Me"),
        FastSwitch(value=True, checked_message="Checked", unchecked_message="Unchecked"),
        _navigation_menu(),
    ]


def test_simple_app():
    FastGridTemplate(
        title="Fast Template",
    )


def test_theme_toggle():
    enabled = FastGridTemplate(title="Fast Template", enable_theme_toggle=True)
    assert enabled.enable_theme_toggle
    assert enabled._render_variables["enable_theme_toggle"]
    disabled = FastGridTemplate(title="Fast Template", enable_theme_toggle=False)
    assert not disabled.enable_theme_toggle
    assert not disabled._render_variables["enable_theme_toggle"]


def test_app():
    pn.config.sizing_mode = "stretch_width"
    # theme_arg = pn.state.session_args.get("theme", "dark")
    # if isinstance(theme_arg, list):
    #     theme_arg = theme_arg[0].decode("utf-8")
    #     theme_arg = theme_arg.strip("'").strip('"')
    # if theme_arg == "dark":
    #     theme = FastDarkTheme
    # else:
    #     theme = FastDefaultTheme
    app = FastGridTemplate(
        title="Fast Template",
        enable_theme_toggle=True,
    )
    assert app._render_variables["enable_theme_toggle"] is True
    app.main[0:2, 0:6] = pn.pane.HoloViews(_create_hvplot(), sizing_mode="stretch_both")
    app.main[0:2, 6:12] = pn.pane.HoloViews(_create_hvplot(), sizing_mode="stretch_both")
    # app.main[0:2, 6:12] = pn.layout.Card(
    #     hvplot_pane, header="BOKEH via HOLOVIEWS", sizing_mode="stretch_both"
    # )
    app.main[2:4, 0:12] = pn.pane.Markdown("Hello World", sizing_mode="stretch_both")
    app.main[4:6, 0:6] = pn.Column(
        FastTextInput(value="text", name="Text"),
        FastTextAreaInput(value="text " * 10, name="Text"),
        sizing_mode="stretch_both",
    )
    app.sidebar.extend(_sidebar_items())
    return app


if __name__.startswith("bokeh"):
    test_app().servable()
