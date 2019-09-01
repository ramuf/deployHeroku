import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask import Flask
import os

server = Flask(__name__)
server.secret_key = os.environ.get('secret_key', 'secret')
app = dash.Dash(name = __name__, server = server)
app.config.supress_callback_exceptions = True

path = 'data/' 
files = os.listdir(path)
files_txt = [i for i in files if i.endswith('.csv')]

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
                id="metric-select-dropdown",
                options=list({"label": file, "value": file} for file in files_txt),
                placeholder="Select a file",
                clearable=False,
                #value=files_txt[1],
                )
        ],
        style={'width': '30%'},
        
    ),
    
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])