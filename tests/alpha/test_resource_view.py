# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.alpha import resource_view
from awesome_panel_extensions.models.resource import Author
from awesome_panel_extensions.site import Application

ASSETS = (
    "https://github.com/MarcSkovMadsen/awesome-panel-assets/blob/master/awesome-panel/applications/"
)


def test_view():
    jochem_smit = Author(
        name="Jochem Smit",
        url="https://github.com/Jhsmit",
        avatar_url="https://avatars1.githubusercontent.com/u/7881506",
    )
    resource = Application(
        name="Async Tasks",
        description="""
    When creating apps you sometimes want to run jobs in the background or provide streaming analytics to your users.

    Panel supports these use cases as its running on top of the asynchronous web server Tornado.

    Below we show case how a user can start a background thread that updates a progressbar while the rest of the application remains responsive.

    This example is based on the discussion [Can I load data asynchronously in Panel](https://discourse.holoviz.org/t/can-i-load-data-asynchronously-in-panel/452)?
    """,
        url="async-tasks",
        # pylint: disable=line-too-long
        thumbnail_url="https://github.com/MarcSkovMadsen/awesome-panel/raw/master/assets/images/thumbnails/async_tasks.png",
        code_url="https://github.com/MarcSkovMadsen/awesome-panel/blob/master/application/pages/async_tasks",
        # pylint: enable=line-too-long
        youtube_url="",
        mp4_url=ASSETS + "async_tasks.mp4",
        gif_url=ASSETS + "async_tasks.gif",
        documentation_url="",
        author=jochem_smit,
        tags=[
            "Code",
            "App In Gallery",
        ],
    )

    return resource_view.view(resource)


if __name__.startswith("bokeh"):
    import panel as pn

    pn.config.sizing_mode = "stretch_width"

    test_view().servable()
