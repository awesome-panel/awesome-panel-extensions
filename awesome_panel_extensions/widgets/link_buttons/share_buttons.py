"""This module provides button to share on social media"""
import urllib.parse

import panel as pn
import param

from awesome_panel_extensions.assets import svg_icons

DEFAULT_URL = "https://awesome-panel.org"
DEFAULT_TEXT = "Checkout"
STYLE = """.bk a.button-share-link {
    color: inherit;
    font-style: none;
}
svg.pnx-icon {
    height: 1em;
    width: 1em;
}
"""
if not STYLE in pn.config.raw_css:
    pn.config.raw_css.append(STYLE)


class ShareOnBase(pn.pane.HTML):
    """Base class for implementing ShareOnFacebook, ShareOnLinkedIn links etc.

    - The href property should be overridden
    """

    url = param.String(DEFAULT_URL)
    icon = param.String(svg_icons.EXTERNAL_LINK, doc="A SVG icon")
    text = param.String(DEFAULT_TEXT)
    size = param.Integer(default=1, bounds=(0, 20), doc="The fontsize in em")

    priority = 0
    _rename = dict(pn.pane.HTML._rename, url=None, icon=None, text=None, size=None)

    def __init__(self, **params):
        super().__init__(**params)

        self._update_html_object()

    @property
    def _url_parsed(
        self,
    ):
        return urllib.parse.quote(self.url).replace(
            "/",
            "%2F",
        )

    @property
    def href(
        self,
    ) -> str:
        """The href to goto when clicked

        Override this method in a base class

        Raises:
            NotImplementedError:

        Returns:
            str: A href string
        """
        raise NotImplementedError()

    def to_html(
        self,
    ) -> str:
        """A html string with link and icon tags

        Returns:
            str: A html string with link and icon tags
        """
        return (
            f'<a href="{self.href}" class="button-share-link" style="font-size: {self.size}em" '
            f'target="_blank">{self.icon}</a>'
        )

    @param.depends("url", "icon", "size", watch=True)
    def _update_html_object(
        self,
    ):
        """A HTML pane with the a link and icon"""
        self.object = self.to_html()


class ShareOnFacebook(ShareOnBase):
    """A Share on Facebook button"""

    icon = param.String(svg_icons.FACEBOOK)

    @property
    def href(
        self,
    ):
        return f"https://www.facebook.com/sharer/sharer.php?u={self._url_parsed}"


class ShareOnLinkedIn(ShareOnBase):
    """A Share on LinkedIn button"""

    icon = param.String(svg_icons.LINKED_IN)

    @property
    def href(
        self,
    ):
        return (
            f"http://www.linkedin.com/shareArticle?mini=true&url={self._url_parsed}"
            f"&title={self.text}"
        )


class ShareOnTwitter(ShareOnBase):
    """A Share on Twitter button"""

    icon = param.String(svg_icons.TWITTER)

    @property
    def href(
        self,
    ):
        return f"https://twitter.com/intent/tweet?url={self._url_parsed}&text={self.text}"


class ShareOnReddit(ShareOnBase):
    """A Share on Reddit button"""

    icon = param.String(svg_icons.REDDIT)

    @property
    def href(
        self,
    ):
        return f"https://reddit.com/submit?url={self._url_parsed}&amp;title={self.text}"


class ShareOnMail(ShareOnBase):
    """A Share on Mail button"""

    icon = param.String(svg_icons.ENVELOPE)

    @property
    def href(
        self,
    ):
        return f"mailto:?subject={self._url_parsed}&amp;body={self.text}&nbsp;{self._url_parsed}"
