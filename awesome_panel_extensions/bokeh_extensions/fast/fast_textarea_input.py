from bokeh.core import properties
from bokeh.models import TextAreaInput as _BkTextAreaInput


class FastTextAreaInput(_BkTextAreaInput):
    # value  is inherited
    # placeholder is inherited
    # max_length is inherited
    # cols is inherited
    # rows is inherited
    appearance = properties.String(
        help="""Determines the appearance of the textinput. One of `outline` or `filled`.
        Defaults to outlined""",
    )
    autofocus = properties.Bool(
        help="""The autofocus attribute. Defaults to `False`""",
    )
    resize = properties.String(
        help="""The resize attribute. One of
        `None`, `both`, `horizontal` or `vertical`. Defaults to `None`.""",
    )

    min_length = properties.Int(
        help="""The minimum length of the text string""",
    )

    spellcheck = properties.Bool(
        help="""Whether or not the spell check is enabled. Default is False"""
    )
    required = properties.Bool(
        help="""Whether or not the FastTextInput is required. Default is False"""
    )
    readonly = properties.Bool(
        help="""Whether or not the FastTextInput is readonly. Default is False"""
    )
