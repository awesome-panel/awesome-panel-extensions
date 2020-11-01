"""This module provides functionality for defining your site and registrering applications"""
from functools import wraps

import param

from .application import Application


class Site(param.Parameterized):
    """The Site provides meta data and functionality for registrering application meta data and
    views"""

    views = param.Dict(
        doc="A dictionary with the url as key and the view as the value", constant=True
    )
    applications = param.Dict(
        doc="A dictionary with the url as the key and the application as the value", constant=True
    )

    def __init__(self, **params):
        if "views" not in params:
            params["views"] = {}
        if "applications" not in params:
            params["applications"] = {}

        super().__init__(**params)

    def register(self, application: Application):
        """Registers you application meta data and view
        >>> from awesome_panel_extensions.models.resource import Author
        >>> from awesome_panel_extensions.site import Site, Application
        >>> site = Site(name="awesome-panel.org")
        >>> marc_skov_madsen = Author(
        ...     name="Marc Skov Madsen",
        ...     url="https://datamodelsanalytics.com",
        ...     avatar_url="https://avatars0.githubusercontent.com/u/42288570",
        ...     twitter_url="https://twitter.com/MarcSkovMadsen",
        ...     linkedin_url="https://www.linkedin.com/in/marcskovmadsen/",
        ...     github_url="https://github.com/MarcSkovMadsen",
        ... )
        >>> home = Application(
        ...     name="Home",
        ...     description="The home page of awesome-panel.org.",
        ...     url="home",
        ...     thumbnail_url="",
        ...     documentation_url="",
        ...     code_url="",
        ...     youtube_url="",
        ...     gif_url="",
        ...     author=marc_skov_madsen,
        ...     tags=["Site"],
        ... )
        >>> @site.register(application=home)
        ... def view():
        ...     return pn.pane.Markdown("# Home")
        >>> site.views
        {'home': <function view at...>}
        >>> site.applications
        {'home': Home}
        """

        def inner_function(view):
            url = application.url
            self.views[url] = view  # pylint: disable=unsupported-assignment-operation
            self.applications[url] = application  # pylint: disable=unsupported-assignment-operation
            application.view = view

            @wraps(view)
            def wrapper(*args, **kwargs):
                print(view, url, application, args, kwargs)
                view(*args, **kwargs)

            return wrapper

        return inner_function
