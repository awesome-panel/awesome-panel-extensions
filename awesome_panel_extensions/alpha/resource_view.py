"""This module provides functionality to render a Resource as a View"""
import panel as pn

from awesome_panel_extensions.assets.svg_icons import (
    CODE_SVG,
    DOC_SVG,
    GIF_SVG,
    MP4_SVG,
    YOUTUBE_SVG,
)
from awesome_panel_extensions.models.resource import Resource

STYLE = """
.pnx-avatar img {
    height: 100%;
    width: 100%;
    border-radius: 30%;
}
.pnx-link img {
    height: 100%;
    width: 100%;
}
"""

ICONS = {"gif": GIF_SVG, "mp4": MP4_SVG, "youtube": YOUTUBE_SVG, "doc": DOC_SVG, "code": CODE_SVG}


def _to_avatar_icon(author):
    html = f"""<a href="{ author.url }" target="_blank">
    <img src="{ author.avatar_url }" alt="Avatar" title="Author: { author.name}">
</a>"""
    return pn.pane.HTML(
        object=html,
        height=25,
        width=25,
        sizing_mode="fixed",
        css_classes=["pnx-avatar"],
    )


def _to_link_icon(url, title):
    html = f"""
<a title="{ title }" appearance="hypertext" href="{ url }" target="_blank">
{ ICONS[title] }
</a>"""
    return pn.pane.HTML(
        object=html,
        height=25,
        width=25,
        sizing_mode="fixed",
        css_classes=["pnx-link"],
    )


def view(resource: Resource) -> pn.layout.Card:
    """Returns a view of the resource as a Card

    Args:
        resource (Resource): A Resource

    Returns:
        pn.layout.Card: A view of the Resource
    """
    if not STYLE in pn.config.raw_css:
        pn.config.raw_css.append(STYLE)
    name = resource.name
    url = resource.url
    header_text = f"# [{name}]({url})"
    header = pn.pane.Markdown(header_text)
    header = name
    description = resource.description
    author = _to_avatar_icon(resource.author)

    links = []
    if resource.code_url:
        links.append(_to_link_icon(resource.code_url, "code"))
    if resource.gif_url:
        links.append(_to_link_icon(resource.gif_url, "gif"))
    if resource.mp4_url:
        links.append(_to_link_icon(resource.mp4_url, "mp4"))
    if resource.youtube_url:
        links.append(_to_link_icon(resource.youtube_url, "youtube"))
    if resource.documentation_url:
        links.append(_to_link_icon(resource.documentation_url, "doc"))
    tags = ", #".join(resource.tags)
    if tags:
        tags = pn.pane.Markdown("#### #" + tags)

    return pn.layout.Card(
        pn.Column(
            description,
            tags,
            pn.Row(
                author,
                *links,
            ),
            margin=25,
        ),
        title=header,
    )
