# Panel Extensions Template

The purpose of this repository is to make it as easy as possible for Panel developers to create custom Panel extensions.

In order to facilitate this, this repo contains

- Documentation (See below)
- Examples (See the [examples](/examples/) folder)
- An Extensions Starter Template (See [src](/examples/) folder)

## Extensions Overview

Panel supports two types of extensions.

- Static Extensions
- Bidirectional Extensions

**One Way Extensions** are extensions that are created using the `HTML` pane. You can combine HTML, CSS and/ or JS to create amazing extensions to Panel. But these extensions cannot communicate from the browser back to Python.

**Bidirectional Extensions** on the other hand supports bidirectional communication from Python to the Browser and back. This is how all the layouts, panes and widgets of Panel are created. In order to create a dynamic extension you need to implement

- Browser side functionality in TypeScript (or JS)
- A Bokeh Model in Python
- A Panel Model in Python

## Examples

### One Way

#### Basic

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

#### ECharts Gauge

#### Others

The [Panel Gallery](https://panel.holoviz.org/gallery/index.html) contains more examples in the section called *External libraries*

[![External Libraries](examples/assets/images/panel_gallery_external_libraries.png)](https://panel.holoviz.org/gallery/index.html)

## Dynamic Extension Example

## Panel Extensions Template

## Resources

- (Extending Bokeh)ttps://docs.bokeh.org/en/latest/docs/user_guide/extensions.html]

