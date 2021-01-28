import dash
from dash.dependencies import Input, Output
# import dash_core_components as dcc
import dash_html_components as html

# User defined modules
from app_layout import app_layout, set_plot_children

app = dash.Dash(__name__)
server = app.server
app.layout = app_layout()


@app.callback(Output(component_id='plot-layer', component_property='children'),
              Input(component_id='function-dropdown', component_property='value')
              )
def update_plot(function_dropdown):
    return set_plot_children(function_dropdown)


if __name__ == '__main__':
    app.run_server()
