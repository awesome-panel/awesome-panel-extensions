import param


import param
from awesome_panel_extensions.data_models import ParameterizedModel
import panel as pn
from awesome_panel_extensions.frameworks.fast import FastTemplate

HTML = """
<fast-text-field id="text-1" placeholder="name"></fast-text-field></br>
<fast-checkbox id="checkbox-1">Checkbox</fast-checkbox></br>
<fast-slider style="width:200px" min="0" max="100" step="1"></fast-slider></br>
<fast-slider id="slider-2" style="width:200px" min="0" max="1" step="0.01"></fast-slider></br>
<fast-tree-view></fast-tree-view>
<fast-button id="button-1">Click Me</fast-button>
"""

INNER_HTML = """
<fast-tree-item>Tree item 1<fast-tree-item slot="item">Tree item 1 - 1</fast-tree-item>
</fast-tree-item>
<fast-tree-item>Tree item 2</fast-tree-item>
"""


def test_app():
    class ExampleClass(ParameterizedModel, param.Parameterized):
        _models = {
            "string_value": {"element": "fast-text-field", "property": "value", "event": "input"},
            "boolean_value": {"element": "checkbox-1", "property": "checked", "event": "change"},
            "integer_value": {"element": "fast-slider", "property": "value", "event": "change"},
            "number_value": {"element": "slider-2", "property": "value", "event": "change"},
            "inner_html": {"element": "fast-tree-view", "property": "innerHTML"},
            "clicks": {"element": "button-1", "event": "click"},
        }
        string_value = param.String()
        boolean_value = param.Boolean()
        integer_value = param.Integer(default=10, bounds=(0, 100), step=1)
        number_value = param.Number(default=0.76, bounds=(0, 1), step=0.01)
        inner_html = param.String(default=INNER_HTML)
        clicks = param.Integer()

    example = ExampleClass(string_value="hello world")

    html_panel = pn.pane.HTML(HTML, height=400, sizing_mode="stretch_width")
    example_panel = pn.Param(
        example,
        parameters=["string_value", "boolean_value", "integer_value", "number_value", "clicks"],
    )

    return FastTemplate(main=[html_panel, example_panel, example.model])


if __name__.startswith("bokeh"):
    test_app().servable()
