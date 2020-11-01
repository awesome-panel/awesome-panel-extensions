# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.models.resource import Resource
from awesome_panel_extensions.site import Application


def test_can_construct(application):
    assert isinstance(application, Application)
    assert application in Resource.all
    assert application in Application.all
    assert Resource.all is not Application.all
