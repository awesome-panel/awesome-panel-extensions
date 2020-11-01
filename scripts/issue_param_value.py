from operator import truediv

import panel as pn
import param

from awesome_panel_extensions.frameworks.fast import FastTemplate, FastTextInput

WIDGETS = {
    "some_text": {"type": FastTextInput, "readonly": True, "sizing_mode": "fixed", "width": 400}
}


class ParameterizedApp(param.Parameterized):
    some_text = param.String(default="This is some text")
    view = param.Parameter()

    def __init__(self, **params):
        super().__init__(**params)

        self.view = pn.Param(self, parameters=["some_text"], widgets=WIDGETS)


parameterized_app = ParameterizedApp()
paremeterized_template = FastTemplate(main=[parameterized_app.view])
paremeterized_template.servable()
