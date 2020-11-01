from bokeh.core import properties
from bokeh.models import TextInput as _BkTextInput


class FastTextInput(_BkTextInput):
    # value  is inherited
    # placeholder is inherited
    # list is not supported
    appearance = properties.String(
        help="""Determines the appearance of the textinput. One of `outline` or `filled`.
        Defaults to outlined""",
    )
    autofocus = properties.Bool(
        help="""The autofocus attribute. Defaults to `False`""",
    )
    type_of_text = properties.String(
        help="""Determines the type of text accepted. One of `email`, `password`, `tel`, `text` or `url`.
        Defaults to text.
        """
    )
    max_length = properties.Int(
        help="""The maximum length of the text string""",
    )
    min_length = properties.Int(
        help="""The minimum length of the text string""",
    )
    pattern = properties.String(
        help="""A regular expression that the input's value must match in order for the value to pass constraint validation"""
    )
    size = properties.Int(
        help="""Valid for email, password, tel, and text input types only. Specifies how much of the input is shown""",
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
