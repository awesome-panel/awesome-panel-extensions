"""The SketchViewer enables viewing a Sketch in the Notebook or in a Panel Application"""
import panel as pn
import param # pylint: disable=wrong-import-order

from awesome_panel_extensions.sketch.sketch import Sketch


class SketchViewer(pn.pane.HTML):
    """The SketchViewer enables viewing a Sketch in the Notebook or in a Panel Application"""
    sketch = param.ClassSelector(class_=Sketch)

    # In order to not be selected by the `pn.panel` selection process
    # Cf. https://github.com/holoviz/panel/issues/1494#issuecomment-663219654
    priority = 0
    # The _rename dict is used to keep track of Panel parameters to sync to Bokeh properties.
    # As value is not a property on the Bokeh model we should set it to None
    _rename = {
        **pn.pane.HTML._rename,
        "sketch": None,
    }

    def __init__(self, sketch: Sketch, **params):
        params["sketch"] = sketch
        super().__init__(**params)
        self._update_object_from_parameters()

    @staticmethod
    def _to_object(html: str, css: str, script: str, script_type: str):
        lines = []
        if html:
            lines.append(html)
        if script:
            lines.append(f"""<script type="text/{script_type}">\n{script}\n</script>""")
        if css:
            lines.append(f"<style>\n{css}\n</style>")
        if lines:
            return "\n".join(lines)
        return ""

    # Don't name the function
    # `_update`, `_update_object`, `_update_model` or `_update_pane`
    # as this will override a function in the parent class.
    @param.depends(
        "sketch", "sketch.html", "sketch.css", "sketch.script", "sketch.script_type", watch=True
    )
    def _update_object_from_parameters(self, *_):
        self.object = self._to_object(
            html=self.sketch.html,
            css=self.sketch.css,
            script=self.sketch.script,
            script_type=self.sketch.script_type,
        )
