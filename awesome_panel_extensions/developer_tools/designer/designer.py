"""The purpose of the Awesome Panel Designer is to improve the development experience in editors
and IDEs by enabling a faster experimentation+development+testing cycle.

Some of the pains the Awesome Panel Designer tries to solve are

- Reload of --dev server is slow and browser window does not automatically update
- Experimenting with layouts and styles takes a long time due to
    - The slow reload of the server
    - You don't have a "live" kernel where you can experiment with changing parameters
    - There is no parameter explorer
    - To work efficiently with an app or component you need long running data and other fixtures to
    be loaded once and for all.

See https://discourse.holoviz.org/t/awesome-panel-designer/643
"""
import pathlib

import panel as pn

from awesome_panel_extensions.developer_tools.designer.designer_core import DesignerCore

ROOT = pathlib.Path(__file__).parent
DESIGNER_TEMPLATE_HTML = ROOT / "designer.html"
# env = Environment(loader=FileSystemLoader("."))
# jinja_template = env.get_template(DESIGNER_TEMPLATE_HTML_STR)


class Designer(pn.Template):
    """The Awesome Panel Designer provides an integrated experience between editor/ IDE and the
Panel Server to enable a quick experiment+develop+test cycle.

Use it from your code or test file.

Args:
    components (Any): A component, ComponentReloader, list of ComponentReloaders one for each
    component or app you want access to in the designer.

Example
-------

The below example can be run via `python`, `panel serve`, `python -m panel serve --dev --show`,
`pytest` or via the integrated `run` or `debug` in your editor which provides a lot of flexibility.

```python
import pathlib

import panel as pn
import param

from awesome_panel_extensions.developer_tools.designer import Designer, ComponentReloader,
components
from awesome_panel.express import Card
from awesome_panel.express.assets import BOOTSTRAP_PANEL_EXPRESS_CSS

FIXTURES = pathlib.Path(__file__).parent / "fixtures"
COMPONENT_CSS = FIXTURES / "component.css"
COMPONENT_JS = FIXTURES / "component.js"
COMPONENT2_JS = FIXTURES / "component2.js"

TITLE_COMPONENT = ComponentReloader(
    component=components.TitleComponent, css_path=COMPONENT_CSS, js_path=COMPONENT_JS,
)
EMPTY_COMPONENT = ComponentReloader(
    component=components.EmptyComponent, css_path=COMPONENT_CSS, js_path=COMPONENT2_JS,
)
CENTERED_COMPONENT = ComponentReloader(
    component=components.CenteredComponent,
    css_path=COMPONENT_CSS,
    js_path=COMPONENT_JS,
    parameters={"component": components.TitleComponent()},
)
STOPPED_COMPONENT = ComponentReloader(
    component=components.StoppedComponent, css_path=COMPONENT_CSS, js_path=COMPONENT_JS,
)
CARD_COMPONENT = ComponentReloader(
    component=Card,
    css_path=BOOTSTRAP_PANEL_EXPRESS_CSS,
    js_path=COMPONENT_JS,
    parameters={
        "header": "Test Card",
        "body": pn.pane.Markdown("Awesome Panel " * 50),
        "collapsable": True,
    },
)


COMPONENT_RELOADERS = [
    TITLE_COMPONENT,
    EMPTY_COMPONENT,
    CENTERED_COMPONENT,
    STOPPED_COMPONENT,
    CARD_COMPONENT,
]


def test_designer():
    return Designer(component_reloaders=COMPONENT_RELOADERS).show()


if __name__.startswith("__main__") or __name__.startswith("bokeh"):
    test_designer()
```
"""

    def __init__(self, components):
        designer = DesignerCore(components=components)
        sidebar = designer.designer_pane
        main = designer.component_pane
        template = DESIGNER_TEMPLATE_HTML.read_text()
        super().__init__(template=template)
        self.add_panel("sidebar", sidebar)
        self.add_panel("main", main)

    def show(  # pylint: disable=too-many-arguments, missing-param-doc, missing-type-doc
        self,
        title=None,
        port=5007,
        websocket_origin=None,
        threaded=False,
        verbose=True,
        open=True,  # pylint: disable=redefined-builtin
        **kwargs
    ):
        """
        Starts a Bokeh server and displays the Viewable in a new tab.

        Arguments
        ---------
        port: int (optional, default=0)
          Allows specifying a specific port
        websocket_origin: str or list(str) (optional)
          A list of hosts that can connect to the websocket.
          This is typically required when embedding a server app in
          an external web site.
          If None, "localhost" is used.
        threaded: boolean (optional, default=False)
          Whether to launch the Server on a separate thread, allowing
          interactive use.
        title : str
          A string title to give the Document (if served as an app)
        verbose: boolean (optional, default=True)
          Whether to print the address and port
        open : boolean (optional, default=True)
          Whether to open the server in a new browser tab

        Returns
        -------
        server: bokeh.server.Server or threading.Thread
          Returns the Bokeh server instance or the thread the server
          was launched on (if threaded=True)
        """
        super().show(
            title=title,
            port=port,
            websocket_origin=websocket_origin,
            threaded=threaded,
            verbose=verbose,
            open=open,
            **kwargs
        )

    def __repr__(self, *_):  # pylint: disable=unused-argument, no-self-use
        return "Designer"

    def __str__(self):
        return "Designer"
