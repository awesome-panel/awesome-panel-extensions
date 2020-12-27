"""This module provides functionality for defining your site and registrering applications"""
import pathlib
from functools import wraps
from typing import Callable, Dict, List, Optional

import param
from panel.template.base import BasicTemplate

from awesome_panel_extensions.site.application import Application
from awesome_panel_extensions.site.template import TemplateGenerator


class Site(param.Parameterized):
    """The Site provides meta data and functionality for registrering application meta data and
    views"""

    applications = param.List(doc="The list of applications to include in the site", constant=True)
    authors = param.List(doc="The list of authors contributing to the site", constant=True)
    css_path = param.ClassSelector(doc="A path to custom css", class_=pathlib.Path)
    js_path = param.ClassSelector(doc="A path to custom js", class_=pathlib.Path)

    def __init__(self, **params):
        if "applications" not in params:
            params["applications"] = []
        if "authors" not in params:
            params["authors"] = []

        super().__init__(**params)

        self._template_generator = TemplateGenerator(css_path=self.css_path, js_path=self.js_path)

    def create_application(  # pylint: disable=too-many-arguments
        self,
        url: str,
        name: str,
        introduction: str,
        description: str,
        author: str,
        thumbnail_url: str,
        code_url: str = "",
        documentation_url: str = "",
        gif_url: str = "",
        mp4_url: str = "",
        youtube_url: str = "",
        tags: Optional[List] = None,
    ) -> Application:
        """A Site consists of meta data, Resources, Applications and Routes.

        Args:
            url (str): The base url of the Site. For example 'https://awesome-panel.org'
            name (str): The name of the site. For example 'Awesome Panel'.
            introduction (str): A short description of the site.
            description (str): A longer description of the site.
            author (str): The name of the Author of the site.
            thumbnail_url (str): A Thumbnail visualising the site.
            code_url (str, optional): [description]. Defaults to "".
            documentation_url (str, optional): [description]. Defaults to "".
            gif_url (str, optional): [description]. Defaults to "".
            mp4_url (str, optional): [description]. Defaults to "".
            youtube_url (str, optional): [description]. Defaults to "".
            tags (Optional[List], optional): [description]. Defaults to None.

        Raises:
            ValueError: [description]

        Returns:
            Application: [description]
        """
        if tags is None:
            tags = []

        # pylint: disable=unsubscriptable-object, not-an-iterable
        author_list = [auth for auth in self.authors if auth.name == author]
        if author_list:
            author_ = author_list[0]
        else:
            raise ValueError(f"Error. Author '{author}' is not in the list of site authors!")

        return Application(
            url=url,
            name=name,
            introduction=introduction,
            description=description,
            author=author_,
            thumbnail_url=thumbnail_url,
            tags=tags,
            category="Application",
            documentation_url=documentation_url,
            code_url=code_url,
            gif_url=gif_url,
            mp4_url=mp4_url,
            youtube_url=youtube_url,
        )

    def add(
        self,
        application=None,
    ):
        """Registers you application meta data and view
        >>> from awesome_panel_extensions.site import Author
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
        >>> site.authors.append(marc_skov_madsen)
        >>> application = site.create_application(
        ...     url="home",
        ...     name="Home",
        ...     author="Marc Skov Madsen",
        ...     description="The home page of awesome-panel.org.",
        ...     introduction="The home page",
        ...     thumbnail_url="",
        ...     documentation_url="",
        ...     code_url="",
        ...     gif_url="",
        ...     mp4_url="",
        ...     youtube_url="",
        ...     tags=["Site"],
        ... )
        >>> @site.add(application)
        ... def view():
        ...     return pn.pane.Markdown("# Home")
        >>> site.applications
        [Home]
        >>> site.routes
        {'home': <function view at...>}
        """
        # pylint: disable=unsupported-assignment-operation
        if not application in self.applications:  # pylint: disable=unsupported-membership-test
            self.applications.append(application)

        def inner_function(view):
            @wraps(view)
            def wrapper(*args, **kwargs):
                template = view(*args, **kwargs)
                if (
                    isinstance(template, BasicTemplate)
                    and template.title == template.param.title.default
                ):
                    if not self.name == application.name:
                        template.title = application.name
                    else:
                        template.title = ""
                self.register_post_view(template=template, application=application)
                return template

            application.view = wrapper
            return wrapper

        return inner_function

    # pylint: disable=unused-argument
    def register_post_view(self, template: BasicTemplate, application: Application):
        """Updates the template or application"""
        template.site = self.name

    @property
    def routes(self) -> Dict[str, Callable]:
        """Returns a dictionary with the url as key and the view as the value

        Returns:
            Dict[str, Callable]: [description]
        """
        # pylint: disable=not-an-iterable
        return {app.url: app.view for app in self.applications}

    def create_template(  # pylint: disable=too-many-arguments, too-complex
        self,
        template: Optional[str] = None,
        theme: Optional[str] = None,
        **params,
    ) -> BasicTemplate:
        """Returns a BasicTemplate

        Args:
            template (str, optional): The name of the template. Defaults to TEMPLATE.
            theme (str, optional): The name of the theme. Defaults to THEME.
            **params: Optional template parameters

        Returns:
            BasicTemplate: The specified Template
        """
        params["site"] = params.get("site", self.name)
        return self._template_generator.get_template(
            template=template,
            theme=theme,
            **params,
        )

    def get_application(self, name: str) -> Optional[Application]:
        """Returns the application with the specified name

        Args:
            name (str): [description]

        Returns:
            Optional[Application]: [description]
        """
        # pylint: disable=not-an-iterable
        _app = [app for app in self.applications if app.name == name]
        if _app:
            return _app[0]
        return None
