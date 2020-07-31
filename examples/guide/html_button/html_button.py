import panel as pn
import param
from panel.widgets.base import Widget

from . import html_button_model


class HTMLButton(Widget):
    # Set the Bokeh model to use
    _widget_type = html_button_model.HTMLButton

    # Rename panel Parameters -> Bokeh Model properties
    # title should always be renamed to None as it does not exist on the Bokeh model.
    _rename = {
        "title": None,
    }

    # Parameters to be mapped to Bokeh model properties
    object = param.String(default=html_button_model.DEFAULT_OBJECT)
    clicks = param.Integer(default=0)


def _example_app():
    # Default Button
    html_button = HTMLButton()

    # Material Button
    material_js = (
        "https://cdn.jsdelivr.net/gh/marcskovmadsen/awesome-panel"
        "@be59521090b7c9d9ba5eb16e936034e412e2c86b/assets/js/mwc.bundled.js"
    )
    pn.config.js_files["material"] = material_js
    material_html = """\
<link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Material+Icons&display=block" rel="stylesheet">
<style>
mwc-button {
    --mdc-theme-primary: #4CAF50;
    --mdc-theme-on-primary: white;
}
</style>
    """
    material_html_pane = pn.pane.HTML(
        material_html, width=0, height=0, margin=0, sizing_mode="fixed"
    )
    material_button = HTMLButton(
        object="<mwc-button style='width:100%' raised label='Panel' icon='favorite'></mwc-button>",
        height=40,
    )

    # Image Button
    src = "https://github.com/holoviz/panel/raw/master/doc/_static/logo_stacked.png"
    image_style = (
        "height:95%;cursor: pointer;border: 1px solid #ddd;border-radius: 4px;padding: 5px;"
    )
    image_html = f"<img class='image-button' src='{src}' style='{image_style}'>"
    image_button = HTMLButton(object=image_html, height=100, align="center")

    # Bar
    bar = pn.pane.Markdown(
        "## Panel Extension: HTMLButton",
        background="black",
        sizing_mode="stretch_width",
        style={"color": "white", "padding-left": "25px", "padding-top": "10px"},
    )

    app = pn.Column(
        bar,
        material_html_pane,
        html_button,
        html_button.param.clicks,
        material_button,
        material_button.param.clicks,
        image_button,
        image_button.param.clicks,
        width=500,
    )
    return app


if __name__ == "__main__":
    # python -m examples.html_button.html_button
    _example_app().show(port=5006)
