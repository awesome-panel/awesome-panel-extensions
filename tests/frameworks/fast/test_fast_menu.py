# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from awesome_panel_extensions.frameworks.fast.fast_menu import (
    Resource,
    _group_and_sort,
    _sort_applications,
    to_menu,
    to_menu_item,
)


@pytest.fixture
def resources_by_category():
    return {
        "Main": [Resource(name="Home", category="Main", url="https://panel.holoviz.org")],
        "Apps": [
            Resource(name="Streaming Dashboard", category="Apps", url="https://panel.holoviz.org"),
            Resource(name="Streaming Plots", category="Apps", url="https://panel.holoviz.org"),
        ],
    }


@pytest.fixture
def resources(resources_by_category):
    return resources_by_category["Main"] + resources_by_category["Apps"]


@pytest.fixture
def resource():
    return Resource(name="Panel", url="https://panel.holoviz.org")


def test_to_menu_item(resource):
    # When
    item = to_menu_item(resource)
    # Then
    assert item == '<li><a href="https://panel.holoviz.org">Panel</a></li>'


def test_to_categories_dict(resources, resources_by_category):
    # When
    actual = _group_and_sort(resources)
    # Then
    assert actual == resources_by_category


def test_to_menu(resource):
    resources = [resource]
    # When
    item = to_menu(resources).replace("\n", "")
    # Then
    assert '<li><a href="https://panel.holoviz.org">Panel</a></li' in item


def test_sort_applications():
    # Given
    gallery = Resource(name="Gallery")
    home = Resource(name="Home")
    applications = [gallery, home]
    # When
    actual = _sort_applications(applications)
    # Then
    assert actual == [home, gallery]
