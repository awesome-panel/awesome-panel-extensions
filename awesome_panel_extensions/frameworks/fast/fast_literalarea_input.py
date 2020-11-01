from panel.widgets.input import LiteralInput

from awesome_panel_extensions.bokeh_extensions.fast.fast_textarea_input import (
    FastTextAreaInput as _BkFastTextAreaInput,
)
from awesome_panel_extensions.frameworks.fast.fast_textarea_input import _FastTextAreaInputMixin


class FastLiteralAreaInput(_FastTextAreaInputMixin, LiteralInput):
    _widget_type = _BkFastTextAreaInput

    _rename = {**LiteralInput._rename}
