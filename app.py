import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask import Flask
import pandas as pd
import os
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = Flask(__name__)
server.secret_key = os.environ.get('secret_key', 'secret')
app = dash.Dash(name = __name__, server = server)
app.config.supress_callback_exceptions = True


path = 'data/' 
files = os.listdir(path)
files_txt = [i for i in files if i.endswith('.csv')]


#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    html.Br(),
    
    html.Div(
        children=[
            html.P(
                "Select the file to plot."
            ),
            dcc.Dropdown(
                id="my-dropdown",
                options=list({"label": file, "value": file} for file in files_txt),
                placeholder="Select a file",
                clearable=False,
                value=files_txt[1],
                ),

            dcc.Dropdown(
                id='my-dropdown2',
                options=[
                    {'label': 'New York City', 'value': 'NYC'},
                    {'label': 'Montreal', 'value': 'MTL'},
                    {'label': 'San Francisco', 'value': 'SF'}
                ],
                value='NYC'
            ),
        ],
        style={'width': '30%'},       
    ),

    html.Div(
        id = 'some-text'
    ),
    
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                #{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': ['WHITE', 'BLACK', 'ASIAN'], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    
    dcc.Graph(
        id='plot-graph'        
    )


])

@app.callback(
    dash.dependencies.Output('some-text', 'children'),
    #dash.dependencies.Output('plot-graph', 'figure'),
    [dash.dependencies.Input('my-dropdown', 'value')])
def update_graph(value):
    #df = pd.read_csv(value)
    return 'You have selected "{}"'.format(path + value)
    



#if __name__ == '__main__':
#    app.run_server(debug=True)
