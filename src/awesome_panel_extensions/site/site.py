"""This module provides functionality for defining your site and registrering applications"""
import pathlib
from functools import wraps
from typing import Callable, Dict, Optional

import param
from panel.template.base import BasicTemplate

from awesome_panel_extensions.site.models import Application, User


class Site(param.Parameterized):
    """The Site provides meta data and functionality for registrering application meta data and
    views"""

    applications = param.List(doc="The list of applications to include in the site", constant=True)
    users = param.List(doc="The list of users contributing to the site", constant=True)
    css_path = param.ClassSelector(doc="A path to custom css", class_=pathlib.Path)
    js_path = param.ClassSelector(doc="A path to custom js", class_=pathlib.Path)

    def __init__(self, **params):
        if "applications" not in params:
            params["applications"] = []
        if "users" not in params:
            params["users"] = []

        super().__init__(**params)

    def _get_or_create_user(self, user: str) -> User:
        for item in self.users:  # pylint: disable=not-an-iterable
            if item.uid == user:
                return item
        return User(uid=user, name=user)

    def create_application(  # pylint: disable=too-many-arguments
        self,
        **params,
    ) -> Application:
        """Returns an Application from specified params.

        If you specify the author and owner uid as a string it will automatically be converted into
        a User.

        Returns:
            Application: An application
        """
        for key in ["author", "owner"]:
            value = params.get(key, None)
            if isinstance(value, str):
                params[key] = self._get_or_create_user(value)

        return Application(**params)

    def add(
        self,
        application=None,
    ):
        """Registers your Application and view function
        >>> from awesome_panel_extensions.site.models import User, Application
        >>> from awesome_panel_extensions.site import Site
        >>> site = Site(name="awesome-panel.org")
        >>> marc_skov_madsen = User(
        ...     uid="Marc",
        ...     name="Marc Skov Madsen",
        ...     url="https://datamodelsanalytics.com",
        ...     avatar="https://avatars0.githubusercontent.com/u/42288570",
        ...     resources = {
        ...         "twitter": "https://twitter.com/MarcSkovMadsen",
        ...         "linkedin": "https://www.linkedin.com/in/marcskovmadsen/",
        ...         "github": "https://github.com/MarcSkovMadsen",
        ...     }
        ... )
        >>> site.users.append(marc_skov_madsen)
        >>> application = site.create_application(
        ...     url="home",
        ...     name="Home",
        ...     author="Marc",
        ...     description="The home page",
        ...     description_long="The home page of awesome-panel.org.",
        ...     thumbnail="",
        ...     resources={
        ...         "documentation": "",
        ...         "code": "",
        ...         "gif": "",
        ...         "mp4": "",
        ...         "youtube": "",
        ...     },
        ...     tags=["Site"],
        ... )
        >>> @site.add(application)
        ... def view():
        ...     return pn.pane.Markdown("# Home")
        >>> site.applications
        [Application(name='Home')]
        >>> site.routes
        {'home': <function view at...>}
        """
        # pylint: disable=unsupported-assignment-operation
        if not application.url in [
            app.url for app in self.applications  # pylint: disable=not-an-iterable
        ]:  # pylint: disable=unsupported-membership-test
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

    @property
    def routes(self) -> Dict[str, Callable]:
        """Returns a dictionary with the url as key and the view as the value

        Returns:
            Dict[str, Callable]: [description]
        """
        # pylint: disable=not-an-iterable
        return {app.url: app.view for app in self.applications}

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
