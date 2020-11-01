# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.models.resource import Author, Resource


def test_can_construct(author):
    assert isinstance(author, Author)
    assert author in Author.all
    assert Resource.all is not Author.all
