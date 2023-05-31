
import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc
from weather import main as get_weather


#app = dash.Dash(__name__, use_pages=True,external_stylesheets=[dbc.themes.BOOTSTRAP])
#app.config.suppress_callback_exceptions=True


# Definición del diseño de la barra de navegación
'''navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Inicio", href="/")),
        dbc.NavItem(dbc.NavLink("Acerca de", href="/acercade")),
    ],
    brand="Aplicación del Clima",
    brand_href="#",
    color="dark",
    dark=True
)'''

dash.register_page(__name__,name="Clima", path="/")

# Definición del contenido principal de la aplicación
content = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Label("Ciudad"),
                                dbc.Input(id="input-ciudad", type="text", placeholder="Ingrese la ciudad"),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Label("Estado"),
                                dbc.Input(id="input-estado", type="text", placeholder="Ingrese el estado"),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Label("País"),
                                dbc.Input(id="input-pais", type="text", placeholder="Ingrese el país"),
                            ]
                        ),
                        dbc.Button("Buscar", id="btn-buscar", color="primary", className="mt-3"),
                    ],
                    md=6,
                ),
                dbc.Col(
                    [
                        html.Div(id="text-output"),  # Salida para el texto
                        html.Img(id ='html-img', src = '') 
                    ],
                    md=6,
                    className="d-flex justify-content-center align-items-center"
                ),
            ], 
        ),
    ],
    className="mt-4"
)

# Definición del diseño de la aplicación
# Definición del diseño de la aplicación 
layout = html.Div(
    content,
    style={"backgroundColor": "#c0eaf0", "height": "100vh"}
)


@dash.callback(
    Output("text-output", "children"),
    Output("html-img", "src"),
    Input("btn-buscar", "n_clicks"),
    [
        Input("input-pais", "value"),
        Input("input-ciudad", "value"),
        Input("input-estado", "value")
    ]
)

def obtener_valores_clima(n_clicks, pais, ciudad, estado):
    if n_clicks:
        # Aquí puedes utilizar los valores ingresados por el usuario
        # Realiza las acciones necesarias, como llamar a la API del clima o procesar los datos
      
        data=get_weather(pais,estado, ciudad)
        imagen_url="https://openweathermap.org/img/wn/"+data.icon+"@2x.png"
        dataText=str(data.main)+" : "+str(data.description) + "\nTemperatura : "+str(data.temperature)
        
        return dataText, imagen_url
    else:
        return "",""

