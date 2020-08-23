# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel as pn

from awesome_panel_extensions.widgets.file_input import FileInputStyler


def test_app():
    app = pn.Column(FileInputStyler(), pn.widgets.FileInput(), max_width=800,)
    return app


if __name__.startswith("bokeh"):
    pn.config.sizing_mode = "stretch_width"
    test_app().servable()
