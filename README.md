# Panel Extensions Template

[Panel](https://panel.holoviz.org/) is a framework for creating **powerful, reactive analytics apps in Python using to tools you know and love**.

<a href="https://panel.holoviz.org/" target="_blank"><img src="https://panel.holoviz.org/_static/logo_stacked.png" style="display: block;margin-left: auto;margin-right: auto;height: 50px;"></a>

The purpose of this repository is to **make it easy for Panel developers to create custom Panel extensions**.

In order to facilitate this, this repo contains

- Documentation (See below)
- Examples (See the [examples](/examples/) folder)
- An Extensions Starter Template (See [src](/examples/) folder)

## Extensions Overview

Panel supports two types of extensions *One Way Extensions* and *Bidirectional Extensions*.

**One Way Extensions** are extensions that are created using the `HTML` pane. You can combine HTML, CSS and/ or JS to create amazing extensions to Panel. But these extensions cannot communicate from the browser back to Python.

**Bidirectional Extensions** on the other hand supports bidirectional communication from Python to the Browser and back. This is how all the layouts, panes and widgets of Panel are created. This functionality is uses the [Bokeh Extensions](ttps://docs.bokeh.org/en/latest/docs/user_guide/extensions.html) api.

## Examples

### Basic One Way Example

```Python
import panel as pn
import param

def get_html(value):
    """Main functionality of Extension"""
    font_size = value
    alpha = 1-value/100
    green = int(value*255/100)
    return f"""
<div style="font-size: {font_size}px;color: rgba(0,{green},0,{alpha}">{value}</div>
"""

class BasicExtension(param.Parameterized):
    """Extension Implementation"""
    value = param.Integer(default=30, bounds=(0,100))
    view = param.Parameter()

    def __init__(self, **params):
        super().__init__(**params)
        self.view = pn.pane.HTML(width=125, height=125)
        self._update()

    @param.depends("value", watch=True)
    def _update(self, *events):
        self.view.object = get_html(self.value)
```

You can try out the extension via

```Python
# Create app
extension = BasicExtension()
app = pn.Column(
    extension.view,
    extension.param.value,
    width=150,
)
# Serve the app
app.servable()
```

and it will look like

![Basic One Way Video](examples/assets/videos/basic-oneway.gif)

### Advanced One Way Examples

Click the images below to see more examples

[![Echarts Gauge Video](examples/assets/videos/echarts-gauge-oneway.gif)](examples/echarts_gauge_oneway.py)

The [Panel Gallery](https://panel.holoviz.org/gallery/index.html) contains more examples in the section called *External libraries*

[![External Libraries](examples/assets/images/panel_gallery_external_libraries.png)](https://panel.holoviz.org/gallery/index.html)

## Dynamic Extension Example

- Browser side functionality in TypeScript (or JS)
- A Bokeh Model in Python
- A Panel Model in Python


## Panel Extensions Template

## Resources

- (Extending Bokeh)ttps://docs.bokeh.org/en/latest/docs/user_guide/extensions.html]

