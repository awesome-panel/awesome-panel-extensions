"""This module contains functionality used by awesome-panel in Notebooks"""
import panel as pn

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
        **params
    ):
        params["sizing_mode"] = params.get("sizing_mode", "stretch_width")
        super().__init__(**params)
        self.binder_link_button = BinderLinkButton(
            repository=repository, branch=branch, folder=folder, notebook=notebook,
        )
        self.nbviewer_link_button = NBViewerLinkButton(
            repository=repository, branch=branch, folder=folder, notebook=notebook,
        )
        self.panel_link_button = PanelLinkButton(theme="dark")

        text = pn.pane.Markdown(message, sizing_mode="stretch_width")
        buttons = pn.Row(
            self.panel_link_button,
            self.binder_link_button,
            self.nbviewer_link_button,
            sizing_mode="stretch_width",
        )
        self[:] = [buttons, text]
