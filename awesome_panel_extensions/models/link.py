"""The Link contains meta data like name, url, description and icon"""
import param

from awesome_panel_extensions.assets import svg_icons
from awesome_panel_extensions.models import category
from awesome_panel_extensions.models.base_model import BaseModel


class Link(BaseModel):
    """The Link contains meta data like name, url, description and icon"""

    name = param.String(doc="The name")
    url = param.String(doc="A unique, identifying link.")
    description = param.String(doc="A description. Can contain HTML")
    category = param.ObjectSelector(default=category.NOT_AVAILABLE, objects=category.ALL)
    icon = param.String(doc="A SVG icon")


class CodeLink(Link):
    """A link to code"""

    category = param.ObjectSelector(default=category.CODE, objects=category.ALL)
    icon = param.String(default=svg_icons.CODE, doc="A SVG icon")


class DiscourseLink(Link):
    """A link to Discourse"""

    category = param.ObjectSelector(default=category.SOCIAL, objects=category.ALL)
    icon = param.String(default=svg_icons.DISCOURSE, doc="A SVG icon")


class DocumentationLink(Link):
    """A link to Documentation"""

    category = param.ObjectSelector(default=category.DOCUMENTATION, objects=category.ALL)
    icon = param.String(default=svg_icons.DOCUMENTATION, doc="A SVG icon")


class DockerLink(Link):
    """A link to Docker"""

    category = param.ObjectSelector(default=category.DEVOPS, objects=category.ALL)
    icon = param.String(default=svg_icons.DOCKER, doc="A SVG icon")


class FacebookLink(Link):
    """A link to Facebook"""

    category = param.ObjectSelector(default=category.SOCIAL, objects=category.ALL)
    icon = param.String(default=svg_icons.FACEBOOK, doc="A SVG icon")


class ImageLink(Link):
    """A link to an image"""

    category = param.ObjectSelector(default=category.IMAGE, objects=category.ALL)
    icon = param.String(default=svg_icons.IMAGE, doc="A SVG icon")


class GithubLink(Link):
    """A link to Github"""

    category = param.ObjectSelector(default=category.DEVOPS, objects=category.ALL)
    icon = param.String(default=svg_icons.GITHUB, doc="A SVG icon")


class LinkedinLink(Link):
    """A link to LinkedIn"""

    category = param.ObjectSelector(default=category.SOCIAL, objects=category.ALL)
    icon = param.String(default=svg_icons.LINKEDIN, doc="A SVG icon")


class MailLink(Link):
    """A mailto link"""

    category = param.ObjectSelector(default=category.SOCIAL, objects=category.ALL)
    icon = param.String(default=svg_icons.MAIL, doc="A SVG icon")


class Mp4Link(Link):
    """A link to a mp4 video"""

    category = param.ObjectSelector(default=category.VIDEO, objects=category.ALL)
    icon = param.String(default=svg_icons.MP4, doc="A SVG icon")


class PypiLink(Link):
    """A link to a package on PyPi"""

    category = param.ObjectSelector(default=category.DEVOPS, objects=category.ALL)
    icon = param.String(default=svg_icons.PYPI, doc="A SVG icon")


class RedditLink(Link):
    """A link to a Reddit article"""

    category = param.ObjectSelector(default=category.SOCIAL, objects=category.ALL)
    icon = param.String(default=svg_icons.REDDIT, doc="A SVG icon")


class TwitterLink(Link):
    """A link to a tweet"""

    category = param.ObjectSelector(default=category.SOCIAL, objects=category.ALL)
    icon = param.String(default=svg_icons.TWITTER, doc="A SVG icon")


class YoutubeLink(Link):
    """A link to a YouTube video"""

    category = param.ObjectSelector(default=category.VIDEO, objects=category.ALL)
    icon = param.String(default=svg_icons.YOUTUBE, doc="A SVG icon")
