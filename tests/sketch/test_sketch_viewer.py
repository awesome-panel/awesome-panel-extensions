# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from awesome_panel_extensions.sketch.sketch import Sketch
from awesome_panel_extensions.sketch.sketch_viewer import SketchViewer

TEST_CASES = [
    (
        Sketch(
            html="<div>Hello World</div>",
            css=".div {background: blue;}",
            script="console.log('Hello World)",
            script_type="javascript",
        ),
        """\
<div>Hello World</div>
<script type="text/javascript">
console.log('Hello World)
</script>
<style>
.div {background: blue;}
</style>""",
    ),
    (
        Sketch(
            html="<div>Hello World</div>",
            css=".div {background: blue;}",
            script="print('Hello World')",
            script_type="python",
        ),
        """\
<div>Hello World</div>
<script type="text/python">
print('Hello World')
</script>
<style>
.div {background: blue;}
</style>""",
    ),
]


@pytest.fixture(params=TEST_CASES)
def test_case(request):
    return request.param


@pytest.fixture
def sketch(test_case):
    return test_case[0]


@pytest.fixture
def sketch_viewer_object(test_case):
    return test_case[1]


def test_can_convert_to_object(sketch, sketch_viewer_object):
    # When
    actual = SketchViewer._to_object(
        html=sketch.html, css=sketch.css, script=sketch.script, script_type=sketch.script_type,
    )
    # Then
    assert actual == sketch_viewer_object


def test_can_construct_from_sketch(sketch, sketch_viewer_object):
    # When
    viewer = SketchViewer(sketch=sketch)
    # Then
    assert viewer.object == sketch_viewer_object


def test_updates_when_sketch_script_changes(sketch: Sketch, sketch_viewer_object):
    # Given
    script = sketch.script
    sketch.script = ""
    viewer = SketchViewer(sketch=sketch)
    assert viewer.object != sketch_viewer_object
    # When
    sketch.script = script
    # Then
    assert viewer.object == sketch_viewer_object


def test_updates_when_html_changes(sketch: Sketch, sketch_viewer_object):
    # Given
    html = sketch.html
    sketch.html = ""
    viewer = SketchViewer(sketch=sketch)
    assert viewer.object != sketch_viewer_object
    # When
    sketch.html = html
    # Then
    assert viewer.object == sketch_viewer_object


def test_updates_when_css_changes(sketch: Sketch, sketch_viewer_object):
    # Given
    css = sketch.css
    sketch.css = ""
    viewer = SketchViewer(sketch=sketch)
    assert viewer.object != sketch_viewer_object
    # When
    sketch.css = css
    # Then
    assert viewer.object == sketch_viewer_object
