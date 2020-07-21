# Awesome Panel Extensions

WORK IN PROGRESS. JUST STARTED. UNDERGOING MAJOR REFACTOR.

CONTRIBUTIONS ARE VERY, VERY WELCOME via

- [Panel Github Issue 1014](https://github.com/holoviz/panel/issues/1014) or
- [A new Github Issue](https://github.com/MarcSkovMadsen/awesome-panel-extensions/issues)

[Panel](https://panel.holoviz.org/) is a framework for creating **powerful, reactive analytics apps in Python using to tools you know and love**.

<a href="https://panel.holoviz.org/" target="_blank"><img src="https://panel.holoviz.org/_static/logo_stacked.png" style="display: block;margin-left: auto;margin-right: auto;height: 50px;"></a>

The purpose of this repository is to **make it easy for Panel developers to develop, share and use awesome Panel extensions**.

Panel Extensions enables developers to compose existing Panel components into new reusable components or wrap an awesome javascript plotting library like [ECharts](https://echarts.apache.org/en/index.html) into a reusable Panel component.

In order to facilitate I've created

- [The Awesome Panel Extensions Package](#the-awesome-panel-extensions-package), that adds additional power and ease of use to Panel.
  - including a [reference gallery](#reference-gallery) of notebooks
- [The Awesome Panel Extensions Guide](https://awesome-panel.readthedocs.io/en/latest/guides/awesome-panel-extensions-guide/index.html), where you can learn how to create your own extensions.
  - including [code examples](examples/guide/)

The Awesome Panel Extensions are provided by [awesome-panel.org](https://awesome-panel.org).


### The Awesome Panel Extensions Package

The Awesome Panel Extensions package contains Panel Extensions that add to the power of Panel.

In this section you will find a description of how to use the Awesome Panel Extensions Package.

#### Reference Gallery

##### Panes

[![Pandas Profile Report Reference Notebook](assets/awesome-panel-extensions/videos/pandas-profile-report-reference.gif)](https://github.com/MarcSkovMadsen/awesome-panel-extensions/blob/master/examples/reference_gallery/panes/PandasProfileReport.ipynb)

#### Installation

You can install the package via

```python
pip install awesome-panel-extensions
```

SHOULD I ADD CONDA PACKAGE?

## Resources

### Awesome Panel Extensions

COMING UP

### Awesome Extensions in Other Frameworks

- [Streamlit Component Gallery](https://www.streamlit.io/components)
- [Streamlit Embed Code](https://github.com/randyzwitch/streamlit-embedcode)
- Jupyter/ IpyWidgets/ Voila - TBD
- Dash - TBD

## Ideas for Awesome Extensions

The below is a list of Awesome Extensions I could come up with that I have currently (20200718) not seen examples of.

Feel free to use them as inspiration for a learning or contributing to the community.

Feel free to implement them in any of the awesome Python Frameworks (Bokeh, Dash, Panel, Streamlit or Voila). If they are implemented in one framework parts of the work can be reused across the frameworks.

### Python in the Browser - BrythonComponent

Wouldn't it be awesome if you could use Python in your browser instead of on the server only? Well it might be possible with [Brython](https://brython.info/index.html).

I would like to be able to write something like

```Python
BrythonComponent(python_code_string)
```

and see something like

[![Brython Tutorial Calculator](assets/awesome-panel-extensions/videos/brython-calculator.gif)](https://brython.info/static_tutorial/en/index.html)

or

[![Brython Snake Game](assets/awesome-panel-extensions/videos/brython_snake_game.gif)](https://medium.com/swlh/sick-of-javascript-just-use-browser-python-4b9679efe08b)

powered by Python running in the Browser.

Maybe the extension can also support bidirectional communication?

I hope this could help you and the Python community create awesome things. I also hope it could help to get Python working in the browser in general.

MORE IDEAS COMING UP. FEEL FREE TO SHARE YOURS.

### Python Scientific Stack in the Browser - PyodideComponent

Wouldn't it be awesome if you could use the Python Scientific Stack in the Browser? Well maybe you can with [Pyodide](https://hacks.mozilla.org/2019/04/pyodide-bringing-the-scientific-python-stack-to-the-browser/).

I would like to be able to write something like

```python
PyodideComponent(python_code_string)
```

and see something like

[![Pyodide Random Walk](assets/awesome-panel-extensions/videos/pyodide-random-walk.gif)](https://www.guangshi.io/posts/run-a-random-walker-in-your-website-using-pyodide/)

powered by the Python Scientific Stack running in the browser.

Maybe the extension can also support bidirectional communication?

I hope this could help you and the Python community create awesome things. I also hope it could help to get Python working in the browser in general.

## Tips & Tricks

### Start With a Working Example and Iterate

Developing extensions and Bokeh extensions in particular can be a bit tricky until you get familiar with it. You might get error messages that you don't understand or know how to solve. For me the best way to start a new extension is to

- Copy a simple example into your project.
  - For Bokeh extensions the [HTMLButton Extension](examples/guide/html_button) is a good, simple example to start with.
- Test that it works via `panel serve` or similar and solve any problems that you might find.
- Stage (`git add`) the changes when the example works.

Then you do very small iterations of develop-test-stage. For example

- Rename folder. Test. Stage.
- Rename files. Test. Stage.
- Rename class (and similar) names in the files. Test. Stage.
- Add incremental functionality. Test. Stage.

Everytime you need to add incremental functionality, you can find the inspiration by studying the documentation or a similar example.

### Use Your Extension Across Frameworks

Wouldn't it be cool if your awesome panel extension could be used in another framework like Streamlit, Bokeh, Voila or Dash?

This is actually becoming more and more of a possibility.

The figure below provides an overview of how components currently can be used across frameworks.

To be determined:

- How to convert Plotly Dash? [jupyter-plotly-dash](https://pypi.org/project/jupyter-plotly-dash/)?

## FAQ

### Should I define default values on the Bokeh .ts, Bokeh .py or Panel .py Model?

TBD

## Roadmap

- How to Test
- How to Debug
- How to use VS Code efficiently to develop extensions
- How to use frameworks like React, Vue and maybe Angular
- Tips & Tricks
- FAQ
- Convert examples to notebooks.
- Integrate with official Panel site
     - For example as example Notebooks in the Gallery?

## LICENSE

The documentation is released under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

The software, including the awesome-panel-extensions package, is released under the [GPLv3 license](https://www.gnu.org/licenses/gpl-3.0.html).

My understanding is that these licenses enables you to use and reuse the material freely as long as you give due credit in the form of a citation.

## For Contributers

### Package build

```bash
python setup.py sdist bdist_wheel
```

### Package Deploy

To test

```bash
python -m twine upload --repository testpypi dist/*
```

to production

```bash
python -m twine upload dist/*
```