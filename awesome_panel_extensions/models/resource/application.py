import param

from . import category
from .resource import Resource


class Application(Resource):
    category = param.ObjectSelector(
        default=category.APPLICATION, objects=category.ALL, constant=True
    )
