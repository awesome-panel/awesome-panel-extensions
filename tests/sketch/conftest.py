# # pylint: disable=redefined-outer-name,protected-access, too-many-arguments
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pathlib

import pytest

from awesome_panel_extensions.sketch import Sketch
from awesome_panel_extensions.sketch.sketch_build import SketchBuild
from awesome_panel_extensions.sketch.sketch_builder import SketchBuilder
from awesome_panel_extensions.sketch.sketch_configuration import SketchConfiguration
from awesome_panel_extensions.sketch.sketch_source import SketchSource

SKETCHES = pathlib.Path(__file__).parent / "sketches"
SKETCHES_URL = (
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel-extensions/master/tests/sketch/"
)


@pytest.fixture
def sketch_folder_name() -> str:
    return "hello_world"


@pytest.fixture
def sketch_source(sketch_folder_name):
    path = SKETCHES / sketch_folder_name
    return SketchSource(path=path)

@pytest.fixture
def sketch_configuration():
    return SketchConfiguration(
        name="Hello World Sketch",
        author="Marc Skov Madsen",
        description="A small Hello World Sketch for testing",
        links=["https://awesome-panel.org"],
        license="MIT",
        js_files={},
        css_files=[],
    )


@pytest.fixture
def python_functions():
    def log(iterations):
        node = document.getElementById("sketch-holder")
        for _ in iterations:
            textnode = document.createTextNode("Hello World")
            node.appendChild(textnode)
            br = document.createElement("br")
            node.appendChild(br)

    def main(iterations):
        log(range(iterations))

    return log, main


@pytest.fixture
def python_text():
    return """\
import math

def log(iterations):
    node = document.getElementById("sketch-holder")
    for _ in iterations:
        textnode = document.createTextNode("Hello World")
        node.appendChild(textnode)
        br = document.createElement("br")
        node.appendChild(br)

def main(iterations):
    log(range(iterations))

main(6)"""


@pytest.fixture
def python_functions_prefix():
    return "import math"


@pytest.fixture
def python_functions_postfix():
    return "main(6)"


@pytest.fixture
def python_file():
    return SKETCHES + "hello_world/hello_world.py"


@pytest.fixture
def html_text():
    return '<div id="sketch-holder"></div>'


@pytest.fixture
def css_text():
    return "#sketch-holder {background: salmon;}"


@pytest.fixture
def resources():
    return SketchResources(js_files={}, css_files=[])


@pytest.fixture()
def sketch_from_functions(
    template,
    python_functions,
    python_prefix,
    python_postfix,
    html_text,
    css_text,
    meta_data,
    resources,
):
    # When
    return Sketch(
        *python_functions,
        template=template,
        prefix=python_prefix,
        postfix=python_postfix,
        html=html_text,
        css=css_text,
        meta_data=meta_data,
        resources=resources,
    )


@pytest.fixture()
def sketch(python_text, html_text, css_text, sketch_configuration):
    # When
    return Sketch(
        python=python_text,
        html=html_text,
        css=css_text,
        configuration=sketch_configuration,
    )


@pytest.fixture()
def file_sketch(sketch_source_path):
    # When
    return SketchSource(
        path=sketch_source_path
    )


@pytest.fixture()
def js_file_sketch(js_file, html_file, css_file, meta_data, resources):
    # When
    return JsFileSketch(
        js=js_file, html=html_file, css=css_file, meta_data=meta_data, resources=resources,
    )

@pytest.fixture
def sketch_builder() -> SketchBuilder:
    return SketchBuilder()