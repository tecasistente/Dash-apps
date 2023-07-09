import dash
from dash import Input, Output, html, dcc

import dash_bootstrap_components as dbc
from weather import main as get_weather

#register the page for the web and the path
dash.register_page(__name__,name="Clima", path="/")

#Layout for the actual page
content = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Label("Ciudad"),
                                dbc.Input(id="input-city", type="text", placeholder="Ingrese la ciudad"),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Label("Estado"),
                                dbc.Input(id="input-state", type="text", placeholder="Ingrese el estado"),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Label("País"),
                                dbc.Input(id="input-country", type="text", placeholder="Ingrese el país"),
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


#Load the layout 
layout = html.Div(
    content,
    style={"backgroundColor": "#c0eaf0", "height": "100vh"}
)


@dash.callback(
    Output("text-output", "children"), #weather results
    Output("html-img", "src"), #image to represent the weather
    Input("btn-buscar", "n_clicks"),
    [
        Input("input-country", "value"),
        Input("input-city", "value"),
        Input("input-state", "value")
    ]
)
def get_weather_values(n_clicks, country, city, state):
    try:
        if n_clicks:
            # Here you can use the values entered by the user
            # Perform the necessary actions, such as calling the weather API or processing the data
            data=get_weather(country,state, city)
            imagen_url="https://openweathermap.org/img/wn/"+data.icon+"@2x.png"
            dataText=str(data.main)+" : "+str(data.description) + "\nTemperatura : "+str(data.temperature)
            
            return dataText, imagen_url
        else:
            return "",""
    except:
        return "",""
