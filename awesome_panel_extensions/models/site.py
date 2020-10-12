"""A model of a Site of Applications. For example like awesome-panel.org"""
import param

from .base_model import BaseModel
from .logo import Logo


class Site(BaseModel):
    """A model of a Site of Applications. For example like awesome-panel.org"""

    url = (param.String(doc="A link to the site"),)
    description = (param.String(doc="A short description of the site"),)
    logo = param.ClassSelector(class_=Logo, doc="The default logo of the site")
    logo_dark = param.ClassSelector(
        class_=Logo, doc="The default logo of the site when using a dark theme."
    )
    applications = param.List(doc="A list of Applications")
    resources = param.List(doc="A list of Resources")
