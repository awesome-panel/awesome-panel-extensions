from bokeh.models import Button as _BkButton
from bokeh.core import properties

class FastButton(_BkButton):
    __javascript__ = [
        "https://unpkg.com/@finos/perspective@0.5.2/dist/umd/perspective.js",
        "https://unpkg.com/@finos/perspective-viewer@0.5.2/dist/umd/perspective-viewer.js",
        "https://unpkg.com/@finos/perspective-viewer-datagrid@0.5.2/dist/umd/perspective-viewer-datagrid.js",
        "https://unpkg.com/@finos/perspective-viewer-hypergrid@0.5.2/dist/umd/perspective-viewer-hypergrid.js",
        "https://unpkg.com/@finos/perspective-viewer-d3fc@0.5.2/dist/umd/perspective-viewer-d3fc.js",
    ]

    appearance = properties.String(
        default="neutral",
        help="The appearance attribute",
    )
    autofocus = properties.Bool(
        default=False,
        help="The autofocus attribute",
    )