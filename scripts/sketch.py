import pathlib

from awesome_panel_extensions.sketch.sketch_builder import SketchBuilder
from awesome_panel_extensions.sketch.sketch_source import SketchSource

path=pathlib.Path("tests/sketch/sketches/hello_world")
source = SketchSource(path=path)
builder=SketchBuilder()
build=builder.build(source)
print(build.output)

