"""The Icon can be used to add SVG based icons inline to buttons, menus etc."""
import panel as pn

# See https://github.com/holoviz/panel/issues/1586 for motivation, possibilities and requirements.
import param

from awesome_panel_extensions.bokeh_extensions.icon import Icon as _BkIcon

_CSS = """
@-ms-keyframes spin {
    from {
        -ms-transform: rotate(0deg);
    }
    to {
        -ms-transform: rotate(360deg);
    }
}
@-moz-keyframes spin {
    from {
        -moz-transform: rotate(0deg);
    }
    to {
        -moz-transform: rotate(360deg);
    }
}
@-webkit-keyframes spin {
    from {
        -webkit-transform: rotate(0deg);
    }
    to {
        -webkit-transform: rotate(360deg);
    }
}
@keyframes spin {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(360deg);
    }
}
    """
# Please remove .bk-btn-light above when https://github.com/bokeh/bokeh/issues/10505 has been
# solved
pn.config.raw_css.append(_CSS)


class Icon(param.Parameterized):
    # pylint: disable=line-too-long
    """The Icon can be used to add SVG based icons inline to buttons, menus etc.

    >>> Icon(
    ...    name="Github",
    ...    value='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 19 20"><path d="M6.71154 17.0776C2.09615 18.4906 2.09615 14.7226 0.25 14.2517L6.71154 17.0776ZM13.1731 19.9036V16.2581C13.2077 15.8089 13.1482 15.3574 12.9986 14.9335C12.849 14.5096 12.6127 14.123 12.3054 13.7995C15.2038 13.4698 18.25 12.3489 18.25 7.20563C18.2498 5.89046 17.754 4.62572 16.8654 3.67319C17.2862 2.52257 17.2564 1.25074 16.7823 0.121918C16.7823 0.121918 15.6931 -0.207776 13.1731 1.51605C11.0574 0.930913 8.82722 0.930913 6.71154 1.51605C4.19154 -0.207776 3.10231 0.121918 3.10231 0.121918C2.62819 1.25074 2.59844 2.52257 3.01923 3.67319C2.12396 4.63279 1.62771 5.90895 1.63462 7.23389C1.63462 12.3394 4.68077 13.4604 7.57923 13.8278C7.27554 14.148 7.04132 14.5299 6.89182 14.9486C6.74233 15.3674 6.6809 15.8135 6.71154 16.2581V19.9036"></path></svg>',
    ...    fill_color="#E1477E",
    ...    spin_duration=2000,
    ... )
    Icon(...
    """
    # pylint: enable=line-too-long
    name = param.String(
        default=None,
        constant=False,
        doc="""The name of the icon. We will append 'icon' and 'icon-{name}'
        to enable custom styling""",
    )
    value = param.String(
        doc="""
        A html string defining the icon.
        """
    )
    size = param.Number(
        default=1.0,
        bounds=(0.0, None),
        step=0.1,
        doc="The size in em units, i.e. a multiplier of the current font-size.",
    )
    fill_color = param.String(
        default="currentColor",
        doc="""The fill color of the Icon. Any valid css color like '#eb4034', 'rgb(235, 64, 52)'
        or 'currentColor'. Default is 'currentColor' which is the color of the surrounding text""",
    )
    # For CSS Spin See https://codepen.io/eveness/pen/BjLaoa
    spin_duration = param.Integer(
        default=0,
        bounds=(0, None),
        doc="""The spin duration in miliseconds.
        If greater than 0 the Icon will do a spinning animation. Defaults to 0""",
    )

    _bk_icon = param.ClassSelector(class_=_BkIcon)

    def __init__(self, **params):
        super().__init__(**params)

        self._bk_icon = _BkIcon(
            label=self.name,
            text=self.value,
            size=self.size,
            fill_color=self.fill_color,
            spin_duration=self.spin_duration,
        )

    @param.depends("name", watch=True)
    def _update_label(self, *_):
        self._bk_icon.label = self.name

    @param.depends("value", watch=True)
    def _update_value(self, *_):
        self._bk_icon.text = self.value

    @param.depends("size", watch=True)
    def _update_size(self, *_):
        self._bk_icon.size = self.size

    @param.depends("fill_color", watch=True)
    def _update_fill_color(self, *_):
        self._bk_icon.fill_color = self.fill_color

    @param.depends("spin_duration", watch=True)
    def _update_spin_duration(self, *_):
        self._bk_icon.spin_duration = self.spin_duration
