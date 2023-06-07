from dash import Dash, html, dcc
import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc


app = dash.Dash(__name__, use_pages=True,external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions=True
server=app.server()


layout = html.Div([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Clima", href="/")),
            dbc.NavItem(dbc.NavLink("Gramática", href="/gramatica")),
            #dbc.NavItem(dbc.NavLink("Imagen", href="/imagen")),
            dbc.NavItem(dbc.NavLink("Acerca de", href="/acercade")),
        ],
        brand="Aplicación en Dash",
        brand_href="/",
        color="dark",
        dark=True
    ),

	dash.page_container
])

app.layout=html.Div(
	layout,
	style={"backgroundColor": "#c0eaf0", "height": "100vh"}
)

if __name__ == '__main__':
	app.run_server(debug=False)