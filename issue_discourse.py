from holoviews import opts
hv.extension('bokeh', width=90)
pn.extension()

os.environ["AWS_REQUEST_PAYER"] = "requester"

greatest = pn.pane.Markdown('# Max height is '+ str(maxheight))
least = pn.pane.Markdown('# The Min height is '+ str(minheight))

def options(where):
    data = xr.open_rasterio(where)
    data = data.where(data>0)[0,:,:]

    maxheight = float(data.where(data>0).max())
    minheight = float(data.where(data>0).min())
    greatest.object = '# Max height is '+ str(maxheight)
    least.object = '# The Min height is '+ str(minheight)

    return gv.tile_sources.OSM *data.hvplot.quadmesh(rasterize=True,geo=True,colormap='viridis',project = True).opts(alpha=0.7)

pn.Row(
    pn.interact(options, where=places),
    greatest,
    least
    ).servable()