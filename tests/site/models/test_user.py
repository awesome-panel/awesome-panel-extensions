# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.site.models import User

from .conftest import user


def test_can_construct(user):
    assert isinstance(user, User)
    assert user._repr_html_()


if __name__.startswith("bokeh"):
    import panel as pn

    from .conftest import create_user

    user = create_user()
    pn.panel(user, sizing_mode="stretch_both").servable()
