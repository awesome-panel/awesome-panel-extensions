"""Utilities used by awesome-panel.org"""
import pathlib
from typing import Dict, Optional

import panel as pn
import param
from panel.template.base import BasicTemplate

from awesome_panel_extensions._shared.logger import get_logger
from awesome_panel_extensions.frameworks.fast.templates import FastGridTemplate, FastListTemplate

# pylint: disable=line-too-long
from awesome_panel_extensions.frameworks.fast.templates.fast_grid_template.fast_grid_template import (
    FastGridDarkTheme,
    FastGridDefaultTheme,
)

# pylint: disable=line-too-long
from awesome_panel_extensions.frameworks.fast.templates.fast_list_template.fast_list_template import (
    FastDarkTheme,
    FastDefaultTheme,
)

# pylint: enable=line-too-long
from awesome_panel_extensions.site.template.template_settings import (
    DEFAULT_TEMPLATE,
    DEFAULT_THEME,
    TemplateSettings,
)

logger = get_logger(__name__)

TEMPLATES: Dict[str, pn.template.BaseTemplate] = {
    "vanilla": pn.template.VanillaTemplate,
    "golden": pn.template.GoldenTemplate,
    "material": pn.template.MaterialTemplate,
    "bootstrap": pn.template.BootstrapTemplate,
    "react": pn.template.ReactTemplate,
    "fast": FastListTemplate,
    "fastgrid": FastGridTemplate,
}
THEMES = {
    "vanilla": {"default": pn.template.DefaultTheme, "dark": pn.template.DarkTheme},
    "golden": {"default": pn.template.DefaultTheme, "dark": pn.template.DarkTheme},
    "bootstrap": {"default": pn.template.DefaultTheme, "dark": pn.template.DarkTheme},
    "react": {"default": pn.template.DefaultTheme, "dark": pn.template.DarkTheme},
    "material": {
        "default": pn.template.material.MaterialDefaultTheme,
        "dark": pn.template.material.MaterialDarkTheme,
    },
    "fast": {"default": FastDefaultTheme, "dark": FastDarkTheme},
    "fastgrid": {"default": FastGridDefaultTheme, "dark": FastGridDarkTheme},
}

_TEMPLATE_CSS_ID = "/* CUSTOM TEMPLATE CSS */\n"
_TEMPLATE_JS_ID = "// CUSTOM TEMPLATE JS"


class TemplateGenerator(param.Parameterized):
    """The TemplateGenerator can create templates based on the url query arguments"""

    css_path = param.ClassSelector(doc="A path to custom css", class_=pathlib.Path)
    js_path = param.ClassSelector(doc="A path to custom js", class_=pathlib.Path)

    default_template = param.String(doc="The default template to use", default=DEFAULT_TEMPLATE)
    default_theme = param.String(doc="The default theme to use", default=DEFAULT_THEME)
    templates = param.Dict(doc="A dictionary of template name: template class", default=TEMPLATES)
    themes = param.Dict(
        doc="A dictionary of template name: a dictionary of theme name: theme class", default=THEMES
    )

    def _set_template_css(self, template, theme):
        # remove other site css
        pn.config.raw_css = [
            css for css in pn.config.raw_css if not css.startswith(_TEMPLATE_CSS_ID)
        ]
        if not self.css_path:
            return

        files = [
            "all.css",
            f"all_{theme}.css",
            f"{template}.css",
            f"{template}_{theme}.css",
        ]
        text = ""
        for file in files:
            text = ""
            if not file in pn.state.cache:
                file_css_id = f"/* {file} */\n"
                css_file = self.css_path / file
                if css_file.exists():
                    text = _TEMPLATE_CSS_ID + file_css_id + css_file.read_text()
            else:
                text = pn.state.cache[file]
                pn.state.cache.pop(file)
            if text:
                pn.config.raw_css.append(text)

    def _get_template_js(self, template):
        if not self.js_path:
            return ""
        jss = []
        files = [
            f"{template}.js",
        ]
        for file in files:
            if not file in pn.state.cache:
                file_js_id = f" {file} \n"
                text = _TEMPLATE_JS_ID + file_js_id + (self.js_path / file).read_text()
            else:
                text = pn.state.cache[file]
                pn.state.cache.pop(file)
            jss.append(text)
        return "\n".join(jss)

    @staticmethod
    def _get_params(value, class_):
        logger.debug("_get_params %s %s", value, class_)
        if isinstance(value, class_):
            return value
        if isinstance(value, tuple):
            value = [*value]
        elif not isinstance(value, list):
            value = [value]
        # Important to fx. convert @param.depends functions
        value = [pn.panel(item) for item in value]

        if class_ == pn.layout.ListLike:
            return class_(objects=value)
        if class_ == pn.layout.GridSpec:
            logger.debug(
                "grid %s",
                value,
            )
            grid = class_()
            for index, item in enumerate(value):
                print(index, item)
                grid[index, :] = item
            return grid

        return value

    def get_template(  # pylint: disable=too-many-arguments, too-complex
        self,
        template: Optional[str] = None,
        theme: Optional[str] = None,
        **params,
    ) -> BasicTemplate:
        """Returns the specified BasicTemplate

        Args:
            template (str, optional): The name of the template. Defaults to TEMPLATE.
            theme (str, optional): The name of the theme. Defaults to THEME.
            **params: Optional parameters

        Returns:
            BasicTemplate: The specified Template
        """
        logger.info("Getting Template")
        logger.info(pn.state.session_args)
        site_parameters = []
        if not template:
            site_parameters.append("template")
        if not theme:
            site_parameters.append("theme")

        if not template:
            template = pn.state.session_args.get("template", self.default_template)
            if isinstance(template, list):
                template = template[0].decode("utf-8")
                template = template.strip("'").strip('"')
        if not theme:
            theme = pn.state.session_args.get("theme", self.default_theme)
            if isinstance(theme, list):
                theme = theme[0].decode("utf-8")
                theme = theme.strip("'").strip('"')
        # pylint: disable=unsubscriptable-object
        template_class = self.templates.get(str(template), self.templates[self.default_template])
        # pylint: enable=unsubscriptable-object
        # To be fixed with PR https://github.com/holoviz/panel/pull/1694
        if "header" in params:
            params["header"] = self._get_params(
                params["header"], template_class.param.header.class_
            )
        if "main" in params:
            params["main"] = self._get_params(params["main"], template_class.param.main.class_)
        if "sidebar" in params:
            params["sidebar"] = self._get_params(
                params["sidebar"], template_class.param.sidebar.class_
            )
        if "modal" in params:
            params["modal"] = self._get_params(params["modal"], template_class.param.modal.class_)

        self._set_template_css(template, theme)
        # pylint: disable=unsubscriptable-object
        template_instance = template_class(
            theme=self.themes.get(str(template), self.themes[self.default_template]).get(
                str(theme), self.default_theme
            ),
            **params,
        )
        # enable: disable=unsubscriptable-object

        if site_parameters and "fast" not in str(template_class).lower():
            site_settings = TemplateSettings(parameters=site_parameters)
            header = pn.Row(pn.layout.HSpacer(), site_settings.view, sizing_mode="stretch_width")
            template_instance.header.append(header)

        return template_instance


if __name__.startswith("bokeh"):
    FAVICON = (
        "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/"
        "2781d86d4ed141889d633748879a120d7d8e777a/assets/images/favicon.ico"
    )
    template_generator = TemplateGenerator()
    _template = template_generator.get_template(
        title="Test App",
        site="Awesome Panel",
        favicon=FAVICON,
        main_max_width="1100px",
        main=[pn.pane.Markdown("hello world")],
    )
    _template.servable()
