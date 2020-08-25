import panel as pn
import pathlib

pn.config.js_files.update({
    "p5": "https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.1.9/p5.min.js",
})

def app():
    source_path_or_url = pathlib.Path(__file__).parent/"__target__/p5test.js"
    source_js = "" # source_path_or_url.read_text()

    HTML = f"""
    "Hello"
    <div id="sketch-holder">
        <!-- Our sketch will go here! -->
    </div>
    <script type="module" src="__target__/p5test.js"></script>
    """

    return pn.pane.HTML(HTML)

pn.serve(
    {"": app},
    static_dirs={"__target__": "./__target__"},
    port=5006,
)