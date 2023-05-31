import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from image_text import check_text

dash.register_page(__name__,name="gramatica", path="/gramatica")


# Definir el contenido de la página
def layout():
    content = dbc.Container(
        
        dbc.Row(
            
            dbc.Col(
                [
                    html.Div(
                        html.H1("Corrección de texto"),
                        className="text-center",
                    ), 
                   
                    dbc.Row(
                        dbc.Col(
                            dbc.Textarea(id='input-text', placeholder='Ingresa tu texto en inglés', style={'width': '100%'}),
                            width=6,
                            className="mx-auto",
                        ),
                        className="mt-4",
                        
                    ),
                    html.Div(
                        dbc.Button('Corregir', id='corregir-btn', color='primary'),
                        className="text-center mt-4 mb-4"
                    ),
                   
                   
                    
                    html.Div(id='output-text', className="mt-4")
                ],
            )
        )
    )
    return content

# Definir el callback para corregir el texto
@dash.callback(
    Output('output-text', 'children'),
    [Input('corregir-btn', 'n_clicks')],
    [Input('input-text', 'value')]
)
def corregir_texto(n_clicks, input_text):
    if n_clicks:
        # Utilizar  para corregir el texto
        text=check_text(input_text)
        # Devolver el texto corregido
        return html.Div([
            html.Div(
                html.H3("Texto corregido:"),
                className="text-center",    
            ),
            html.Div(
                dcc.Markdown(text),
                className="text-center",
            )
           
            
        ])

    # Si no se ha hecho clic en el botón, no mostrar ningún resultado
    return ''