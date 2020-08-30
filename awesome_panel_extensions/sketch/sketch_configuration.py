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

    def __init__(self, **params):
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
            links=links,
            js_files=js_files,
            css_files=css_files,
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, SketchConfiguration):
            return False
        return SketchConfiguration(
            name=o.name,
            author=o.author,
            author_url=o.author_url,
            description=o.description,
            links=o.links,
            js_files=o.js_files,
            css_files=o.css_files,
        )

    def save(self, path: pathlib.Path):
        json_text = self.to_json()
        path.write_text(json_text)

    @classmethod
    def read(cls, path: pathlib.Path) -> 'SketchConfiguration':
        json_text = path.read_text()
        json_dict = json.loads(json_text)
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
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
