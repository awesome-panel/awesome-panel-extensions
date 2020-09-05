from inspect import isclass
from awesome_panel_extensions.frameworks.fast import FastTemplate
from panel import Template
import panel as pn

def test_constructor():
    # Given
    column = pn.Column()
    main = [column]
    # When
    template = FastTemplate(main=main)
    # Then
    assert issubclass(FastTemplate, Template)
    assert template.main == main

