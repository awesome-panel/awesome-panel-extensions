import param
import panel as pn

class StyleApp(param.Parameterized):
    color = param.Color(default="#000000")
    view = param.Parameter()

    def __init__(self, **params):
        super().__init__(**params)

        self._html_pane = pn.pane.HTML(height=100, width=100)
        self.view = pn.Column(self._html_pane, self.param.color)
        self._update_style()

    @param.depends("color", watch=True)
    def _update_style(self, *events):
        self._html_pane.style = {"background-color": self.color}

StyleApp().view.servable()
