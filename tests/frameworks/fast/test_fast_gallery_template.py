# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
# pylint: disable=line-too-long

from awesome_panel_extensions.frameworks.fast.templates.fast_gallery_template import (
    FastGalleryTemplate,
)
from awesome_panel_extensions.site.models import Application, User


def get_applications():
    jochem_smit = User(
        name="Jochem Smit",
        url="https://github.com/Jhsmit",
        avatar="https://avatars1.githubusercontent.com/u/7881506?s=400&u=bdf7b6635bf57e7022763ce3b002649fe80ef6a8&v=40",
    )
    marc_skov_madsen = User(
        name="Marc Skov Madsen",
        url="https://datamodelsanalytics.com",
        avatar="https://avatars0.githubusercontent.com/u/42288570",
    )

    applications = [
        Application(
            name="Async Tasks",
            description="We show case how to start a background thread that updates a progressbar while the rest of the application remains responsive.",
            url="https://awesome-panel.org",
            thumbnail="https://github.com/MarcSkovMadsen/awesome-panel/raw/main/assets/images/thumbnails/async_tasks.png",
            resources={
                "code_url": "https://github.com/MarcSkovMadsen/awesome-panel/blob/main/application/pages/async_tasks/async_tasks.py",
                "youtube_url": "https://www.youtube.com/watch?v=Ohr29FJjBi0&t=791s",
                "documentation_url": "https://awesome-panel.readthedocs.org",
            },
            author=jochem_smit,
            tags=[
                "Code",
                "App In Gallery",
            ],
        ),
        Application(
            name="Bootstrap Dashboard",
            description="",
            url="https://awesome-panel.org",
            thumbnail="https://github.com/MarcSkovMadsen/awesome-panel/raw/main/assets/images/thumbnails/bootstrap_dashboard.png",
            resources={
                "code": "https://github.com/MarcSkovMadsen/awesome-panel/blob/main/application/pages/bootstrap_dashboard/main.py",
            },
            author=marc_skov_madsen,
            tags=[
                "Code",
                "App In Gallery",
            ],
        ),
        Application(
            name="Custom Bokeh Model",
            description="",
            url="https://awesome-panel.org",
            thumbnail="https://github.com/MarcSkovMadsen/awesome-panel/raw/main/assets/images/thumbnails/custom_bokeh_model.png",
            resources={
                "code": "https://github.com/MarcSkovMadsen/awesome-panel/blob/main/application/pages/custom_bokeh_model/custom.py",
            },
            author=marc_skov_madsen,
            tags=[
                "Code",
                "App In Gallery",
            ],
        ),
    ]
    return applications


def test_can_construct():
    FastGalleryTemplate(
        site_name="Awesome Panel Gallery",
        site_url="https://awesome-panel.org",
        description="ABCD",
        resources=get_applications(),
        target="_blank",
    )


def test_get_manual_test_app():
    return FastGalleryTemplate(
        site="Awesome Panel",
        site_url="https://awesome-panel.org",
        title="Gallery",
        description="""The purpose of the Awesome Panel Gallery is to inspire and help you create awesome analytics apps in using the tools you know and love.""",
        # background_image_url="https://ih1.redbubble.net/image.875683605.8623/ur,mug_lifestyle,tall_portrait,750x1000.jpg",
        resources=get_applications(),
        target="_blank",
        theme_toggle=False,
    )


if __name__.startswith("bokeh"):
    test_get_manual_test_app().servable()
