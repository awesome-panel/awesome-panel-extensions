from awesome_panel_extensions.sketch import sketch
from awesome_panel_extensions.sketch.sketch_builder import SketchBuilder
from awesome_panel_extensions.sketch.sketch_build import SketchBuild


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
