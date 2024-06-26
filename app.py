import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.DARKLY, 'https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css'],
)
server = app.server

# Set up colour palettes
fill1 = 'rgba(83, 253, 215)' # turqoise blue 
fill2 = 'rgba(135, 206, 235)' # sky blue 
fill3 = 'rgba(0, 255, 255)' # aqua blue 
fill4 = 'rgba(0, 191, 255)' # deep sky blue 
fill5 = 'rgba(0, 51, 102, 1)' # dark blue

page_sequence = ["Home", "Dashboard", "About"]

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand("", href="#"),
            dbc.Nav(
                [
                    dbc.NavLink(page["name"], href=page["path"], className="ml-2")
                    for page_name in page_sequence
                    for page in dash.page_registry.values()
                    if page["name"] == page_name and page.get("top_nav")
                ],
                navbar=True,
                className="ml-auto",  # Align nav links to the right
            ),
        ],
        fluid=True
    ),
    className="ml-3",
    color=fill5,
    dark=True,
    style=dict(
        backgroundColor='rgba(0, 51, 102, 1)',  
        color='white',                         
        fontFamily='Century Gothic',
        fontSize='22px'
    ),
)



# Layout 
app.layout = dbc.Container(
    [navbar, dash.page_container],
    fluid=True,
)


if __name__ == "__main__":
    app.run_server(debug=True)
