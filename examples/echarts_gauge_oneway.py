import panel as pn
import param

pn.config.js_files["echart1"] = "https://cdn.bootcss.com/echarts/3.7.2/echarts.min.js"
pn.config.sizing_mode = "stretch_width"

HTML = """
<div id="855be12876564e2fb3fd5fe122d3d221" class="chart-container" style="width:500px; height:300px;"></div>
"""

SCRIPT = """
<script>
var myScript = document.currentScript;
var myDiv = myScript.parentElement.firstElementChild;
var myChart = echarts.init(myDiv);
myDiv.eChart = myChart;

var option = {
tooltip: {
    formatter: '{a} <br/>{b} : {c}%'
},
toolbox: {
    feature: {
        restore: {},
        saveAsImage: {}
    }
},
series: [
    {
        name: 'Echarts velocimeter',
        type: 'gauge',
        detail: {formatter: '{value}%'},
        data: [{value: 50, name: 'vel'}]
    }
]
};

option.series[0].data[0].value = 25;
myChart.setOption(option, true);

myDiv.after_layout = myChart.resize; // Resizes the chart after layout of parent element

</script>

"""

PANEL_LOGO_PNG = (
    "<img src='https://panel.holoviz.org/_static/logo_horizontal.png' style='height:30px'>"
)


class EChartsGauge(param.Parameterized):
    value = param.Integer(default=0, bounds=(0, 100))
    view = param.Parameter()

    def __init__(self, **params):
        super().__init__(**params)

        self.plot_pane = pn.pane.HTML(HTML + SCRIPT)
        self.js_pane = pn.pane.HTML("", width=0, sizing_mode="fixed", margin=0)
        self.view = pn.Column(self.js_pane, self.plot_pane)
        self._update()

    @param.depends("value", watch=True)
    def _update(self, *events):
        part1 = " <script> option.series[0].data[0].value = "
        part3 = " ; myChart.setOption(option, true); </script> "
        self.js_pane.object = part1 + str(self.value) + part3

if __name__.startswith("bokeh"):
    gauge = EChartsGauge()
    bar = pn.pane.Markdown(
        "## Panel Extension: Echarts Gauge",
        background="black",
        style={"color": "white", "padding-left": "25px", "padding-top": "10px"},
    )
    settings = pn.Param(gauge, parameters=["value"], show_name=False, align="center")
    app = pn.Column(bar, gauge.view, settings, align="center", max_width=500,)
    app.servable()
