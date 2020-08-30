# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from awesome_panel_extensions.sketch.sketch_build import SketchBuild


def test_can_construct(tmp_path):
    # Given
    arguments = ["transcrypt", "-n"]
    returncode = 1
    output = "An error"

    # When
    sketch_build = SketchBuild(
        path=tmp_path, arguments=arguments, returncode=returncode, output=output
    )

    # Then
    assert sketch_build.path == tmp_path
    assert sketch_build.js == tmp_path / "sketch.js"
    assert sketch_build.html == tmp_path / "sketch.html"
    assert sketch_build.css == tmp_path / "sketch.css"
    assert sketch_build.arguments == arguments
    assert sketch_build.returncode == returncode
    assert sketch_build.output == output
