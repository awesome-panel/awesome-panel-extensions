# Panel Extensions Template

WORK IN PROGRESS. JUST STARTED.

[Panel](https://panel.holoviz.org/) is a framework for creating **powerful, reactive analytics apps in Python using to tools you know and love**.

<a href="https://panel.holoviz.org/" target="_blank"><img src="https://panel.holoviz.org/_static/logo_stacked.png" style="display: block;margin-left: auto;margin-right: auto;height: 50px;"></a>

The purpose of this repository is to **make it easy for Panel developers to create custom Panel extensions**.

Panel Extensions enables javascript developers to wrap an awesome javascript plotting library like [ECharts](https://echarts.apache.org/en/index.html) and give Python develops access to use it in Panel.

In order to facilitate this, this repo contains

- Documentation (See below)
- Examples (See [examples](/examples/) folder)
- An Extensions Starter Template (See [src](/src/) folder)

## Extensions Overview

Panel supports two types of extensions *One Way Extensions* and *Bidirectional Extensions*.

**One Way HTML Extensions** are extensions that are created using the `HTML` pane. You can combine HTML, CSS and/ or JS to create amazing extensions to Panel. But these extensions cannot communicate from the browser (Javascript) back to the server (Python).

**Bidirectional Bokeh Extensions** on the other hand supports efficient, bidirectional communication from server (Python) to the browser (Javascript) and back. The layouts, panes and widgets built into Panel are bidirectional extensions. This functionality uses the [Bokeh Extensions](ttps://docs.bokeh.org/en/latest/docs/user_guide/extensions.html) api.

## Examples

### Basic One Way Example

This example will work like shown below

![Basic One Way Video](examples/assets/videos/basic-oneway.gif)

We start by importing the dependencies

```Python
import panel as pn
import param
```

Then we implement the HTML functionality we would like to show.

```python
def get_html(value):
    """Main functionality of Extension"""
    font_size = value
    alpha = 1-value/100
    green = int(value*255/100)
    return f"""
<div style="font-size: {font_size}px;color: rgba(0,{green},0,{alpha}">{value}</div>
"""
```

Then make wrap it into a reactive extension.

```python
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

Finally we try out the extension

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

### Advanced One Way Examples

**Click the images** below for more code examples.

[![Echarts Gauge Video](examples/assets/videos/echarts-gauge-oneway.gif)](examples/echarts_gauge_oneway.py)

The [Panel Gallery](https://panel.holoviz.org/gallery/index.html) contains more examples in the section called *External libraries*

[![External Libraries](examples/assets/images/panel_gallery_external_libraries.png)](https://panel.holoviz.org/gallery/index.html)

### Basic Bokeh Extension - Bidirectional Example

Now we start moving into Bokeh Extensions and Javascript territory.

Please note that in order for Bokeh Extensions to compile you will need to have [node.js](https://nodejs.org) installed. You can install it directly from their web site or via `conda install -c conda-forge nodejs`.

In this example we will create a Panel `HTMLButton` extension that enables a user
to catch a click event from any HTML element he/ she would like as shown below.

[![html_button.py](examples/assets/videos/html-button.gif)](examples/html_button/html_button.py)

CLICK ON THE VIDEO TO SEE THE CODE - WALK THROUGH COMING UP

You can find an one-way example called "Custom Bokeh Model" in the Gallery at [awesome-panel.org](https://awesome-panel.org). You can find the code [here](https://github.com/MarcSkovMadsen/awesome-panel/tree/master/application/pages/custom_bokeh_model).

[![Custom Bokeh Model](examples/assets/videos/custom-bokeh-model.gif)](https://github.com/MarcSkovMadsen/awesome-panel/tree/master/application/pages/custom_bokeh_model)

### Advanced Bokeh Extensions

Every layout, pane or widget in Panel is essentially a Bokeh Extension so a good place to get inspiration is to navigate the [Panel Reference Gallery]() to find an extension similar to the one you would like to implement and then study the code

[![Panel Reference Gallery](examples/assets/videos/panel-reference-gallery.gif)](https://panel.holoviz.org/reference/index.html)

You can find the code of the Panel components on Github via

- [Panel Layouts](https://github.com/holoviz/panel/tree/master/panel/layout)
- [Panel Panes](https://github.com/holoviz/panel/tree/master/panel/pane)
- [Panel Widgets](https://github.com/holoviz/panel/tree/master/panel/widgets)

and the underlying Bokeh extensions via

- [Bokeh Model Widgets](https://github.com/bokeh/bokeh/tree/master/bokehjs/src/lib/models/widgets)
- [Panel Bokeh Models](https://github.com/holoviz/panel/tree/master/panel/models)

## Prebuilt Bokeh Extensions

COPY FROM AWESOME-PANEL.ORG REPO - TO BE REVISED

In this document I will describe how I got **prebuilt bokeh model extensions** setup
as a part of the awesome-panel package. I needed it temporarily while waiting for the `WebComponent` PR to be reviewed and released by Panel.

Setting up prebuilt extensions using `Bokeh init --interactive` is briefly described in the Bokeh Docs. See [Bokeh Pre-built extensions](https://docs.bokeh.org/en/latest/docs/user_guide/extensions.html).

I hope this description can help others who would like to create prebuilt custom bokeh models for Bokeh or Panel.

### Steps

I navigated to the root of the awesome-panel package

```bash
cd awesome-panel/package
```

ran `bokeh init --interactive`

```bash
$ bokeh init --interactive
Working directory: C:\repos\private\awesome-panel\package\awesome_panel
Wrote C:\repos\private\awesome-panel\package\awesome_panel\bokeh.ext.json
Create package.json? This will allow you to specify external dependencies. [y/n] y
  What's the extension's name? [awesome_panel]
  What's the extension's version? [0.0.1]
  What's the extension's description? []
Wrote C:\repos\private\awesome-panel\package\awesome_panel\package.json
Create tsconfig.json? This will allow for customized configuration and improved IDE experience. [y/n] y
Wrote C:\repos\private\awesome-panel\package\awesome_panel\tsconfig.json
Created empty index.ts. This is the entry point of your extension.
You can build your extension with bokeh build
All done.
```

In the `package.json` I had to replace

```ts
"dependencies": {
    "bokehjs": "^2.0.2"
  },
```

with

```ts
"dependencies": {
    "@bokeh/bokehjs": "^2.0.2"
  },
```

See [bokeh init issue](https://github.com/bokeh/bokeh/issues/10055).

I also replaced the `tsconfig.json` contents with

```ts
{
  "compilerOptions": {
    "noImplicitAny": true,
    "noImplicitThis": true,
    "noImplicitReturns": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "strictNullChecks": true,
    "strictBindCallApply": false,
    "strictFunctionTypes": false,
    "strictPropertyInitialization": false,
    "alwaysStrict": true,
    "noErrorTruncation": true,
    "noEmitOnError": false,
    "declaration": true,
    "sourceMap": true,
    "importHelpers": false,
    "experimentalDecorators": true,
    "module": "esnext",
    "moduleResolution": "node",
    "esModuleInterop": true,
    "resolveJsonModule": true,
    "skipLibCheck": true,
    "target": "ES2017",
    "lib": ["es2017", "dom", "dom.iterable"],
    "baseUrl": ".",
    "outDir": "./dist/lib",
    "paths": {
      "@bokehjs/*": [
        "./node_modules/@bokeh/bokehjs/build/js/lib/*",
        "./node_modules/@bokeh/bokehjs/build/js/types/*"
      ]
    }
  },
  "include": ["./**/*.ts"]
}
```

At least including the `path` section is needed to be able to `import { div, label } from "@bokehjs/core/dom"` like @philippjfr does in Panel.

In the `index.ts` file I imported my models

```ts
import * as AwesomePanel from "./express/models/"
export {AwesomePanel}

import {register_models} from "@bokehjs/base"
register_models(AwesomePanel as any)
```

In the `express/models/index.ts` file I exported the `WebComponent`.

```ts
export {WebComponent} from "./web_component"
```

Then I could `build` my extension

```bash
$ panel build
Working directory: C:\repos\private\awesome-panel\package\awesome_panel
Using C:\repos\private\awesome-panel\package\awesome_panel\tsconfig.json
Compiling TypeScript (3 files)
Linking modules
Output written to C:\repos\private\awesome-panel\package\awesome_panel\dist
All done.
```

The result is in the `dist` folder.

I discovered I did not even have to `serve` the `awesome_panel.js` file.

I could just `panel serve` something

## How to use the template

COMING UP - DESCRIBE HOW TO USE THE Template

## Sharing the extension(s) as a Python Package on PYPI

COMING UP

## Resources

### Awesome Panel Extensions

COMING UP

### Inspiration

- [Streamlit Component Gallery](https://www.streamlit.io/components)
- Jupyter/ IpyWidgets/ Voila - TBD
- Dash - TBD

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

