from awesome_panel_extensions.frameworks.fast.templates.fast import FastTemplate
import panel as pn

def test_app():
    app = FastTemplate(title="Fast Template", )
    app.main[0:2,0:12]=pn.pane.Markdown("Hello World", sizing_mode="stretch_both", background="blue")
    app.main[2:4,0:12]=pn.pane.Markdown("Hello World", sizing_mode="stretch_both", background="green")

    return app

if __name__.startswith("bokeh"):
    test_app().servable()