from inspect import isclass

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
