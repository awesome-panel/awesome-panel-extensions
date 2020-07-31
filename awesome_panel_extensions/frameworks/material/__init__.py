"""Implementation of MWC Material Components"""
import panel as pn
import param

from .material_button import Button
from .slider import MWCSlider
from .select import MWCSelect

from .config import MWC_ICONS, get_extend_pane
from .style.stylesheet import Stylesheet
