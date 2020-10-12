# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring


def test_can_construct(link):
    assert isinstance(link.name, str)
    assert isinstance(link.url, str)
    assert isinstance(link.icon, str)
    assert isinstance(link.description, str)
