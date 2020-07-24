import param
import panel as pn

class NotebookHeader(pn.pane.Markdown):
    # In order to not be selected by the `pn.panel` selection process
    # Cf. https://github.com/holoviz/panel/issues/1494#issuecomment-663219654
    priority=0
    repository = param.String(
        default="MarcSkovMadsen/awesome-panel-extensions",
        doc="The url to the GitHub repository containing the Notebook",
    )
    def __init__(self, **params):
        self._rename["repository"]=None

        super().__init__(**params)

pn.Column("Hello", "you").show(port=5006)