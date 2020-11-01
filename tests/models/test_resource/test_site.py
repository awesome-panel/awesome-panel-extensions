# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from awesome_panel_extensions.site import Site


@pytest.fixture
def site():
    return Site(name="awesome-panel.org")


def test_site(site, application):
    @site.register(application=application)
    def view():
        print("hello")

    assert site.applications == {"https://awesome-panel.org": application}
    assert site.views["https://awesome-panel.org"].__name__ == view.__name__
