"""In this module we use the Awesome Panel Designer as a show case for developing the ...
Awesome Panel Designer :-)"""
# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring

from awesome_panel_extensions.developer_tools.designer import Designer
from tests.developer_tools.designer.test_designer_core_show import RELOAD_SERVICES


def test_designer(port=5007, show=False):
    """Run this with `python`, `panel serve --dev` or the integrated python runner or debugger in
    your editor or IDE.

    Args:
        port (int, optional): The port number to show the server on. Defaults to 5007.
        show (bool, optional): [description]. Defaults to False. Change to True if you want to
        use with Python instead of Pytest.

    """
    designer = Designer(reload_services=RELOAD_SERVICES)
    if show:
        designer.show(port=port)


if __name__.startswith("__main__") or __name__.startswith("bokeh"):
    test_designer(show=True)
