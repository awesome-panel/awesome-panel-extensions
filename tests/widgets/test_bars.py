# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
# pylint: disable=line-too-long
import panel as pn
import pytest

from awesome_panel_extensions.models.link import Link
from awesome_panel_extensions.widgets.bars import TopBar


@pytest.fixture
def left_logo_url():
    return "https://panel.holoviz.org/_static/logo_horizontal.png"


@pytest.fixture
def right_logo_url():
    return "https://panel.holoviz.org/_static/logo_horizontal.png"


@pytest.fixture
def index_application():
    return Link(name="Awesome Panel", url="https://awesome-panel.org")


@pytest.fixture
def active_application():
    return Link(name="Top Bar", url="https://awesome-panel.org")


@pytest.fixture
def applications(index_application, active_application):
    return [index_application, active_application]


@pytest.fixture
def resources():
    return [
        Link(
            name="Twitter",
            url="https://twitter.com/intent/tweet?url=https%3A%2F%2Fawesome-panel.org&text=Checkout",
            icon="""<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" viewBox="0 0 512 512"><path fill="currentColor" d="M459.37 151.716c.325 4.548.325 9.097.325 13.645 0 138.72-105.583 298.558-298.558 298.558-59.452 0-114.68-17.219-161.137-47.106 8.447.974 16.568 1.299 25.34 1.299 49.055 0 94.213-16.568 130.274-44.832-46.132-.975-84.792-31.188-98.112-72.772 6.498.974 12.995 1.624 19.818 1.624 9.421 0 18.843-1.3 27.614-3.573-48.081-9.747-84.143-51.98-84.143-102.985v-1.299c13.969 7.797 30.214 12.67 47.431 13.319-28.264-18.843-46.781-51.005-46.781-87.391 0-19.492 5.197-37.36 14.294-52.954 51.655 63.675 129.3 105.258 216.365 109.807-1.624-7.797-2.599-15.918-2.599-24.04 0-57.828 46.782-104.934 104.934-104.934 30.213 0 57.502 12.67 76.67 33.137 23.715-4.548 46.456-13.32 66.599-25.34-7.798 24.366-24.366 44.833-46.132 57.827 21.117-2.273 41.584-8.122 60.426-16.243-14.292 20.791-32.161 39.308-52.628 54.253z"/></svg>""",
            description="Share on Twitter",
        )
    ]


@pytest.fixture
def social_links():
    return [
        Link(
            name="Twitter",
            url="https://twitter.com/intent/tweet?url=https%3A%2F%2Fawesome-panel.org&text=Checkout",
            icon="""<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" viewBox="0 0 512 512"><path fill="currentColor" d="M459.37 151.716c.325 4.548.325 9.097.325 13.645 0 138.72-105.583 298.558-298.558 298.558-59.452 0-114.68-17.219-161.137-47.106 8.447.974 16.568 1.299 25.34 1.299 49.055 0 94.213-16.568 130.274-44.832-46.132-.975-84.792-31.188-98.112-72.772 6.498.974 12.995 1.624 19.818 1.624 9.421 0 18.843-1.3 27.614-3.573-48.081-9.747-84.143-51.98-84.143-102.985v-1.299c13.969 7.797 30.214 12.67 47.431 13.319-28.264-18.843-46.781-51.005-46.781-87.391 0-19.492 5.197-37.36 14.294-52.954 51.655 63.675 129.3 105.258 216.365 109.807-1.624-7.797-2.599-15.918-2.599-24.04 0-57.828 46.782-104.934 104.934-104.934 30.213 0 57.502 12.67 76.67 33.137 23.715-4.548 46.456-13.32 66.599-25.34-7.798 24.366-24.366 44.833-46.132 57.827 21.117-2.273 41.584-8.122 60.426-16.243-14.292 20.791-32.161 39.308-52.628 54.253z"/></svg>""",
            description="Share on Twitter",
        )
    ]


def test_can_construct_top_bar_without_parameters():
    top_bar = TopBar()

    assert len(top_bar) == 2


def test_can_construct_top_bar_with_parameters(# pylint: disable=too-many-arguments
    left_logo_url,
    index_application,
    active_application,
    applications,
    resources,
    social_links,
    right_logo_url,
):
    applications = (applications,)
    resources = (resources,)
    social_links = (social_links,)

    TopBar(
        left_logo=left_logo_url,
        site=site,
        active_application=active_application,
        right_logo=right_logo_url,
    )


def test_can_add_left_logo_url(left_logo_url):
    top_bar = TopBar(left_logo_url=left_logo_url)

    assert len(top_bar) == 2
    assert isinstance(top_bar[0], pn.pane.PNG)
    assert top_bar[0].object == left_logo_url


