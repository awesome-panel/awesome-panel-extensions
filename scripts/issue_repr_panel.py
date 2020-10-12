import panel as pn
import param


class MyClass(param.Parameterized):
    clicks = param.Integer()


button = pn.widgets.Button("hello")

button.link()

my = MyClass()
pn.Param(my)
