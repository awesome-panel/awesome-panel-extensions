import numpy as np
import panel as pn

pn.extension()
from bokeh.models import Button, ColumnDataSource, CustomJS
from bokeh.plotting import figure

p = figure(title="I", height=450)

lx = [np.arange(i, i + 10) for i in [3, 20, 40]]
ly = [np.arange(i, i + 10) for i in [3, 20, 40]]

source = ColumnDataSource(dict(xs=lx, ys=ly))

p.multi_line(xs="xs", ys="ys", source=source)


# btn = Button(name='update') # working
btn = pn.widgets.Button(name="update")

TOGGLE = True


def update_cds(event):
    global TOGGLE
    if TOGGLE:
        lx = [np.arange(i, i + 5) for i in [5, 10, 15, 20, 40]]
        ly = [np.arange(i, i + 5) for i in [5, 10, 15, 20, 40]]
    else:
        lx = [np.arange(i, i + 10) for i in [3, 20, 40]]
        ly = [np.arange(i, i + 10) for i in [3, 20, 40]]
    source.data = dict(xs=lx, ys=ly)
    TOGGLE = not TOGGLE
    print(" Python: working or not working ??")


source.js_on_change("data", CustomJS(code="console.log('JS:data_change_detected');"))

btn.on_click(update_cds)

pn.Column(btn, p).servable()
