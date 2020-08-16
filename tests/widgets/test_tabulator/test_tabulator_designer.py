# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.developer_tools.designer import ComponentReloader as Reloader
from awesome_panel_extensions.developer_tools.designer import Designer
from awesome_panel_extensions.widgets.tabulator import Tabulator
from tests.widgets.test_tabulator.tabulator_examples import (
    TabulatorDataCDSApp, tabulator_data_specified_as_column_data_source_value, tabulator_data_specified_as_data_frame_value,
    tabulator_data_specified_in_configuration,
)

from tests.widgets.test_tabulator.tabulator_data import (
    _column_data_source,
    _configuration_basic,
    _data_records,
    _dataframe,
)


def _configuration_basic_with_data():
    configuration = _configuration_basic()
    configuration["data"] = _data_records()
    return configuration


def test_designer():
    reloader_cds_actions = Reloader(
        component=TabulatorDataCDSApp,
        parameters={"configuration": _configuration_basic, "data": _dataframe},
    )
    reloaders = [
        reloader_cds_actions,
        tabulator_data_specified_in_configuration,
        tabulator_data_specified_as_data_frame_value,
        tabulator_data_specified_as_column_data_source_value,
    ]
    return Designer(components=reloaders)


if __name__ == "__main__":
    Tabulator.config(css="site")
    # Tabulator()
    test_designer().show()
