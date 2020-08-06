import altair
import panel as pn
from bokeh.sampledata import sea_surface_temperature as sst
from bokeh.sampledata import unemployment1948
from panel.pane import holoviews

from awesome_panel_extensions.developer_tools.designer import ComponentReloader, Designer
from awesome_panel_extensions.widgets import link_buttons
from tests.developer_tools.designer.example.example_components import (
    altair_bar_plot,
    get_altair_bar_data,
    get_holoviews_plot,
    get_plotly_carshare_data,
    matplotlib_plot,
    plotly_carshare_plot,
)

pn.extension("vega", "plotly")


def get_designer():
    altair_reloader = ComponentReloader(
        component=altair_bar_plot, parameters={"data": get_altair_bar_data}
    )
    plotly_reloader = ComponentReloader(
        component=plotly_carshare_plot, parameters={"carshare": get_plotly_carshare_data()},
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

    return Designer(components=components)


get_designer().show()
