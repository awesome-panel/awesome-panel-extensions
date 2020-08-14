"""The Tabulator Pane wraps the [Tabulator](http://tabulator.info/) table."""
from typing import Dict, List, Union

import pandas as pd
import panel as pn
from panel.layout import Column
import param
from bokeh.models.sources import ColumnDataSource
from panel.widgets.base import Widget

from awesome_panel_extensions.bokeh_extensions.tabulator_model import \
    TabulatorModel as _BkTabulator, JS_SRC, MOMENT_SRC, CSS_HREFS

# /themes/tabulator_site.css

_DEFAULT_CONFIGURATION = {"autoColumns": True}
_FORMATTERS = {
    "bool": "plaintext",
    "category": "plaintext",
    "datetime64": "datetime",
    "datetime64[ns]": "datetime",
    "float64": "money",
    "int64": "money",
    "object": "plaintext",
    "timedelta[ns]": "datetimediff",
}
_SORTERS = {
    "bool": "tickCross",
    "category": "plaintext",
    "datetime64": "datetime",
    "datetime64[ns]": "datetime",
    "float64": "number",
    "int64": "number",
    "object": "plaintext",
    "timedelta[ns]": "datetime",
}
_HOZ_ALIGNS = {
    "bool": "center",
    "category": "left",
    "datetime64": "left",
    "datetime64[ns]": "left",
    "float64": "right",
    "int64": "right",
    "object": "left",
    "timedelta[ns]": "right",
}


class Tabulator(Widget):
    configuration = param.Dict(doc="""The Tabulator configuration""")
    value = param.Parameter(
        doc="""One of pandas.DataFrame or bokeh.models.ColumnDataSource.
        If specified it will transfered efficiently to the browser and added to the configuration
        """
    )
    _source = param.ClassSelector(
        class_=ColumnDataSource, doc="Used to transfer data efficiently to frontend" ""
    )
    selection = param.List(doc="The list of selected row indexes")

    height = param.Integer(default=300, bounds=(0, None))

    _rename = {
        "value": None,
        "selection": None,
        "_source": "source",
    }
    _widget_type = _BkTabulator

    def __init__(self, **params):
        if "configuration" not in params:
            params["configuration"] = _DEFAULT_CONFIGURATION.copy()
        params["selection"] = []

        super().__init__(**params)

        self._update_column_data_source()

    @param.depends("value", watch=True)
    def _update_column_data_source(self, *events):
        if self.value is None:
            self._source = ColumnDataSource({})
        elif isinstance(self.value, pd.DataFrame):
            if self._source:
                self._source.data = self.value
            else:
                self._source = ColumnDataSource(self.value)
        elif isinstance(self.value, ColumnDataSource):
            self._source = self.value
        else:
            raise ValueError("The `data` provided is not of a supported type!")

    @classmethod
    def to_columns_configuration(
        cls, data: Union[pd.DataFrame, ColumnDataSource]
    ) -> List[Dict[str, str]]:
        """Returns a relevant configuration dictionary of the specified data source

        Args:
            data (Union[pd.DataFrame, ColumnDataSource]): The data source

        Returns:
            Dict: The configuration

        Example:

        >>> import pandas as pd
        >>> data = {"name": ["python", "panel"]}
        >>> df = pd.DataFrame(data)
        >>> Tabulator.to_columns_configuration(df)
        [{'title': 'Name', 'field': 'name', 'sorter': 'string', 'formatter': 'plaintext', 'hozAlign': 'left'}]
        """
        col_conf = []
        for field in data.columns:
            dtype = str(data.dtypes[field])
            conf = cls._core(field=field, dtype=dtype)
            col_conf.append(conf)
        return col_conf

    @classmethod
    def _core(cls, field: str, dtype: str) -> Dict[str, str]:
        dtype_str = str(dtype)
        return {
            "title": cls._to_title(field),
            "field": field,
            "sorter": _SORTERS.get(dtype_str, "string"),
            "formatter": _FORMATTERS.get(dtype_str, "plaintext"),
            "hozAlign": _HOZ_ALIGNS.get(dtype_str, "left"),
        }

    @staticmethod
    def _to_title(field: str) -> str:
        return field.replace("_", " ").title()

    @staticmethod
    def config(css: str="default", momentjs: bool=True):
        # pn.config.js_files["tabulator"]=JS_SRC
        # if momentjs:
        #     pn.config.js_files["moment"]=MOMENT_SRC
        if css:
            href = CSS_HREFS[css]
            if href not in pn.config.css_files:
                pn.config.css_files.append(href)

    @property
    def selected_values(self) -> Union[pd.DataFrame, ColumnDataSource]:
        """Returns the selected rows of the data based

        Raises:
            NotImplementedError: [description]

        Returns:
            Union[pd.DataFrame, ColumnDataSource]: [description]
        """
        # Selection is a list of row indices. For example [0,2]
        if self.value is None:
            return None
        if isinstance(self.value, pd.DataFrame):
            return self.value.iloc[self.selection,]
        if isinstance(self.value, ColumnDataSource):
            # I could not find a direct way to get a selected ColumnDataSource
            selected_data = self.value.to_df().iloc[self.selection,]
            return ColumnDataSource(selected_data)
        raise NotImplementedError()
