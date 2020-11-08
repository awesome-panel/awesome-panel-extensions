# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.site import Author, Resource


def test_can_construct(author):
    assert isinstance(author, Author)
    assert author in Author.all
    assert Resource.all is not Author.all
    assert author._repr_html_()


if __name__.startswith("bokeh"):
    import panel as pn

    from tests.models.test_resource.conftest import create_author

    author = create_author()
    pn.panel(author, sizing_mode="stretch_both").servable()
