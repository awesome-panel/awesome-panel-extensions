import builtins
import json
import pathlib
import shutil

import param

from awesome_panel_extensions.sketch.sketch_configuration import \
    SketchConfiguration


class SketchSource(param.Parameterized):
    path = param.ClassSelector(
        class_=pathlib.Path,
        constant=True,
        doc="The Path to the folder containing the sketch.py etc. source files.",
    )

    @property
    def python(self):
        "The Path to the sketch.py file."
        return self.path / "sketch.py"

    @property
    def html(self):
        "The Path to the sketch.html file."
        return self.path / "sketch.html"

    @property
    def css(self):
        "The Path to the sketch.css file."
        return self.path / "sketch.css"

    @property
    def configuration(self):
        "The Path to the configuration.json file."
        return self.path / "configuration.json"

    def __init__(self, path: pathlib.Path, create: bool=False):
        """The SketchSource represents a local folder of files needed to develop, test and build a
        Sketch.

        Args:
            path (pathlib.Path): The Path to the Sketch source folder.
            create (bool): Whether or not to create the folder and any sketch related files if
            they do not exist.
        """
        super().__init__(path=path)

        if create:
            if not self.path.exists():
                self.path.mkdir(parents=True)
            if not self.python.exists():
                self.python.write_text("")
            if not self.html.exists():
                self.html.write_text("")
            if not self.css.exists():
                self.css.write_text("")
            if not self.configuration.exists():
                self.configuration.write_text("")

    def copy(self, path: pathlib.Path) -> 'SketchSource':
        """Returns a copy of the path source

        This includes copying the original sketch files to the new path

        Returns:
            [SketchSource]: A copy of the SketchSource
        """
        if self.path==path:
            return self

        sketch_source = SketchSource(
            path=path,
        )

        shutil.copy(self.python, sketch_source.python)
        shutil.copy(self.html, sketch_source.html)
        shutil.copy(self.css, sketch_source.css)
        shutil.copy(self.configuration, sketch_source.configuration)

        return sketch_source