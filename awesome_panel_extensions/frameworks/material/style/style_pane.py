import param
import panel as pn

class StylePane(pn.pane.HTML):
    primary_color = param.Color(default="#22ddff")
    settings_pane = param.Parameter()

    def __init__(self, **params):
        self._rename["primary_color"]=None
        self._rename["settings_pane"]=None

        params["height"]=0
        params["width"]=0
        params["sizing_mode"]="fixed"
        params["margin"]=0
        super().__init__(**params)

        self.settings_pane = pn.Param(
            self.param.primary_color, background="lightgray"
        )

        self._update_object()

    @param.depends("primary_color", watch=True)
    def _update_object(self, *events):
        self.object = f"""
<style>
:root {{
  --mdc-theme-primary: {self.primary_color};
}}
</style>
"""
        print("update", self.primary_color, self.object)