def test_can_add_index_and_active_application(index_application, active_application):
    top_bar = TopBar(index_application=index_application, active_application=active_application,)

    assert len(top_bar) == 2
    assert isinstance(top_bar[0], pn.pane.HTML)
    assert index_application.name in top_bar[0].object
    assert index_application.url in top_bar[0].object
    assert active_application.name in top_bar[0].object
    assert active_application.url in top_bar[0].object


def test_can_add_index_and_active_application_and_applications(
    index_application, active_application, applications
):
    bar = TopBar(
        index_application=index_application,
        active_application=active_application,
        applications=applications,
    )

    assert len(bar) == 2
    assert isinstance(bar[0], pn.pane.HTML)
    assert index_application.name in bar[0].object
    assert index_application.url in bar[0].object
    assert active_application.name in bar[0].object
    assert active_application.url in bar[0].object
    assert "<select" in bar[0].object
    for app in applications:
        assert app.name in bar[0].object
        assert app.url in bar[0].object


if __name__.startswith("bokeh"):
    LEFT_LOGO_URL = "https://panel.holoviz.org/_static/logo_horizontal.png"

    index_application = Link(name="Awesome Panel", url="https://awesome-panel.org")
    active_application = Link(name="Top Bar", url="https://awesome-panel.org")
    applications = [index_application, active_application]

    RIGHT_LOGO_URL = "https://panel.holoviz.org/_static/logo_horizontal.png"
    resources = [
        Link(
            name="Twitter",
            url="https://twitter.com/intent/tweet?url=https%3A%2F%2Fawesome-panel.org&text=Checkout",
            icon="""<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" viewBox="0 0 512 512"><path fill="currentColor" d="M459.37 151.716c.325 4.548.325 9.097.325 13.645 0 138.72-105.583 298.558-298.558 298.558-59.452 0-114.68-17.219-161.137-47.106 8.447.974 16.568 1.299 25.34 1.299 49.055 0 94.213-16.568 130.274-44.832-46.132-.975-84.792-31.188-98.112-72.772 6.498.974 12.995 1.624 19.818 1.624 9.421 0 18.843-1.3 27.614-3.573-48.081-9.747-84.143-51.98-84.143-102.985v-1.299c13.969 7.797 30.214 12.67 47.431 13.319-28.264-18.843-46.781-51.005-46.781-87.391 0-19.492 5.197-37.36 14.294-52.954 51.655 63.675 129.3 105.258 216.365 109.807-1.624-7.797-2.599-15.918-2.599-24.04 0-57.828 46.782-104.934 104.934-104.934 30.213 0 57.502 12.67 76.67 33.137 23.715-4.548 46.456-13.32 66.599-25.34-7.798 24.366-24.366 44.833-46.132 57.827 21.117-2.273 41.584-8.122 60.426-16.243-14.292 20.791-32.161 39.308-52.628 54.253z"/></svg>""",
            description="Share on Twitter",
        )
    ]
    social_links = [
        Link(
            name="Twitter",
            url="https://twitter.com/intent/tweet?url=https%3A%2F%2Fawesome-panel.org&text=Checkout",
            icon="""<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" viewBox="0 0 512 512"><path fill="currentColor" d="M459.37 151.716c.325 4.548.325 9.097.325 13.645 0 138.72-105.583 298.558-298.558 298.558-59.452 0-114.68-17.219-161.137-47.106 8.447.974 16.568 1.299 25.34 1.299 49.055 0 94.213-16.568 130.274-44.832-46.132-.975-84.792-31.188-98.112-72.772 6.498.974 12.995 1.624 19.818 1.624 9.421 0 18.843-1.3 27.614-3.573-48.081-9.747-84.143-51.98-84.143-102.985v-1.299c13.969 7.797 30.214 12.67 47.431 13.319-28.264-18.843-46.781-51.005-46.781-87.391 0-19.492 5.197-37.36 14.294-52.954 51.655 63.675 129.3 105.258 216.365 109.807-1.624-7.797-2.599-15.918-2.599-24.04 0-57.828 46.782-104.934 104.934-104.934 30.213 0 57.502 12.67 76.67 33.137 23.715-4.548 46.456-13.32 66.599-25.34-7.798 24.366-24.366 44.833-46.132 57.827 21.117-2.273 41.584-8.122 60.426-16.243-14.292 20.791-32.161 39.308-52.628 54.253z"/></svg>""",
            description="Share on Twitter",
        )
    ]

    TopBar(
        # left_logo_url=left_logo_url,
        index_application=index_application,
        active_application=active_application,
        applications=applications,
        resources=resources,
        social_links=social_links,
        right_logo_url=RIGHT_LOGO_URL,
        background="black",
    ).servable()
