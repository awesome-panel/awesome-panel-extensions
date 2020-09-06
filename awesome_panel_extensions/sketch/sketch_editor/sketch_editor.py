import pathlib
from typing import Optional

import panel as pn
import param

from awesome_panel_extensions.frameworks import fast
from awesome_panel_extensions.sketch.sketch import Sketch
from awesome_panel_extensions.sketch.sketch_repository import SketchRepository
from awesome_panel_extensions.sketch.sketch_viewer import SketchViewer

ROOT = pathlib.Path(__file__).parent
TEMPLATE = ROOT/"sketch_editor.html"
CSS = ROOT/"sketch_editor.css"
JS = ROOT/"sketch_editor.js"
THEMES = ["light", "dark"]
DEFAULT_THEME = "dark"
ACE_THEMES = {
    "light": [
        'chrome',
        'clouds',
        'crimson_editor',
        'dawn',
        'dreamweaver',
        'eclipse',
        'github',
        'iplastic',
        'katzenmilch',
        'kuroir',
        'merbivore',
        'solarized_light',
        'sqlserver',
        'textmate',
        'tomorrow',
        'xcode'
    ],
    "dark":
    [
        'ambiance',
        'chaos',
        'clouds_midnight',
        'cobalt',
        'dracula',
        'gob',
        'gruvbox',
        'idle_fingers',
        'kr_theme',
        'merbivore_soft',
        'mono_industrial',
        'monokai',
        'pastel_on_dark',
        'solarized_dark',
        'terminal',
        'tomorrow_night_blue',
        'tomorrow_night_bright',
        'tomorrow_night_eighties',
        'tomorrow_night',
        'twilight',
        'vibrant_ink',
        ]
}
DEFAULT_ACE_THEME = {
    "light": 'chrome',
    "dark": "tomorrow_night_eighties"
}

class SketchEditor(pn.Template):
    sketch = param.ClassSelector(
        class_=Sketch,
        doc="""The Sketch to edit"""
    )
    viewer = param.ClassSelector(
        class_=SketchViewer,
        doc="""The SketchViewer used to view the build of the Sketch""",
        constant=True
    )
    examples = param.ClassSelector(
        class_=SketchRepository,
        doc="A repository of Sketch examples",
        constant=True
    )
    build = param.Action(
        doc="""Builds the sketch and updates the viewer when triggered"""
    )
    save = param.Action(
        doc="""Saves the sketch"""
    )
    download = param.Action(
        doc="""Downloads the sketch folder as a .zip file"""
    )
    ace_theme = param.ObjectSelector(
        default=DEFAULT_ACE_THEME["dark"],
        objects=ACE_THEMES["dark"],
    )
    ace_theme_select = param.Parameter()

    def __init__(
        self,
        sketch: Optional[Sketch]=None,
        ace_theme: str=DEFAULT_ACE_THEME["dark"]
    ):
        if not sketch:
            sketch=Sketch()

        pn.config.js_files["sketch_editor"]=str(JS.resolve())
        pn.config.css_files.append(str(CSS.resolve()))
        pn.extension()

        super().__init__(
            sketch=sketch,
            viewer=SketchViewer(sketch=sketch),
            examples=SketchRepository.get_examples(),
            build=self._build,
            save=self._save,
            download=self._download,
            ace_theme=ace_theme,
            ace_theme_select=pn.widgets.Select(default=ace_theme, options=ACE_THEMES["dark"], sizing_mode="stretch_width"),
            template=TEMPLATE.read_text()
        )

        self.download_button=pn.widgets.FileDownload(
                callback=self._get_download_file,
                filename='sketch.zip'
        ),

        self.add_variable("sketch_editor_js", JS.read_text())

        self._python_editor = pn.widgets.Ace(
            value=self.sketch.python,
            theme=self.ace_theme,
            sizing_mode="stretch_both",
        )
        self.add_panel("python_editor", self._python_editor)

        self._html_editor = pn.widgets.Ace(
            value=self.sketch.html,
            theme=self.ace_theme,
            sizing_mode="stretch_both",
        )
        self.add_panel("html_editor", self._html_editor)

        self._css_editor = pn.widgets.Ace(
            value=self.sketch.css,
            theme=self.ace_theme,
            sizing_mode="stretch_both",
        )
        self.add_panel("css_editor", self._css_editor)

        self._save_button = fast.FastButton(name="Build", sizing_mode="stretch_width", appearance="accent")
        self.add_panel("build_button", self._save_button)
        self._download_button = fast.FastButton(name="Download", sizing_mode="stretch_width")
        self.add_panel("download_button", self._download_button)
        self._save_button = fast.FastButton(name="Save", sizing_mode="stretch_width")
        self.add_panel("save_button", self._save_button)
        self.add_panel("ace_theme_select", self.ace_theme_select)

        self._configuration_editor = pn.Param(sketch.configuration, sizing_mode="stretch_width")
        self.add_panel("configuration_editor", self._configuration_editor)

    @param.depends("ace_theme_select.value", watch=True)
    def _set_ace_theme(self, *events):
        self._python_editor.theme = self.ace_theme_select.value
        self._html_editor.theme = self.ace_theme_select.value
        self._css_editor.theme = self.ace_theme_select.value


    def _build(self, *events):
        raise NotImplementedError()

    def _save(self, *events):
        raise NotImplementedError()

    def _download(self, *events):
        raise NotImplementedError()

    def _get_download_file(self, *events):
        raise NotImplementedError()


if __name__=="__main__":
    SketchEditor().show(port=5007)
if __name__.startswith("bokeh"):
    SketchEditor().servable()
