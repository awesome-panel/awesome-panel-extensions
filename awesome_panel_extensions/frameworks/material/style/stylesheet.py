"""The Material `Stylesheet` can be included in your app
if you want to have customized styles for your widgets and panes.

The styles are based on [Material Design](https://material.io/design) and the
[MWC](https://github.com/material-components/material-components-web-components) implementation.

As an example you can set the `primary_color` and this corresponds to the `--mdc-theme-primary`
css value.

The Stylesheet `.editor` parameter provides an interactive stylesheet editor.
"""
import panel as pn
import param

_STYLE_PARAMETERS = [
    "primary_color",
    "primary_on_color",
    "secondary_color",
    "secondary_on_color",
    "error_color",
    "error_on_color",
]
_SETTINGS_PARAMETERS = _STYLE_PARAMETERS + ["reset_to_defaults"]
_STYLEPANE_RENAME = {p: None for p in _SETTINGS_PARAMETERS}


class Stylesheet(pn.pane.HTML):
    """The Material `Stylesheet` can be included in your app
    if you want to have customized styles for your widgets and panes.

    The styles are based on [Material Design](https://material.io/design) and the
    [MWC](https://github.com/material-components/material-components-web-components) implementation.

    As an example you can set the `primary_color` and this corresponds to the `--mdc-theme-primary`
    css value.

    The Stylesheet `.editor` parameter provides an interactive stylesheet editor."""

    primary_color = param.Color(default="#4caf50")
    primary_on_color = param.Color(default="#000000")

    secondary_color = param.Color(default="#9c27b0")
    secondary_on_color = param.Color(default="#ffffff")

    error_color = param.Color(default="#f44336")
    error_on_color = param.Color(default="#000000")

    reset_to_defaults = param.Action()

    editor = param.Parameter(doc="An interactive style editor component")

    # Needed for inheritance to work
    priority = 0
    _rename = {**pn.pane.HTML._rename, **_STYLEPANE_RENAME}

    def __init__(self, **params):
        params["height"] = 0
        params["width"] = 0
        params["sizing_mode"] = "fixed"
        params["margin"] = 0
        super().__init__(**params)

        self.editor = pn.WidgetBox(
            pn.Param(
                self,
                parameters=(_SETTINGS_PARAMETERS),
            ),
            name="Material StyleSheet Editor",
        )
        self.reset_to_defaults = self._reset_to_defaults

        self._handle_style_parameter_change()

    # Don't name the function
    # `_update`, `_update_object_from_parameters`, `_update_model` or `_update_pane`
    # as this will override a function in the parent class.
    @param.depends(*_STYLE_PARAMETERS, watch=True)
    def _handle_style_parameter_change(self, *_):
        self.object = f"""
<style>
:root {{
  --mdc-theme-primary: {self.primary_color};
  --mdc-theme-on-primary: {self.primary_on_color};
  --mdc-theme-secondary: {self.secondary_color};
  --mdc-theme-on-secondary: {self.secondary_on_color};
  --mdc-theme-error: {self.error_color};
  --mdc-theme-on-error: {self.error_on_color};

  --mdc-typography-button-font-size: 1.33rem;
}}
body {{
    font-family: roboto;
    font-size: 14px;
}}
mwc-circular-progress {{
    margin-left: auto;
    margin-right: auto;
    display: block;
}}

mwc-button.secondary,
mwc-linear-progress.secondary,
mwc-circular-progress.secondary
{{
    --mdc-theme-primary: {self.secondary_color};
    --mdc-theme-on-primary: {self.secondary_on_color};
}}
mwc-button.warning, mwc-button.danger,
mwc-linear-progress.warning, mwc-linear-progress.danger,
mwc-circular-progress.warning, mwc-circular-progress.danger
{{
    --mdc-theme-primary: {self.error_color};
    --mdc-theme-on-primary: {self.error_on_color};
}}
mwc-button.light,
mwc-linear-progress.light,
mwc-circular-progress.light
{{
    --mdc-theme-primary: #fafafa;
    --mdc-theme-on-primary: black;
}}
mwc-button.dark,
mwc-linear-progress.dark,
mwc-circular-progress.dark
{{
    --mdc-theme-primary: #212121;
    --mdc-theme-on-primary: white;
}}
</style>
"""

    def _reset_to_defaults(self, *_):
        defaults = {p: self.param[p].default for p in _STYLE_PARAMETERS}
        self.param.set_param(**defaults)

    # Needed to avoid infinite recursion
    def __str__(self):
        return "Stylesheet()"

    def __repr__(self, depth=0):  # pylint: disable=unused-argument
        return "Stylesheet()"
