"""Implementation of the Tabulator pane.

See http://tabulator.info/
"""

from bokeh.core import properties
from bokeh.models import ColumnDataSource
from bokeh.models.layouts import HTMLBox

JS_SRC = "https://unpkg.com/tabulator-tables@4.7.2/dist/js/tabulator.min.js"
MOMENT_SRC = "https://unpkg.com/moment@2.27.0/moment.js"

CSS_HREFS = {
    "default": "https://unpkg.com/tabulator-tables@4.7.2/dist/css/tabulator.min.css",
    "site": "https://unpkg.com/tabulator-tables@4.7.2/dist/css/tabulator_site.min.css",
    "simple": "https://unpkg.com/tabulator-tables@4.7.2/dist/css/tabulator_simple.min.css",
    "midnight": "https://unpkg.com/tabulator-tables@4.7.2/dist/css/tabulator_midnight.min.css",
    "modern": "https://unpkg.com/tabulator-tables@4.7.2/dist/css/tabulator_modern.min.css",
    "bootstrap": "https://unpkg.com/tabulator-tables@4.7.2/dist/css/bootstrap/tabulator_bootstrap.min.css",
    "bootstrap4": "https://unpkg.com/tabulator-tables@4.7.2/dist/css/bootstrap/tabulator_bootstrap4.min.css",
    "semantic-ui": "https://unpkg.com/tabulator-tables@4.7.2/dist/css/semantic-ui/tabulator_semantic-ui.min.css",
    "bulma": "https://unpkg.com/tabulator-tables@4.7.2/dist/css/bulma/tabulator_bulma.min.css",
    "materialize": "https://unpkg.com/tabulator-tables@4.7.2/dist/css/materialize/tabulator_materialize.min.css",
}

class TabulatorModel(HTMLBox):
    """A Bokeh Model that enables easy use of Tabulator tables

    See http://tabulator.info/
    """
    # __implementation__ = "tabulator_model.ts"

    __javascript__ = [
        JS_SRC,
        MOMENT_SRC,
    ]
    # __css__ = [CSS_HREFS["default"]]

    configuration = properties.Dict(properties.String, properties.Any)
    data = properties.Instance(ColumnDataSource)
    selected_indicies = properties.List(properties.Int)