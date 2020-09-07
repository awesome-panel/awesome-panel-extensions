"""The FastAnchor enables the user to click a link and navigate to it.

The component supports several visual apperances
(accent, lightweight, neutral, outline, stealth, hypertext).

The FastAnchor wraps the `fast-anchor` of the [Fast Design](https://fast.design/) Framework.

For more information view the [component specification]\
(https://github.com/microsoft/fast/tree/master/packages/web-components/fast-foundation/\
src/anchor/anchor.spec.md).

See also https://explore.fast.design/components/fast-anchor.
    """
import param  # pylint: disable=wrong-import-order
from panel.widgets import Widget

from awesome_panel_extensions.bokeh_extensions.fast.fast_anchor import FastAnchor as _BkFastAnchor

FAST_ANCHOR_APPEARENCES = [
    "accent",
    "lightweight",
    "neutral",
    "outline",
    "stealth",
    "hypertext",
]
# pylint: disable=line-too-long
RELS = [
    None,
    "alternate",  # Provides a link to an alternate representation of the document (i.e. print page, translated or mirror)
    "author",  # Provides a link to the author of the document
    "bookmark",  # Permanent URL used for bookmarking
    "external",  # Indicates that the referenced document is not part of the same site as the current document
    "help",  # Provides a link to a help document
    "license",  # Provides a link to licensing information for the document
    "next",  # Provides a link to the next document in the series
    "nofollow",  # Links to an unendorsed document, like a paid link.
    "noreferrer",  # Requires that the browser should not send an HTTP referer header if the user follows the hyperlink
    "noopener",  # Requires that any browsing context created by following the hyperlink must not have an opener browsing context
    "prev",  # The previous document in a selection
    "search",  # Links to a search tool for the document
    "tag",  # A tag (keyword) for the current document
]
# pylint: enable=line-too-long
TARGETS = [
    None,
    "_blank",
    "_parent",
    "_self",
    "_top",
]
REFERRER_POLICIES = [
    None,
    "no-referrer",
    "no-referrer-when-downgrade",
    "origin",
    "origin-when-cross-origin",
    "same-origin",
    "strict-origin",
    "strict-origin-when-cross-origin",
    "unsafe-url",
]


class FastAnchor(Widget):
    """The FastAnchor enables the user to click a link and navigate to it.

The component supports several visual apperances
(accent, lightweight, neutral, outline, stealth, hypertext).

When using the `FastTemplate` you can also use the `<fast-anchor>` tag directly inside
`pn.pane.Markdown` and `pn.pane.HTML`.

The FastAnchor wraps the `fast-anchor` of the [Fast Design](https://fast.design/) Framework.

For more information view the [component specification]\
(https://github.com/microsoft/fast/tree/master/packages/web-components/fast-foundation/\
src/anchor/anchor.spec.md).

See also https://explore.fast.design/components/fast-anchor.
    """

    value = param.String(
        default=None,
        allow_None=True,
        doc="""The URL that the hyperlink points to. Default is None.""",
        label="Href",
    )
    appearance = param.ObjectSelector(
        default=None,
        objects=FAST_ANCHOR_APPEARENCES,
        doc="""Determines the appearance of the anchor. One of `accent`, `lightweight`, `neutral`,
        `outline`, `stealth` or `hypertext`. Defaults to None/ neutral""",
        allow_None=True,
    )
    target = param.ObjectSelector(
        default=None,
        objects=TARGETS,
        allow_None=True,
        doc="""Where to display the linked URL. One of None, `_self`, `_blank`, `_parent`, `_self`
        or `_top`. Defaults to None""",
    )

    download = param.String(
        default=None,
        allow_None=True,
        doc="""Prompts the user to save the linked URL instead of navigating to it.
        Can be used with or without a value. Defaults to None""",
    )
    # We call this value instead of href in order to be able to use it
    # with pn.Param
    hreflang = param.String(
        default=None,
        allow_None=True,
        doc="""Hints at the human language of the linked URL. No built-in functionality.
        Default is None.""",
    )
    ping = param.String(
        default=None,
        allow_None=True,
        doc="""A space-separated list of URLs. When the link is followed, the browser will send
        POST requests with the body PING to the URLs. Typically for tracking.
        Default is None.""",
    )
    referrerpolicy = param.ObjectSelector(
        default=None,
        objects=REFERRER_POLICIES,
        allow_None=True,
        doc="""How much of the referrer to send when following the link.
        one of no-referrer, no-referrer-when-downgrade, origin,origin-when-cross-origin,
        same-origin, strict-origin, strict-origin-when-cross-origin and unsafe-url.check_on_set.
        Defaults to None""",
    )
    rel = param.ObjectSelector(
        default=None,
        objects=RELS,
        allow_None=True,
        doc="""The relationship of the linked URL as space-separated link types like alternate,
        archives, ... See https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types.
        Defaults to None""",
    )
    mimetype = param.String(
        default=None,
        allow_None=True,
        doc="""Hints at the linked URL’s format with a MIME type. No built-in functionality.
        Default is None.""",
        label="Type",
    )

    height = param.Integer(default=40, bounds=(0, None))

    _widget_type = _BkFastAnchor

    _rename = {
        "value": "href",
        "ref": "referrer",  # pylint: disable=protected-access
    }

    def __init__(self, **params):
        super().__init__(**params)

        self._set_height()

    @param.depends("appearance", watch=True)
    def _set_height(self, *_):
        if self.appearance == "hypertext":
            self.height = 20
        else:
            self.height = 40
