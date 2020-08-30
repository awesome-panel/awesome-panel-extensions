from awesome_panel_extensions.sketch.sketch import Sketch
from awesome_panel_extensions.sketch.sketch_configuration import SketchConfiguration


def test_can_construct():
    # When
    actual = SketchConfiguration()
    # Then
    assert actual.name == "New Sketch"
    assert actual.author == ""
    assert actual.author_url == ""
    assert actual.license == "MIT"
    assert actual.description == ""
    assert actual.links == []
    assert actual.js_files is None
    assert actual.css_files == []


def test_can_copy(sketch_configuration):
    # When
    actual = sketch_configuration.copy()
    # Then
    assert not actual is sketch_configuration
    assert actual == sketch_configuration


def test_can_compare(sketch_configuration):
    # When
    actual = SketchConfiguration(
        name=sketch_configuration.name,
        author=sketch_configuration.author,
        author_url=sketch_configuration.author_url,
        description=sketch_configuration.description,
        links=sketch_configuration.links,
        js_files=sketch_configuration.js_files,
        css_files=sketch_configuration.css_files,
    )
    # Then
    assert not actual is sketch_configuration
    assert actual == sketch_configuration


def test_can_save_and_read(sketch_configuration: SketchConfiguration, tmp_path):
    # Given
    path = tmp_path / "sketch.json"
    # When
    sketch_configuration.save(path)
    actual = SketchConfiguration.read(path)
    # Then
    assert actual == sketch_configuration
