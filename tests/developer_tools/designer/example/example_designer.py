"""Example that demonstrates the use of the Designer"""
import panel as pn
from bokeh.sampledata import unemployment1948

from awesome_panel_extensions.developer_tools.designer import (
    ComponentReloader,
    Designer,
)
from tests.developer_tools.designer.example.example_components import (
    altair_bar_plot,
    get_altair_bar_data,
    get_holoviews_plot,
    get_plotly_carshare_data,
    matplotlib_plot,
    plotly_carshare_plot,
)

pn.extension("vega", "plotly")


def _designer():
    # Define your components
    altair_reloader = ComponentReloader(
        component=altair_bar_plot, parameters={"data": get_altair_bar_data}
    )
    plotly_reloader = ComponentReloader(
        component=plotly_carshare_plot,
        parameters={"carshare": get_plotly_carshare_data()},
    )
    holoviews_reloader = ComponentReloader(
        component=get_holoviews_plot, parameters={"data": unemployment1948.data}
    )
    components = [
        matplotlib_plot,
        altair_reloader,
        holoviews_reloader,
        plotly_reloader,
    ]

    # Configure the Designer with you components
    return Designer(components=components)


if __name__ == "__main__":
    _designer().show()
