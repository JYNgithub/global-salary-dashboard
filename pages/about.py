import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

dash.register_page(__name__, name="About",top_nav=True)

rgba1 = 'rgba(83, 253, 215)' # turqoise blue 

layout = html.Div([
    
    html.Div(style=dict(height='50px')),  # Empty div to create space above the container
    
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Img(src='assets/ab_source.png', style=dict(width='100%'))
            ], width=2, style=dict(padding='10px')),
            
            dbc.Col([
                html.P([html.B('Data Source')], style=dict(fontSize='25px', margin='0px')),
                html.P(['Data sourced from ', html.A('ai-jobs.net', href='https://ai-jobs.net/salaries/', target='_blank', style=dict(color=rgba1)),', ',
                    'Their goal is to help hire the best candidates and find the most attractive positions worldwide by providing open salary data for everyone.',
                    html.Br(), 'This dataset is published in the public domain under CC0.',
                    html.Br(),'Free to copy, modify, and distribute, even for commercial purposes without asking permission.'
                ], style=dict(
                    fontSize='16px'))
            ], 
                width=9, 
                style=dict(
                    padding='10px', 
                    marginLeft='20px', 
                    marginTop='23px'))
            
        ])
    ], fluid=True, style=dict(maxWidth='80%'), className='animate__animated animate__fadeInUp'),
    
    html.Div(style=dict(height='100px')),
    
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.P([html.B('Data Wrangling')], style=dict(fontSize='25px', margin='0px')),
                html.A('Click here to download', href='assets/eda.zip', target='_blank', style=dict(margin='0px', display='block', color=rgba1)),
                html.P(['The link above will download a zip file.'], style=dict(fontSize='16px', margin='0px'))
            ], 
                width=9, 
                style=dict(
                    padding='10px', 
                    marginLeft='20px', 
                    marginTop='23px', 
                    textAlign='right')),
            
            dbc.Col([
                html.Img(src='assets/ab_doc.png', style=dict(width='100%'))
            ], 
                width=2, 
                style=dict(
                    padding='10px'))
            
        ])
    ], fluid=True, style=dict(maxWidth='80%'),className='animate__animated animate__fadeInUp'),
    
    html.Div(style=dict(height='100px')),
    
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Img(src='assets/ab_limit.png', style=dict(width='100%'))
            ], 
                width=2, 
                style=dict(
                    padding='10px')),
            
            dbc.Col([
                html.P([html.B('Limitations')], style=dict(fontSize='25px', margin='0px')),
                html.P([
                    html.Ul([
                        html.Li('Data last updated on 20 June 2024.'),
                        html.Li('Data collected are mostly from the United States and may not provide an accurate representation on a global scale.'),
                        html.Li('Limited options for job titles.')
                    ])
                ], style=dict(fontSize='16px', margin='0px'))
            ], 
                width=9, 
                style=dict(
                    padding='10px', 
                    marginTop='40px'))
            
        ])
    ], fluid=True, style=dict(maxWidth='80%'),className='animate__animated animate__fadeInUp'),
    
    html.Div(style=dict(height='100px')),
    
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.P([html.B('Reach Out')], 
                       style=dict(
                           fontSize='25px', 
                           margin='0px')),
                html.P(['... or any feedback would be appreciated!'],
                       style = dict(
                           margin = '0px')),
                html.P(['LinkedIn: ', html.A('My LinkedIn Profile', href='https://www.linkedin.com/in/chong-jin-jye/', target='_blank', style=dict(color=rgba1)),
                        html.Br(),'Gmail: chongjinjye@gmail.com'
                        ], 
                       style=dict(
                           fontSize='16px', 
                           marginTop='20px'))
                ], 
                    width=9, 
                    style=dict(
                        padding='10px', 
                        marginLeft='20px',
                        textAlign = 'right')),
            
            dbc.Col([
                html.Img(src='assets/ab_contact.png', style=dict(width='100%'))
            ], width=2, style=dict(padding='10px'))
            
        ])
    ], fluid=True, style=dict(maxWidth='80%'),className='animate__animated animate__fadeInUp'),
    
    html.Div(style=dict(height='100px'))
])

