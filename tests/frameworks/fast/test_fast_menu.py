# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from awesome_panel_extensions.frameworks.fast.fast_menu import (
    Application,
    _group_and_sort,
    _sort_applications,
    to_menu,
    to_menu_item,
)


@pytest.fixture
def applications_by_category():
    return {
        "Main": [Application(name="Home", category="Main", url="https://panel.holoviz.org")],
        "Apps": [
            Application(
                name="Streaming Dashboard", category="Apps", url="https://panel.holoviz.org"
            ),
            Application(name="Streaming Plots", category="Apps", url="https://panel.holoviz.org"),
        ],
    }


@pytest.fixture
def applications(applications_by_category):
    return applications_by_category["Main"] + applications_by_category["Apps"]


@pytest.fixture
def application():
    return Application(name="Panel", url="https://panel.holoviz.org")


def test_to_menu_item(application):
    # When
    item = to_menu_item(application)
    # Then
    assert item == '<li><a href="https://panel.holoviz.org">Panel</a></li>'


def test_to_categories_dict(applications, applications_by_category):
    # When
    actual = _group_and_sort(applications)
    # Then
    assert actual == applications_by_category


def test_to_menu(application):
    applications = [application]
    # When
    item = to_menu(applications).replace("\n", "")
    # Then
    assert '<li><a href="https://panel.holoviz.org">Panel</a></li' in item


def test_sort_applications():
    # Given
    gallery = Application(name="Gallery")
    home = Application(name="Home")
    applications = [gallery, home]
    # When
    actual = _sort_applications(applications)
    # Then
    assert actual == [home, gallery]
