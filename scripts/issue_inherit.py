import param
import panel as pn


# class NotebookHeader(param.Parameterized):
#     repository = param.String(
#         default="MarcSkovMadsen/awesome-panel-extensions",
#         doc="The url to the GitHub repository containing the Notebook",
#     )

#     def __init__(self, **params):
#         # self._rename["repository"]=None

#         super().__init__(**params)

if __name__.startswith("bokeh"):
    pn.Column("Hello").servable()
