"""Implementation of the PerspectiveViewer Web Component"""

import panel as pn
import param

from awesome_panel_extensions.bokeh_extensions.pivot_table import PivotTable as _BkPivotTable
from awesome_panel_extensions.widgets.dataframe_base import DataFrameWithStreamAndPatchBaseWidget

# This is need to be able to use Perspective in notebook via pn.extension("perspective")
pn.extension._imports[  # pylint: disable=protected-access
    "pivottable"
] = "awesome_panel_extensions.bokeh_extensions.pivot_table"


class PivotTable(DataFrameWithStreamAndPatchBaseWidget):  # pylint: disable=abstract-method
    """The PivotTable widget enables exploring large tables of data
    in an interactive pivot table"""

    _widget_type = _BkPivotTable

    # I set this to something > 0. Otherwise the PerspectiveViewer widget will have a height of 0px
    # It will appear as if it does not work.
    height = param.Integer(default=300, bounds=(0, None))
