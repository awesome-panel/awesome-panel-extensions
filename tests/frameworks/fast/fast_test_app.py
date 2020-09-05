from typing import List
import panel as pn
from awesome_panel_extensions.frameworks.fast import FastTemplate

def create_fast_test_app(component, parameters: List) -> pn.Column:
    parameters=[
                # Old
                "name",
                "height",
                "width",
                "margin",
                "sizing_mode",
                *parameters,
            ]
    parameters = list(set(parameters))
    app = pn.Column(
        pn.Column(
            pn.pane.SVG("https://explore.fast.design/e1e15bd85334e4346744078af2f52308.svg", height=100),
            pn.Spacer(height=25),
            pn.pane.PNG("https://panel.holoviz.org/_static/logo_horizontal.png", height=100),
        ),
        pn.Spacer(height=10),
        pn.pane.HTML("<fast-divider></fast-divider>", sizing_mode="stretch_width", height=25),
        component,
        pn.Spacer(height=10),
        pn.pane.HTML("<fast-divider></fast-divider>", sizing_mode="stretch_width", height=25),
        pn.Param(
            component,
            parameters=parameters,
            show_name=False,
        ),
    )

    return FastTemplate(main=[app])