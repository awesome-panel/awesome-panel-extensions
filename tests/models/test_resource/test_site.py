# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from awesome_panel_extensions.site import Site


@pytest.fixture
def site():
    return Site(name="awesome-panel.org")


def test_site(site, author):
    site.authors.append(author)

    app = site.create_application(
        url="home",
        name="Home",
        author="Marc Skov Madsen",
        description="The home page of awesome-panel.org.",
        introduction="The home page",
        thumbnail_url="",
        documentation_url="",
        code_url="",
        gif_url="",
        mp4_url="",
        youtube_url="",
        tags=["Site"],
    )

    @site.add(app)
    def view():  # pylint: disable=unused-variable
        return "abcd"

    assert len(site.applications) == 1
    assert site.applications[0].name == "Home"
    assert view() == "abcd"
