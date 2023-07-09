from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash

# dataset for visualization
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#register the page for the web and the path
dash.register_page(__name__,name="html", path="/html", external_stylesheets=external_stylesheets)

#Layout for the actual page
def layout():
    layout = html.Div([
        html.Div(className='row', children='Aplicación con gráficas ',
                style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),

        html.Div(className='row', children=[
            dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'],
                        value='lifeExp',
                        inline=True,
                        id='my-radio-buttons-final')
        ]),

        html.Div(className='row', children=[
            html.Div(className='six columns', children=[
                dash_table.DataTable(data=df.to_dict('records'), page_size=11, style_table={'overflowX': 'auto'})
            ]),
            html.Div(className='six columns', children=[
                dcc.Graph(figure={}, id='histo-chart-final')
            ])
        ])
    ])
    return layout

#callback for update the graph
@callback(
    Output(component_id='histo-chart-final', component_property='figure'),
    Input(component_id='my-radio-buttons-final', component_property='value')
)
#update graph based on radio buttons
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

