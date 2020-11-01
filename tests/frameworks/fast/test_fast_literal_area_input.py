# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.frameworks.fast import FastLiteralAreaInput
from tests.frameworks.fast.fast_test_app import create_fast_test_app


def test_can_construct_list():
    # When
    literal_input = FastLiteralAreaInput(type=(type, list), value=["a", "b", "c"])
    # Then
    assert isinstance(literal_input.placeholder, str)


def test_can_construct_dict():
    # Given
    _type = (type, dict)
    value = {"a": 1, "b": 2, "c": 3}
    # When
    literal_input = FastLiteralAreaInput(type=_type, value=value)
    # Then
    assert literal_input.type == _type
    assert literal_input.value == value
    # assert literal_input.type_of_text=="text"


if __name__.startswith("bokeh"):
    textinput = FastLiteralAreaInput(
        name="List Value!", placeholder="Write a list. For example ['a']!", type=list
    )
    app = create_fast_test_app(
        component=textinput,
        parameters=[
            "appearance",
            "autofocus",
            "cols",
            "disabled",
            "max_length",
            "min_length",
            "name",
            "placeholder",
            "readonly",
            "required",
            "resize",
            "rows",
            "serializer",
            "spellcheck",
            "value",
            # "type" does not work
            # Some attributes do not work. See https://github.com/microsoft/fast/issues/3852
        ],
    )
    app.servable()
