# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
"""This module contains tests of the tabulator Data Grid"""

# http://tabulator.info/docs/4.7/quickstart
# https://github.com/paulhodel/jexcel

from awesome_panel_extensions.developer_tools.designer.services.component_reloader import ComponentReloader
import pandas as pd
import panel as pn
import param
import pytest
from bokeh.models import ColumnDataSource

from awesome_panel_extensions.developer_tools.designer import Designer
from awesome_panel_extensions.widgets.tabulator import (CSS_HREFS, JS_SRC,
                                                        MOMENT_SRC, Tabulator)
def _data_records():
    return [
        {"id": 1, "name": "Oli Bob", "age": 12, "col": "red", "dob": pd.Timestamp("14/05/1982")},
        {"id": 2, "name": "Mary May", "age": 1, "col": "blue", "dob": pd.Timestamp("14/05/1982")},
        {
            "id": 3,
            "name": "Christine Lobowski",
            "age": 42,
            "col": "green",
            "dob": pd.Timestamp("22/05/1982"),
        },
        {
            "id": 4,
            "name": "Brendon Philips",
            "age": 125,
            "col": "orange",
            "dob": pd.Timestamp("01/08/1980"),
        },
        {
            "id": 5,
            "name": "Margret Marmajuke",
            "age": 16,
            "col": "yellow",
            "dob": pd.Timestamp("31/01/1999"),
        },
    ]

@pytest.fixture()
def data_records():
    return _data_records

@pytest.fixture()
def dataframe(data_records):
    return pd.DataFrame(data=data_records)

@pytest.fixture()
def data_list(dataframe):
    return dataframe.to_dict("list")

@pytest.fixture()
def column_data_source(data_list):
    return ColumnDataSource(data_list)


@pytest.fixture()
def columns():
    return [
        {
            "title": "Id",
            "field": "id",
            "sorter": "number",
            "formatter": "money",
            "hozAlign": "right",
        },
        {
            "title": "Name",
            "field": "name",
            "sorter": "plaintext",
            "formatter": "plaintext",
            "hozAlign": "left",
        },
        {
            "title": "Age",
            "field": "age",
            "sorter": "number",
            "formatter": "money",
            "hozAlign": "right",
        },
        {
            "title": "Col",
            "field": "col",
            "sorter": "plaintext",
            "formatter": "plaintext",
            "hozAlign": "left",
        },
        {
            "title": "Dob",
            "field": "dob",
            "sorter": "datetime",
            "formatter": "datetime",
            "hozAlign": "left",
        },
    ]


@pytest.fixture()
def configuration():
    # http://tabulator.info/docs/4.7/quickstart
    return {"autoColumns": True}


def test_constructor():
    # When
    tabulator = Tabulator()
    # Then
    assert not tabulator.data
    assert not tabulator._data
    assert tabulator.configuration == {"autoColumns": True}
    assert tabulator.selected_indicies == []
    assert tabulator.selected_data is None


def test_tabulator_from_dataframe(dataframe, configuration):
    tabulator = Tabulator(data=dataframe, configuration=configuration)
    assert isinstance(tabulator._data, ColumnDataSource)


def test_tabulator_from_column_data_source(column_data_source, configuration):
    tabulator = Tabulator(data=column_data_source, configuration=configuration)
    assert tabulator._data == tabulator.data


def test_dataframe_to_columns_configuration(dataframe, columns):
    # Given
    value = dataframe
    # When
    actual = Tabulator.to_columns_configuration(value)
    # Then
    assert actual == columns


def test_config_default():
    # When
    Tabulator.config()
    # Then
    assert pn.config.js_files["tabulator"] == JS_SRC
    assert pn.config.js_files["moment"] == MOMENT_SRC
    assert CSS_HREFS["default"] in pn.config.css_files


def test_config_none():
    # Given
    css_count = len(pn.config.css_files)
    pn.config.js_files.clear()
    # When
    Tabulator.config(css=None, momentjs=False)
    # Then
    assert pn.config.js_files["tabulator"] == JS_SRC
    assert "moment" not in pn.config.js_files
    assert len(pn.config.css_files)==css_count


def test_config_custom():
    # When
    Tabulator.config(css="materialize")
    # Then
    assert pn.config.js_files["tabulator"] == JS_SRC
    assert pn.config.js_files["moment"] == MOMENT_SRC
    assert CSS_HREFS["materialize"] in pn.config.css_files


def test_selection_dataframe(data_records, dataframe):
    # Given
    tabulator = Tabulator(data=dataframe)
    # When
    with param.edit_constant(tabulator):
        tabulator.selected_indicies = [0, 1, 2]
    actual = tabulator.selected_data
    # Then
    expected = pd.DataFrame(data=data_records[0:3])
    pd.testing.assert_frame_equal(actual, expected)

def test_selection_column_data_source(data_records, column_data_source):
    # Given
    tabulator = Tabulator(data= column_data_source)
    # When
    with param.edit_constant(tabulator):
        tabulator.selected_indicies = [0, 1, 2]
    actual = tabulator.selected_data
    # Then
    # I could not find a more direct way to test this.
    expected_as_df = pd.DataFrame(data=data_records[0:3])
    pd.testing.assert_frame_equal(actual.to_df().drop(columns="index"), expected_as_df)


@pytest.mark.parametrize(
    ["field", "expected"],
    [("name", "Name"), ("cheese cake", "Cheese Cake"), ("cheese_cake", "Cheese Cake"),],
)
def test_to_title(field, expected):
    assert Tabulator._to_title(field) == expected

def test_tabulator_comms(document, comm, column_data_source, configuration):
    # Given
    tabulator = Tabulator(data=column_data_source, configuration=configuration)
    widget = tabulator.get_root(document, comm=comm)

    # Then
    assert isinstance(widget, tabulator._widget_type)
    assert widget.data == column_data_source
    assert widget.configuration == configuration
    assert widget.selected_indicies == []

    # When
    tabulator._process_events({
        'selected_indicies': [1],
        })

    # Then
    assert tabulator.selected_indicies == [1]