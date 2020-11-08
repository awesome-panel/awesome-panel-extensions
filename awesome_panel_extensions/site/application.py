"""The purpose of this module is to provide functionality for defining meta data about an
application. This can be done via the Application class"""
from typing import List

import param

from awesome_panel_extensions.site import category
from awesome_panel_extensions.site.resource import Resource


class Application(Resource):
    """The Application Class is a placeholder for Meta Data about an application"""

    category = param.ObjectSelector(
        default=category.APPLICATION, objects=category.ALL, constant=True
    )
    view = param.Parameter()

    all: List["Application"] = []

    def __init__(self, **params):
        super().__init__(**params)

        Resource.all.append(self)
