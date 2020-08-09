"""The Material Extension should be included in your app layout of the value of `.object`
included in your Template"""
# pylint: enable=line-too-long
import panel as pn
import param

# pylint: disable=line-too-long
# <script src="https://cdn.jsdelivr.net/gh/marcskovmadsen/awesome-panel@be59521090b7c9d9ba5eb16e936034e412e2c86b/assets/js/mwc.bundled.js"></script>

_MWC_SCRIPTS = """
    <script src="https://unpkg.com/@material/mwc-button@0.18.0?module" type="module"></script>
    <script src="https://unpkg.com/@material/mwc-select@0.18.0?module" type="module"></script>
    <script src="https://unpkg.com/@material/mwc-list@0.18.0?module" type="module"></script>
    <script src="https://unpkg.com/@material/mwc-slider@0.18.0?module" type="module"></script>
    <script src="https://unpkg.com/@material/mwc-linear-progress@0.18.0?module" type="module"></script>
    <script src="https://unpkg.com/@material/mwc-circular-progress@0.18.0?module" type="module"></script>
"""
_MWC_FONTS = (
    '<link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500" rel="stylesheet">'
    '<link href="https://fonts.googleapis.com/css?family=Material+Icons&display=block" rel="stylesheet">'
)
_MDC_STYLE_SHEET = '<link rel="stylesheet" href="https://unpkg.com/material-components-web@latest/dist/material-components-web.min.css">'
_MWC_ALL = _MWC_FONTS + _MDC_STYLE_SHEET + _MWC_SCRIPTS


class Extension(pn.pane.HTML):  # pylint: disable=too-few-public-methods
    """The Material Extension should be included in your app layout of the value of `.object`
    included in your Template"""

    object = param.Parameter(
        default=None,
        doc="""
        The .js and .css dependencies to include.""",
        constant=True,
    )
    # In order to not be selected by the `pn.panel` selection process
    # Cf. https://github.com/holoviz/panel/issues/1494#issuecomment-663219654
    priority = 0
    # The _rename dict is used to keep track of Panel parameters to sync to Bokeh properties.
    # As value is not a property on the Bokeh model we should set it to None
    _rename = {
        **pn.pane.HTML._rename,
        "value": None,
    }

    def __init__(self, **params):
        params["object"] = _MWC_ALL
        params["height"] = 0
        params["width"] = 0
        params["sizing_mode"] = "fixed"
        params["margin"] = 0
        super().__init__(**params)
