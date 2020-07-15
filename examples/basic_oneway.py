import panel as pn
import param

def get_html(value):
    """Main functionality of Extension"""
    font_size = value
    alpha = 1-value/100
    green = int(value*255/100)
    return f"""
<div style="font-size: {font_size}px;color: rgba(0,{green},0,{alpha}">{value}</div>
"""

class BasicExtension(param.Parameterized):
    """Extension Implementation"""
    value = param.Integer(default=30, bounds=(0,100))
    view = param.Parameter()

    def __init__(self, **params):
        super().__init__(**params)
        self.view = pn.pane.HTML(width=125, height=125)
        self._update()

    @param.depends("value", watch=True)
    def _update(self, *events):
        self.view.object = get_html(self.value)

if __name__.startswith("bokeh"):
    # Create app
    extension = BasicExtension()
    app = pn.Column(
        extension.view,
        extension.param.value,
        width=150,
    )
    # Serve the app
    app.servable()

    # Run panel serve 'examples\basic_static.py' in the command line
