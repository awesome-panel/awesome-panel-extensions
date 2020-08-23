# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest
from awesome_panel_extensions.frameworks.material import FloatSlider, IntSlider


def test_int_constructor():
    IntSlider(
        value=4, start=3, end=8, step=2, pin=True, markers=True,
    )


def test_int_pin():
    # Given
    slider = IntSlider()
    margin = slider.margin
    # When/ Then
    slider.pin = True
    assert slider.margin != margin
    slider.pin = False
    assert slider.margin == margin


@pytest.fixture
def float_slider():
    return FloatSlider(value=5.0, start=4.2, end=5.6, step=0.2,)


def test_float_constructor(float_slider):
    # Then
    assert float_slider._value == round(5.0 / 0.2)
    assert float_slider._start == round(4.2 / 0.2)
    assert float_slider._end == round(5.6 / 0.2)
    assert float_slider._step == round(0.2 / 0.2)


def test_float_step_set_step(float_slider):
    # When
    float_slider.step = 0.4
    # Then
    assert float_slider._value == round(5.0 / 0.4)
    assert float_slider._start == round(4.2 / 0.4)
    assert float_slider._end == round(5.6 / 0.4)
    assert float_slider._step == round(0.2 / 0.2)


def test_float_step_set_value(float_slider):
    # When
    float_slider.value = 5.2
    # Then
    assert float_slider._value == round(5.2 / 0.2)
    assert float_slider._start == round(4.2 / 0.2)
    assert float_slider._end == round(5.6 / 0.2)
    assert float_slider._step == round(0.2 / 0.2)


def test_float_start(float_slider):
    # When
    float_slider.start = 4.4
    assert float_slider._value == round(5.0 / 0.2)
    assert float_slider._start == round(4.4 / 0.2)
    assert float_slider._end == round(5.6 / 0.2)
    assert float_slider._step == round(0.2 / 0.2)


def test_float_end(float_slider):
    # When
    float_slider.end = 5.8
    assert float_slider._value == round(5.0 / 0.2)
    assert float_slider._start == round(4.2 / 0.2)
    assert float_slider._end == round(5.8 / 0.2)
    assert float_slider._step == round(0.2 / 0.2)
