"""The FastLiteralInput extends the Panel LiteralInput to a Fast Design Framework LiteralInput.

It is built on the the fast-text-input web component. The component supports two visual apperances
(outline and filled).

For more information view the [component specification]\
(https://github.com/microsoft/fast/tree/master/packages/web-components/fast-foundation/src/text-field).

See also https://explore.fast.design/components/fast-text-field.
    """
from PIL.ImageChops import constant
import param
from panel.widgets.input import LiteralInput

from awesome_panel_extensions.bokeh_extensions.fast.fast_text_input import \
    FastTextInput as _BkFastTextInput
from awesome_panel_extensions.frameworks.fast.fast_text_input import \
    DEFAULT_TEXT_INPUT_APPEARANCE, FAST_TEXT_INPUT_APPEARENCES, _FastTextInputMixin, DEFAULT_TYPE, TYPES

# _FastTextInputMixin
class FastLiteralInput(_FastTextInputMixin, LiteralInput):
    type_of_text = param.String(
        default=DEFAULT_TYPE,
        label="Type",
        constant=True,
        doc="""Determines the type of text accepted. Set to the constant 'text'.
        """,
    )
    _rename = {**LiteralInput._rename}
