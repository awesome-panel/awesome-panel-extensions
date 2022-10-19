"""Configuration and settings for the Designer. TO BE REFACTORED."""
ACTION_PARAMETERS = [
    "reload_component",
    "reload_css_file",
    "reload_js_file",
    "last_reload",
]

CSS = """
body {
    margin: 0px;
    max-width: 100vw;
    min-height: 100vh;
    margin: 0px;
}

.bk.designer-design-pane a:link {
    color: black;
    font-style: normal;
    text-decoration: none;
}

.bk-root .bk-btn-primary, .bk-root .bk-btn-primary:hover, .bk-root .bk-btn-primary.bk-active {
    background: #66bb6a;
    border-color: #66bb6a;
}

.bk.designer-design-pane {
    color: black;
    border-left-color: #9E9E9E;
    border-left-width: 1px;
    border-left-style: solid;
    border-bottom-color: #9E9E9E;
    border-bottom-width: 1px;
    border-bottom-style: solid;
}
.bk.designer-component-pane {
    color: black;
    border-right-color: #9E9E9E;
    border-right-width: 1px;
    border-right-style: solid;
    border-bottom-color: #9E9E9E;
    border-bottom-width: 1px;
    border-bottom-style: solid;
    border-left-color: #9E9E9E;
    border-left-width: 1px;
    border-left-style: solid;
    border-top-color: #9E9E9E;
    border-top-width: 1px;
    border-top-style: solid;
}
"""
