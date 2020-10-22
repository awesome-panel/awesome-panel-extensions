"""The AwesomeButton extends the `panel.widgets.Button` with support for Icons

    Please note that when the Panel gets extended to support Icons the AwesomeButton will be
    removed.
"""
from typing import Optional

import panel as pn
import param
from panel.widgets.button import Button as _PnButton

from awesome_panel_extensions.models.icon import Icon

_CSS = """
.bk-btn-light .bk-btn-default {
    border-width: 0px;
}

.bk-btn-light .bk-btn-default:hover, .bk-btn-light .bk-btn-default:focus {
            border-width: 1px;
            color: #212529;
            background-color: #e2e6ea;
            border-color: #dae0e5;
}

.bk-btn-light .bk-btn-default:active, .bk-btn-light .bk-btn-default.bk-active  {
            border-width: 1px;
            color: #212529;
            background-color: #dae0e5;
            border-color: #d3d9df;
            box-shadow: none;
}
"""
pn.config.raw_css.append(_CSS)

# pylint: disable=line-too-long
class AwesomeButton(_PnButton):
    """The AwesomeButton extends the Panel Button with support for Icons

    Example:

    >>> icon = Icon(
    ...     name="Github",
    ...     value='<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-github" viewBox="0 0 19 20"><path d="M6.71154 17.0776C2.09615 18.4906 2.09615 14.7226 0.25 14.2517L6.71154 17.0776ZM13.1731 19.9036V16.2581C13.2077 15.8089 13.1482 15.3574 12.9986 14.9335C12.849 14.5096 12.6127 14.123 12.3054 13.7995C15.2038 13.4698 18.25 12.3489 18.25 7.20563C18.2498 5.89046 17.754 4.62572 16.8654 3.67319C17.2862 2.52257 17.2564 1.25074 16.7823 0.121918C16.7823 0.121918 15.6931 -0.207776 13.1731 1.51605C11.0574 0.930913 8.82722 0.930913 6.71154 1.51605C4.19154 -0.207776 3.10231 0.121918 3.10231 0.121918C2.62819 1.25074 2.59844 2.52257 3.01923 3.67319C2.12396 4.63279 1.62771 5.90895 1.63462 7.23389C1.63462 12.3394 4.68077 13.4604 7.57923 13.8278C7.27554 14.148 7.04132 14.5299 6.89182 14.9486C6.74233 15.3674 6.6809 15.8135 6.71154 16.2581V19.9036"></path></svg>',
    ...     fill_color="#E1477E",
    ...     spin_duration=2000,
    ... )
    >>> AwesomeButton(
    ...     name="Click Me",
    ...     icon = icon
    ... )
    AwesomeButton(_bk_icon=Icon(id='...', ...), icon=Icon, name='Click Me'...

    Args:
        icon (Optional[Icon], optional): An Icon. Defaults to None.
        **params: Any parameter the Panel Button supports
    """

    icon = param.ClassSelector(class_=Icon)
    _bk_icon = param.Parameter()

    _rename = {"clicks": None, "name": "label", "icon": None, "_bk_icon": "icon"}

    def __init__(self, icon: Optional[Icon] = None, **params):
        if icon:
            params["icon"] = icon
            params["_bk_icon"] = icon._bk_icon
        super().__init__(**params)

    @param.depends("icon", watch=True)
    def _update_bk_icon(self, *_):
        if self.icon:
            self._bk_icon = self.icon._bk_icon  # pylint: disable=protected-access
        else:
            self.icon = None
