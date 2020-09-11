# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.frameworks.fast import FastLiteralAreaInput


def test_can_construct_list():
    FastLiteralAreaInput(type=list, value=["a", "b", "c"])


def test_can_construct_dict():
    FastLiteralAreaInput(type=dict, value={"a": 1, "b": 2, "c": 3})
