import pathlib
from typing import List

import panel as pn
from panel import Template

from awesome_panel_extensions.models.resource import Resource

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "fast_gallery_template.css").read_text()
JS = (ROOT / "fast_gallery_template.js").read_text()
TEMPLATE = (ROOT / "fast_gallery_template.html").read_text()

pn.config.raw_css.append(CSS)

class FastGalleryTemplate(Template):
    def __init__(
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
        """[summary]

        Args:
            items (List[ApplicationMetaData]): [description]
            target (str, optional): How to open the url. One of _blank, _self, _parent or _top.
            Defaults to "_self".
        """
        JS = (ROOT / "fast_gallery_template.js").read_text()
        TEMPLATE = (ROOT / "fast_gallery_template.html").read_text()
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

        if not target in ["_blank", "_parent", "_top", "_self"]:
            target = "_self"
        self.add_variable("target", target)

