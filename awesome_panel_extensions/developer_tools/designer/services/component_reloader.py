"""This module implements the ComponentReloader. The ComponentReloader is used by the Designer.
For each component you want access to in the Designer you should provide a seperate
Reload Service"""

import datetime
import importlib
import inspect
import pathlib
import sys
import traceback

import panel as pn
import param

from awesome_panel_extensions.developer_tools.designer.views import ErrorView


def _instance(parameter):
    if callable(parameter):
        return parameter()
    if inspect.isfunction(parameter) or inspect.isclass(parameter):
        return parameter()
    return parameter


def _to_instances(dictionary):
    return {parameter: _instance(value) for parameter, value in dictionary.items()}


def _to_parameterized(component_instance) -> param.Parameterized:
    """The component_instance should be an instance of param.Parameterized in order to be
    able to show it in the settings_pane via pn.Param. If not we wrap it with pn.panel"""
    if not isinstance(component_instance, param.Parameterized):
        component_instance = pn.panel(
            component_instance,
            min_height=400,
            sizing_mode="stretch_both",
        )
        if isinstance(component_instance, pn.pane.Plotly):
            component_instance.config = {"responsive": True}
        elif isinstance(component_instance, pn.pane.Vega):
            component_instance.margin = 25

    return component_instance


class ComponentReloader(param.Parameterized):  # pylint: disable=too-many-instance-attributes
    """The ComponentReloader is used by the Designer.
    For each component you want access to in the Designer you should provide a seperate
    Reload Service

    Args:
        component ([type]): For now the components that are know to be supported are

        - subclasses of `pn.reactive.Reactive`
        - subclasses of `param.Parameterized` with a `view` parameter which is a subclass of
        `pn.reactive.Reactive`

    Please NOTE that in order for the reload service to be able to reload the compoonent, the component
    specified cannot be defined in the __main__ file.

    Example
    -------

    ```python
    TITLE_COMPONENT = ComponentReloader(
        component=components.TitleComponent, css_path=COMPONENT_CSS, js_path=COMPONENT_JS,
    )
    EMPTY_COMPONENT = ComponentReloader(
        component=components.EmptyComponent, css_path=COMPONENT_CSS, js_path=COMPONENT2_JS,
    )
    ```"""

    component = param.Parameter(allow_None=False)
    parameters = param.Dict()
    component_instance = param.Parameter()
    css_path = param.Parameter(constant=True)
    js_path = param.Parameter(constant=True)
    modules_to_reload = param.List()

    reload_component = param.Action(label="RELOAD COMPONENT")
    reload_css_file = param.Action(label="RELOAD CSS")
    reload_js_file = param.Action(label="RELOAD JS")

    css_text = param.String()
    js_text = param.String()

    reloading = param.Boolean(default=False)
    last_reload = param.String(constant=True)
    error_message = param.String()

    def __init__(self, component, **params):
        if not isinstance(params, dict):
            params = {}
        params["component"] = component
        super().__init__(**params)

        try:
            name = self.component.name
        except AttributeError:
            name = self.component.__name__

        with param.edit_constant(self):
            self.name = name

        self.reload_component = self._reload_component
        self.reload_css_file = self._reload_css_file
        self.reload_js_file = self._reload_js_file

        self._parameter_instances = None

    def __repr__(self):
        return f"ComponentReloader({self.name})"

    def __str__(self):
        return f"ComponentReloader({self.name})"

    def _reload_component(self, _=None):
        try:
            self._signal_reload_start()

            if self.component_instance is not None:
                for mod in self.modules_to_reload:  # pylint: disable=not-an-iterable
                    importlib.reload(mod)

                mod = sys.modules[self.component.__module__]
                importlib.reload(mod)
                with param.edit_constant(self):
                    self.component = getattr(mod, self.component.__name__)
            if self.parameters:
                if not self._parameter_instances:
                    self._parameter_instances = _to_instances(self.parameters)

                # pylint: disable=not-a-mapping
                component_instance = self.component(**self._parameter_instances)
            else:
                component_instance = self.component()

            self.component_instance = _to_parameterized(component_instance)

            self._reset_error_message()
        except Exception as ex:  # pylint: disable=broad-except
            self._report_exception(ex)
        finally:
            self._signal_reload_end()

    def _reload_css_file(self, _=None):
        try:
            self._signal_reload_start()
            if not self.css_path:
                pass
            elif isinstance(self.css_path, pathlib.Path):
                self.css_text = self.css_path.read_text()
            else:
                raise NotImplementedError

            self._reset_error_message()
        except Exception as ex:  # pylint: disable=broad-except
            self._report_exception(ex)
        finally:
            self._signal_reload_end()

    def _reload_js_file(self, _=None):
        try:
            self._signal_reload_start()
            if not self.js_path:
                pass
            elif isinstance(self.js_path, pathlib.Path):
                self.js_text = self.js_path.read_text()
            else:
                raise NotImplementedError

            self._reset_error_message()
        except Exception as ex:  # pylint: disable=broad-except
            self._report_exception(ex)
        finally:
            self._signal_reload_end()

    def _signal_reload_start(self):
        self.reloading = True
        print("reload start", self.name, datetime.datetime.now())

    def _report_exception(self, ex):  # pylint: disable=unused-argument
        self.error_message = traceback.format_exc()
        self.component_instance = ErrorView(error_message=self.error_message)
        print(self.name, self.error_message)

    def _signal_reload_end(self):
        self.reloading = False
        with param.edit_constant(self):
            self.last_reload = str(datetime.datetime.now())
        print("reload end", self.name, datetime.datetime.now())

    def _reset_error_message(self):
        self.error_message = ""
