# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring

from awesome_panel_extensions.p5 import JSSketch

def test_construct():
    # When
    JSSketch()
    # Then
    assert JSSketch.src is None
    assert JSSketch.inner_html is None
    assert JSSketch.div_id.startswith("sketch-holder")

def test_construct_from_src_local_path():
    # Given
    src = "assets/js/sketch.js"
    # When
    JSSketch(script_scr=src)
    # Then
    assert JSSketch.src == src
    assert JSSketch.inner_html is None
    assert JSSketch.div_id.startswith("sketch-holder")

def test_construct_from_url():
    # Given
    src = "https://example.com/assets/js/sketch.js"
    # When
    JSSketch(script_scr=src)
    # Then
    assert JSSketch.src == src
    assert JSSketch.inner_html is None
    assert JSSketch.div_id.startswith("sketch-holder")

def test_construct_from_inner_html():
    # Given
    inner_html = """
function setup() {
    createCanvas(400, 400);
  }

function draw() {
  background(220);
}
"""
    # When
    JSSketch(inner_html)
    # Then
    assert JSSketch.inner_html == inner_html
    assert JSSketch.src is None
    assert JSSketch.div_id.startswith("sketch-holder")

def test_construct_from_div_id():
    # Given
    div_id= "custom-sketch-holder"
    # When
    JSSketch(div_id=div_id)
    # Then
    assert JSSketch.src is None
    assert JSSketch.inner_html is None
    assert JSSketch.div_id == div_id