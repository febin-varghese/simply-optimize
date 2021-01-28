import dash
# from dash.dependencies import Input, Output
# import dash_core_components as dcc
import dash_html_components as html


class SimplyOptimize:
    def __init__(self):
        self.app = dash.Dash(__name__)
        self.server = self.app.server
        self.app.layout = self.build_layout()

    def build_layout(self):
        layout = html.Div([html.H1("Simply Optimize")])
        return layout


if __name__ == '__main__':
    simply_optimize = SimplyOptimize()
    # server = simply_optimize.app.server
    simply_optimize.app.run_server()
