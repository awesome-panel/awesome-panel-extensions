# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.models.resource import Application


def test_can_construct(application):
    assert isinstance(application, Application)
