# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring

from awesome_panel_extensions.p5 import JSSketch
from awesome_panel_extensions.p5.examples.sketches import js_sketches
import pytest

def test_construct_simple():
    # When
    JSSketch()
    # Then
    assert JSSketch.src is None
    assert JSSketch.inner_html is None
    JSSketch.div_id.starts_width("sketch-")

def test_construct_from_src():
    # Given
    src = "assets/js/sketch.js"
    # When
    JSSketch(script_scr=src)
    # Then
    assert JSSketch.src == src
    assert JSSketch.inner_html is None
    JSSketch.div_id.starts_width("sketch-")

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
    assert JSSketch.div_id.starts_width("sketch-")

def test_construct_from_div_id():
    # Given
    div_id= "my_sketch"
    # When
    JSSketch(div_id=div_id)
    # Then
    assert JSSketch.src is None
    assert JSSketch.inner_html is None
    assert JSSketch.div_id == div_id