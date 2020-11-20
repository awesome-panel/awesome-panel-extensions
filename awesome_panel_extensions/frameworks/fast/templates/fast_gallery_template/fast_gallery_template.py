"""The FastGalleryTemplate can be used to show case your applications in a nice way"""
import pathlib
from typing import List

from panel import Template

from awesome_panel_extensions.site import Resource

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "fast_gallery_template.css").read_text()
JS = (ROOT / "fast_gallery_template.js").read_text()
TEMPLATE = (ROOT / "fast_gallery_template.html").read_text()


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
        background_image_url: str = "",
        target: str = "_self",
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
        """
        super().__init__(template=TEMPLATE)
        self.add_variable("title", site_name + "|" + name)
        self.add_variable("site_name", site_name)
        self.add_variable("site_url", site_url)
        self.add_variable("name", name)
        self.add_variable("url", url)
        self.add_variable("description", description)
        self.add_variable("background_image_url", background_image_url)
        self.add_variable("items", items)
        self.add_variable("gallery_js", JS)
        self.add_variable("gallery_css", CSS)

        if target not in ["_blank", "_parent", "_top", "_self"]:
            target = "_self"
        self.add_variable("target", target)
