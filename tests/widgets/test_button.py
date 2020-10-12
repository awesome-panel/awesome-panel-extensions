# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel as pn

from awesome_panel_extensions.bokeh_extensions.icon import Icon as _BkIcon
from awesome_panel_extensions.models.icon import Icon
from awesome_panel_extensions.widgets.button import AwesomeButton


# pylint: disable=line-too-long
def _icon():
    return Icon(
        name="Github",
        value="""<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-github" viewBox="0 0 19 20"><path d="M6.71154 17.0776C2.09615 18.4906 2.09615 14.7226 0.25 14.2517L6.71154 17.0776ZM13.1731 19.9036V16.2581C13.2077 15.8089 13.1482 15.3574 12.9986 14.9335C12.849 14.5096 12.6127 14.123 12.3054 13.7995C15.2038 13.4698 18.25 12.3489 18.25 7.20563C18.2498 5.89046 17.754 4.62572 16.8654 3.67319C17.2862 2.52257 17.2564 1.25074 16.7823 0.121918C16.7823 0.121918 15.6931 -0.207776 13.1731 1.51605C11.0574 0.930913 8.82722 0.930913 6.71154 1.51605C4.19154 -0.207776 3.10231 0.121918 3.10231 0.121918C2.62819 1.25074 2.59844 2.52257 3.01923 3.67319C2.12396 4.63279 1.62771 5.90895 1.63462 7.23389C1.63462 12.3394 4.68077 13.4604 7.57923 13.8278C7.27554 14.148 7.04132 14.5299 6.89182 14.9486C6.74233 15.3674 6.6809 15.8135 6.71154 16.2581V19.9036"></path></svg>""",
        fill_color="#E1477E",
        spin_duration=2000,
    )


def _icon_button(icon=None) -> AwesomeButton:
    if not icon:
        icon = _icon()
    return AwesomeButton(name="Click Me", icon=icon)


# pylint: enable=line-too-long


def test_can_use_icon_in_button():
    # Given
    icon = _icon()
    # When
    button = _icon_button(icon=icon)
    # Then
    assert button._bk_icon is icon._bk_icon
    return button


def test_can_construct_button_without_icon():
    # When
    button = AwesomeButton(name="Click Me",)
    # Then
    assert button.icon is None
    assert button._bk_icon is None


def test_can_set_icon_on_button():
    # When
    button = AwesomeButton(name="Click Me",)
    # When
    button.icon = _icon()
    # Then
    assert isinstance(button._bk_icon, _BkIcon)
    assert button._bk_icon is button.icon._bk_icon


def test_can_change_icon_parameter():
    # Given
    button = _icon_button()
    assert button._bk_icon.size == 1.0
    # When
    button.icon.size = 2.0
    # Then
    assert button._bk_icon.size == 2.0


def test_app():
    pn.config.sizing_mode = "stretch_width"
    button = _icon_button()

    def toggle_border(*_):
        if button.css_classes:
            button.css_classes = []
        else:
            button.css_classes = ["bk-btn-light"]

    toggle_border_button = pn.widgets.Button(name="Toggle Border")
    toggle_border_button.on_click(toggle_border)
    icon_settings_pane = pn.Param(
        button.icon,
        parameters=["name", "value", "size", "fill_color", "spin_duration",],
        widgets={"value": {"type": pn.widgets.TextAreaInput, "height": 300}},
    )
    button_settings_pane = pn.Param(button, parameters=["height", "width", "sizing_mode", "name"],)
    return pn.Column(
        button,
        pn.WidgetBox(icon_settings_pane, button_settings_pane),
        toggle_border_button,
        width=500,
        sizing_mode="fixed",
    )


if __name__.startswith("bokeh"):
    test_app().servable()

if __name__ == "__main__":
    test_app().show(port=5007)
