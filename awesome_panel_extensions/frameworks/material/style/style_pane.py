import param
import panel as pn

class StylePane(pn.pane.HTML):
    primary_color = param.Color(default="#22ddff")
    settings_pane = param.Parameter()

    # In order to not be selected by the `pn.panel` selection process
    # Cf. https://github.com/holoviz/panel/issues/1494#issuecomment-663219654
    priority = 0

    def __init__(self, **params):
        # The _rename dict is used to keep track of Panel parameters to sync to Bokeh properties.
        # As value is not a property on the Bokeh model we should set it to None
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

        self._update_object_from_parameters()

    # Don't name the function
    # `_update`, `_update_object_from_parameters`, `_update_model` or `_update_pane`
    # as this will override a function in the parent class.
    @param.depends("primary_color", watch=True)
    def _update_object_from_parameters(self, *events):
        self.object = f"""
<style>
:root {{
  --mdc-theme-primary: {self.primary_color};
}}
</style>
"""
