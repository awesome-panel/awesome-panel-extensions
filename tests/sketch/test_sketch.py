# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.sketch.sketch_configuration import SketchConfiguration
from awesome_panel_extensions.sketch import Sketch
from awesome_panel_extensions.sketch.sketch_source import SketchSource
from awesome_panel_extensions.sketch.sketch_build import SketchBuild


def test_constructor_no_arguments():
    sketch = Sketch()

    # Then
    assert sketch.python == ""
    assert sketch.html == ""
    assert sketch.css == ""
    assert isinstance(sketch.configuration, SketchConfiguration)

def test_can_construct_from_text(python_text, html_text, css_text, sketch_configuration):
    # When
    sketch = Sketch(
        python=python_text,
        html=html_text,
        css=css_text,
        configuration=sketch_configuration,
    )
    # Then
    assert sketch.python == python_text
    assert sketch.html == html_text
    assert sketch.css == css_text
    assert sketch.configuration == sketch_configuration

def test_constructor_from_text_and_callables(python_functions, python_functions_prefix, python_functions_postfix, python_text):
    # When
    actual = Sketch(
        python=[python_functions_prefix, *python_functions, python_functions_postfix]
    )
    # Assert
    assert actual.python==python_text

def test_save(sketch, tmp_path):
    # When
    actual_source = sketch.save(path=tmp_path)
    actual = Sketch.read(actual_source)
    # Assert
    assert isinstance(actual_source, SketchSource)
    assert actual == sketch

def test_can_read(sketch_source, sketch):
    # When
    actual = Sketch.read(sketch_source)
    # Then
    assert actual == sketch

def test_can_copy(sketch):
    # When
    actual = sketch.copy()
    # Then
    assert not actual is sketch
    assert actual==sketch

def test_can_compare(sketch):
    # When
    actual = Sketch(
        python=sketch.python,
        html=sketch.html,
        css=sketch.css,
        configuration=sketch.configuration.copy(),
    )
    # Then
    assert not actual is sketch
    assert actual == sketch
