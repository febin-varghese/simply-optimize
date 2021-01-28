import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# User defined modules
from test_functions import available_functions
from optimizers import available_optimizers


def set_optimum_labels(predicted_min=None, position=()):
    pred_min = f"Predicted minimum: {predicted_min} at {position}" if predicted_min is not None \
        else f"Predicted minimum: - at ()"
    return html.Label(id='predicted-minimum', children=pred_min)


def set_plot_children(name, predicted_min=None, position=(), optimization_path=None):
    test_functions = available_functions()
    function_obj = test_functions[name]()
    fig = function_obj.plot()
    if optimization_path is not None:
        fig.add_trace(optimization_path)
    global_min = f"Global minimum: {function_obj.global_min} at {function_obj.global_min_parameters}"
    plot_children = [html.H2(name, style={'textAlign': 'center', 'color': '#31E531'}),
                     dcc.Graph(id='function-plot', figure=fig),
                     html.Label(global_min, style={'padding-right': '50px'}),
                     set_optimum_labels(predicted_min, position)]
    return plot_children


def app_layout(name="Ackley"):
    """
    Layout of the application
    :param name: Name of the test function
    :return: Layout
    """
    test_fns = available_functions()
    fn_options = [{'label': key, 'value': key} for key in test_fns.keys()]
    opt_algs = available_optimizers()
    alg_options = [{'label': key, 'value': key} for key in opt_algs.keys()]
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
