from bokeh.models.widgets import CheckboxGroup as _BkCheckboxGroup
from bokeh.core.properties import Bool

class FastCheckboxGroup(_BkCheckboxGroup):
    readonly = Bool()