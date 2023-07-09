from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import dash

# dataset for visualization
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

#register the page for the web and the path
external_stylesheets = [dbc.themes.LUX]
dash.register_page(__name__,name="Boostrap", path="/boostrap", external_stylesheets=external_stylesheets)


#Layout for the actual page
def layout():
    layout = dbc.Container([
        dbc.Row([
            html.Div('Aplicación con gráficas', className="text-primary text-center fs-3")
        ]),

        dbc.Row([
            dbc.RadioItems(options=[{"label": x, "value": x} for x in ['pop', 'lifeExp', 'gdpPercap']],
                        value='lifeExp',
                        inline=True,
                        id='radio-buttons')
        ]),

        dbc.Row([
            dbc.Col([
                dash_table.DataTable(data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'})
            ], width=6),

            dbc.Col([
                dcc.Graph(figure={}, id='graph-final')
            ], width=6),
        ]),

    ], fluid=True)
    return layout


#callback for update the graph
@callback(
    Output(component_id='graph-final', component_property='figure'),
    Input(component_id='radio-buttons', component_property='value')
)

#update graph based on radio buttons
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

