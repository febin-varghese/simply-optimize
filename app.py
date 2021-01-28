import dash
from dash.dependencies import Input, Output

# User defined modules
from app_layout import app_layout, set_plot_children, set_optimum_labels
from optimizers import optimize_function


app = dash.Dash(__name__)
server = app.server
app.layout = app_layout()


@app.callback(Output(component_id='plot-layer', component_property='children'),
              Input(component_id='function-plot', component_property='clickData'),
              Input(component_id='function-dropdown', component_property='value'),
              Input(component_id='algorithm-dropdown', component_property='value'),
              )
def update_plot(clicked_data, function_name, optimizer_name):
    if clicked_data is not None:
        clicked_point = [clicked_data['points'][0]['x'], clicked_data['points'][0]['y']]
        minimum, position, opt_path_fig_obj = optimize_function(clicked_point, function_name, optimizer_name)
        return set_plot_children(function_name, minimum, position, opt_path_fig_obj)
    else:
        return set_plot_children(function_name)


if __name__ == '__main__':
    app.run_server()
