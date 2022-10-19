"""The FastCheckBoxGroup enables using the `fast-checkbox` with Bokeh."""
from bokeh.core.properties import Bool
from bokeh.models.widgets import CheckboxGroup as _BkCheckboxGroup


class FastCheckboxGroup(_BkCheckboxGroup):
    """The FastCheckBoxGroup enables using the `fast-checkbox` with Bokeh."""

    readonly = Bool()
