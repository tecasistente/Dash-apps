import dash
from dash import html
import dash_bootstrap_components as dbc

# Initialize the Dash application
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True#App will display an error message in the user interface.


#server=app.server

# Define the layout for the actual page
layout = html.Div([
    dbc.NavbarSimple(  # Navbar that contains all the routes
        children=[
            dbc.NavItem(dbc.NavLink("Clima", href="/")),  # Main route
            #other routes of tha page
            dbc.NavItem(dbc.NavLink("Gramática", href="/gramatica")),
            dbc.NavItem(dbc.NavLink("Html", href="/html")),
            dbc.NavItem(dbc.NavLink("Boostrap", href="/boostrap")),
            dbc.NavItem(dbc.NavLink("Acerca de", href="/acercade")),
        ],
        brand="Aplicación en Dash",
        brand_href="/",
        color="dark",
        dark=True
    ),

    dash.page_container  # Container for the page content
])

# Set the overall application layout
app.layout = html.Div(
    layout,
    style={"backgroundColor": "#c0eaf0", "height": "100vh"}  # Set background color and height
)

if __name__ == '__main__':
    app.run_server(debug=True)  # Run the application in debug mode
