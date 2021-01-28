import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# User defined modules
from test_functions import available_functions


def set_plot_children(name):
    test_functions = available_functions()
    function_obj = test_functions[name]()
    fig = function_obj.plot()
    plot_children = [html.H2(name, style={'textAlign': 'center', 'color': '#31E531'}),
                     dcc.Graph(figure=fig)]
    return plot_children


def app_layout(name="Ackley"):
    """
    Layout of the application
    :param name: Name of the test function
    :return: Layout
    """
    test_fns = available_functions()
    fn_options = [{'label': key, 'value': key} for key in test_fns.keys()]
    alg_options = [{'label': "WIP", 'value': "1"}]
    layout = html.Div([
        html.H1("Simply Optimize", style={'textAlign': 'center', 'color': '#40D3F3'}),
        html.Div(id='plot-layer', style={'width': '80%', 'height': '100%', 'display': 'block', 'margin-left': 'auto',
                                         'margin-right': 'auto'}, children=set_plot_children(name)
                 ),
        html.Div(className="row", style={'width': '80%', 'height': '100%', 'display': 'block', 'margin-left': 'auto',
                                         'margin-right': 'auto'},
                 children=[
                     html.Div([dcc.Dropdown(id='function-dropdown', options=fn_options, value=fn_options[0]['value'],
                                            clearable=False)
                               ], className="six columns", style={'display': 'block'}),
                     html.Div([dcc.Dropdown(id='algorithm-dropdown', options=alg_options, value=alg_options[0]['value'],
                                            clearable=False)
                               ], className="six columns", style={'display': 'block'})],
                 )

    ])
    return layout
