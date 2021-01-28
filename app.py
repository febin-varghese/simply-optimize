import dash
# from dash.dependencies import Input, Output
# import dash_core_components as dcc
import dash_html_components as html

import flask
import os

# server = flask.Flask('app')
# server.secret_key = os.environ.get('secret_key', 'secret')

app = dash.Dash('app')
server = app.server

app.layout = html.Div([html.H1("Simply Optimize")])


if __name__ == '__main__':
    app.run_server()