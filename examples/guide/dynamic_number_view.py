"""The DynamicNumber is an example of a HTML Extension for Panel"""
import panel as pn
import param


class DynamicNumber(param.Parameterized):
    """Extension Implementation"""

    value = param.Integer(default=30, bounds=(0, 100))
    view = param.ClassSelector(class_=pn.reactive.Reactive)

    def __init__(self, **params):
        super().__init__(**params)
        self.view = pn.pane.HTML()
        self._update_object()

    @param.depends("value", watch=True)
    def _update_object(self, *events):
        self.view.object = self._get_html(self.value)

    def _get_html(self, value):
        """Main functionality of Extension"""
        font_size = value
        alpha = 1 - value / 100
        green = int(value * 255 / 100)
        return f"""
    <div style="font-size: {font_size}px;color: rgba(0,{green},0,{alpha}">{value}</div>
    """


# Create app
extension = DynamicNumber()
extension.view.width = 125
extension.view.height = 125
app = pn.Column(
    extension.view,
    extension.param.value,
    width=150,
)
# Serve the app
app.servable()
