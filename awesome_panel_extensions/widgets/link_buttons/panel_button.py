"""The PanelLinkButton displayes the Panel Logo and if clicked opens the Panel site"""
import panel as pn
import param

from awesome_panel_extensions.widgets.link_buttons.image_link_button import (
    _STYLE,
    DerivedImageLinkButton,
)

THEMES = ["light", "dark"]
IMAGE_URLS = {
    "light": "https://panel.holoviz.org/_static/logo_stacked.png",
    "dark": "https://panel.holoviz.org/_static/logo_horizontal.png",
}
_DARK_STYLE = {
    "background": "black",
    "cursor": "pointer",
    "border": "1px solid #ddd",
    "border-radius": "4px",
    "padding": "5px",
}
LAYOUTS = {
    "light": {"height": 31, "width": 37, "background": "white", "style": _STYLE},
    "dark": {"height": 31, "width": 140, "background": "black", "style": _DARK_STYLE},
}
LINK_URL = "https://panel.holoviz.org"


class PanelLinkButton(DerivedImageLinkButton):
    """The PanelLinkButton displayes the Panel Logo and if clicked opens the Panel site"""

    theme = param.ObjectSelector(default="light", objects=THEMES)

    image_url = param.String(doc="The url to the image", constant=True)
    link_url = param.String(default=LINK_URL, doc="The url to open when clicked", constant=True)

    def __init__(self, **params):
        super().__init__(**params)

        self._update_image_url_from_theme()

    @param.depends("theme", watch=True)
    def _update_image_url_from_theme(self, *events):  # pylint: disable=unused-argument
        with param.edit_constant(self):
            self.image_url = IMAGE_URLS[self.theme]
            height = LAYOUTS[self.theme]["height"]
            width = LAYOUTS[self.theme]["width"]
            if self.height:
                self.width = int(self.height * width / height)
            else:
                self.height = height
                self.width = width
            self.style = LAYOUTS[self.theme]["style"]


if __name__.startswith("bokeh"):
    button = PanelLinkButton()
    settings_pane = pn.Param(
        button,
        parameters=["theme", "height", "width", "sizing_mode", "margin"],
        background="lightgray",
        sizing_mode="stretch_width",
    )
    app = pn.Column(button, settings_pane, width=500, height=800)
    app.servable()
