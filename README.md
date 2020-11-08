# Awesome Panel Extensions

THIS PROJECT HAS JUST STARTED (20200721) AND IS RAPIDLY DEVELOPING

[Panel](https://panel.holoviz.org/) is a framework for creating **powerful, reactive analytics apps in Python using to tools you know and love**.

<a href="https://panel.holoviz.org/" target="_blank"><img src="https://panel.holoviz.org/_static/logo_stacked.png" style="display: block;margin-left: auto;margin-right: auto;height: 50px;"></a>

The `awesome-panel-extensions` package contains Panel Extensions and Tools that add to the power of Panel.

You can install the package via

```python
pip install awesome-panel-extensions
```

If you wan't to get started with an **example** check out the [Pandas Profile Report Reference Notebook](https://github.com/MarcSkovMadsen/awesome-panel-extensions/blob/master/examples/reference/panes/PandasProfileReport.ipynb)

[![Pandas Profile Report Reference Notebook](https://github.com/MarcSkovMadsen/awesome-panel-extensions/raw/master/assets/images/pandas-profile-report-pane-app.png)](https://github.com/MarcSkovMadsen/awesome-panel-extensions/blob/master/examples/reference/panes/PandasProfileReport.ipynb)

If you wan't to **learn more** checkout the [Package Documentation](https://awesome-panel.readthedocs.io/en/latest/packages/awesome-panel-extensions/index.html).

If you wan't to **develop your own Awesome Panel Extensions** check out the [Awesome Panel Extensions Guide](https://github.com/marcskovmadsen/awesome-panel-extensions).

Please note that this package is an **alpha stage**. The api might change or functionality might be moved into Panel or to stand alone packages. If you find a version that works for you please pin it.

Awesome Panel Extensions are provided by [awesome-panel.org](https://awesome-panel.org).

## LICENSE

The documentation is released under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

The software, including the awesome-panel-extensions package, is released under the [GPLv3 license](https://www.gnu.org/licenses/gpl-3.0.html).

My understanding is that these licenses enables you to use and reuse the material freely as long as you give due credit in the form of a citation.

## For Contributers

### Bokeh Extensions build

```bash
cd awesome_panel_extensions
bokeh build
cd ..
```

### Package build

In the `setup.py` file update the `version` number and then run

```bash
python setup.py sdist bdist_wheel
```

### Package Deploy

to production

```bash
python -m twine upload dist/*20201101.2*
```

or to test

```bash
python -m twine upload --repository testpypi dist/*20200910.1*
```

Have binder build the new image: [binder](https://mybinder.org/v2/gh/MarcSkovMadsen/awesome-panel-extensions/master?filepath=examples%2Freference%2Fframeworks%2Fmaterial%2FMaterialIntSlider.ipynb)

### Build and Run Binder Image Locally

In order to test the Binder Image you can install repo2docker

```python
python -m pip install jupyter-repo2docker
```

You can then run

```python
jupyter-repo2docker https://github.com/MarcSkovMadsen/awesome-panel-extensions
```

Note: Does not work on Windows.

### Open Binder

Open Binder to rebuild the package

[Open Binder](https://mybinder.org/v2/gh/MarcSkovMadsen/awesome-panel-extensions/master?filepath=examples%2Freference%2Fpanes%2FPandasProfileReport.ipynb)