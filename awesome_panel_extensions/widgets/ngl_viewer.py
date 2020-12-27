"""The [NGL Viewer](https://github.com/nglviewer/ngl) can be used
to visualize and analyse pdb molecule structures.

Source: Discussion on [Discourse 583]\
(https://discourse.holoviz.org/t/how-to-use-ngl-webgl-protein-viewer-in-panel/583)

Author: https://github.com/Jhsmit
"""

import panel as pn
import param

NGL_JS = "https://unpkg.com/ngl@2.0.0-dev.37/dist/ngl.js"
if not "ngl_js" in pn.config.js_files:
    pn.config.js_files["ngl_js"] = NGL_JS

REPRESENTATIONS = [
    "ball+stick",
    "backbone",
    "ball+stick",
    "cartoon",
    "hyperball",
    "licorice",
    "ribbon",
    "rope",
    "spacefill",
    "surface",
]
COLOR_SCHEMES = ["chainid", "residueindex", "chainname"]


class NGLViewer(pn.pane.HTML):
    """The [NGL Viewer](https://github.com/nglviewer/ngl) can be used
    to show and analyse pdb molecule structures"""

    pdb_string = param.String()
    rcsb_id = param.String()
    representation = param.Selector(
        default="ribbon",
        objects=REPRESENTATIONS,
    )
    color_scheme = param.Selector(default="chainid", objects=COLOR_SCHEMES)
    spin = param.Boolean(default=False)
    priority = 0
    _rename = dict(
        pn.pane.HTML._rename,
        pdb_string=None,
        rcsb_id=None,
        representation=None,
        spin=None,
        color_scheme=None,
    )

    def __init__(self, **params):
        super().__init__(**params)
        self.load_string = """
        stage = new NGL.Stage("viewport");
        stage.loadFile()"""
        self._update_object_from_parameters()

    @param.depends("representation", "spin", "color_scheme", watch=True)
    def _update_object_from_parameters(self):
        html = f"""\
<div id="viewport" style="width:100%; height:100%;"></div>
<script>
{self.load_string}.then(function(o){{
    o.addRepresentation("{self.representation}", {{colorScheme: "{self.color_scheme}"}});
    o.autoView();
    }}
);
stage.setSpin({'true' if self.spin else 'false'});
</script>
"""
        self.object = html

    @param.depends("pdb_string", watch=True)
    def _update_object_from_pdb_string(self):
        self.load_string = f"""
            var PDBString = `{self.pdb_string}`;
            stage = new NGL.Stage("viewport");
            stage.loadFile( new Blob([PDBString], {{type: 'text/plain'}}), {{ ext:'pdb'}} )"""
        self._update_object_from_parameters()

    @param.depends("rcsb_id", watch=True)
    def _update_object_from_rcsb_id(self):
        self.load_string = f"""
            stage = new NGL.Stage("viewport");
            stage.loadFile("rcsb://{self.rcsb_id}")"""
        self._update_object_from_parameters()
