"""Functionality for importing the Fast javascript library"""
from panel.pane import HTML

FAST_JS_MODULE = "https://unpkg.com/@microsoft/fast-components"
FAST_JS_SCRIPT = f'<script type="module" src="{FAST_JS_MODULE}"></script>'


def get_fast_js_panel() -> HTML:
    """Returns a panel with the Fast Javascript libary import

    Returns:
        HTML: A Panel to be included in your Fast Application
    """

    return HTML(FAST_JS_SCRIPT, width=0, height=0, sizing_mode="fixed", margin=0)
