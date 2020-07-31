from awesome_panel_extensions.frameworks.material import Extension


def test_can_construct():
    # When
    extension = Extension()
    # Then
    assert extension.width == 0
    assert extension.height == 0
    assert extension.margin == 0
    assert extension.sizing_mode == "fixed"
    assert "<script" in extension.object
    assert "<link" in extension.object
