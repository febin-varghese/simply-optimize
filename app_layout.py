import dash
# from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

# User defined modules
from test_functions import Ackley
from test_functions import available_functions


def set_plot_children(name):
    test_functions = available_functions()
    function_obj = test_functions[name]()
    fig = function_obj.plot()
    plot_children = [html.H2(name, style={'textAlign': 'center', 'color': '#31E531'}),
                     dcc.Graph(figure=fig)]
    return plot_children


def app_layout(name="Ackley"):
    test_fns = available_functions()
    fn_options = [{'label': key, 'value': key} for key in test_fns.keys()]
    layout = html.Div([
        html.H1("Simply Optimize", style={'textAlign': 'center', 'color': '#40D3F3'}),
        html.Div(id='plot-layer', style={'width': '80%', 'height': '100%', 'display': 'block', 'margin-left': 'auto',
                                         'margin-right': 'auto'}, children=set_plot_children(name)
                 ),
        html.Div(style={'width': '80%', 'height': '100%', 'display': 'block', 'margin-left': 'auto',
                        'margin-right': 'auto'},
                 children=[dcc.Dropdown(id='function-dropdown', options=fn_options, value=fn_options[0]['value'],
                                        clearable=False)],
                 )

    ])
    return layout
