from typing import List
from panel import Template
import param

# The key to the template is to insert the '<fast-design-system-provider>' tag around the content
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
        <style>
            body {
                margin: 0px;
                height: 100vh;
                width: 100vw;
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
</body>
{% endblock %}
</html>
"""

class FastTemplate(Template):
    main = param.ClassSelector(class_=list, constant=True, doc="""
        A list-like container which populates the main area.""")

    def __init__(self, main: List):
        items = {str(key): value for key, value in enumerate(main)}
        super().__init__(template=TEMPLATE, items=items, main=main)

