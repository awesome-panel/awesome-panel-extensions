from typing import List
import panel as pn
from awesome_panel_extensions.frameworks.fast import FastTemplate

FAST_LOGO_HTML = """\
<a href="https://fast.design" target="_blank">
    <img src="https://explore.fast.design/e1e15bd85334e4346744078af2f52308.svg" style="height:100px">
    </img>
</a>
"""

def create_fast_test_app(component, parameters: List) -> pn.Column:
    parameters=[
                # Old
                "name",
                "height",
                "width",
                "sizing_mode",
                *parameters,
            ]
    parameters = list(set(parameters))
    app = pn.Column(
        pn.Spacer(height=5),
        pn.Row(
            pn.pane.SVG("https://explore.fast.design/e1e15bd85334e4346744078af2f52308.svg", height=120, link_url="https://fast.design"),
            pn.Spacer(width=10),
            pn.pane.PNG("https://panel.holoviz.org/_static/logo_horizontal.png", height=120, link_url="https://panel.holoviz.org"),
        ),
        pn.Spacer(height=5),
        pn.pane.HTML("<fast-divider></fast-divider>", sizing_mode="stretch_width", height=25),
        pn.Column(
            pn.pane.HTML(f"<fast-badge>{type(component).__name__}</fast-badge>"),
            component,
            pn.Spacer(height=10),
            pn.pane.HTML("<fast-divider></fast-divider>", sizing_mode="stretch_width", height=25),
            pn.pane.HTML(f"<fast-badge>Parameters</fast-badge>"),
            pn.Param(
                component,
                parameters=parameters,
                show_name=False,
            ),
            pn.Spacer(),
        sizing_mode="stretch_height", width=300,
        )
    )

    return FastTemplate(main=[app])