import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

#register the page for the web and the path
dash.register_page(__name__,name="acercade", path="/acercade")

"""
Layout for the actual page
"""
def layout():
    layout=dbc.Container(
        html.Div(
            [
                html.H1("Acerca de"),
                html.P("Esta es una aplicación desarrollada con Dash."),
                html.P("Contiene diferentes funcionalidades para explorar los usos de la aplicación"),
            ],
            className="mt-4",
        )
    )
    return layout
