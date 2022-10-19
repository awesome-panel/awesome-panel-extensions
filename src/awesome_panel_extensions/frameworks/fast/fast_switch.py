"""The FastSwitch extends the Panel Switch to a Fast Design Framework Switch.

It is built on the the fast-switch web component.

For more information view the [component specification]\
(https://github.com/microsoft/fast/tree/master/packages/web-components/fast-foundation/\
src/switch/switch.spec.md).

See also https://explore.fast.design/components/fast-switch.
    """
import panel as pn
import param  # pylint: disable=wrong-import-order
from panel.widgets import Checkbox

from awesome_panel_extensions.bokeh_extensions.fast.fast_switch_group import (
    FastSwitchGroup as _BkFastSwitchGroup,
)


class FastSwitch(Checkbox):
    """The FastSwitch extends the Panel Switch into the Fast Design Framework.

It is built on the the fast-switch web component.

For more information view the [component specification]\
(https://github.com/microsoft/fast/tree/master/packages/web-components/fast-foundation/\
src/switch/switch.spec.md).

See also https://explore.fast.design/components/fast-switch.
    """

    checked_message = param.String(doc="the message that displays when the switch is checked")
    unchecked_message = param.String(doc="the message that displays when the switch is checked")
    readonly = param.Boolean(
        default=False, doc="""Whether or not the widget is readonly. Default is False"""
    )

    height = param.Integer(default=31, bounds=(0, None))

    _widget_type = _BkFastSwitchGroup

    _rename = {
        **pn.widgets.Checkbox._rename,  # pylint: disable=protected-access
    }
