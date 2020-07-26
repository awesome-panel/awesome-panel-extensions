import param
import panel as pn
from awesome_panel_extensions.widgets.link_buttons.image_link_button import _STYLE, DerivedImageLinkButton


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
    "light": {"height": 50, "width": 60, "background": "white", "style": _STYLE},
    "dark": {"height": 50, "width": 190, "background": "black", "style": _DARK_STYLE},
}
LINK_URL ="https://panel.holoviz.org"

class PanelButton(DerivedImageLinkButton):
    """The PanelButton displayes the Panel Log and if clicked opens the Panel site"""
    theme = param.ObjectSelector(default="light", objects=THEMES)

    image_url = param.String(doc="The url to the image", constant=True)
    link_url = param.String(default=LINK_URL, doc="The url to open when clicked", constant=True)

    def __init__(self, **params):
        super().__init__(**params)

        self._update_image_url_from_theme()

    @param.depends(
        "theme", watch=True
    )
    def _update_image_url_from_theme(self, *events):
        with param.edit_constant(self):
            self.image_url = IMAGE_URLS[self.theme]
            self.height = LAYOUTS[self.theme]["height"]
            self.width = LAYOUTS[self.theme]["width"]
            self.style = LAYOUTS[self.theme]["style"]

if __name__.startswith("bokeh"):
    button = PanelButton()
    settings_pane = pn.Param(
        button, parameters=["theme", "height", "width", "sizing_mode", "margin"], background="lightgray", sizing_mode="stretch_width"
    )
    app = pn.Column(button, settings_pane, width=500, height=800)
    app.servable()