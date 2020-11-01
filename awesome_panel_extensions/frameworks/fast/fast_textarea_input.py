"""The FastTextAreaInput extends the Panel TextAreaInput to a Fast Design Framework TextAreaInput.

It is built on the the fast-text-area web component. The component supports two visual apperances
(outline and filled).

For more information view the [component specification]\
(https://github.com/microsoft/fast/tree/master/packages/web-components/fast-foundation/src/text-area).

See also https://explore.fast.design/components/fast-text-area.
    """
import panel as pn
import param  # pylint: disable=wrong-import-order
from panel.widgets import TextAreaInput

from awesome_panel_extensions.bokeh_extensions.fast.fast_textarea_input import (
    FastTextAreaInput as _BkFastTextAreaInput,
)

FAST_TEXT_AREA_APPEARENCES = [
    "outline",
    "filled",
]
DEFAULT_TEXT_AREA_APPEARANCE = None
RESIZES = [None, "both", "horizontal", "vertical"]
DEFAULT_RESIZE = None


class _FastTextAreaInputMixin(pn.widgets.Widget):
    # value  is inherited
    # placeholder is inherited
    # disabled is inherited
    # list is not supported
    placeholder = param.String(
        default="", doc="A placeholder string displayed when no value is entered."
    )
    appearance = param.ObjectSelector(
        default=DEFAULT_TEXT_AREA_APPEARANCE,
        objects=FAST_TEXT_AREA_APPEARENCES,
        doc="""Determines the appearance of the TextAreaInput. One of None, `outline` or `filled`.
        Defaults to None which is the same a `outline`""",
        allow_None=True,
    )
    autofocus = param.Boolean(
        default=False,
        doc="""The autofocus attribute. Defaults to `False`""",
    )
    resize = param.ObjectSelector(
        default=DEFAULT_RESIZE,
        objects=RESIZES,
        constant=True,
        doc="""The resize attribute. One of
        `None`, `both`, `horizontal` or `vertical`. Defaults to `None`.
        Currently constant since Panel does not (yet?) support resizing widgets by dragging.
        """,
        allow_None=True,
    )
    cols = param.Integer(default=20, bounds=(0, None))
    rows = param.Integer(
        doc="The number of visible text lines for the control.", default=2, bounds=(0, None)
    )
    min_length = param.Integer(
        default=0,
        doc="""The minimum length of the text string""",
    )
    spellcheck = param.Boolean(
        default=False, doc="""Whether or not the spell check is enabled. Default is False"""
    )
    required = param.Boolean(
        default=False, doc="""Whether or not the FastTextAreaInput is required. Default is False"""
    )
    readonly = param.Boolean(
        default=False, doc="""Whether or not the FastTextAreaInput is readonly. Default is False"""
    )

    # If we don't set this then the pane below will overlap
    height = param.Integer(default=100, bounds=(0, None))

    _widget_type = _BkFastTextAreaInput


class FastTextAreaInput(_FastTextAreaInputMixin, TextAreaInput):
    """The FastTextAreaInput extends the Panel TextAreaInput to a Fast Design Framework TextAreaInput.

It is built on the the fast-text-area web component. The component supports two visual apperances
(outline and filled).

For more information view the [component specification]\
(https://github.com/microsoft/fast/tree/master/packages/web-components/fast-foundation/src/text-area).

See also https://explore.fast.design/components/fast-text-area.
    """

    _rename = {
        **pn.widgets.TextAreaInput._rename,  # pylint: disable=protected-access
    }
