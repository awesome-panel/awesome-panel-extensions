# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.sketch.sketch import Sketch
import pytest

from awesome_panel_extensions.sketch.sketch_source import SketchSource
from awesome_panel_extensions.sketch.sketch_build import SketchBuild

def test_can_construct(tmp_path):
    # When
    sketch = SketchSource(path=tmp_path)

    # Then
    assert sketch.path == tmp_path

    assert sketch.python == tmp_path/"sketch.py"
    assert sketch.html == tmp_path/"sketch.html"
    assert sketch.css == tmp_path/"sketch.css"
    assert sketch.configuration == tmp_path/"configuration.json"

    assert not (sketch.python).exists()
    assert not (sketch.html).exists()
    assert not (sketch.css).exists()
    assert not (sketch.configuration).exists()


def test_can_construct_with_create_argument(tmp_path):
    # When
    sketch = SketchSource(path=tmp_path, create=True)

    # Then
    assert sketch.python == tmp_path/"sketch.py"
    assert sketch.html == tmp_path/"sketch.html"
    assert sketch.css == tmp_path/"sketch.css"
    assert sketch.configuration == tmp_path/"configuration.json"

    # Then
    assert sketch.path == tmp_path
    assert (tmp_path/sketch.python).exists()
    assert (tmp_path/sketch.html).exists()
    assert (tmp_path/sketch.css).exists()
    assert (tmp_path/sketch.configuration).exists()

def test_can_copy(sketch_source, tmp_path):
    # When
    actual = sketch_source.copy(path=tmp_path)
    # Then
    assert not actual is sketch_source
    assert actual.path == tmp_path
    # - This is a short hand for making sure the content of the files of the two are identical
    assert Sketch.read(actual) == Sketch.read(sketch_source)

