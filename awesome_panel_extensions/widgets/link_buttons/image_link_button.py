"""The ImageLinkButton displays the image_url. When clicked the link_url is opened in a new tab"""
import param
from panel.pane.markup import HTML

_STYLE = {
    "cursor": "pointer",
    "border": "1px solid #ddd",
    "border-radius": "4px",
    "padding": "5px",
}


class ImageLinkButton(HTML):
    """The ImageLinkButton widget is a Link Button that
    - looks like the specified image_url
    - Open the link_url in a new tab when clicked"""

    image_url = param.String(default=None, doc="The url to the image")
    link_url = param.String(default=None, doc="The url to open when clicked")
    object = param.String(
        default=None,
        doc="""
        The object being wrapped, which will be converted to a
        Bokeh model.""",
        constant=True,
    )
    height = param.Integer(
        default=31,
        bounds=(0, None),
        doc="""
        The height of the component (in pixels).  This can be either
        fixed or preferred height, depending on height sizing policy.""",
    )
    width = param.Integer(
        default=300,
        bounds=(0, None),
        doc="""
        The width of the component (in pixels). This can be either
        fixed or preferred width, depending on width sizing policy.""",
    )

    # In order to not be selected by the `pn.panel` selection process
    # Cf. https://github.com/holoviz/panel/issues/1494#issuecomment-663219654
    priority = 0

    def __init__(self, **params):
        parent_parameters = [parameter.name for parameter in HTML.param.objects().values()]
        child_parameters = [parameter.name for parameter in self.param.objects().values()]
        parameters_to_rename = list(set(child_parameters) - set(parent_parameters))
        self._rename = self._rename.copy()
        self._rename.update({parameter: None for parameter in parameters_to_rename})

        params["style"] = params.get("style", {**_STYLE})

        super().__init__(**params)
        self._update_object_from_parameters()

    @param.depends("image_url", "link_url", watch=True)
    def _update_object_from_parameters(self, *_):
        with param.edit_constant(self):
            self.object = (
                f'<a href="{self.link_url}" target="_blank">'
                f'<img src="{self.image_url}" style="height:100%;max-width:100%;display:block;'
                'margin-left:auto;margin-right:auto"></a>'
            )


class DerivedImageLinkButton(ImageLinkButton):
    """Base Class for other Link Buttons like BinderLinkButton"""

    image_url = param.String(default=None, doc="The url to the image", constant=True)
    link_url = param.String(default=None, doc="The url to open when clicked", constant=True)

    @staticmethod
    def _html_encode(item: str) -> str:
        return item.replace("/", "%2F").replace("\\", "%2F")
