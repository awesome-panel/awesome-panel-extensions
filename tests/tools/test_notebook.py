# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.tools.notebooks import _get_notebook_header, _get_binder_button
import pytest

@pytest.fixture
def name():
    return "WebComponent"

@pytest.fixture
def repository():
    return "MarcSkovMadsen/awesome-panel-extensions"

@pytest.fixture
def branch():
    return "master"

@pytest.fixture
def folder():
    return "examples/reference_gallery/panes"

def test_binder_button(name, repository, branch, folder):
    actual=_get_binder_button(name=name, repository=repository, branch=branch, folder=folder)
    assert actual=='<a href="https://mybinder.org/v2/gh/MarcSkovMadsen/awesome-panel-extensions/master?filepath=examples%2Freference_gallery%2Fpanes%2FWebComponent.ipynb" target="_blank"><img src="https://mybinder.org/badge_logo.svg" style="height: 25px ; display: inline ; margin: 5px"></a>'

def test_get_notebook_header(name):
    # Then
    actual = _get_notebook_header(name=name)
    # Then
    assert actual == """\
[<img src="https://mybinder.org/badge_logo.svg" style="height:25px;display:inline;margin:5px">](https://mybinder.org/v2/gh/MarcSkovMadsen/awesome-panel-extensions/master?filepath=examples%2Freference_gallery%2Fpanes%2FWebComponent.ipynb) [<img src="https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg" style="height:25px;display:inline;margin:5px">](https://nbviewer.jupyter.org/github/MarcSkovMadsen/awesome-panel-extensions/blob/master/examples/reference_gallery/panes/WebComponent.ipynb)

 [<img src="https://panel.holoviz.org/_static/logo_stacked.png" style="height:25px;display:inline;margin:5px">](https://panel.holoviz.org) is a framework for creating powerful, reactive analytics apps in Python using the tools you know and love. 💪🐍&#x1F9E1;

The `WebComponent` is included in the [awesome-panel-extensions](https://awesome-panel.readthedocs.io/en/latest/packages/awesome-panel-extensions/index.html) package.
"""
