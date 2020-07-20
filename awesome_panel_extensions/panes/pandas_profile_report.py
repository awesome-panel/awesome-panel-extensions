"""# PandasProfileReport

The PandasProfileReport pane enables a user to show a ProfileReport generated by the
[Pandas profile_report](https://github.com/pandas-profiling/pandas-profiling) package.
"""
import html

import panel as pn
import param
from pandas_profiling import ProfileReport

# pylint: disable=line-too-long
object_when_loading_report_REPORT = "<p class='pandas-profile-report-loading'>Loading Report ...</p>"
GREEN = "#174c4f"
ORANGE = "#cc5c29"
LOGO_URL = "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/application/pages/pandas_profiling_app/pandas_profiler_logo.png"
# pylint: enable=line-too-long
STYLE = "width:100%;height:100%;"
OBJECT_WHEN_NO_REPORT = f"<p class='pandas-profile-report-no-report'>No Report Available</p>"



class PandasProfileReport(pn.pane.HTML):
    """The PandasProfilingApp showcases how to integrate the Pandas Profiling Report with Panel"""

    profile_report = param.ClassSelector(class_=ProfileReport)
    object_when_loading_report = param.String(object_when_loading_report_REPORT)
    object_when_no_report = param.String(OBJECT_WHEN_NO_REPORT)

    def __init__(self, **params):
        self._rename["profile_report"]=None
        super().__init__(**params)

        self._update_object()

    @param.depends("profile_report", "object_when_no_report", watch=True)
    def _update_object(self):
        if not self.profile_report:
            self.object = self.object_when_no_report
            return

        self.object = self.object_when_loading_report
        self.object = self._to_html(self.profile_report)

    def _to_html(self, profile_report: ProfileReport) -> str:
        html_report = profile_report.to_html()
        html_report = html.escape(html_report)
        return (
            f"""<iframe srcdoc="{html_report}" style={STYLE} frameborder="0" allowfullscreen></iframe>"""
        )

    def __str__(self):
        return "Pandas Profile Report"

    def __repr__(self):
        return self.__str__()