"""The FastGalleryTemplate can be used to show case your applications in a nice way"""
import pathlib
from typing import List

from panel import Template

from awesome_panel_extensions.site import Resource

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "fast_gallery_template.css").read_text()
JS = (ROOT / "fast_gallery_template.js").read_text()
TEMPLATE = (ROOT / "fast_gallery_template.html").read_text()
FAVICON = (
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/"
    "2781d86d4ed141889d633748879a120d7d8e777a/assets/images/favicon.ico"
)


class FastGalleryTemplate(Template):
    """The FastGalleryTemplate can be used to show case your applications in a nice way"""

    def __init__(  # pylint: disable=too-many-arguments
        self,
        items: List[Resource],
        site_name: str = "Awesome Panel",
        site_url: str = "https://awesome-panel.org",
        name: str = "Gallery",
        url: str = "https://awesome-panel.org/gallery",
        description: str = "",
        background_image_url: str = "https://preview.redd.it/9oi428ohy7t21.png?auto=webp&s=5051b77d33e85446b6492a1e02725c6729777d4f",
        target: str = "_self",
        favicon: str = FAVICON,
        accent_base_color: str = "#E1477E",
        font_family: str = "Open Sans",
    ):
        """The FastGalleryTemplate can be used to show case your applications in a nice way

        TO BE IMPROVED

        Args:
            items (List[Resource]): [description]
            site_name (str, optional): [description]. Defaults to "Awesome Panel".
            site_url (str, optional): [description]. Defaults to "https://awesome-panel.org".
            name (str, optional): [description]. Defaults to "Gallery".
            url (str, optional): [description]. Defaults to "https://awesome-panel.org/gallery".
            description (str, optional): [description]. Defaults to "".
            background_image_url (str, optional): [description]. Defaults to "".
            target (str, optional): [description]. Defaults to "_self".
            favicon (str, optional): The url of a favicon to put on the browser tab.
                Defaults to the Panel favicon.
            accent_base_color (str, optional): A HEX color value. Defaults to "#E1477E",
            font_family (str, optional): A comma separated list of fonts. Defaults to "Open Sans",
        """
        super().__init__(template=TEMPLATE)
        self.add_variable("title_names", site_name + "|" + name)
        self.add_variable("site_name", site_name)
        self.add_variable("site_url", site_url)
        self.add_variable("name", name)
        self.add_variable("url", url)
        self.add_variable("description", description)
        self.add_variable("background_image_url", background_image_url)
        self.add_variable("items", items)
        self.add_variable("gallery_js", JS)
        self.add_variable("gallery_css", CSS)
        self.add_variable("favicon", favicon)
        self.add_variable("accent_base_color", accent_base_color)
        self.add_variable("font_family", font_family)

        if target not in ["_blank", "_parent", "_top", "_self"]:
            target = "_self"
        self.add_variable("target", target)
