import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path


# Register the homepage
dash.register_page(__name__, path="/", name='Home', top_nav=True)

# Set up colour palettes
fill1 = '#53FDD7' # turqoise blue (83, 253, 215)
fill2 = '#87CEEB' # sky blue (135, 206, 235)
fill3 = '#00FFFF' # aqua blue (0, 255, 255)
fill4 = '#00BFFF' # deep sky blue (0, 191, 255)
rgba1 = 'rgba(83, 253, 215)' # turqoise blue 
rgba2 = 'rgba(135, 206, 235)' # sky blue 
rgba3 = 'rgba(0, 255, 255)' # aqua blue 
rgba4 = 'rgba(0, 191, 255)' # deep sky blue 
rgba5 = 'rgba(0, 51, 102, 1)' # dark blue

# Prepare data
mappath = Path(__file__).parent.parent/'data'/'mapdata.csv'
dff = pd.read_csv(mappath)
dfftext = dff.sort_values('percentage', ascending = False)
dfftext = dfftext[['country_name', 'percentage']].head(8)


# Build figure
fig = go.Figure(go.Choropleth(
    locations=dff['company_location'],  
    z=dff['percentage'],  
    text=dff['country_name'],  
    hovertemplate="%{z:.2f}% of data is from <b>%{text}</b><extra></extra>",  
    customdata=dff['country_name'],  
    colorscale='balance',  
    autocolorscale=False,  
    reversescale=True,  # Reverse color spectrum
    marker_line_color='darkgrey',  
    marker_line_width=1, 
))
fig.update_layout(
    title=dict(text='', font=dict(size=1)),
    margin=dict(l=30, r=30, t=10, b=10),
        template=dict(layout=dict(
            plot_bgcolor='#222222',
            paper_bgcolor='#222222',
            margin=dict(t=100)  
        )),
    geo=dict(
        projection_type='natural earth',
        bgcolor='#222222',  # Set background color inside the map
        showland=True,  # Show land masses
        landcolor='#222222',  # Set land color to match background
        showocean=True,  # Show ocean color
        oceancolor='#222222',  # Set ocean color to match background
        framecolor = 'white',
        framewidth = 0.5
    )
)
fig.update_traces(
    hoverlabel=dict(
        font=dict(size=18, color='black'),
        bgcolor='white'
    ),
    showscale = False
)
fig.add_annotation(
    text='Hover or drag to interact',
    xref='paper', yref='paper',
    x=0.5, y=0.009,  # Adjust x and y to position the annotation
    showarrow=False,
    font=dict(size=14, color='white', family='Century Gothic'),
)

# Define layout
layout = html.Div([
    
    html.Div(style=dict(height='50px')),  # Empty div to create space above the container
    
    dbc.Container(
        fluid=True, 
        children=[
            dbc.Row([
                dbc.Col([
                    html.H1([html.B("Global Data Science and Machine Learning Salary Dashboard")], 
                            style=dict(
                                paddingLeft='50px', 
                                paddingRight='5px',
                                paddingTop='50px',
                                fontSize = '42px')
                            ),  
                    
                    html.P([html.Br(), "Salary data are displayed in USD per year from 2020 to 2024.", html.Div(style=dict(height = '10px')),
                            f"Data available are {round(dfftext['percentage'].iloc[0], 2)}% from ", html.B(f"{dfftext['country_name'].iloc[0]}, "), 
                            f"{round(dfftext['percentage'].iloc[1], 2)}% from ", html.B(f"{dfftext['country_name'].iloc[1]}, "), html.Br(),
                            f"{round(dfftext['percentage'].iloc[2], 2)}% from ", html.B(f"{dfftext['country_name'].iloc[2]}, "), 
                            f"{round(dfftext['percentage'].iloc[3], 2)}% from ", html.B(f"{dfftext['country_name'].iloc[3]}, "), html.Br(),
                            "and others such as ", 
                            html.B(dfftext['country_name'].iloc[4]), ", ", 
                            html.B(dfftext['country_name'].iloc[5]), ", ", 
                            html.B(dfftext['country_name'].iloc[6]), ", ", 
                            html.B(dfftext['country_name'].iloc[7]), " etc."], 
                           
                           style=dict(
                               paddingLeft='50px', 
                               fontSize='18px')  
                           ),
                    
                    dbc.Button([html.B("Head to Dashboard >>>")], 
                               style=dict(
                                   marginLeft='150px', 
                                   marginTop='20px', 
                                   border='none',
                                   fontSize = '22px',
                                   backgroundColor = rgba5,
                                   color = 'white',
                                   width = '300px'), 
                               href="/dashboard", 
                               className="border rounded-pill",
                               size='lg')
                    ],
                        width=6,
                        className='pl-3',
                        style = dict(
                            paddingLeft='10px'
                            )
                ),  

                dbc.Col([
                    dcc.Graph(
                        figure=fig
                    )
                ], width=6),
            ])
    ],className='animate__animated animate__fadeInUp'),
    
    # footer
    dbc.Container(
        html.Div(
            ['Data sourced from ', html.A('ai-jobs.net', href='https://ai-jobs.net/salaries/', target='_blank', style={'color': 'white'}),'.'],
            className='footer',
            style=dict(
                fontSize='12px',
                flexShrink='0', 
                marginTop='auto',  
                color='white', 
                width = '100%',
                textAlign='center', 
                padding='8px'
            )
        ),
        fluid = True,
        style=dict(
            position='fixed', 
            bottom='0', 
            width='100%', 
            zIndex='999'
        )
    )
])

