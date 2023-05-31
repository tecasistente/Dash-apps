from PIL import Image
import dash
import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc


dash.register_page(__name__,name="Imagen", path="/imagen")

def layout():

    content=dbc.Container(
        [
            html.H1("Carga y descarga de imágenes optimizadas", className="mt-4 mb-4"),
            dcc.Upload(
                id='upload-image',
                children=html.Div([
                    'Arrastra y suelta o ',
                    html.A('selecciona una imagen')
                ]),
                className="upload-area",
                multiple=False
            ),
            html.Div(id='output-image'),
            html.A(
                html.Button('Descargar imagen optimizada', className="btn btn-primary mt-3"),
                id='download-link',
                download='imagen_optimizada.jpg',
                href='',
                target='_blank',
                style={'display': 'none'}
            )
        ],
        className="main-container",
    )
    return content


@dash.callback(
    Output('output-image', 'children'),
    Output('download-link', 'href'),
    Input('upload-image', 'contents'),
    Input('upload-image', 'filename')
)
def update_image(contents, filename):
    if contents is not None:
        # Optimizar la imagen cargada
        optimized_image = optimize_image(contents, filename)

        return html.Img(src='data:image/jpeg;base64,{}'.format(optimized_image)), 'data:image/jpeg;base64,{}'.format(optimized_image)

    return '', ''

