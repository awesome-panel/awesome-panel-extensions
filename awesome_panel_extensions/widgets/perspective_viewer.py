"""Implementation of the PerspectiveViewer Web Component"""
from enum import Enum
from typing import List

import panel as pn
import param
from bokeh.models import ColumnDataSource

from awesome_panel_extensions.web_component import WebComponent

# pylint: disable=line-too-long
JS_FILES = {
    "perspective": "https://unpkg.com/@finos/perspective@0.5.2",
    "perspective_viewer": "https://unpkg.com/@finos/perspective-viewer@0.5.2",
    "perspective_viewer_datagrid": "https://unpkg.com/@finos/perspective-viewer-datagrid@0.5.2/dist/umd/perspective-viewer-datagrid.js",
    "perspective_viewer_d3fc": "https://unpkg.com/@finos/perspective-viewer-d3fc@0.5.2",
    "perspective_viewer_hypergrid": "https://unpkg.com/@finos/perspective-viewer-hypergrid@0.5.2",
    # "perspective-jupyterlab": "https://unpkg.com/@finos/perspective-jupyterlab@0.5.2",
}

JS_FILES = {
    "perspective": "https://unpkg.com/@finos/perspective@0.5.2/dist/umd/perspective.js",
    "perspective_viewer": "https://unpkg.com/@finos/perspective-viewer@0.5.2/dist/umd/perspective-viewer.js",
    "perspective_viewer_datagrid": "https://unpkg.com/@finos/perspective-viewer-datagrid@0.5.2/dist/umd/perspective-viewer-datagrid.js",
    "perspective_viewer_hypergrid": "https://unpkg.com/@finos/perspective-viewer-hypergrid@0.5.2/dist/umd/perspective-viewer-hypergrid.js",
    "perspective_viewer_d3fc": "https://unpkg.com/@finos/perspective-viewer-d3fc@0.5.2/dist/umd/perspective-viewer-d3fc.js",
}

CSS_FILES = {
    "all": "https://unpkg.com/@finos/perspective-viewer@0.5.2/dist/umd/all-themes.css",
    "material": "https://unpkg.com/@finos/perspective-viewer@0.5.2/dist/umd/material.css",
    "material_dark": "https://unpkg.com/@finos/perspective-viewer@0.5.2/dist/umd/material.dark.css",
    "material_dense": "https://unpkg.com/@finos/perspective-viewer@0.5.2/dist/umd/material-dense.css",
    "material_dense_dark": "https://unpkg.com/@finos/perspective-viewer@0.5.2/dist/umd/material-dense.dark.css",
    "vaporwave": "https://unpkg.com/@finos/perspective-viewer@0.5.2/dist/umd/vaporwave.css",
}
# pylint: enable=line-too-long
DEFAULT_THEME = "perspective-viewer-material"
THEMES = {
    "material": "perspective-viewer-material",
    "material-dark": "perspective-viewer-material-dark",
    "material-dense": "perspective-viewer-material-dense",
    "material-dense-dark": "perspective-viewer-material-dense-dark",
    "vaporwave": "perspective-viewer-vaporwave",
}
# Hack: When the user drags some of the columns, then the class attribute contains "dragging" also.
THEMES_DRAGGING = {key + " dragging": value + " dragging" for key, value in THEMES.items()}
THEMES = {**THEMES, **THEMES_DRAGGING}


# Source: https://github.com/finos/perspective/blob/e23988b4b933da6b90fd5767d059a33e70a2493e/python/perspective/perspective/core/plugin.py#L49 # pylint: disable=line-too-long
class Plugin(Enum):
    """The plugins (grids/charts) available in Perspective.  Pass these into
    the `plugin` arg in `PerspectiveWidget` or `PerspectiveViewer`.
    Examples:
        >>> widget = PerspectiveWidget(data, plugin=Plugin.TREEMAP)
    """

    HYPERGRID = "hypergrid"  # hypergrid
    GRID = "datagrid"  # hypergrid

    # YBAR = 'y_bar'  # highcharts
    # XBAR = 'x_bar'  # highcharts
    # YLINE = 'y_line'  # highcharts
    # YAREA = 'y_area'  # highcharts
    # YSCATTER = 'y_scatter'  # highcharts
    # XYLINE = 'xy_line'  # highcharts
    # XYSCATTER = 'xy_scatter'  # highcharts
    # TREEMAP = 'treemap'  # highcharts
    # SUNBURST = 'sunburst'  # highcharts
    # HEATMAP = 'heatmap'  # highcharts

    YBAR_D3 = "d3_y_bar"  # d3fc
    XBAR_D3 = "d3_x_bar"  # d3fc
    YLINE_D3 = "d3_y_line"  # d3fc
    YAREA_D3 = "d3_y_area"  # d3fc
    YSCATTER_D3 = "d3_y_scatter"  # d3fc
    XYSCATTER_D3 = "d3_xy_scatter"  # d3fc
    TREEMAP_D3 = "d3_treemap"  # d3fc
    SUNBURST_D3 = "d3_sunburst"  # d3fc
    HEATMAP_D3 = "d3_heatmap"  # d3fc

    CANDLESTICK = "d3_candlestick"  # d3fc
    CANDLESTICK_D3 = "d3_candlestick"  # d3fc
    OHLC = "d3_ohlc"  # d3fc
    OHLC_D3 = "d3_ohlc"  # d3fc

    @staticmethod
    def options() -> List:
        """Returns the list of options of the PerspectiveViewer, like Hypergrid, Grid etc.

        Returns:
            List: [description]
        """
        return list(c.value for c in Plugin)


