"""The SiteConfig model holds your Site configuration and settings"""
from typing import Dict

import param


class SiteConfig(param.Parameterized):
    """Can hold the configuration of a site"""

    site_name = param.String("Awesome Panel Starter")

    gallery_description = param.String("Search and find your app or other resource")

    color_primary = param.String("#A01346")
    color_cycle = param.List(["#A01346"])

    site_prefix = param.String("")

    assets_prefix = param.String()
    avatar_prefix = param.String()
    thumbnails_prefix = param.String()
    mp4_prefix = param.String()
    code_prefix = param.String()

    static_dirs = param.Dict()

    persons = param.Dict()
    applications = param.Dict()

    @property
    def routes(self) -> Dict:
        """Returns the routes to serve in the site

        Returns:
            Dict: The key is the url and the value the servable. Either a .py, .ipynb or a Callable
        """
        # pylint: disable=not-an-iterable, no-member
        return {app.url: app.servable for app in self.applications.values()}
