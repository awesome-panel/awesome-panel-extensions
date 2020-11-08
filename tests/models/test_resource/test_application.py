# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.site import Application, Resource
from tests.models.test_resource.conftest import create_application


def test_can_construct(application):
    assert isinstance(application, Application)
    assert application in Resource.all
    assert application in Application.all
    assert application._repr_html_()
    assert Resource.all is not Application.all


if __name__.startswith("bokeh"):
    import panel as pn

    pn.config.sizing_mode = "stretch_width"
    pn.panel(create_application()).servable()
