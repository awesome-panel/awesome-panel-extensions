import param
from panel import Template

FAST_CSS = """
html {
    height:100%;
}
html, fast-design-system-provider {
    min-height: 100vh;
}
body {
    margin: 0px;
    padding: 0;
    font-style: normal;
    font-variant-ligatures: normal;
    font-variant-caps: normal;
    font-variant-numeric: normal;
    font-variant-east-asian: normal;
    font-weight: normal;
    font-stretch: normal;
    font-size: 16px;
    line-height: normal;
    font-family: aktiv-grotesk, "Segoe UI", Arial, Helvetica, sans-serif;
    overflow-x: hidden;
    overflow-y: hidden;
}
.bk-root .bk-fast-input {
  display: inline-block;
  width: 100%;
  flex-grow: 1;
  -webkit-flex-grow: 1;
  min-height: 31px;
  padding: 0 12px;
}
"""
# The key to the template is to insert the '<fast-design-system-provider>' tag around the content
# For now the FAST_CSS is included directly in the template. Will have to find a better way.
# Please also note that the template loads the fast js dependency as Panel does not currently
# support loading js modules.
# Please also note that for usage on server the height is set to 100vh to not get a mix of
# black and white backgrounds. We only want the background from the fast-design-system-provider
TEMPLATE = """
{% from macros import embed %}

<!DOCTYPE html>
<html lang="en">
{% block head %}
<head>
    {% block inner_head %}
    <meta charset="utf-8">
    <title>{% block title %}{{ title | e if title else "Panel App" }}{% endblock %}</title>
    {% block preamble %}{% endblock %}
    {% block resources %}
        {% block css_resources %}
        {{ bokeh_css | indent(8) if bokeh_css }}
        {% endblock %}
        {% block js_resources %}
        {{ bokeh_js | indent(8) if bokeh_js }}
        {% endblock %}
    {% endblock %}
    {% block postamble %}
        <link href="https://use.typekit.net/spx2dgm.css" rel="stylesheet">
        <style>
            html {
                height:100%;
            }
            html, fast-design-system-provider {
                min-height: 100vh;
            }
            body {
                margin: 0px;
                padding: 0;
                font-style: normal;
                font-variant-ligatures: normal;
                font-variant-caps: normal;
                font-variant-numeric: normal;
                font-variant-east-asian: normal;
                font-weight: normal;
                font-stretch: normal;
                font-size: 16px;
                line-height: normal;
                font-family: aktiv-grotesk, "Segoe UI", Arial, Helvetica, sans-serif;
            }
            .bk-root .bk-fast-input {
                display: inline-block;
                width: 100%;
                flex-grow: 1;
                -webkit-flex-grow: 1;
            }
        </style>
    {% endblock %}
    {% endblock %}
</head>
{% endblock %}
{% block body %}
<body>
    <fast-design-system-provider use-defaults>
        {% block inner_body %}
        {% block contents %}
            {% for doc in docs %}
            {{ embed(doc) if doc.elementid }}
            {% for root in doc.roots %}
                {{ embed(root) | indent(10) }}
            {% endfor %}
            {% endfor %}
        {% endblock %}
        {{ plot_script | indent(8) }}
        {% endblock %}
    </fast-design-system-provider>
    <script type="module" src="https://unpkg.com/@microsoft/fast-components"></script>
</body>
{% endblock %}
</html>
"""

NB_TEMPLATE = """
{% from macros import embed %}

<!DOCTYPE html>
<html lang="en">
{% block head %}
<head>
    {% block inner_head %}
    <meta charset="utf-8">
    <title>{% block title %}{{ title | e if title else "Panel App" }}{% endblock %}</title>
    {% block preamble %}{% endblock %}
    {% block resources %}
        {% block css_resources %}
        {{ bokeh_css | indent(8) if bokeh_css }}
        {% endblock %}
        {% block js_resources %}
        {{ bokeh_js | indent(8) if bokeh_js }}
        {% endblock %}
    {% endblock %}
    {% block postamble %}
        <style>
            body {
                margin: 0px;
                padding: 0;
                font-style: normal;
                font-variant-ligatures: normal;
                font-variant-caps: normal;
                font-variant-numeric: normal;
                font-variant-east-asian: normal;
                font-weight: normal;
                font-stretch: normal;
                font-size: 16px;
                line-height: normal;
                font-family: aktiv-grotesk, "Segoe UI", Arial, Helvetica, sans-serif;
            }
            .bk-root .bk-fast-input {
                display: inline-block;
                width: 100%;
                flex-grow: 1;
                -webkit-flex-grow: 1;
            }
        </style>
    {% endblock %}
    {% endblock %}
</head>
{% endblock %}
{% block body %}
<body>
    <fast-design-system-provider use-defaults>
        {% block inner_body %}
        {% block contents %}
            {% for doc in docs %}
            {{ embed(doc) if doc.elementid }}
            {% for root in doc.roots %}
                {{ embed(root) | indent(10) }}
            {% endfor %}
            {% endfor %}
        {% endblock %}
        {{ plot_script | indent(8) }}
        {% endblock %}
    </fast-design-system-provider>
    <script type="module" src="https://unpkg.com/@microsoft/fast-components"></script>
</body>
{% endblock %}
</html>
"""


class FastTemplate(Template):
    main = param.ClassSelector(
        class_=list,
        constant=True,
        doc="""
        A list-like container which populates the main area.""",
    )

    def __init__(self, main):
        if not isinstance(main, list):
            main = [main]
        items = {str(key): value for key, value in enumerate(main)}
        super().__init__(template=TEMPLATE, nb_template=NB_TEMPLATE, items=items, main=main)
