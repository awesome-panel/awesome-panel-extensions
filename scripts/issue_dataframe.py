import pandas as pd
import numpy as np
import panel as pn
from datetime import datetime, date

component = component = pn.widgets.MultiChoice(name='MultiSelect', value=['Apple', 'Pear'],
                options=['Apple', 'Banana', 'Pear', 'Strawberry'], disabled=True)
component.servable()