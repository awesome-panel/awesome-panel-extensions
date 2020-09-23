from .resource import Resource
from . import category
import param

class Application(Resource):
    category = param.ObjectSelector(
        default=category.APPLICATION, objects=category.ALL, constant=True
    )
