"""The BinderLinkButton displayes the Binder badge and if clicked opens the Notebook on Binder
in a new tab"""
import panel as pn
import param

from awesome_panel_extensions.widgets.link_buttons.image_link_button import DerivedImageLinkButton

BINDER_IMAGE_URL = "https://mybinder.org/badge_logo.svg"


class BinderLinkButton(DerivedImageLinkButton):
    """The BinderLinkButton displayes the Binder badge and if clicked opens the Notebook on Binder
    in a new tab"""

    repository = param.String()
    branch = param.String()
    folder = param.String()
    notebook = param.String()

    image_url = param.String(default=BINDER_IMAGE_URL, doc="The url to the image", constant=True)

    width = param.Integer(default=125, bounds=(0, None))

    def __init__(self, **params):
        super().__init__(**params)
        self.style = {}
        self._update_link_url_from_parameters()

    @param.depends(
        "repository", "branch", "folder", "notebook", "height", "width", "sizing_mode", watch=True
    )
    def _update_link_url_from_parameters(self, *_):
        folder = self._html_encode(self.folder)
        notebook = self._html_encode(self.notebook)

        with param.edit_constant(self):
            self.link_url = (
                f"https://mybinder.org/v2/gh/{self.repository}/{self.branch}"
                f"?filepath={folder}%2F{notebook}"
            )


if __name__.startswith("bokeh"):
    button = BinderLinkButton(
        repository="marcskovmadsen/awesome-panel-extensions",
        branch="master",
        folder="examples/panes",
        notebook="WebComponent.ipynb",
    )
    settings_pane = pn.Param(
        button,
        parameters=[
            "repository",
            "branch",
            "folder",
            "notebook",
            "height",
            "width",
            "sizing_mode",
            "margin",
        ],
        background="lightgray",
        sizing_mode="stretch_width",
    )
    app = pn.Column(button, settings_pane, width=500, height=800)
    app.servable()
