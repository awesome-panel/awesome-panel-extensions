# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pathlib

from awesome_panel_extensions.site.gallery import GalleryTemplate
from awesome_panel_extensions.site.models import Application

ROOT = pathlib.Path(__file__).parent
GALLERY_YAML = ROOT / "gallery.yaml"


def test_get_manual_test_app():
    return GalleryTemplate(
        site="Panel",
        site_url="https://awesome-panel.org",
        title="Gallery",
        background_image="https://ih1.redbubble.net/image.875683605.8623/ur,mug_lifestyle,tall_portrait,750x1000.jpg",  # pylint: disable=line-too-long
        applications=Application.read(GALLERY_YAML),
        target="_blank",
        accent_base_color="green",
        footer="Made with &#x1f40d;, &#10084;&#65039; and <fast-anchor href='https://panel.holoviz.org' appearance='hypertext' target='_blank'>Panel</fast-anchor>.",  # pylint: disable=line-too-long
    )


if __name__.startswith("bokeh"):
    test_get_manual_test_app().servable()
