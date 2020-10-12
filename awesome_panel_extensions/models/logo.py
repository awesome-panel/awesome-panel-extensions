"""The Logo contains the name and url meta data of an image"""

import param

from .base_model import BaseModel


class Logo(BaseModel):
    url = param.String(doc="A link to the image. Does not currently support svg")
    link_url = param.String(doc="A link to a web site or resource")
    target = param.ObjectSelector(
        "_self",
        objects=["_blank", "_parent", "_self", "_top"],
        doc="The target tells the browser where the link should be opened. Default is '_self'",
    )
    description = param.String(doc="A description which could be used as a tooltip")
    width = param.Integer(50, doc="The width of the logo")
    height = param.Integer(50, doc="The height of the logo")
    background = param.String("transparent", doc="The background color. default is transparent")
    unit = param.ObjectSelector(
        default="px", objects=["px", "%"], doc="The unit of the height and width"
    )

    def _repr_html_(self):
        return f"""\
<a href="{self.link_url}"" target="{self.target}" title="{self.description}"><img src="{self.url}" style="\
width:{self.width}{self.unit};\
height:{self.height}{self.unit};\
background:{self.background}">\
</img></a>\
"""


PANEL_LOGO_SQUARE_LIGHT_BACKGROUND = Logo(
    name="Panel Logo - Square, White Background",
    description="The Panel site contains tutorials, examples and api documentation",
    url="https://panel.holoviz.org/_static/logo_stacked.png",
    link_url="https://panel.holoviz.org/",
    target="_blank",
)
PANEL_LOGO_RECTANGULAR_DARK_BACKGROUND = Logo(
    width=215,
    height=50,
    name="Panel Logo - Rectangular, Dark Background",
    description="The Panel site contains tutorials, examples and api documentation",
    url="https://panel.holoviz.org/_static/logo_horizontal.png",
    link_url="https://panel.holoviz.org/",
    target="_blank",
)
