"""Base Progress WebComponent"""
import param

from awesome_panel_extensions.web_component import WebComponent


class Progress(WebComponent):
    """Base Progress WebComponent"""

    active = param.Boolean(
        default=True,
        doc="""
        If no value is set the active property toggles animation of the
        progress bar on and off.""",
    )

    bar_color = param.ObjectSelector(
        default="success",
        objects=["primary", "secondary", "success", "info", "danger", "warning", "light", "dark"],
    )

    max = param.Integer(default=100, doc="The maximum value of the progress bar.")

    value = param.Integer(
        default=None,
        bounds=(0, 100),
        doc="""
        The current value of the progress bar. If set to None the progress
        bar will be indeterminate and animate depending on the active
        parameter.""",
    )

    @param.depends("max", watch=True)
    def _update_value_bounds(self):
        self.param.value.bounds = (0, self.max)
