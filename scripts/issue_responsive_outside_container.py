import altair as alt
import pandas as pd
import panel as pn

pn.extension("vega")


def get_altair_bar_data():
    return pd.DataFrame(
        {
            "project": ["a", "b", "c", "d", "e", "f", "g"],
            "score": [25, 57, 23, 19, 8, 47, 8],
            "goal": [25, 47, 30, 27, 38, 19, 4],
        }
    )


def altair_bar_plot(data):
    bar_chart = alt.Chart(data).mark_bar().encode(x="project", y="score")

    tick_chart = (
        alt.Chart(data)
        .mark_tick(
            color="red",
            thickness=2,
            size=40 * 0.9,
        )  # controls width of tick.
        .encode(x="project", y="goal")
    )

    return (bar_chart + tick_chart).properties(width="container", height="container")


data = get_altair_bar_data()
component = altair_bar_plot(data)
component_panel = pn.pane.Vega(component, sizing_mode="stretch_both")
pn.Column(
    component_panel,
    background="lightgray",
    sizing_mode="stretch_both",
    css_classes=["designer-centered-component"],
).show(port=5007)
