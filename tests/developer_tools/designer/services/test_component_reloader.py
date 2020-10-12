# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring

import panel as pn
import param
import plotly.express as px

from awesome_panel_extensions.developer_tools.designer.services import ComponentReloader
from awesome_panel_extensions.developer_tools.designer.services.component_reloader import (
    _instance,
    _to_instances,
    _to_parameterized,
)


class MyComponent(pn.Column):
    pass


def parameter():
    return 200


class MyComponentWithWidth:  # pylint: disable=too-few-public-methods
    def __init__(self, width):
        self.width = width


def test_instance():
    assert _instance(parameter) == 200


def test_to_instances():
    # Given
    dictionary = {"width": parameter}
    # When/ Then
    assert _to_instances(dictionary) == {"width": 200}


def test_can_construct_fixture(component_reloader):
    assert isinstance(component_reloader, ComponentReloader)


def test_can_reload_component(component_reloader, component):
    # Given: I have my component_reloader with an existing component_instance
    old_instance = component_reloader.component_instance
    # When: I reload the component
    component_reloader.reload_component()
    new_instance = component_reloader.component_instance
    # Then: I have a new component instance
    assert not component_reloader.error_message
    assert isinstance(new_instance, component)
    assert component_reloader.component_instance != old_instance


def test_can_reload_reactive_component(component_reloader):
    # Given: MyComponent
    old_instance = component_reloader.component_instance
    # When
    component_reloader.component = MyComponent
    component_reloader.reload_component()
    new_instance = component_reloader.component_instance
    # Then: I have a new component instance
    assert not component_reloader.error_message
    assert isinstance(new_instance, MyComponent)
    assert component_reloader.component_instance != old_instance


def test_can_reload_css_file(component_reloader):
    # Given
    component_reloader.css_text = "dummy"
    # When
    component_reloader.reload_css_file()
    # Then
    assert component_reloader.css_text != "dummy"


def test_can_reload_js_file(component_reloader):
    # Given
    component_reloader.js_text = "dummy"
    # When
    component_reloader.reload_js_file()
    # Then
    assert component_reloader.js_text != "dummy"


def test_can_communicate_reloading_progress(component_reloader):
    assert isinstance(component_reloader.param.reloading, param.Boolean)


def test_can_handle_reload_error(component_reloader_with_error):
    # Given

    # When
    component_reloader_with_error.reload_component()
    # Then
    assert component_reloader_with_error.error_message


def test_can_load_parameters_from_function():
    # Given
    reloader = ComponentReloader(component=MyComponentWithWidth, parameters={"width": parameter})
    reloader.reload_component()
    # Then
    assert isinstance(reloader.component_instance, pn.pane.Str)
    assert isinstance(reloader.component_instance.object, MyComponentWithWidth)
    assert reloader.component_instance.object.width == parameter()


def test_to_parameterized_already_parameterized():
    # Given
    instance = pn.Column()
    # When
    actual = _to_parameterized(instance)
    # Then
    assert actual == instance


def test_to_parameterized_not_parameterized():
    # Given
    instance = MyComponentWithWidth(width=200)
    # When
    actual = _to_parameterized(instance)
    # Then
    assert isinstance(actual, pn.pane.Str)
    assert actual.object == instance


def test_to_parameterized_can_handle_responsive_plotly():
    # Given
    instance = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
    instance.layout.autosize = True
    # When
    actual = _to_parameterized(instance)
    # Then
    assert isinstance(actual, pn.pane.Plotly)
    assert actual.object == instance
    assert actual.config == {"responsive": True}
