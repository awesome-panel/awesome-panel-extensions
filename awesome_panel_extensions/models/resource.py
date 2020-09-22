"""The Resource contains meta data like name, description and url"""
import param

from .base_model import BaseModel
from .author import Author

class Resource(BaseModel):
    """The Resource contains meta data like name, description and url"""
    name=param.String(doc="The name")
    description = param.String(doc="A description")

    url = param.String(doc="A link to the resource")
    thumbnail_url = param.String(doc="A link to a thumbnail.")
    documentation_url = param.String(doc="A link to the documentation.")
    code_url = param.String(doc="A link to the source code.")
    video_url = param.String(doc="A link to a video.")
    gif_url = param.String(doc="A link to a .gif video")

    author = param.ClassSelector(class_=Author)

    tags = param.List(
        class_=str,
        doc="A list of tags like 'machine-learning', 'panel', 'holoviews'. Don't use spaces."
        )
