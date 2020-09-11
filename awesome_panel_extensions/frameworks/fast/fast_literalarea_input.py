from panel.widgets.input import LiteralInput
from awesome_panel_extensions.bokeh_extensions.fast.fast_textarea_input import (
    FastTextAreaInput as _BkFastTextAreaInput,
)


class FastLiteralAreaInput(LiteralInput):
    _widget_type = _BkFastTextAreaInput
