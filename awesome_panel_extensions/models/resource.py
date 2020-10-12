"""The Resource contains meta data like name, description and url"""
import param

from awesome_panel_extensions.models.link import Link

from .author import Author


class Resource(Link):
    """The Resource contains meta data like name, description and url"""

    # name, url, description and icon is inherited

    author = param.ClassSelector(class_=Author, doc="The author of the resource")
    thumbnail_url = param.String(doc="A link to a thumbnail image visualizing the resource.")
    tags = param.List(
        class_=str,
        doc="A list of tags like 'machine-learning', 'panel', 'holoviews'. Don't use spaces in the tag.",
    )

    documentation_url = param.String(doc="A link to the documentation.")
    code_url = param.String(doc="A link to the source code.")
    mp4_url = param.String(doc="A link to a mp4 video.")
    youtube_url = param.String(doc="A link to a youtube video.")
    gif_url = param.String(doc="A link to a .gif video")
