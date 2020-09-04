from awesome_panel_extensions.sketch import sketch_repository
import panel as pn

from awesome_panel_extensions.sketch import (
    Sketch,
    SketchEditor,
    SketchViewer,
    SketchRepository
)


def test_can_construct_with_no_arguments():
    # When
    editor = SketchEditor()
    # Then
    assert isinstance(editor.sketch, Sketch)
    assert isinstance(editor.viewer, SketchViewer)
    assert editor.viewer.sketch is editor.sketch
    assert callable(editor.build)
    assert callable(editor.save)
    assert callable(editor.download)
    assert isinstance(editor.examples, SketchRepository)

    assert callable(editor.servable)
    assert callable(editor.show)


def test_can_construct_with_sketch_argument(
    sketch
):
    # When
    editor = SketchEditor(sketch)
    # Then
    assert editor.sketch is sketch
    assert isinstance(editor.viewer, SketchViewer)
    assert editor.viewer.sketch is editor.sketch

    assert isinstance(editor.examples, SketchRepository)

    assert callable(editor.build)
    assert callable(editor.save)
    assert callable(editor.download)

    assert callable(editor.servable)
    assert callable(editor.show)
