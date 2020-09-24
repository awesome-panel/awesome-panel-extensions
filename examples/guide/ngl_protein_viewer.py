"""
This is an example of a Protein viewer app, using [NGL Viewer](https://github.com/nglviewer/ngl), implemented as
panel HTML pane.

Source: Discussion on [Discourse 583]\
(https://discourse.holoviz.org/t/how-to-use-ngl-webgl-protein-viewer-in-panel/583)
"""

import panel as pn
import param


class NGLViewer(pn.pane.HTML):
    pdb_string = param.String()
    rcsb_id = param.String()
    representation = param.Selector(default='ribbon',
                                    objects=['ball+stick', 'backbone', 'ball+stick', 'cartoon', 'hyperball', 'licorice',
                                             'ribbon', 'rope', 'spacefill', 'surface'])
    color_scheme = param.Selector(default='chainid', objects=['chainid', 'residueindex', 'chainname'])
    spin = param.Boolean(default=False)
    priority = 0
    _rename = dict(pn.pane.HTML._rename, pdb_string=None, rcsb_id=None, representation=None, spin=None, color_scheme=None)

    def __init__(self, **params):
        super().__init__(**params)
        self.load_string = \
        f"""
        stage = new NGL.Stage("viewport");
        stage.loadFile()"""
        self._update_object_from_parameters()

    @param.depends('representation', 'spin', 'color_scheme', watch=True)
    def _update_object_from_parameters(self):
        html =\
            f"""
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

    @param.depends('pdb_string', watch=True)
    def _update_object_from_pdb_string(self):
        self.load_string = \
            f"""
            var PDBString = `{self.pdb_string}`;
            stage = new NGL.Stage("viewport");
            stage.loadFile( new Blob([PDBString], {{type: 'text/plain'}}), {{ ext:'pdb'}} )"""
        self._update_object_from_parameters()

    @param.depends('rcsb_id', watch=True)
    def _update_object_from_rcsb_id(self):
        self.load_string = \
            f"""
            stage = new NGL.Stage("viewport");
            stage.loadFile("rcsb://{self.rcsb_id}")"""
        self._update_object_from_parameters()


class ProteinViewer(param.Parameterized):

    input_option = param.Selector(objects=['Upload File', 'RCSB PDB'])
    rcsb_id = param.String()
    load_structure = param.Action(lambda self: self._load_structure())

    def __init__(self, **param):
        super(ProteinViewer, self).__init__(**param)
        self.file_widget = pn.widgets.FileInput(accept='.pdb')
        self.ngl_html = NGLViewer(height=500, width=500)

    def _load_structure(self):
        if self.input_option == 'Upload File':
            if self.file_widget.value:
                string = self.file_widget.value.decode()
                self.ngl_html.pdb_string = string
            else:
                pass

        elif self.input_option == 'RCSB PDB':
            self.ngl_html.rcsb_id = self.rcsb_id

    def view(self):
        col = pn.Column(*pn.Param(self.param))
        col.insert(2, self.file_widget)
        col.append(self.ngl_html.param.representation)
        col.append(self.ngl_html.param.color_scheme)
        col.append(self.ngl_html.param.spin)
        app = pn.Row(
            col,
            self.ngl_html
        )

        return app


pn.config.js_files["ngl"]="https://unpkg.com/ngl@2.0.0-dev.37/dist/ngl.js"
pn.extension()

pv = ProteinViewer()
pv.view().servable()