class PerspectiveViewer(WebComponent):  # pylint: disable=abstract-method
    """The PerspectiveViewer WebComponent enables exploring large tables of data"""

    html = param.String(
        """
    <perspective-viewer class='perspective-viewer-material-dark' \
style="height:100%;width:100%"></perspective-viewer>"""
    )
    attributes_to_watch = param.Dict(
        {
            "class": "theme",
            "plugin": "plugin",
            "row-pivots": "row_pivots",
            "columns": "columns",
            "computed-columns": "computed_columns",
            "column-pivots": "column_pivots",
            "sort": "sort",
            "aggregates": "aggregates",  # Have not been able to manually test this one
            "filters": "filters",
        }
    )

    data = param.DataFrame(doc="""The data loaded to the viewer.""")

    columns = param.List(
        None, doc='A list of source columns to show as columns. For example ["x", "y"]'
    )
    computed_columns = param.List(
        None,
        doc='A list of computed columns. For example [{"name":"x+y","func":"add","inputs":["x","y"]}]',
    )
    column_pivots = param.List(
        None, doc='A list of source columns to pivot by. For example ["x", "y"]'
    )
    row_pivots = param.List(
        None, doc='A list of source columns to group by. For example ["x", "y"]'
    )
    aggregates = param.Dict(None, doc='How to aggregate. For example {x: "distinct count"}')
    sort = param.List(None, doc='How to sort. For example[["x","desc"]]')
    filters = param.List(
        None, doc='How to filter. For example [["x", "<", 3],["y", "contains", "abc"]]'
    )

    theme = param.ObjectSelector(
        DEFAULT_THEME,
        objects=THEMES,
        doc="The style of the PerspectiveViewer. For example perspective-viewer-material-dark",
    )
    plugin = param.ObjectSelector(
        Plugin.GRID.value,
        objects=Plugin.options(),
        doc="The name of a plugin to display the data. For example hypergrid or d3_xy_scatter.",
    )

    def __init__(self, **params):
        self._initial_parameters = {}

        # We cannot set parameters on the perspective-viewer webcomponent before it has been loaded
        # with data. See also _handle_attributes_last_change
        for parameter in list(params):
            if parameter in self.attributes_to_watch.values():
                self._initial_parameters[parameter] = params.pop(parameter)

        params["column_data_source_orient"] = "records"
        params["column_data_source_load_function"] = "load"
        super().__init__(**params)

        self._set_column_data_source()

    def _handle_attributes_last_change(self, event):
        # When the <perspective-viewer> WebComponent loads it sets is parameters to default values
        # This may override values specified to the python object on construction or later
        # We need to be able to handle this situation.
        # See also test_perspective_viewer_load.
        # Please note that this hack only works on server and not in notebook.
        is_perspective_viewer_first_load = (
            set(self.attributes_to_watch.keys()) == set(self.attributes_last_change.keys())
            and self._initial_parameters != {}
        )

        # # This is situation where PerspectiveViewer is being reloaded > 1 times
        # if is_perspective_viewer_reset and not self._initial_parameters:
        #     self._initial_parameters = {
        #         p: getattr(self, p) for p in self.attributes_to_watch.values()
        #     }

        super()._handle_attributes_last_change(event)

        if is_perspective_viewer_first_load:
            for parameter, value in self._initial_parameters.items():
                setattr(self, parameter, value)
            self._initial_parameters = {}

    @param.depends("data", watch=True)
    def _set_column_data_source(self):
        if not self.data is None:
            self.column_data_source = ColumnDataSource(ColumnDataSource.from_df(self.data))
        else:
            self.column_data_source = ColumnDataSource()

    @staticmethod
    def get_imports() -> str:
        """Returns an HTML string with the required import to use the PerspectiveViewer

        Returns:
            str: [description]
        """
        extension = ""
        for js_ in JS_FILES.values():
            extension += f'<script src="{js_}"></script>'
        for css in CSS_FILES.values():
            extension += f'<link rel="stylesheet" href="{css}" is="custom-style">'

        return extension

    @classmethod
    def get_imports_pane(cls) -> pn.pane.HTML:
        """Returns an HTML pane with the JS and CSS imports required by the perspective-viewer

        Returns:
            pn.pane.HTML: [description]
        """
        imports = cls.get_imports()
        return pn.pane.HTML(imports, width=0, height=0, margin=0, sizing_mode="stretch_width")

    @staticmethod
    def config():
        """Add required .js and .css files to pn.config.js_files and pn.config.css_files"""
        for key, value in JS_FILES.items():
            pn.config.js_files[key] = value
        pn.config.css_files.append(CSS_FILES["all"])
