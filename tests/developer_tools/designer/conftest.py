# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pathlib

import pytest

from awesome_panel_extensions.developer_tools.designer import (
    ComponentReloader,
    Designer,
)
from awesome_panel_extensions.developer_tools.designer.components.component_with_error import (
    ComponentWithError,
)
from awesome_panel_extensions.developer_tools.designer.designer_core import DesignerCore

from .fixtures.component import Component

FIXTURES = pathlib.Path(__file__).parent / "fixtures"
COMPONENT_CSS = FIXTURES / "component.css"
COMPONENT_JS = FIXTURES / "component.js"


@pytest.fixture
def css_path():
    return COMPONENT_CSS


@pytest.fixture
def js_path():
    return COMPONENT_JS


@pytest.fixture
def modules_to_reload():
    return []


@pytest.fixture
def component():
    return Component


@pytest.fixture
def component_with_error():
    return ComponentWithError


@pytest.fixture
def parameters(css_path, js_path, modules_to_reload):
    return {
        "css_path": css_path,
        "js_path": js_path,
        "modules_to_reload": modules_to_reload,
    }


@pytest.fixture
def component_reloader(component, css_path, js_path, parameters):
    return ComponentReloader(
        component=component,
        css_path=css_path,
        js_path=js_path,
        parameters=parameters,
    )


@pytest.fixture
def component_reloader_with_error(component_with_error):
    return ComponentReloader(component=component_with_error)


@pytest.fixture
def component_reloaders(component_reloader, component_reloader_with_error):
    return [component_reloader, component_reloader_with_error]


@pytest.fixture
def designer_core(component_reloaders):
    return DesignerCore(components=component_reloaders)


@pytest.fixture
def designer(component_reloaders):
    return Designer(components=component_reloaders)
