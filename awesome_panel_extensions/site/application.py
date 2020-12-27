"""The purpose of this module is to provide functionality for defining meta data about an
application. This can be done via the Application class"""
from typing import List

import param

from awesome_panel_extensions.site import category
from awesome_panel_extensions.site.resource import Resource


class Application(Resource):
    """The Application Class is a placeholder for Meta Data about an application"""

    category = param.String(default=category.APPLICATION)
    view = param.Parameter()
    servable = param.Parameter(
        doc="""A path to a .py file, a path to a .ipynb file or a callable
    returning the object to be served"""
    )

    all: List["Application"] = []

    def __init__(self, **params):
        super().__init__(**params)

        Resource.all.append(self)
