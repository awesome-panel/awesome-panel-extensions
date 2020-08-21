"""Implementation of the [Perspective Viewer]\
(https://github.com/finos/perspective/tree/master/packages/perspective-viewer).
"""

from bokeh.core import properties
from bokeh.models import ColumnDataSource
from bokeh.models.layouts import HTMLBox

JS_FILES = [
    "https://unpkg.com/@finos/perspective@0.5.2/dist/umd/perspective.js",
    "https://unpkg.com/@finos/perspective-viewer@0.5.2/dist/umd/perspective-viewer.js",
    "https://unpkg.com/@finos/perspective-viewer-datagrid@0.5.2/dist/umd/perspective-viewer-datagrid.js",
    "https://unpkg.com/@finos/perspective-viewer-hypergrid@0.5.2/dist/umd/perspective-viewer-hypergrid.js",
    "https://unpkg.com/@finos/perspective-viewer-d3fc@0.5.2/dist/umd/perspective-viewer-d3fc.js",
    # "perspective-jupyterlab": "https://unpkg.com/@finos/perspective-jupyterlab@0.5.2",
]
CSS_FILE = "https://unpkg.com/@finos/perspective-viewer@0.5.2/dist/umd/all-themes.css"
CSS_FILES = {
    "material": "https://unpkg.com/@finos/perspective-viewer@0.5.2/dist/umd/material.css",
    "material-dark": "https://unpkg.com/@finos/perspective-viewer@0.5.2/dist/umd/material.dark.css",
    "material-dense": "https://unpkg.com/@finos/perspective-viewer@0.5.2/dist/umd/material-dense.css",
    "material-dense-dark": "https://unpkg.com/@finos/perspective-viewer@0.5.2/dist/umd/material-dense.dark.css",
    "vaporwave": "https://unpkg.com/@finos/perspective-viewer@0.5.2/dist/umd/vaporwave.css",
}
class PerspectiveViewer(HTMLBox):
    """A Bokeh Model that enables easy use of perspective-viewer widget
    """

    __javascript__ = JS_FILES

    __css__ = [CSS_FILE]

    source = properties.Instance(ColumnDataSource)
    columns = properties.List(properties.String())
    parsed_computed_columns = properties.List(properties.Dict(properties.String(), properties.Any()))
    computed_columns = properties.List(properties.String())
    column_pivots = properties.List(properties.String())
    row_pivots = properties.List(properties.String())
    aggregates = properties.Dict(properties.String(), properties.String())
    sort = properties.List(properties.List(properties.String()))
    filters = properties.List(properties.List(properties.Any()))
    plugin = properties.String()
    theme = properties.String()