"""The FastSwitchGroup enables using the `fast-switch` with Bokeh."""
from bokeh.core.properties import Bool, String
from bokeh.models.widgets import CheckboxGroup as _BkCheckboxGroup


class FastSwitchGroup(_BkCheckboxGroup):
    """The FastSwitchGroup enables using the `fast-switch` with Bokeh."""

    readonly = Bool()
    checked_message = String()
    unchecked_message = String()
