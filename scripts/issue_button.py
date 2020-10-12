import param
from panel.widgets import button


class Button(button.Button):
    _name = param.String()

    _rename = {**button.Button._rename, "name": None, "_name": "label"}

    def __init__(self, **params):
        super().__init__(**params)

        self._update_name()

    @param.depends("name")
    def _update_name(self, *_):
        print("update name")
        self._name = "allo " + self.name


Button(name="world").servable()
