from awesome_panel_extensions.sketch import sketch
from awesome_panel_extensions.sketch.sketch_builder import SketchBuilder
from awesome_panel_extensions.sketch.sketch_build import SketchBuild
import json

def test_can_construct():
    # When
    sketch_builder = SketchBuilder()
    # Then

    assert sketch_builder.arguments == ["transcrypt", "-b", "-n", "-m"]

    # - Has Build Arguments for Transcrypt
    assert sketch_builder.build_from_scratch is True
    assert sketch_builder.no_minification is True
    assert sketch_builder.generate_source_map is True

    # - Has Build Arguments for types of output
    assert sketch_builder.build_notebook is False
    assert sketch_builder.build_panel is False


def test_can_build(sketch_source, tmp_path):
    # Given
    sketch_builder = SketchBuilder()
    sketch_source = sketch_source.copy(tmp_path)
    # When
    sketch_build = sketch_builder.build(sketch_source)
    # Then
    assert isinstance(sketch_build, SketchBuild)
    assert sketch_build.js.exists()
    assert sketch_build.html.exists()
    assert sketch_build.css.exists()

    assert set(["transcrypt", "-b", "-n", "-m"]).issubset(sketch_build.arguments)
    assert sketch_build.returncode == 0
    assert sketch_build.output.startswith("\nTranscrypt (TM) Python to JavaScript Small Sane Subset Transpiler")
    assert sketch_build.output.endswith("Ready\n\n")

def test_can_convert_to_dict(sketch_builder):
    assert sketch_builder.to_dict() == {
        "class": "TranscryptSketchBuilder",
        "parameters": {
            "build_from_scratch": sketch_builder.build_from_scratch,
            "no_minification": sketch_builder.no_minification,
            "generate_source_map": sketch_builder.no_minification,
            "build_notebook": sketch_builder.build_notebook,
            "build_pane": sketch_builder.build_panel,
            }
    }

def test_can_convert_to_json(sketch_builder):
    # When
    actual = sketch_builder.to_json()
    # Then
    assert actual == json.dumps(sketch_builder.to_dict())

def test_can_compare(sketch_builder):
    # When
    parameters = sketch_builder.to_dict()["parameters"]
    actual = SketchBuilder(**parameters)
    # Then
    assert actual==sketch_builder

def test_can_copy(sketch_builder):
    # When
    actual = sketch_builder.copy()
    # Then
    assert not actual is sketch_builder
    assert actual == sketch_builder
