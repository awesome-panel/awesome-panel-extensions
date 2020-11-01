"""This module contains functionality used by awesome-panel in Notebooks"""
import panel as pn
import param

from awesome_panel_extensions.widgets.link_buttons import (
    BinderLinkButton,
    NBViewerLinkButton,
    PanelLinkButton,
)

pn.extension()

DEFAULT_HEADER_MESSAGE = """\
[Panel](https://panel.holoviz.org) is a framework for creating powerful, reactive analytics apps in
Python using the tools you know and love. 💪🐍❤️.
This notebook is brought to you by [awesome-panel.org](https://awesome-panel.org).
"""


class Header(pn.Column):
    """Extension Implementation"""

    def __init__(  # pylint: disable=too-many-arguments
        self,
        folder: str,
        notebook: str,
        repository: str = "marcskovmadsen/awesome-panel-extensions",
        branch: str = "master",
        message: str = DEFAULT_HEADER_MESSAGE,
        **params,
    ):
        params["sizing_mode"] = params.get("sizing_mode", "stretch_width")
        super().__init__(**params)
        self.binder_link_button = BinderLinkButton(
            repository=repository,
            branch=branch,
            folder=folder,
            notebook=notebook,
        )
        self.nbviewer_link_button = NBViewerLinkButton(
            repository=repository,
            branch=branch,
            folder=folder,
            notebook=notebook,
        )
        self.panel_link_button = PanelLinkButton(theme="dark")

        text = pn.pane.Markdown(message, sizing_mode="stretch_width")
        buttons = pn.Row(
            self.panel_link_button,
            self.binder_link_button,
            self.nbviewer_link_button,
            Style(container_width="90%"),
            sizing_mode="stretch_width",
        )
        self[:] = [buttons, text]


class Style(pn.pane.HTML):
    """Class for styling a reference notebook"""

    container_width = param.String(default="100%")

    # In order to not be selected by the `pn.panel` selection process
    # Cf. https://github.com/holoviz/panel/issues/1494#issuecomment-663219654
    priority = 0
    # The _rename dict is used to keep track of Panel parameters to sync to Bokeh properties.
    # As value is not a property on the Bokeh model we should set it to None
    _rename = {
        **pn.pane.HTML._rename,
        "container_width": None,
    }

    def __init__(self, **params):
        super().__init__(**params)
        self._update_object_from_parameters()

    # Don't name the function
    # `_update`, `_update_object`, `_update_model` or `_update_pane`
    # as this will override a function in the parent class.
    @param.depends("container_width", watch=True)
    def _update_object_from_parameters(self, *_):
        self.object = f"<style>.container {{ width:{self.container_width} !important; }}</style>"
