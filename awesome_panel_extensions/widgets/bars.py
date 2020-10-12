import uuid

import panel as pn
import param

from awesome_panel_extensions.models.link import Link

CSS = """
body { margin: 0px }
.top-app-bar {
    box-shadow: 5px 5px 20px #9E9E9E;
    font-size: 16px;
    color: white;
}
.top-app-bar p {
    display: inline-block;
    margin: 5px;
}
.top-app-bar a {
    color: white;
    text-decoration: none;
    font-size: 16px;
    padding: 5px;
    border-radius: 4px;
    height: 30px;
}
.top-app-bar-link:hover {
    background: #2B2B2B;
}
.top-app-bar-select {
    border-color: rgb(211, 211, 211);
    border-radius: 4px;
    font-size: 16px;
    height: 30px;
    background: black;
    color: white;
    padding: 5px;
}
"""


class TopBar(pn.Row):
    """Extension Implementation"""

    left_logo_url = param.String()
    index_application = param.ClassSelector(class_=Link)
    active_application = param.ClassSelector(class_=Link)
    applications = param.List(class_=Link)
    resources = param.List(class_=Link)
    social_links = param.List(class_=Link)
    right_logo_url = param.String()

    # The _rename dict is used to keep track of Panel parameters to sync to Bokeh properties.
    # As value is not a property on the Bokeh model we should set it to None
    _rename = {
        **pn.Row._rename,
        "left_logo_url": None,
        "index_application": None,
        "active_application": None,
        "applications": None,
        "resources": None,
        "social_links": None,
        "right_logo_url": None,
    }

    def __init__(self, css=CSS, **params):
        if not "height" in params:
            params["height"] = 50
        if not "sizing_mode" in params:
            params["sizing_mode"] = "stretch_width"
        if not "css_classes" in params:
            params["css_classes"] = ["top-app-bar"]
        super().__init__(**params)

        self._css = css

        # Please note that the alternative of setting
        # @param.depends('value', watch=True)
        # on _update_plot_pane does not work.
        # See https://github.com/holoviz/panel/issues/1060
        # Please upvote the issue if you think it is important to fix
        # self.param.watch(self._update_something_based_on_value, 'value')
        # "left_logo_url": None,
        # "index_application": None,
        # "application": None,
        # "applications": None,
        # "resources": None,
        # "social_links": None,
        # "right_logo_url": None,
        self._update_all()

    def _update_all(self, *events):
        objects = []
        if self.left_logo_url and self.left_logo_url != "":
            left_logo_url_panel = self._get_logo_panel(self.left_logo_url, self.index_application)
            objects.append(left_logo_url_panel)

        breadcrumps = ""
        if self.index_application:
            breadcrumps += f'<a class="top-app-bar-link" href="{self.index_application.url}">{self.index_application.name}</a>'
        if self.index_application and self.active_application:
            breadcrumps += "<p>/</p>"
        if self.active_application:
            if not self.applications:
                breadcrumps += f'<a class="top-app-bar-link" href="{self.active_application.url}">{self.active_application.name}</a>'
            else:
                breadcrumps += self._get_select()
        if breadcrumps:
            objects.append(
                pn.pane.HTML(breadcrumps, align="center", margin=(0, 10, 0, 10), width=300)
            )

        objects.append(pn.layout.HSpacer())

        if self.right_logo_url and self.right_logo_url != "":
            right_logo_url_panel = self._get_logo_panel(self.right_logo_url, None)
            objects.append(right_logo_url_panel)

        style_panel = pn.pane.HTML(
            f"""
            <style>
            {self._css}
            </style>
            """
        )
        objects.append(style_panel)

        self[:] = objects

    def _get_logo_panel(self, logo_url, logo_link):
        if logo_url.lower().endswith(".png"):
            logo_link_panel = pn.pane.PNG(object=logo_url, align="center")

            if logo_link and logo_link.url:
                logo_link_panel.link_url = logo_link.url
        else:
            raise ValueError("Type of left_logo_url is not supported")
        if self.height > 0:
            logo_link_panel.height = self.height - 20
            logo_link_panel.margin = (0, 10, 0, 10)
        return logo_link_panel

    def _get_select(self):
        select_id = uuid.uuid4()
        text = f"""<select class="top-app-bar-select" name="applications" id="{select_id}" onChange="openUrl()">"""
        for app in self.applications:
            if app.name == self.active_application.name:
                text += f"""<option value="{app.url}" selected>{app.name}</option>"""
            else:
                text += f"""<option value="{app.url}">{app.name}</option>"""
        text += """</select>"""
        text += f"""
        <script>
        function openUrl(){{
            el=document.getElementById("{select_id}")
            const value = el.value
            window.open(value,'_blank');
        }}
        </script>
        """
        return text


class BottomBar:
    pass
