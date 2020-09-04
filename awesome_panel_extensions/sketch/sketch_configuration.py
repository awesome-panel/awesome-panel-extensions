from awesome_panel_extensions.sketch.sketch_builder import SketchBuilder
import json
import pathlib
import param


class SketchConfiguration(param.Parameterized):
    name = param.String(
        default="New Sketch", doc="""The name of the Sketch. For example 'New Sketch'"""
    )
    author = param.String(
        default="", doc="""The name of the Author. For example 'Marc Skov Madsen'"""
    )
    author_url = param.String(
        default="",
        doc="""A link to the some web page by or about the author. For example \
'https://github.com/marcSkovMadsen'""",
    )
    thumbnail_url = param.String(
        doc = """A link to a 300px X 300px thumbnail .png image. Default is ''"""
    )
    license = param.String(default="MIT", doc="""The name of the license. For example 'MIT'.""",)
    description = param.String(default="", doc="""""")
    links = param.List(
        doc="""A list of links. For example \
["https://awesome-panel.org"]""",
    )
    js_files = param.Dict(
        doc="""A dictionary of js files used by the Sketch For example \
{"tabulator": "https://unpkg.com/tabulator-tables@4.7.2/dist/js/tabulator.min.js"}""",
    )
    css_files = param.List(
        doc="""A list of css files used by the Sketch. For example \
["https://unpkg.com/tabulator-tables@4.7.2/dist/css/tabulator.min.css"]"""
    )
    builder = param.ClassSelector(
        class_=SketchBuilder,
        doc="A Builder used to build a SketchSource to a SketchBuild"
    )

    def __init__(self, **params):
        if "builder" not in "params":
            params["builder"]=SketchBuilder()
        if "js_files" not in params:
            params["js_files"]={}

        super().__init__(**params)
        if self.name.startswith("SketchConfiguration"):
            self.name = "New Sketch"

    def copy(self) -> "SketchConfiguration":
        if isinstance(self.links, list):
            links = self.links.copy()
        else:
            links = []
        if isinstance(self.js_files, dict):
            js_files = self.js_files.copy()
        else:
            js_files = {}
        if isinstance(self.css_files, list):
            css_files = self.css_files.copy()
        else:
            css_files = []

        return SketchConfiguration(
            name=self.name,
            author=self.author,
            author_url=self.author_url,
            license=self.license,
            description=self.description,
            links=links,
            js_files=js_files,
            css_files=css_files,
            builder=self.builder.copy(),
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, SketchConfiguration):
            return False
        sd = self.to_dict()
        od = o.to_dict()
        sb = sd.pop("builder")
        ob = od.pop("builder")
        return (sd==od and sb==ob)

    def save(self, path: pathlib.Path):
        json_text = self.to_json()
        path.write_text(json_text)

    @classmethod
    def read(cls, path: pathlib.Path) -> 'SketchConfiguration':
        json_text = path.read_text()
        json_dict = json.loads(json_text)
        build_dict = json_dict.get("builder", {})
        builder_parameters_dict = build_dict.get("parameters", {})
        json_dict["builder"]=SketchBuilder(**builder_parameters_dict)
        return cls(**json_dict)

    def to_dict(self)->dict:
        return {
            "name": self.name,
            "author": self.author,
            "author_url": self.author_url,
            "license": self.license,
            "links": self.links,
            "js_files": self.js_files,
            "css_files": self.css_files,
            "builder": self.builder.to_dict()
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
