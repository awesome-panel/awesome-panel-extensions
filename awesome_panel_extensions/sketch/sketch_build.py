import pathlib
import param
from typing import List

class SketchBuild(param.Parameterized):
    path = param.ClassSelector(
        class_=pathlib.Path,
        doc="""The Path to the build folder.""",
        constant=True,
    )
    python = param.ClassSelector(
        class_=pathlib.Path,
        doc="""The Path to the sketch.py file.""",
        constant=True,
    )
    js = param.ClassSelector(
        class_=pathlib.Path,
        doc="""The Path to the sketch.js file.""",
        constant=True,
    )
    html = param.ClassSelector(
        class_=pathlib.Path,
        doc="""The Path to the sketch.html file.""",
        constant=True,
    )
    css = param.ClassSelector(
        class_=pathlib.Path,
        doc="""The Path to the build sketch.css file.""",
        constant=True,
    )
    arguments = param.List(
        doc="""The arguments used to transpile from sketch.py to sketch.js""",
        constant=True,
    )
    returncode = param.Integer(
        default=0,
        doc="""The return code from the build process""",
        constant=True,
    )
    output = param.String(
        default="",
        doc="""The output to STDOUT or STDERR during the build and any additional messages logged""",
        constant=True,
    )

    def __init__(self, path: pathlib.Path, arguments: List, returncode: int, output: str):
        super().__init__(
            path=path,
            python=path/"sketch.py",
            js=path/"sketch.js",
            html=path/"sketch.html",
            css=path/"sketch.css",
            arguments=arguments,
            returncode=returncode,
            output=output,
        )