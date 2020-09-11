# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.frameworks.fast import FastLiteralInput
from tests.frameworks.fast.fast_test_app import create_fast_test_app

def test_can_construct_list():
    # When
    literal_input = FastLiteralInput(type=(type, list), value=["a", "b", "c"])
    # Then
    # assert literal_input.type_of_text=="text"


def test_can_construct_dict():
    # Given
    _type = (type, dict)
    value ={"a": 1, "b": 2, "c": 3}
    # When
    literal_input = FastLiteralInput(type=_type, value=value)
    # Then
    assert literal_input.type == _type
    assert literal_input.value == value
    # assert literal_input.type_of_text=="text"

if __name__.startswith("bokeh"):
    textinput = FastLiteralInput(name="Be Fast!", placeholder="Write a list. For example ['a']!", type=(type,list))
    app = create_fast_test_app(
        component=textinput,
        parameters=[
            "name",
            "value",
            # "type",
            "disabled",
            "placeholder",
            "appearance",
            "autofocus",
            # "type_of_text", # Constant
            "serializer",
            # Some attributes do not work. See https://github.com/microsoft/fast/issues/3852
            # "maxlength",
            # "minlength",
            # "pattern",
            # "size",
            # "spellcheck",
            # "required",
            "readonly",
        ],
    )
    app.servable()