import panel as pn

pn.extension("echarts")

ACCENT_REST = "#DF3874"


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


pn.config.sizing_mode = "stretch_width"
component = pn.pane.ECharts(
                _create_echarts_plot(), min_height=400, min_width=200, sizing_mode="stretch_both"
            )
controls = component.controls()
# pn.template.VanillaTemplate(
#     title="Test",
#     theme=pn.template.vanilla.DarkTheme,
#     main=[component, controls],
# ).servable()
pn.Column(
    component, controls
).servable()
