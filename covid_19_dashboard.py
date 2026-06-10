import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import dash
from dash import html,dcc
from dash.dependencies import Input,Output
import plotly.express as ps
from matplotlib.pyplot import title
external_stylesheet = [
    {
        "href":"https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css",
        "rel" :"stylesheet",
        "integrity":"sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2",
        "crossorigin":"anonymous"
    }
]
patients = pd.read_csv('state_level_latest.csv')
Confirmed = patients[['Confirmed']].sum()
Recovered = patients[['Recovered']].sum()
Deaths = patients[['Deaths']].sum()
Active = patients[['Active']].sum()
options=[
    {'label':"Confirmed",'value':'Confirmed'},
    {'label':"Recovered",'value':'Recovered'},
    {'label':"Deaths",'value':'Deaths'},
    {'label': "Active", 'value': 'Active'}
]
option_1= [
    {'label':"All",'value':'All'},
    {'label':"Oxygen",'value':'Oxygen'},
    {'label':"PulseRate",'value':'PulseRate'},
    {'label':"Temperature",'value':'Temperature'}
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheet)
app.layout= html.Div([
    html.H1('COVID-19 pandemic Dashboard',style={'textAlign':'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total cases',className='text-light'),
                    html.H4(Confirmed,className='text-light'),
                ], className='Card-Body'),

            ],className='card bg-danger'),
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Active cases',className='text-light'),
                    html.H4(Active,className='text-light'),
                ], className='Card-Body'),

            ],className='card bg-success'),
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Recovered cases',className='text-light'),
                    html.H4(Recovered,className='text-light'),
                ], className='Card-Body'),
            ],className='card bg-warning'),
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Deaths',className='text-light'),
                    html.H4(Deaths,className='text-light'),
                ], className='Card-Body'),

            ],className='card bg-primary'),
        ],className='col-md-3'),

    ],className="row"),
    html.Div([],className="row"),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='picker',options=options,value='All'),
                    dcc.Graph(id='bar'),
                ],className='card-body')
            ],className='card')
        ],className="col-md-12"),
    ],className="row"),

], className="container")

@app.callback(Output('bar','figure'),[Input('picker','value')])
def update_graph(selected_type):
    if selected_type == 'Confirmed':
        return {'data': [go.Bar(x=patients['State'],y=patients['Confirmed'])],
                'layout':go.Layout(title= 'state_total_count -{selected_type}' ,plot_bgcolor='orange')
                }
    if selected_type == 'Recovered':
        return {'data': [go.Bar(x=patients['State'],y=patients['Recovered'])],
                'layout':go.Layout(title= f'State total count -{selected_type}',plot_bgcolor='orange')
                }
    if selected_type == 'Deaths':
        return {'data': [go.Bar(x=patients['State'],y=patients['Deaths'])],
                'layout':go.Layout(title= f'State total count -{selected_type}',plot_bgcolor='orange')
                }
    if selected_type == 'Active':
        return {'data': [go.Bar(x=patients['State'],y=patients['Active'])],
                'layout':go.Layout(title= 'State total count -{selected_type}',plot_bgcolor='orange')
                }
if __name__=='__main__':
    app.run(debug=True)

