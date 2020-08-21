# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.widgets.dataframe_base import DataFrameWithStreamAndPatchBaseWidget
import pandas as pd
import panel as pn
from bokeh.models import ColumnDataSource
import pytest
from awesome_panel_extensions.widgets.perspective_viewer import PerspectiveViewer

pn.config.sizing_mode = "stretch_width"

@pytest.fixture
def data():
    return {
        "x": [1,2,3,4],
        "y": ["a", "b", "c", "d"],
        "z": [True, False, True, False]
    }

@pytest.fixture
def dataframe(data):
    return pd.DataFrame(data)

def test_is_dataframe_base_widget():
    """A lot of the functionality comes by inheriting from
    DataFrameWithStreamAndPatchBaseWidget. If that is changed we would need to add or change some
    testing here"""
    assert issubclass(PerspectiveViewer, DataFrameWithStreamAndPatchBaseWidget)

def test_constructor(dataframe):
    # When
    component = PerspectiveViewer(value=dataframe)

    # Then
    assert component.theme == "material"
    assert component.value is dataframe
    assert component.plugin == "datagrid"
    assert component.columns is None
    assert component.computed_columns is None
    assert component.column_pivots is None
    assert component.row_pivots is None
    assert component.aggregates is None
    assert component.sort is None
    assert component.filters is None

    assert isinstance(component._source, ColumnDataSource)
    pd.testing.assert_frame_equal(component._source.to_df(), dataframe.reset_index())

def test_perspective_comms(document, comm, dataframe):
    # Given
    perspective = PerspectiveViewer(value=dataframe)
    widget = perspective.get_root(document, comm=comm)

    # Then
    assert isinstance(widget, perspective._widget_type)
    assert widget.source == perspective._source

    # # When
    # with param.edit_constant(tabulator):
    #     tabulator._process_events(
    #         {"configuration": {"a": 1},}
    #     )

    # # Then
    # assert tabulator.configuration == {"a": 1}

if __name__.startswith("bokeh") or __name__ == "__main__":
    SHOW_HTML = True
    data = [
        {"x": 1, "y": "a", "z": True},
        {"x": 2, "y": "b", "z": False},
        {"x": 3, "y": "c", "z": True},
        {"x": 4, "y": "d", "z": False},
    ]
    dataframe = pd.DataFrame(data)
    perspective = PerspectiveViewer(height=300, value=dataframe, columns=["x", "y"])

    def section(component, message=None, show_html=SHOW_HTML):
        print(str(type(component)))
        title = "## " + str(type(component)).split(".")[-1][:-2]

        parameters = [
            "value",
            "columns",
            "parsed_computed_columns",
            "computed_columns",
            "column_pivots",
            "row_pivots",
            "aggregates",
            "sort",
            "filters",
            "plugin",
            "theme",
            ]

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

    pn.Column(*section(perspective), width=400, sizing_mode="stretch_height").show(port=5007)

