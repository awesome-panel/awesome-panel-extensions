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

import panel as pn
import param

from awesome_panel_extensions.developer_tools.designer import config
from awesome_panel_extensions.developer_tools.designer.components import (
    CenteredComponent,
    StoppedComponent,
    TitleComponent,
)
from awesome_panel_extensions.developer_tools.designer.services import ComponentReloader
from awesome_panel_extensions.developer_tools.designer.views import ErrorView


def _to_component_reloaders(reloaders):
    """Converts the reloaders list to a valid list of ComponentReloaders

    Helper function to enable more easily instantiating the DesignerCore"""
    if not isinstance(reloaders, list):
        return [ComponentReloader(component=reloaders)]

    new = []
    for item in reloaders:
        if isinstance(item, ComponentReloader):
            new.append(item)
        else:
            new.append(ComponentReloader(component=item))
    return new


class DesignerCore(param.Parameterized):  # pylint: disable=too-many-instance-attributes
    """The Awesome Panel Designer provides an integrated experience between editor/ IDE and the
    Panel Server to enable a quick experiment+develop+test cycle.

    Use it from your code or test file.

    Args:
        components (Any): A component, ComponentReloader or list of ComponentReloaders one for each
        component or app you want access to in the designer.

    Example
    -------

    The below example can be run via `python`, `panel serve`, `python -m panel serve --dev --show`,
    `pytest` or via the integrated `run` or `debug` in your editor which provides a lot of
    flexibility.

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
    ```"""

    component_reloader = param.ObjectSelector(label="Component")

    action_pane = param.ClassSelector(class_=pn.Param, constant=True)
    settings_pane = param.ClassSelector(class_=pn.Param, constant=True)
    settings_scroll_pane = param.ClassSelector(class_=pn.Column, constant=True)
    font_pane = param.ClassSelector(class_=pn.pane.HTML, constant=True)

    css_pane = param.ClassSelector(class_=pn.pane.HTML, constant=True)
    js_pane = param.ClassSelector(class_=pn.pane.HTML, constant=True)
    error_pane = param.ClassSelector(class_=pn.pane.Markdown, constant=True)

    title_component = param.ClassSelector(
        class_=TitleComponent, constant=True, label="Title Component"
    )

    designer_pane = param.ClassSelector(class_=pn.reactive.Reactive, constant=True)
    component_pane = param.ClassSelector(class_=CenteredComponent, constant=True)
    stop_server_pane = param.ClassSelector(class_=pn.Param, constant=True)

    view = param.ClassSelector(class_=pn.Row, constant=True)

    show = param.Action(label="SHOW")
    stop_server = param.Action(label="STOP SERVER AND EXIT")

    server = param.Parameter(constant=True)

    def __init__(self, components):
        if not components:
            raise ValueError("Error: component_reloaders is empty. This is allowed")

        pn.config.raw_css.append(config.CSS)

        components = _to_component_reloaders(components)
        self.param.component_reloader.objects = components
        self.param.component_reloader.default = components[0]

        super().__init__()

        with param.edit_constant(self):
            self.name = "Panel Designer App"
            self.title_component = TitleComponent()
            self.css_pane = self._create_css_pane()
            self.js_pane = self._create_js_pane()
            self.component_pane = self._create_component_pane()
            self.action_pane = self._create_action_pane()
            self.settings_pane = self._create_settings_pane()
            self.settings_scroll_pane = self._create_settings_scroll_pane(self.settings_pane)
            self.font_pane = self._create_font_pane()
            self.error_pane = self._create_error_pane()
            self.stop_server_pane = self._create_stop_server_pane()
            self.designer_pane = self._create_designer_pane(
                title_component=self.title_component,
                action_pane=self.action_pane,
                settings_scroll_pane=self.settings_scroll_pane,
                stop_server_pane=self.stop_server_pane,
                font_pane=self.font_pane,
                css_pane=self.css_pane,
                js_pane=self.js_pane,
            )
            self.view = self._create_view(self.component_pane, self.designer_pane)
            self.show = self._show
            self.stop_server = self._stop_server

        self._create_watchers(components)
        self._handle_component_reloader_change()

    def _create_watchers(self, component_reloaders):
        for component_reloader in component_reloaders:
            component_reloader.param.watch(
                self._update_component, ["component_instance"], onlychanged=False
            )
            component_reloader.param.watch(self._update_css_pane, ["css_text"], onlychanged=True)
            component_reloader.param.watch(self._update_js_pane, ["js_text"], onlychanged=True)

    @param.depends("component_reloader", watch=True)
    def _handle_component_reloader_change(self):
        self.component_reloader_.reload_component()  # pylint: disable=not-callable
        self.component_reloader_.reload_css_file()  # pylint: disable=not-callable
        self.component_reloader_.reload_js_file()  # pylint: disable=not-callable

        self._update_component()
        self._update_css_pane()
        self._update_js_pane()

    @property
    def component_reloader_(self) -> ComponentReloader:
        """The same value as component_reloader.

        Use this to avoid linting errors and enable context help and tab completion.

        Returns:
            ComponentReloader: [description]
        """
        return self.component_reloader  # type: ignore

    def _update_component(self, *events):  # pylint: disable=unused-argument
        # pylint: disable=no-member
        action_pane_index = self.designer_pane.objects.index(self.action_pane)
        # pylint: enable=no-member
        with param.edit_constant(self):
            self.action_pane = self._create_action_pane()
        self.designer_pane[action_pane_index] = self.action_pane

        if self.component_reloader_.component_instance:
            self.settings_pane.object = self.component_reloader_.component_instance

            if isinstance(self.component_reloader_.component_instance, pn.reactive.Reactive):
                component_view = self.component_reloader_.component_instance
            elif hasattr(self.component_reloader_.component_instance, "view"):
                component_view = self.component_reloader_.component_instance.view
            else:
                component_view = self.component_reloader_.component_instance

            self.component_pane.component = component_view
            self.component_pane._update()  # pylint: disable=protected-access

        print("_update_component", self.component_reloader)

    def _update_css_pane(self, *events):  # pylint: disable=unused-argument
        self.css_pane.object = f"<style>{self.component_reloader_.css_text}</style>"
        if self.component_reloader_.error_message:
            self._set_error_message()
        print("_update_css_pane", self.component_reloader)

    def _update_js_pane(self, *events):  # pylint: disable=unused-argument
        self.js_pane.object = f"<script>{self.component_reloader_.js_text}</script>"
        if self.component_reloader_.error_message:
            self._set_error_message()
        print("_update_js_pane", self.component_reloader)

    def _set_error_message(self):
        component_view = ErrorView(self.component_reloader_.error_message)
        self.component_pane.component = component_view
        self.component_pane._update()  # pylint: disable=protected-access

    @staticmethod
    def _create_css_pane():
        return pn.pane.HTML(
            name="CSS Pane",
            sizing_mode="fixed",
            width=0,
            height=0,
            margin=0,
            css_classes=["designer-css-pane"],
        )

    @staticmethod
    def _create_js_pane():
        return pn.pane.HTML(
            name="JS Pane",
            sizing_mode="fixed",
            width=0,
            height=0,
            margin=0,
            css_classes=["designer-js-pane"],
        )

    @staticmethod
    def _create_component_pane():
        return CenteredComponent(
            pn.pane.Markdown("hello"),
            name="Component Pane",
            sizing_mode="stretch_both",
            margin=25,
            css_classes=["designer-component-pane"],
        )

    def _create_designer_pane(  # pylint: disable=too-many-arguments
        self,
        title_component,
        action_pane,
        settings_scroll_pane,
        stop_server_pane,
        font_pane,
        css_pane,
        js_pane,
    ):

        return pn.Column(
            title_component.view,
            pn.layout.Divider(margin=(10, 5, 5, 10)),
            pn.Param(
                self,
                parameters=["component_reloader"],
                show_name=False,
                expand_button=False,
                sizing_mode="stretch_width",
            ),
            action_pane,
            pn.layout.Divider(margin=(10, 5, 5, 10)),
            settings_scroll_pane,
            pn.layout.Divider(margin=(10, 5, 5, 10)),
            stop_server_pane,
            font_pane,
            css_pane,
            js_pane,
            name="Designer Pane",
            sizing_mode="stretch_width",
            background="#F5F5F5",
            margin=(0, 0, 0, 0),
            css_classes=["designer-design-pane"],
        )

    def _create_action_pane(self):

        widgets = {
            "reload_component": {
                "button_type": "success",
                "disabled": not self.component_reloader_.component,
            },
            "reload_css_file": {"disabled": not self.component_reloader_.css_path},
            "reload_js_file": {"disabled": not self.component_reloader_.js_path},
        }

        return pn.Param(
            self.component_reloader,
            name="Action Pane",
            sizing_mode="stretch_width",
            parameters=config.ACTION_PARAMETERS,
            widgets=widgets,
            show_name=False,
            css_classes=["designer-action-pane"],
        )

    @staticmethod
    def _create_settings_pane():
        return pn.Param(
            name="Settings Pane",
            sizing_mode="stretch_both",
            css_classes=["designer-settings-pane"],
            margin=(10, 25, 10, 5),
            show_name=False,
        )

    @staticmethod
    def _create_settings_scroll_pane(settings_pane):
        return pn.Column(
            settings_pane,
            name="Settings Scroll Pane",
            css_classes=["designer-settings-scroll"],
            sizing_mode="stretch_width",
            scroll=True,
            height=300,
        )

    @staticmethod
    def _create_error_pane():
        return pn.pane.Markdown(
            name="Error Pane", sizing_mode="stretch_both", css_classes=["designer-error-pane"]
        )

    def _create_stop_server_pane(self):
        return pn.Param(
            self,
            name="Stop Server Pane",
            parameters=["stop_server"],
            widgets={"stop_server": {"button_type": "danger"}},
            sizing_mode="stretch_width",
            show_name=False,
        )

    @staticmethod
    def _create_view(component_pane, designer_pane):
        return pn.Row(
            component_pane,
            designer_pane,
            name="Panel Designer View",
            sizing_mode="stretch_both",
            margin=(0, 0, 0, 0),
            css_classes=["designer-view"],
        )

    @staticmethod
    def _create_font_pane():
        return pn.pane.HTML(
            '<link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500&display=swap"'
            ' rel="stylesheet">'
        )

    def _show(self, _=None, port=5007):
        if not self.server:
            with param.edit_constant(self):
                self.server = self.view.show(port=port)
        else:
            raise NotImplementedError

    def _stop_server(self, _=None):
        self.view[:] = [StoppedComponent().view]
        if self.server:
            self.server.stop()
            with param.edit_constant(self):
                self.server = None
        raise SystemExit

    def __repr__(self):
        return f"PanelDesigner({self.name})"

    def __str__(self):
        return f"PanelDesigner({self.name})"
