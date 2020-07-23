import param
import panel as pn

def _get_binder_button(name: str, repository: str, branch: str, folder: str) -> str:
    folder=folder.replace("/","%2F").replace("\\", "%2F")
    url=f'https://mybinder.org/v2/gh/{repository}/{branch}?filepath={folder}%2F{name}.ipynb'
    image = '<img src="https://mybinder.org/badge_logo.svg" style="height: 25px ; display: inline ; margin: 5px">'
    return f'<a href="{url}" target="_blank">{image}</a>'

def _get_notebook_header(name: str, repository: str, branch: str, folder: str) -> str:
    return f"""\
{_get_binder_button(name, repository, branch, folder)}

 [<img src="https://panel.holoviz.org/_static/logo_stacked.png" style="height:25px;display:inline;margin:5px">](https://panel.holoviz.org) is a framework for creating powerful, reactive analytics apps in Python using the tools you know and love. 💪🐍&#x1F9E1;

The `{name}` is included in the [awesome-panel-extensions](https://awesome-panel.readthedocs.io/en/latest/packages/awesome-panel-extensions/index.html) package.
"""
