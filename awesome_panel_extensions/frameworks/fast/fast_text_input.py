"""The FastTextInput extends the Panel TextInput to a Fast Design Framework TextInput.

It is built on the the fast-text-field web component. The component supports two visual apperances
(outline and filled).

For more information view the [component specification]\
(https://github.com/microsoft/fast/tree/master/packages/web-components/fast-foundation/src/text-field).

See also https://explore.fast.design/components/fast-text-field.
    """
# Todo:
# rename to fast_text_input in accordance with bokeh text_input
# rename maxlength, minlength in accordance with bokeh text_input
# in the .ts set maxLength, minLength instead of maxlength, minlength.

import panel as pn
import param  # pylint: disable=wrong-import-order
from panel.widgets import TextInput

from awesome_panel_extensions.bokeh_extensions.fast.fast_text_input import (
    FastTextInput as _BkFastTextInput,
)

FAST_TEXT_INPUT_APPEARENCES = [
    "outline",
    "filled",
]
DEFAULT_TEXT_INPUT_APPEARANCE = "outline"
TYPES = ["email", "password", "tel", "text", "url"]
DEFAULT_TYPE = "text"


class _FastTextInputMixin(pn.widgets.Widget):
    # To used by FastTextInput and FastLiteralInput

    # value  is inherited
    # placeholder is inherited
    # list is not supported
    placeholder = param.String(
        default="",
        doc="A placeholder string displayed when no value is entered.",
    )
    appearance = param.ObjectSelector(
        default=DEFAULT_TEXT_INPUT_APPEARANCE,
        objects=FAST_TEXT_INPUT_APPEARENCES,
        doc="""Determines the appearance of the textinput. One of `outline` or `filled`.
        Defaults to outlined""",
        allow_None=True,
    )
    autofocus = param.Boolean(
        default=False,
        doc="""The autofocus attribute. Defaults to `False`""",
    )
    type_of_text = param.ObjectSelector(
        default=DEFAULT_TYPE,
        objects=TYPES,
        label="Type",
        doc="""Determines the type of text accepted. One of `email`, `password`, `tel`, `text` or `url`.
        Defaults to text.
        """,
    )
    max_length = param.Integer(
        default=100,
        doc="""The maximum length of the text string""",
    )
    min_length = param.Integer(
        default=0,
        doc="""The minimum length of the text string""",
    )
    pattern = param.String(
        default=None,
        doc="""A regular expression that the input's value must match in order for the value to pass constraint validation""",
    )
    # Cannot get size working
    # It raises an error and in the Fast Component Explorer I cannot see any effect of this
    # attribute
    # size = param.Integer(
    #     default=None,
    #     doc="""Valid for email, password, tel, and text input types only. Specifies how much of the input is shown""",
    #     allow_None=True,
    # )
    spellcheck = param.Boolean(
        default=False, doc="""Whether or not the spell check is enabled. Default is False"""
    )
    required = param.Boolean(
        default=False, doc="""Whether or not the FastTextInput is required. Default is False"""
    )
    disabled = param.Boolean(
        default=False, doc="""Whether or not the FastTextInput is disabled. Default is False"""
    )
    readonly = param.Boolean(
        default=False, doc="""Whether or not the FastTextInput is readonly. Default is False"""
    )

    # If we don't set this then the pane below will overlap
    height = param.Integer(default=60, bounds=(0, None))

    _widget_type = _BkFastTextInput

    _rename = {
        **pn.widgets.TextInput._rename,  # pylint: disable=protected-access
    }


class FastTextInput(_FastTextInputMixin, TextInput):
    """The FastTextInput extends the Panel TextInput into the Fast Design Framework.

It is built on the the fast-textinput web component.

For more information view the [component specification]\
(https://github.com/microsoft/fast/tree/master/packages/web-components/fast-foundation/src/text-field).

See also https://explore.fast.design/components/fast-text-field.
    """
