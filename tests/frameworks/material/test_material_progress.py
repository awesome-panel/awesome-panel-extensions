# pylint: disable=redefined-outer-name,protected-access, invalid-name
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from awesome_panel_extensions.frameworks.material import (CircularProgress,
                                                          LinearProgress)


@pytest.fixture(params=[CircularProgress, LinearProgress])
def Progress(request):
    return request.param

@pytest.fixture
def progress(Progress):
    return Progress()

@pytest.fixture
def progress_with_values(Progress):
    return Progress(
        max=200, value=50, active=True, bar_color="secondary", style={"background": "blue"}
    )

def test_constructor(progress):
    assert not progress.value
    assert progress.active
    assert progress.bar_color == "success"
    assert progress.max == 100

    assert not progress._progress

def test_progress_constructor_with_values(progress_with_values):
    progress = progress_with_values

    assert progress.value == 50
    assert progress.active
    assert progress.bar_color == "secondary"
    assert progress.max == 200

    assert progress._progress == 0.25

def test_bar_value_change(progress_with_values):
    # Given
    progress = progress_with_values
    # When
    progress.value = 100
    # Then
    assert progress._progress == 0.5

def test_max_value_change(progress_with_values):
    # Given
    progress = progress_with_values
    progress.value = 50
    # When
    progress.max = 100
    # Then
    assert progress.param.value.bounds == (0,100)
    assert progress._progress == 0.5

def test_linear_progress_constructor():
    progress = LinearProgress(name="Progress", value=10, max=100, sizing_mode="fixed", width=200)
    assert progress.active==False

def test_circular_progress_constructor():
    # When
    progress = CircularProgress(density=1)
    # Then
    assert progress.min_height == 53
    assert progress.min_width == 53

def test_circular_progress_density():
    # Given
    progress = CircularProgress()
    # When
    progress.density = 2
    # Then
    assert progress.min_height == 57
    assert progress.min_width == 57

