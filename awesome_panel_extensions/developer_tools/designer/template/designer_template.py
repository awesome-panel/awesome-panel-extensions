import panel as pn
from jinja2 import Environment, FileSystemLoader
import holoviews as hv
import pathlib
from awesome_panel_extensions.developer_tools.designer import Designer

ROOT = pathlib.Path(__file__).parent
DESIGNER_TEMPLATE_HTML = ROOT / 'designer_template.html'
# env = Environment(loader=FileSystemLoader("."))
# jinja_template = env.get_template(DESIGNER_TEMPLATE_HTML_STR)

tmpl = pn.Template(DESIGNER_TEMPLATE_HTML.read_text())
designer = Designer(reload_services=[])
sidebar = pn.Column(designer.designer_pane, pn.Spacer(background="blue"), sizing_mode="stretch_both", background="gray")
main = pn.Column(designer.component_pane, pn.Spacer(background="salmon"), sizing_mode="stretch_both", background="yellow")
tmpl.add_panel('sidebar', sidebar)
tmpl.add_panel('main', main)

tmpl.servable()