# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from awesome_panel_extensions.models.resource import Application
from awesome_panel_extensions.models.resource import Author


@pytest.fixture
def author():
    return Author(
        name="Marc Skov Madsen",
        url="https://datamodelsanalytics.com",
        avatar_url="https://avatars0.githubusercontent.com/u/42288570",
        twitter_url="https://twitter.com/MarcSkovMadsen",
        linkedin_url="https://www.linkedin.com/in/marcskovmadsen/",
        github_url="https://github.com/MarcSkovMadsen",
    )


@pytest.fixture
def application(author):
    return Application(
        name="Awesome Panel",
        description="""A site about Panel. The purpose is to inspire and make it easier to create
        awesome analytics apps in Python and Panel.""",
        url="https://awesome-panel.org",
        thumbnail_url="",
        docs_url="",
        code_url="",
        youtube_url="",
        gif_url="",
        author=author,
        tags=["Site"],
    )


@pytest.fixture
def resource(application):
    return application
