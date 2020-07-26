import param
import panel as pn
from awesome_panel_extensions.widgets.link_buttons.image_link_button import DerivedImageLinkButton

IMAGE_URL = "https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg"

class NBViewerButton(DerivedImageLinkButton):
    """The NBViewerButton displayes the Binder badge and if clicked opens the Notebook on Binder
    in a new tab"""
    repository = param.String()
    branch = param.String()
    folder = param.String()
    notebook = param.String()

    image_url = param.String(default=IMAGE_URL, doc="The url to the image", constant=True)

    width = param.Integer(default=270, bounds=(0, None), doc="""
        The width of the component (in pixels). This can be either
        fixed or preferred width, depending on width sizing policy.""")

    def __init__(self, **params):
        super().__init__(**params)
        self.style={}
        self._update_link_url_from_parameters()

    @param.depends(
        "repository", "branch", "folder", "notebook", "height", "width", "sizing_mode", watch=True
    )
    def _update_link_url_from_parameters(self, *events):
        # if self.sizing_mode == "fixed":
        #     style = f"height:{self.height}px;width:{self.width}px;"
        # elif self.sizing_mode == "stretch_width":
        #     style = f"width:{self.width}px;"
        # elif self.sizing_mode == "stretch_height":
        #     style = f"height:{self.height}px;"
        # else:
        #     style = f"height:100%;width:100%;"
        with param.edit_constant(self):
            self.link_url = (
                f"https://nbviewer.jupyter.org/github/{self.repository}/blob/"
                f"{self.branch}/{self.folder}/{self.notebook}"
            )

if __name__.startswith("bokeh"):
    button = NBViewerButton(
        repository="MarcSkovMadsen/awesome-panel-extensions",
        branch="master",
        folder="examples/panes",
        notebook="WebComponent.ipynb",
    )
    settings_pane = pn.Param(
        button, parameters=["repository", "branch", "folder", "notebook", "height", "width", "sizing_mode", "margin"], background="lightgray", sizing_mode="stretch_width"
    )
    app = pn.Column(button, settings_pane, width=500, height=800)
    app.servable()