# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from awesome_panel_extensions.site.models import Application, User


def create_user():
    return User(
        name="Marc Skov Madsen",
        url="https://datamodelsanalytics.com",
        avatar="https://avatars0.githubusercontent.com/u/42288570",
        resources={
            "twitter": "https://twitter.com/MarcSkovMadsen",
            "linkedin": "https://www.linkedin.com/in/marcskovmadsen/",
            "github": "https://github.com/MarcSkovMadsen",
        },
    )


def create_application(user=None):
    if not user:
        user = create_user()
    return Application(
        name="Awesome Panel",
        description="""A site about Panel. The purpose is to inspire.""",
        url="https://awesome-panel.org",
        thumbnail="",
        tags=["Site"],
        author=user,
        resources={
            "documentation": "d",
            "code": "a",
            "youtube": "b",
            "gif": "c",
            "binder": (
                "https://mybinder.org/v2/gh/MarcSkovMadsen/awesome-panel-extensions/main"
                "?filepath=examples%2Freference%2Fmodels%2FIcon.ipynb"
            ),
        },
    )


@pytest.fixture
def user():
    return create_user()


@pytest.fixture
def application(user):
    return create_application(user)
