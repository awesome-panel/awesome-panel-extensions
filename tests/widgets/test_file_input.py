import panel as pn
from awesome_panel_extensions.widgets.file_input import FileInputStyler

def test_app():
    app = pn.Column(
        FileInputStyler(),
        pn.widgets.FileInput(),
        max_width=800,
    )
    return app

if __name__.startswith("bokeh"):
    pn.config.sizing_mode="stretch_width"
    test_app().servable()