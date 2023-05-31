import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__,name="acercade", path="/acercade")

def layout():
    layout=dbc.Container(
        html.Div(
            [
                html.H1("Acerca de"),
                html.P("Esta es una aplicación del clima desarrollada con Dash."),
                # Agrega aquí más contenido sobre la página "Acerca de"
            ],
            className="mt-4",
        )
    )
    return layout
