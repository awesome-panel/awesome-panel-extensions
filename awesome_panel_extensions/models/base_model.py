"""In this module we define the BaseModel.

The BaseModel adds ordering by the name parameter to a Class"""
import param

class BaseModel(param.Parameterized):
    """The BaseModel adds ordering by the name parameter to a Class"""

    def __lt__(self, other):
        if hasattr(other, "name"):
            return self.name.casefold() < other.name.casefold()
        return True

    def __eq__(self, other):
        if hasattr(other, "name"):
            return self.name == other.name
        return False

    def __str__(self,):
        return self.name

    def __repr__(self,):
        return self.name