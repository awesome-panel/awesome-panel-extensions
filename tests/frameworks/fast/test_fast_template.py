# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel as pn
from panel import Template

from awesome_panel_extensions.frameworks.fast import FastTemplate


def test_constructor():
    # Given
    column = pn.Column()
    main = [column]
    # When
    template = FastTemplate(main=main)
    # Then
    assert issubclass(FastTemplate, Template)
    assert template.main == main
