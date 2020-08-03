# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel as pn

from awesome_panel_extensions.developer_tools.designer.designer_core import DesignerCore


class MyComponent(pn.Column):
    pass


def test_can_construct_fixture(designer_core, reload_services):
    isinstance(designer_core, DesignerCore)
    assert designer_core.param.reload_service.objects == reload_services


# endregion
# region: Actions


def test_has_view(designer_core):
    assert designer_core.view


def test_has_component_pane(designer_core):
    assert designer_core.component_pane


def test_has_designer_pane(designer_core):
    assert designer_core.designer_pane


def test_has_action_pane(designer_core):
    assert designer_core.action_pane


def test_has_settings_pane(designer_core):
    assert designer_core.settings_pane


def test_has_css_pane(designer_core):
    assert designer_core.css_pane is not None


def test_has_js_pane(designer_core):
    assert designer_core.js_pane is not None


def test_has_error_pane(designer_core):
    assert designer_core.error_pane
