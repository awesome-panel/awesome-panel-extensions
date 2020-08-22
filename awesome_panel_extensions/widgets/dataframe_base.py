"""This module contains base functions and classes used to implement
'DataFrame' widgets like the PerspectiveViewer and Tabulator"""
from typing import Dict, Union

import pandas as pd
import param
from bokeh.models import ColumnDataSource
from panel.widgets.base import Widget


class DataFrameWithStreamAndPatchBaseWidget(Widget):
    value = param.DataFrame(
        doc="""A pandas.DataFrame

        Please note when specifying a Pandas.Dataframe we currently have some narrow requirements
        """,
    )
    _source = param.ClassSelector(
        class_=ColumnDataSource, doc="Used to transfer the `value` efficiently to frontend"
    )
    method = param.Number(0)
    _rename = {"value": None, "_source": "source", "method": None}


    def __init__(self, **params):
        super().__init__(**params)

        self._pause_cds_updates = False
        self._set_source()

    @param.depends("value", watch=True)
    def _set_source(self):
        if self._pause_cds_updates:
            return
        if self._source is None:
            if self.value is None:
                self._source = ColumnDataSource({})
            else:
                self._source = ColumnDataSource(self.value)
        else:
            if self.value is None:
                self._source.data = {}
            else:
                self._source.data = self.value

    def stream(self, stream_value: Union[pd.DataFrame, pd.Series, Dict], reset_index: bool = True):
        """Streams (appends) the `stream_value` provided to the existing value in an efficient
        manner.

        Args:
            stream_value (Union[pd.DataFrame, pd.Series, Dict]): The new value(s) to append to the
                existing value.
            reset_index (bool, optional): If the stream_value is a DataFrame and `reset_index` is
                True then the index of it is reset if True. Helps to keep the index unique and
                named `index`. Defaults to True.

        Raises:
            ValueError: Raised if the stream_value is not a supported type.

        Example: Stream a Series to a DataFrame

        >>> value = pd.DataFrame({"x": [1, 2], "y": ["a", "b"]})
        >>> tabulator = Tabulator(value=value)
        >>> stream_value = pd.Series({"x": 4, "y": "d"})
        >>> tabulator.stream(stream_value)
        >>> tabulator.value.to_dict("list")
        {'x': [1, 2, 4], 'y': ['a', 'b', 'd']}

        Example: Stream a Dataframe to a Dataframe

        >>> value = pd.DataFrame({"x": [1, 2], "y": ["a", "b"]})
        >>> tabulator = Tabulator(value=value)
        >>> stream_value = pd.DataFrame({"x": [3, 4], "y": ["c", "d"]})
        >>> tabulator.stream(stream_value)
        >>> tabulator.value.to_dict("list")
        {'x': [1, 2, 3, 4], 'y': ['a', 'b', 'c', 'd']}


        Example: Stream a Dictionary row to a DataFrame

        >>> value = pd.DataFrame({"x": [1, 2], "y": ["a", "b"]})
        >>> tabulator = Tabulator(value=value)
        >>> stream_value = {"x": 4, "y": "d"}
        >>> tabulator.stream(stream_value)
        >>> tabulator.value.to_dict("list")
        {'x': [1, 2, 4], 'y': ['a', 'b', 'd']}

        Example: Stream a Dictionary of Columns to a Dataframe

        >>> value = pd.DataFrame({"x": [1, 2], "y": ["a", "b"]})
        >>> tabulator = Tabulator(value=value)
        >>> stream_value = {"x": [3, 4], "y": ["c", "d"]}
        >>> tabulator.stream(stream_value)
        >>> tabulator.value.to_dict("list")
        {'x': [1, 2, 3, 4], 'y': ['a', 'b', 'c', 'd']}
        """

        if isinstance(self.value, pd.DataFrame):
            value_index_start = self.value.index.max() + 1
            if isinstance(stream_value, pd.DataFrame):
                if reset_index:
                    stream_value = stream_value.reset_index(drop=True)
                    stream_value.index += value_index_start
                self._pause_cds_updates = True
                self.value = pd.concat([self.value, stream_value])
                self._source.stream(stream_value)
                self._pause_cds_updates = False
            elif isinstance(stream_value, pd.Series):
                self._pause_cds_updates = True
                self.value.loc[value_index_start] = stream_value
                self._source.stream(stream_value)
                self.param.trigger("value")
                self._pause_cds_updates = False
            elif isinstance(stream_value, dict):
                if stream_value:
                    try:
                        stream_value = pd.DataFrame(stream_value)
                    except ValueError:
                        stream_value = pd.Series(stream_value)
                    self.stream(stream_value)
            else:
                raise ValueError("The patch value provided is not a DataFrame, Series or Dict!")
        else:
            self._pause_cds_updates = True
            self._source.stream(stream_value)
            self.param.trigger("value")
            self._pause_cds_updates = False

    def patch(self, patch_value: Union[pd.DataFrame, pd.Series, Dict]):
        """Patches (updates) the existing value with the `patch_value` in an efficient manner.

        Args:
            patch_value (Union[pd.DataFrame, pd.Series, Dict]): The value(s) to patch the
                existing value with.

        Raises:
            ValueError: Raised if the patch_value is not a supported type.



        Example: Patch a DataFrame with a Dictionary row.

        >>> value = pd.DataFrame({"x": [1, 2], "y": ["a", "b"]})
        >>> tabulator = Tabulator(value=value)
        >>> patch_value = {"x": [(0, 3)]}
        >>> tabulator.patch(patch_value)
        >>> tabulator.value.to_dict("list")
        {'x': [3, 2], 'y': ['a', 'b']}

        Example: Patch a Dataframe with a Dictionary of Columns.

        >>> value = pd.DataFrame({"x": [1, 2], "y": ["a", "b"]})
        >>> tabulator = Tabulator(value=value)
        >>> patch_value = {"x": [(slice(2), (3,4))], "y": [(1,'d')]}
        >>> tabulator.patch(patch_value)
        >>> tabulator.value.to_dict("list")
        {'x': [3, 4], 'y': ['a', 'd']}

        Example: Patch a DataFrame with a Series. Please note the index is used in the update

        >>> value = pd.DataFrame({"x": [1, 2], "y": ["a", "b"]})
        >>> tabulator = Tabulator(value=value)
        >>> patch_value = pd.Series({"index": 1, "x": 4, "y": "d"})
        >>> tabulator.patch(patch_value)
        >>> tabulator.value.to_dict("list")
        {'x': [1, 4], 'y': ['a', 'd']}

        Example: Patch a Dataframe with a Dataframe. Please note the index is used in the update.

        >>> value = pd.DataFrame({"x": [1, 2], "y": ["a", "b"]})
        >>> tabulator = Tabulator(value=value)
        >>> patch_value = pd.DataFrame({"x": [3, 4], "y": ["c", "d"]})
        >>> tabulator.patch(patch_value)
        >>> tabulator.value.to_dict("list")
        {'x': [3, 4], 'y': ['c', 'd']}
        """
        if isinstance(self.value, pd.DataFrame):
            if isinstance(patch_value, pd.DataFrame):
                patch_value_dict = {}
                for column in patch_value.columns:
                    patch_value_dict[column] = []
                    for index in patch_value.index:
                        patch_value_dict[column].append((index, patch_value.loc[index, column]))

                self.patch(patch_value_dict)
            elif isinstance(patch_value, pd.Series):
                if "index" in patch_value:  # Series orient is row
                    patch_value_dict = {
                        k: [(patch_value["index"], v)] for k, v in patch_value.items()
                    }
                    patch_value_dict.pop("index")
                else:  # Series orient is column
                    patch_value_dict = {
                        patch_value.name: [(index, value) for index, value in patch_value.items()]
                    }
                self.patch(patch_value_dict)
            elif isinstance(patch_value, dict):
                self._pause_cds_updates = True
                for k, v in patch_value.items():
                    for update in v:
                        self.value.loc[update[0], k] = update[1]
                self._source.patch(patch_value)
                self.param.trigger("value")
                self._pause_cds_updates = False
            else:
                raise ValueError(
                    f"""Patching a patch_value of type {type(patch_value)} is not supported.
                    Please provide a DataFrame, Series or Dict"""
                )
        else:
            if isinstance(patch_value, dict):
                self._pause_cds_updates = True
                self._source.patch(patch_value)
                self.param.trigger("value")
                self._pause_cds_updates = False
            else:
                raise ValueError(
                    f"""Patching a patch_value of type {type(patch_value)} is not supported.
                    Please provide a dict"""
                )
