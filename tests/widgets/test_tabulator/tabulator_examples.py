"""This file contains examples testing the Tabulator"""
from typing import Dict
import pandas as pd
import panel as pn
import param
from bokeh.models import ColumnDataSource
from bokeh.models.sources import ColumnarDataSource
from panel.layout import Column

from awesome_panel_extensions.widgets.tabulator import Tabulator


class TabulatorDataCDSApp(pn.Column):
    """Extension Implementation"""

    tabulator = param.Parameter()

    reset = param.Action()
    replace = param.Action()
    stream = param.Action()
    patch = param.Action()

    # The _rename dict is used to keep track of Panel parameters to sync to Bokeh properties.
    # As dope is not a property on the Bokeh model we should set it to None
    _rename = {
        **pn.Column._rename,
        "data": None,
        "tabulator": None,
        "reset": None,
        "replace": None,
        "stream": None,
        "patch": None,
    }

    def __init__(self, configuration: Dict, data: pd.DataFrame, **params):
        super().__init__(**params)

        self.data = data
        self.data_reset = ColumnDataSource(self.data.iloc[0:10,])

        self.tabulator = Tabulator(configuration=configuration, data=self.data_reset, sizing_mode="stretch_both", background="salmon")
        self.sizing_mode="stretch_width"
        self.height=1000

        self.rows_count = len(self.data)
        self.rows_half = 10
        self.stream_count = 10

        self.reset = self._reset_action
        self.replace = self._replace_action
        self.stream = self._stream_action
        self.patch = self._patch_action
        actions_pane = pn.Param(self, parameters=["reset", "replace", "stream", "patch"], name="Actions")
        self[:] = [self.tabulator, actions_pane]

    #     self.data0_10=ColumnarDataSource()
    #     self.tabulator = Tabulator(data=data)

    #     self[:] = [self.param.dope, self.dope + 1]

    #     # Please note that the alternative of setting
    #     # @param.depends('dope', watch=True)
    #     # on _update_plot_pane does not work.
    #     # See https://github.com/holoviz/panel/issues/1060
    #     # Please upvote the issue if you think it is important to fix
    #     self.param.watch(self._update_something_based_on_dope, 'dope')

    def _reset_action(self, *events):
        data = self.data.iloc[0:10,]
        # data = data.reset_index().to_dict("list")
        # print(self.tabulator.data)
        # print(data)
        self.tabulator.data.data = data

    def _replace_action(self, *events):
        data = self.data.iloc[10:20,]
        self.tabulator.data.data = data

    def _stream_action(self, *events):
        if self.stream_count +1 == len(self.data):
            self.stream_count=10
            self._reset_action()
        else:
            stream_data = self.data.iloc[self.stream_count:self.stream_count+1,]
            # stream_data_dict = stream_data.to_dict("list")
            # stream_data_dict["index"]=self.stream_count
            # print(self.data_reset.data)
            # print(stream_data_dict)
            self.tabulator.data.stream(stream_data)
            self.stream_count +=1



    def _patch_action(self, *events):
        def _patch(value):
            value += 10
            if value >= 100:
                return 0
            return value

        data = self.tabulator.data.data
        progress = data["progress"]
        new_progress = [_patch(value) for value in progress]
        patches = {
                'progress' : [ (slice(len(progress)), new_progress) ],
            }
        self.tabulator.data.patch(patches)

    # def _update_something_based_on_dope(self, *events):
    #     print('update')
    #     self[1] = self.dope
