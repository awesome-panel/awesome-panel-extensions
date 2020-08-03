# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel as pn
import param

from awesome_panel_extensions.developer_tools.designer.services import ComponentReloader


class MyComponent(pn.Column):
    pass


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
