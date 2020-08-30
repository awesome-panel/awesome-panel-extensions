import json
from awesome_panel_extensions.sketch.sketch_source import SketchSource
from typing import Callable, Iterable, List, Tuple, Union
from awesome_panel_extensions.sketch.sketch_configuration import SketchConfiguration
import param
import inspect


class Sketch(param.Parameterized):
    python = param.String(doc="The Python code of the Sketch.")
    html = param.String(doc="The HTML code of the Sketch.")
    css = param.String(doc="The CSS code of the Sketch.")
    configuration = param.ClassSelector(
        class_=SketchConfiguration,
        doc="""The configuration of the Sketch. Contains information about name, js_files, css_files \
         etc""",
    )

    def __init__(
        self,
        python: Union[str, Callable, List, Tuple] = "",
        html: str = "",
        css: str = "",
        configuration: SketchConfiguration = None,
    ):
        python = self._to_python_text(python)
        if not configuration:
            configuration = SketchConfiguration()
        super().__init__(name=configuration.name, python=python, html=html, css=css, configuration=configuration)

    @classmethod
    def _to_python_text(cls, python: Union[str, Callable, List, Tuple]) -> str:
        """Converts the

        Args:
            python (Union[str,Callable, Iterable]): A str, callable or iterable of these

        Examples:

        >>> Sketch._to_python_text("a")
        'a'
        >>> def add(a,b):
        ...     return a+b
        >>> Sketch._to_python_text(add)
        'def add(a,b):\\n    return a+b\\n'
        >>> Sketch._to_python_text(["a",[add]])
        'a\\n\\ndef add(a,b):\\n    return a+b\\n'
        """
        if isinstance(python, str):
            return python
        if callable(python):
            python = inspect.getsource(python)
            leading_spaces = len(python)-len(python.lstrip(' '))
            python_lines=[line[leading_spaces:] for line in python.splitlines()]
            return "\n".join(python_lines)

        python = [cls._to_python_text(item) for item in python]
        return "\n\n".join(python)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Sketch):
            return False
        return (
            self.python == o.python
            and self.html == o.html
            and self.css == o.css
            and self.configuration == o.configuration
        )

    def save(self, path) -> SketchSource:
        source = SketchSource(path=path)
        configuration = self.configuration

        source.python.write_text(self.python)
        source.html.write_text(self.html)
        source.css.write_text(self.css)
        configuration.save(path=source.configuration)
        return source

    @classmethod
    def read(cls, sketch_source: SketchSource) -> 'Sketch':
        python_text = sketch_source.python.read_text()
        html_text = sketch_source.html.read_text()
        css_text = sketch_source.css.read_text()
        configuration_text = sketch_source.configuration.read_text()
        configuration_dict = json.loads(configuration_text)
        configuration = SketchConfiguration(**configuration_dict)

        return cls(
            python=python_text,
            html=html_text,
            css=css_text,
            configuration=configuration
        )

    def copy(self)->'Sketch':
        return Sketch(
            python=self.python,
            html=self.html,
            css=self.css,
            configuration=self.configuration.copy()
        )