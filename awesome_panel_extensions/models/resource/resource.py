"""The Resource contains meta data like name, description and url"""
from typing import List

import param

from . import category
from .author import Author
from .base_model import BaseModel


class Resource(BaseModel):
    """The Resource contains meta data like name, description and url"""

    name = param.String(doc="The name")
    description = param.String(doc="A description. Can contain HTML")
    author = param.ClassSelector(class_=Author)
    url = param.String(doc="A unique, identifying link.")
    thumbnail_url = param.String(doc="A link to a thumbnail image visualizing the resource.")

    tags = param.List(
        class_=str,
        doc="A list of tags like 'machine-learning', 'panel', 'holoviews'. Don't use spaces in the tag.",
    )
    category = param.ObjectSelector(default=category.NOT_AVAILABLE, objects=category.ALL)

    documentation_url = param.String(doc="A link to the documentation.")
    code_url = param.String(doc="A link to the source code.")
    mp4_url = param.String(doc="A link to a mp4 video.")
    youtube_url = param.String(doc="A link to a youtube video.")
    gif_url = param.String(doc="A link to a .gif video")

    all: List["Resource"] = []

    def __init__(self, **params):
        super().__init__(**params)

        self.all.append(self)
