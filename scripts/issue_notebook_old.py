import random

a = 1
data = [
    {"x": 1, "y": "a", "z": True},
    {"x": 2, "y": "b", "z": False},
    {"x": 3, "y": "c", "z": True},
    {"x": 4, "y": "d", "z": False},
]
dataframe = pd.DataFrame(data)
perspective = PerspectiveViewer(
    height=500,
    value=dataframe.copy(deep=True),
    columns=["index", "x", None, None, None],
    plugin="d3_xy_scatter",
    sizing_mode="stretch_width",
)


def stream(*events):
    new_index = perspective.value.index.max()
    new_data = {"x": [random.uniform(-3, new_index)], "y": ["e"], "z": [True]}
    new_series = pd.DataFrame(data=new_data)
    perspective.stream(new_series)


stream_button = pn.widgets.Button(name="STREAM", button_type="success")
stream_button.on_click(stream)


def patch(*events):
    new_value = perspective.value.copy(deep=True)
    new_value["x"] = new_value["x"] - 1
    new_value["z"] = ~new_value["z"]
    perspective.patch(new_value)


patch_button = pn.widgets.Button(name="PATCH", button_type="default")
patch_button.on_click(patch)


def reset(*events):
    perspective.value = dataframe.copy(deep=True)


reset_button = pn.widgets.Button(name="RESET", button_type="default")
reset_button.on_click(reset)


@param.depends(perspective.param.value)
def data(_=None):
    return perspective._source.data


pn.Column(
    top_app_bar,
    pn.Row(
        perspective,
        pn.WidgetBox(stream_button, patch_button, reset_button),
        sizing_mode="stretch_width",
    ),
    perspective.param.value,
    data,
    sizing_mode="stretch_width",
)
