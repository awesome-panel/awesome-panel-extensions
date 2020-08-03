import plotly.express as px

def get_carshare():
    return px.data.carshare()

def car_share_plotly_plot(carshare):
    fig = px.scatter_mapbox(carshare, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
                    color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                    mapbox_style="carto-positron")
    return fig

