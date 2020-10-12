"""In this module we test the Site model"""
# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.models import Application, Logo, Site
from awesome_panel_extensions.models.resource import Resource


def test_can_construct(site):
    assert isinstance(site, Site)
    assert isinstance(site.name, str)
    assert isinstance(site.url, str)
    assert isinstance(site.description, str)
    assert isinstance(site.logo, Logo)
    assert isinstance(site.logo_dark, Logo)
    assert isinstance(site.applications, list)
    for application in site.applications:
        assert isinstance(application, Application)
    assert isinstance(site.resources, list)
    for resource in site.resources:
        assert isinstance(resource, Resource)
