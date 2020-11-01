"""The FastCheckbox extends the Panel Checkbox to a Fast Design Framework Checkbox.

It is built on the the fast-checkbox web component. The component supports several visual apperances
(accent, lightweight, neutral, outline, stealth).

For more information view the [component specification]\
(https://github.com/microsoft/fast/tree/master/packages/web-components/fast-foundation/\
src/checkbox/checkbox.spec.md).

See also https://explore.fast.design/components/fast-checkbox.
    """
import panel as pn
import param  # pylint: disable=wrong-import-order
from panel.widgets import Checkbox

from awesome_panel_extensions.bokeh_extensions.fast.fast_checkbox_group import (
    FastCheckboxGroup as _BkFastCheckboxGroup,
)


class FastCheckbox(Checkbox):
    """The FastCheckbox extends the Panel Checkbox into the Fast Design Framework.

It is built on the the fast-checkbox web component.

For more information view the [component specification]\
(https://github.com/microsoft/fast/tree/master/packages/web-components/fast-foundation/\
src/checkbox/checkbox.spec.md).

See also https://explore.fast.design/components/fast-checkbox.
    """

    readonly = param.Boolean(
        default=False, doc="""Whether or not the FastCheckbox is readonly. Default is False"""
    )

    height = param.Integer(default=31, bounds=(0, None))

    _widget_type = _BkFastCheckboxGroup

    _rename = {
        **pn.widgets.Checkbox._rename,  # pylint: disable=protected-access
    }
