"""The DynamicNumber is an example of a HTML Extension for Panel"""
import panel as pn
import param

class DynamicNumber(pn.pane.HTML):
    """Extension Implementation"""
    value = param.Integer(default=30, bounds=(0,100))

    def __init__(self, **params):
        # The _rename dict is used to keep track of Panel parameters to sync to Bokeh properties.
        # As value is not a property on the Bokeh model we should set it to None
        self._rename["value"]=None

        super().__init__(**params)
        self._update_object()

    @param.depends("value", watch=True)
    def _update_object(self, *events):
        # Note:
        # Don't name the function `_update` as this will override a function in the parent class
        self.object = self._get_html(self.value)

    def _get_html(self, value):
        """Main functionality of Extension"""
        font_size = value
        alpha = 1-value/100
        green = int(value*255/100)
        return f"""
    <div style="font-size: {font_size}px;color: rgba(0,{green},0,{alpha}">{value}</div>
    """


if __name__.startswith("bokeh"):
    # Create app
    extension = DynamicNumber(width=125, height=125)
    app = pn.Column(
        extension,
        extension.param.value,
        width=150,
    )
    # Serve the app
    app.servable()