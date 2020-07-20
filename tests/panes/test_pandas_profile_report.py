# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring

from typing import DefaultDict
import pandas as pd
import pytest

from awesome_panel_extensions.panes import PandasProfileReport
from awesome_panel_extensions.panes.pandas_profile_report import EMPTY_HTML_REPORT, HTML_LOADING_REPORT
from pandas_profiling import ProfileReport

@pytest.fixture
def dataframe():
    return pd.DataFrame({"x": list(range(0, 50)), "y": list(range(50, 100)),})

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
    assert "Profile report generated with the `pandas-profiling` Python package" in pandas_profiling_report.object

def test_can_construct_with_no_report():
    # When
    profile_report = PandasProfileReport()
    # Then
    assert profile_report.object == EMPTY_HTML_REPORT
