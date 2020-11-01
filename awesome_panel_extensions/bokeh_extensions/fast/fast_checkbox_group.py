from bokeh.core.properties import Bool
from bokeh.models.widgets import CheckboxGroup as _BkCheckboxGroup


class FastCheckboxGroup(_BkCheckboxGroup):
    readonly = Bool()
