import param
import panel as pn
from param.parameterized import Parameters
from yaml import events


class BinderButton(pn.pane.Markdown):
    repository = param.String()
    branch = param.String()
    folder = param.String()
    file = param.String()

    # In order to not be selected by the `pn.panel` selection process
    # Cf. https://github.com/holoviz/panel/issues/1494#issuecomment-663219654
    priority = 0

    width = param.Integer(default=200, bounds=(0,None))
    height = param.Integer(default=50, bounds=(0,None))

    def __init__(self, **params):
        # The _rename dict is used to keep track of Panel parameters to sync to Bokeh properties.
        # As value is not a property on the Bokeh model we should set it to None
        self._rename.update({"repository": None, "branch": None, "folder": None, "file": None})
        super().__init__(**params)



        self._update_object()

    # Don't name the function `_update` as this will override a function in the parent class
    @param.depends(
        "repository", "branch", "folder", "file", "height", "width", "sizing_mode", watch=True
    )
    def _update_object(self, *events):
        if self.sizing_mode == "fixed":
            style = f"height:{self.height}px;width:{self.width}px;"
        elif self.sizing_mode == "stretch_width":
            style = f"width:{self.width}px;"
        elif self.sizing_mode == "stretch_height":
            style = f"height:{self.height}px;"
        else:
            style = f"height:100%;width:100%;"

        self.object = self.to_markdown(
            repository=self.repository,
            branch=self.branch,
            folder=self.folder,
            file=self.file,
            style=style,
        )

    @classmethod
    def to_markdown(self, repository: str, branch: str, folder: str, file: str, style: str = None):
        folder = folder.replace("/", "%2F").replace("\\", "%2F")
        url = f"https://mybinder.org/v2/gh/{repository}/{branch}?filepath={folder}%2F{file}"
        if style:
            image = f'<img src="https://mybinder.org/badge_logo.svg" style="{style}">'
        else:
            image = f'<img src="https://mybinder.org/badge_logo.svg">'
        markdown = f"[{image}]({url})"
        print(markdown)
        return markdown


button = BinderButton(
    repository="marcskovmadsen/awesome-panel-extensions",
    branch="master",
    folder="examples/panes",
    file="WebComponent.ipynb",
)
settings_pane = pn.Param(
    button, parameters=["repository", "branch", "folder", "file", "height", "width", "sizing_mode", "margin"], background="lightgray", sizing_mode="stretch_width"
)
app = pn.Column(button, settings_pane, width=500, height=800)
app.servable()

# html = f'<a href="{url}" target="_blank">{image}</a>'
# def _get_notebook_header(name: str, repository: str, branch: str, folder: str) -> str:
#     return f"""\
# {_get_binder_button(name, repository, branch, folder)}

#  [<img src="https://panel.holoviz.org/_static/logo_stacked.png" style="height:25px;display:inline;margin:5px">](https://panel.holoviz.org) is a framework for creating powerful, reactive analytics apps in Python using the tools you know and love. 💪🐍&#x1F9E1;

# The `{name}` is included in the [awesome-panel-extensions](https://awesome-panel.readthedocs.io/en/latest/packages/awesome-panel-extensions/index.html) package.
# """
