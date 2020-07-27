# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import awesome_panel_extensions.awesome_panel.notebook as apn
from awesome_panel_extensions.widgets import link_buttons


def test_notebook_header():
    # When
    apn.Header(
        notebook="LinkButtons.ipynb",
        folder="examples//widgets",
        message="testing-1-2-3",
    )
    # Then
    # No Error
