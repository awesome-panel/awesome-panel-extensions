# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.developer_tools.designer import \
    ComponentReloader as Reloader
from awesome_panel_extensions.developer_tools.designer import Designer
from awesome_panel_extensions.widgets.tabulator import Tabulator
from tests.widgets.test_tabulator.tabulator_examples import TabulatorDataCDSApp

from tests.widgets.test_tabulator.tabulator_data import (_column_data_source, _configuration_basic,
                             _data_records, _dataframe)


def _configuration_basic_with_data():
    configuration = _configuration_basic()
    configuration["data"] = _data_records()
    return configuration

def test_designer():
    reloader_basic = Reloader(name="Basic", component=Tabulator, parameters={"configuration": _configuration_basic_with_data})
    reloader_from_dataframe = Reloader(name="From DataFrame", component=Tabulator, parameters={"configuration": _configuration_basic, "data": _dataframe})
    reloader_from_column_data_source = Reloader(name="From CDS", component=Tabulator, parameters={"configuration": _configuration_basic, "data": _column_data_source})
    reloader_cds_actions = Reloader(component=TabulatorDataCDSApp, parameters={"configuration": _configuration_basic, "data":_dataframe})
    reloaders = [
        # reloader_basic(),
        # reloader_from_dataframe,
        # reloader_from_column_data_source(),
        reloader_cds_actions,
    ]
    return Designer(components=reloaders)


if __name__ == "__main__":
    Tabulator.config(css="site")
    Tabulator()
    test_designer().show()
