import json
import shutil
import subprocess

import param
from param.parameterized import shared_parameters

from awesome_panel_extensions.sketch.sketch_build import SketchBuild
from awesome_panel_extensions.sketch.sketch_source import SketchSource

TARGET = "__target__"


class SketchBuilder(param.Parameterized):
    arguments = param.List(
        default=["transcrypt", "-b", "-n", "-m"],
        constant=True,
        doc="""The arguments to transpile from sketch.py to sketch.js""",
    )

    # - Has Build Arguments for Transcrypt
    build_from_scratch = param.Boolean(default=True, doc="Rebuild all target files from scratch")
    no_minification = param.Boolean(default=True, doc="No minification")
    generate_source_map = param.Boolean(default=True, doc="Generate source map")

    # - Has Build Arguments for types of output
    build_js = param.Boolean(default=True, doc="Build sketch.js file?")
    build_notebook = param.Boolean(default=False, doc="Build sketch.ipynb notebook file?")
    build_panel = param.Boolean(default=False, doc="Build app_panel.py Panel App file?")

    def build(self, sketch_source: SketchSource) -> SketchBuild:
        path = str(sketch_source.python.resolve())
        arguments = self.arguments.copy()
        arguments.append(path)
        output = subprocess.run(
            arguments, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
        )

        html = sketch_source.path / TARGET / sketch_source.html.name
        shutil.copy(sketch_source.html, html)
        with html.open("a") as file:
            postfix = self._get_postfix()
            file.write(postfix)
        shutil.copy(sketch_source.css, sketch_source.path / TARGET / sketch_source.css.name)
        return SketchBuild(
            path=sketch_source.path / TARGET,
            arguments=output.args,
            returncode=output.returncode,
            output=output.stdout,
        )

    def _get_postfix(self):
        return """\
<script type="module" src="sketch.js"></script>
<script type="module">import * as sketch from './sketch.js'; window.sketch = sketch;</script>"""

    def to_dict(self):
        return {
            "class": "TranscryptSketchBuilder",
            "parameters": {
                "build_from_scratch": self.build_from_scratch,
                "no_minification": self.no_minification,
                "generate_source_map": self.no_minification,
                "build_notebook": self.build_notebook,
                "build_pane": self.build_panel,
            },
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, SketchBuilder):
            return False
        return self.to_dict() == o.to_dict()

    def copy(self):
        return SketchBuilder(**self.to_dict()["parameters"])
