"""In this module we test the param extensions"""
# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import param

from awesome_panel_extensions.param import link


def test_link():
    class MyClass(param.Parameterized):
        value_ = param.String()

    instance1 = MyClass(value_="hello1")
    instance2 = MyClass(value_="hello2")

    link(instance1.param.value_, instance2.param.value_)

    instance1.value_ = "13"
    assert instance2.value_ == instance1.value_
    instance2.value_ = "14"
    assert instance2.value_ == instance1.value_
