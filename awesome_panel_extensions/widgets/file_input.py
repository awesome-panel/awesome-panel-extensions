import panel as pn
import param


class FileInputStyler(pn.pane.HTML):
    value = param.String(default="Hello World")

    # In order to not be selected by the `pn.panel` selection process
    # Cf. https://github.com/holoviz/panel/issues/1494#issuecomment-663219654
    priority = 0
    # The _rename dict is used to keep track of Panel parameters to sync to Bokeh properties.
    # As value is not a property on the Bokeh model we should set it to None
    _rename = {
        **pn.pane.HTML._rename,
        "value": None,
    }

    def __init__(self, **params):
        super().__init__(**params)
        self._update_object_from_parameters()

    # Don't name the function
    # `_update`, `_update_object`, `_update_model` or `_update_pane`
    # as this will override a function in the parent class.
    @param.depends("value", watch=True)
    def _update_object_from_parameters(self, *events):
        html = """
<style>
input[type=file] {
    width: 100%;
    height: 100px;
    border: 3px dashed #9E9E9E;
    background: #EEEEEE;
    border-radius: 5px;
    text-align: center;
    margin: auto;
}
</style>
        """
        html_extra = """
input[type=file]::before {
  content: 'Select some files';
  color: black;
  display: inline-block;
  background: -webkit-linear-gradient(top, #f9f9f9, #e3e3e3);
  border: 1px solid #999;
  border-radius: 3px;
  padding: 5px 8px;
  outline: none;
  white-space: nowrap;
  -webkit-user-select: none;
  cursor: pointer;
  text-shadow: 1px 1px #fff;
  font-weight: 700;
  font-size: 10pt;
}"""

        example = """
<input type="file" id="file" />
<label for="file">Upload</label>
<style>
[type="file"] {
  border: 0;
  clip: rect(0, 0, 0, 0);
  height: 1px;
  overflow: hidden;
  padding: 0;
  position: absolute !important;
  white-space: nowrap;
  width: 1px;
}

[type="file"] + label {
  background-color: #000;
  border-radius: 4rem;
  color: #fff;
  cursor: pointer;
  display: inline-block;
  padding-left: 2rem 4rem;
}

[type="file"]:focus + label,
[type="file"] + label:hover {
    background-color: #f15d22;
}

[type="file"]:focus + label {
  outline: 1px dotted #000;
}
</style>"""
        self.object = html
