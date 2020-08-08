# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from panel.widgets.slider import IntSlider
from awesome_panel_extensions.frameworks.material import IntSlider, FloatSlider

def test_int_constructor():
    IntSlider(
        value=4,
        start=3,
        end=8,
        step=2,
        pin=True,
        markers=True,
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


def test_float_constructor():
    FloatSlider(
        value=5.0,
        start=4.2,
        end=5.6,
        step=0.2,
        )


