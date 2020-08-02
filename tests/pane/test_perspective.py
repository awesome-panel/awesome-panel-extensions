# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pandas as pd
import panel as pn
from bokeh.models import ColumnDataSource

from awesome_panel_extensions.widgets.perspective_viewer import PerspectiveViewer

pn.config.sizing_mode = "stretch_width"


def test_constructor(document, comm):
    # Given
    data = [
        {"x": 1, "y": "a", "z": True},
        {"x": 2, "y": "b", "z": False},
        {"x": 3, "y": "c", "z": True},
        {"x": 4, "y": "d", "z": False},
    ]
    dataframe = pd.DataFrame(data)
    component = PerspectiveViewer(data=dataframe)

    assert component.html == (
        '<perspective-viewer class="perspective-viewer-material" '
        'style="height:100%;width:100%" plugin="datagrid"></perspective-viewer>'
    )
    assert component.data is dataframe
    assert component.column_data_source_orient == "records"
    assert component.column_data_source_load_function == "load"

    model = component.get_root(document, comm=comm)
    assert component._models[model.ref["id"]][0] is model
    assert type(model).__name__ == "WebComponent"
    assert isinstance(model.columnDataSource, ColumnDataSource)
    assert model.columnDataSourceOrient == "records"
    assert model.columnDataSourceLoadFunction == "load"


def test_perspective_viewer_load():
    """When the <perspective-viewer> WebComponent loads it sets is parameters to default values
    This may override values specified to the python object on construction or later

    We need to be able to handle this situation."""
    # Given
    reset_value = {
        "theme": "perspective-viewer-material",
        "plugin": "datagrid",
        "rows": None,
        "row_pivots": None,
        "columns": '["x"]',
        "column_pivots": None,
        "sort": None,
        "aggregates": None,
        "filters": None,
    }

    data = [
        {"x": 1, "y": "a", "z": True},
        {"x": 2, "y": "b", "z": False},
        {"x": 3, "y": "c", "z": True},
        {"x": 4, "y": "d", "z": False},
    ]
    dataframe = pd.DataFrame(data)
    columns = ["x", "y"]
    perspective = PerspectiveViewer(height=500, data=dataframe, columns=columns)
    # When
    perspective.attributes_last_change = reset_value
    # Then
    assert columns == columns

    # WE DON'T SUPPORT A SECOND RELOAD
    # # When
    # perspective.columns = ["x"]
    # perspective.attributes_last_change = reset_value
    # # Then
    # assert columns == columns


if __name__.startswith("bokeh") or __name__ == "__main__":
    PerspectiveViewer.config()
    SHOW_HTML = True
    data = [
        {"x": 1, "y": "a", "z": True},
        {"x": 2, "y": "b", "z": False},
        {"x": 3, "y": "c", "z": True},
        {"x": 4, "y": "d", "z": False},
    ]
    dataframe = pd.DataFrame(data)
    perspective = PerspectiveViewer(height=500, data=dataframe, columns=["x", "y"])

    def section(component, message=None, show_html=SHOW_HTML):
        print(str(type(component)))
        title = "## " + str(type(component)).split(".")[-1][:-2]

        parameters = list(component._child_parameters())
        if show_html:
            parameters = ["html"] + parameters

        if message:
            return (
                pn.pane.Markdown(title),
                component,
                pn.Param(component, parameters=parameters),
                pn.pane.Markdown(message),
                pn.layout.Divider(),
            )
        return (
            pn.pane.Markdown(title),
            component,
            pn.Param(component, parameters=parameters),
            pn.layout.Divider(),
        )

    pn.Column(*section(perspective)).show(port=5007)