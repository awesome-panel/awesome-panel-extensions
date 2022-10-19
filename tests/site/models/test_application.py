# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
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
        description="""A site about Panel. The purpose is to inspire and make it easier to create
awesome analytics apps in Python and Panel.""",
        url="https://awesome-panel.org",
        thumbnail="",
        tags=["Site"],
        author=user,
        # pylint: disable=line-too-long
        resources={
            "code": "https://github.com/MarcSkovMadsen/awesome-panel/tree/main/application/pages/async_tasks/async_tasks.py",
            "gif": "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel-assets/main/awesome-panel/applications/async_tasks.gif",
            "mp4": "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel-assets/main/awesome-panel/applications/async_tasks.mp4",
            "documentation": "d",
            "youtube": "b",
            "binder": (
                "https://mybinder.org/v2/gh/MarcSkovMadsen/awesome-panel-extensions/main"
                "?filepath=examples%2Freference%2Fmodels%2FIcon.ipynb"
            ),
        },
    )


def test_can_construct(application):
    assert isinstance(application, Application)
    assert application._repr_html_()


if __name__.startswith("bokeh"):
    import panel as pn

    pn.config.sizing_mode = "stretch_width"
    pn.pane.HTML(create_application()).servable()
