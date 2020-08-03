# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring


import pandas as pd
import panel as pn
import pytest
from pandas_profiling import ProfileReport

from awesome_panel_extensions.pane import PandasProfileReport
from awesome_panel_extensions.pane.pandas_profile_report import OBJECT_WHEN_NO_REPORT

DATAFRAME = pd.DataFrame({"x": list(range(0, 50)), "y": list(range(50, 100)),})


@pytest.fixture
def dataframe():
    return DATAFRAME.copy()


@pytest.fixture
def profile_report(dataframe):
    return ProfileReport(dataframe)


@pytest.fixture
def pandas_profiling_report(profile_report):
    return PandasProfileReport(profile_report=profile_report)


def test_can_construct(pandas_profiling_report, profile_report):
    assert isinstance(pandas_profiling_report, PandasProfileReport)
    assert pandas_profiling_report.profile_report == profile_report


def test_shows_report(pandas_profiling_report):
    assert (
        "Profile report generated with the `pandas-profiling` Python package"
        in pandas_profiling_report.object
    )


def test_can_construct_with_no_report():
    # When
    profile_report = PandasProfileReport()
    # Then
    assert profile_report.object == OBJECT_WHEN_NO_REPORT


def test_app():
    pn.config.sizing_mode = "stretch_width"
    profile_report = ProfileReport(DATAFRAME)
    # profile_report = None
    pandas_profile_report = PandasProfileReport(
        profile_report=profile_report, width=800, height=700
    )
    settings_pane = pn.Param(
        pandas_profile_report,
        parameters=[
            "height",
            "width",
            "sizing_mode",
            "object_when_no_report",
            "object_when_loading_report",
        ],
        background="lightgray",
        show_name=False,
    )
    return pn.Column(
        "# Settings",
        settings_pane,
        "# PandasProfileReport Extension",
        pandas_profile_report,
        sizing_mode="stretch_both",
    )


if __name__.startswith("bokeh"):
    test_app().servable()
if __name__ == "__main__":
    test_app().show(port=5007)
