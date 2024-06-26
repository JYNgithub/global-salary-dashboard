import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from pathlib import Path

dash.register_page(__name__, name="Dashboard",top_nav=True)

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

# Line
def return_fig1(input):
    datapath = Path(__file__).parent.parent/'data'/'clean.csv'
    df = pd.read_csv(datapath)
    selected_field = input
    dff = df[df['career'] == selected_field].copy()
    dff = dff.groupby('year')['salary'].median().reset_index()
    
    # for text
    first_year = dff.loc[dff.index[0], 'year']
    final_year = dff.loc[dff.index[-1], 'year']
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dff['year'],
        y=dff['salary'],
        mode='lines+markers',
        name='Median Salary',
        line=dict(
            color = fill3,  # Set line colour
            width = 7      
        ),
        marker=dict(
            color = fill3, # Also set marker colour
            size = 20
        ),
        hovertemplate='<b>Year:</b> %{x}<br><b>Median Salary:</b> %{y}'

    ))
    fig.update_layout(
        title=dict(
            text=f'<b>Salary by Year, {first_year} - {final_year}</b>',
            x=0.5,  
            y=0.95,  
            xanchor='center',  
            yanchor='top',  
            font=dict(
                family='Century Gothic',
                size=36,
                color='white'
            )
        ),
        height=550,
        # Set bg 
        template=dict(layout=dict(
            plot_bgcolor='#1C1C1C',
            paper_bgcolor='#1C1C1C',
            margin=dict(t=150)  
        )),
        margin=dict(t=100),
        xaxis=dict(
            title=dict(
                text = 'Year',
                font=dict(
                    size=24,  
                    color='white',
                    family='Century Gothic'
                )
            ),
            showgrid=False,      
            zeroline=True,       
            zerolinecolor='white',
            zerolinewidth=1,    
            linecolor='white',
            tickfont=dict(size=22,
                          color = 'white',
                          family='Century Gothic'),
            dtick = 1
        ),
        yaxis=dict(
            title=dict(
                font=dict(
                    size=20,  
                    color='white',
                    family='Century Gothic' 
            )),
            showgrid=True,
            gridcolor='rgba(255, 255, 255, 0.3)',  
            gridwidth=0.3,                        
            zeroline=True,      
            zerolinecolor='white',
            zerolinewidth=1,     
            linecolor='white',
            tickfont=dict(size=22,
                          color = 'white',
                          family='Century Gothic')
            
        ),
        hoverlabel=dict(
            bgcolor='white',  
            font=dict(color='black',size = 18)  
        )
    )
    # Calculate percentage difference between the first and last years
    first_salary = dff.loc[dff.index[0], 'salary']
    last_salary = dff.loc[dff.index[-1], 'salary']
    percentage_diff = ((last_salary - first_salary) / first_salary) * 100
    # Dynamic annotation
    if (percentage_diff > 0):
        acolor = 'green'
        atext = f'<b>▲ {int(percentage_diff)}% <br>since {first_year}</b>'
    elif (percentage_diff < 0):
        acolor = 'red'
        atext = f'<b>▼ {int(percentage_diff)}% <br>since {first_year}</b>'
    else:
        acolor = 'white'
        atext = f'<b>No change<br>since {first_year}</b>'

    # Add annotation beside the last marker
    fig.add_annotation(
    x=dff['year'].iloc[-1],
    y=dff['salary'].iloc[-1],
    text=atext,
    showarrow=False,
    font=dict(color=acolor, size=18, family='Century Gothic'),
    align='center',
    xshift=60  # Shift the annotation upwards
    )
    return fig
    
# Salary histogram 
def return_fig2(input):
    datapath = Path(__file__).parent.parent/'data'/'clean.csv'
    df = pd.read_csv(datapath)
    selected_field = input
    dfda = df[(df['career'] == selected_field)]
    median_salary = dfda['salary'].median()
    xaxisrange = [0,350000]
    fig = go.Figure(
        data=[go.Histogram(
            x=dfda['salary'],
            nbinsx=100,
            marker=dict(
                color=fill1,  # Fill color
                line=dict(
                    color='black',  # Border color
                    width=1  
                )
            ),
            # Set hover info
            hovertemplate='<b>Salary Range:</b> %{x}<br><b>Frequency: </b>%{y}<extra></extra>',  
            hoverlabel=dict(
                bgcolor='white',
                font=dict(size=18, color='black') 
            )
        )]
    )
    fig.add_shape(     # Add a vertical line at the median salary
        type='line',
        x0=median_salary,
        y0=0,
        x1=median_salary,
        y1=1,
        xref='x',
        yref='paper',
        line=dict(color='red', width=2, dash='dash')
    )
    fig.update_layout(
        title=dict(
            text=f'<b>Salary Distribution</b>',
            x=0.5,  # Center the title horizontally
            y=0.95,  # Adjust vertical position 
            xanchor='center',  # Anchor point for x coordinate
            yanchor='top',  # Anchor point for y coordinate
            font=dict(
                size=40,  
                color='white',  
                family='Century Gothic' 
            )
        ),
        xaxis=dict(
            range=xaxisrange,
            showgrid=False,  # Remove x-axis grid lines
            title='Salary',  
            titlefont=dict(
                size=20,  
                color='white',
                family = 'Century Gothic'
            ),
            tickfont=dict(
                size=20,  
                color='white' ,
                family = 'Century Gothic'
            )
        ),
        yaxis=dict(
            showgrid=False,  # Remove y-axis grid lines
            title='', # Empty string to remove y-axis title
            showticklabels=False # Hide tick labels on y-axis
            ), 
        height=550,
        shapes=[dict(
            type='line',
            x0=median_salary,
            x1=median_salary,
            y0=0,
            y1=1,
            xref='x',
            yref='paper',
            line=dict(
                color="blue",
                width=2,
                dash="dash",
            ),
        )],
        annotations=[dict(
            x=median_salary,
            y=1.10,
            xref='x',
            yref='paper',
            text=f'<i>Median Salary of {selected_field}s: {int(median_salary):,} USD </i>',
            showarrow=False,
            arrowhead=2,
            ax=0,
            ay=-20,
            font=dict(
                size=23,  
                color='white' ,
                family = 'Century Gothic' 
            )
        )],
        # Set bg 
        template=dict(layout=dict(
            plot_bgcolor='#1C1C1C',
            paper_bgcolor='#1C1C1C',
            margin=dict(t=150)  
        )),
        )
    return fig

# Experience boxplot
def return_fig3(input):
    datapath = Path(__file__).parent.parent/'data'/'clean.csv'
    df = pd.read_csv(datapath)
    selected_field = input
    dff = df[(df['career'] == selected_field)]
    # Remove extreme outliers
    Q1 = dff['salary'].quantile(0.25)
    Q3 = dff['salary'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    dff = dff[(dff['salary'] >= lower_bound) & (dff['salary'] <= upper_bound)]
    # Create lists of data for each boxplot
    dff_entry = dff[dff['experience_level'] == 'Entry-level']
    salaries_entry= dff_entry['salary'].tolist()
    dff_inter = dff[dff['experience_level'] == 'Intermediate']
    salaries_inter = dff_inter['salary'].tolist()
    dff_senior = dff[dff['experience_level'] == 'Senior']
    salaries_senior = dff_senior['salary'].tolist()
    dff_direct = dff[dff['experience_level'] == 'Director']
    salaries_direct = dff_direct['salary'].tolist()
    # For annotations of median
    median_entry = np.median(salaries_entry)
    median_inter = np.median(salaries_inter)
    median_senior = np.median(salaries_senior)
    median_direct = np.median(salaries_direct)
    fig = go.Figure()
    fig.add_trace(go.Box(
        y=salaries_entry,
        name="<b>Entry-level</b>",
        jitter=0.4,
        pointpos=-1.8,
        boxpoints='all',  
        marker=dict(
            color=fill1, 
            opacity=0.5,
            line=dict(
                color='black',  
                width=1  
            )
            ),
        fillcolor='rgba(83, 253, 215 ,0.7)',
        line_color='white',
        line_width = 1.5,
        width = 0.2
    ))
    fig.add_trace(go.Box(
        y=salaries_inter,
        name="<b>Intermediate</b>",
        jitter=0.4,
        pointpos=-1.8,
        boxpoints='all',  
        marker=dict(
            color=fill2, 
            opacity=0.5,
            line=dict(
                color='black', 
                width=1 
            )
            ),
        fillcolor='rgba(135, 206, 235,0.7)',
        line_color='white',
        line_width = 1.5,
        width = 0.2
    ))
    fig.add_trace(go.Box(
        y=salaries_senior,
        name="<b>Senior</b>",
        jitter=0.4,
        pointpos=-1.8,
        boxpoints='all',  
        marker=dict(
            color=fill3, 
            opacity=0.5,
            line=dict(
                color='black', 
                width=1 
            )
            ),
        fillcolor='rgba(0, 255, 255,0.7)',
        line_color='white',
        line_width = 1.5,
        width = 0.2
    ))
    fig.add_trace(go.Box(
        y=salaries_direct,
        name="<b>Director</b>",
        jitter=0.4,
        pointpos=-1.8,
        boxpoints='all', 
        marker=dict(
            color=fill4, 
            opacity=0.5,
            line=dict(
                color='black',  
                width=1  #
            )
            ),
        fillcolor='rgba(0, 191, 255,0.7)',
        line_color='white',
        line_width = 1.5,
        width = 0.2
    ))
    fig.update_layout(
        title=dict(
            text='<b>Salary by Experience Level</b>',
            x=0.5,  # Center the title horizontally
            y=0.95,  # Adjust vertical position 
            xanchor='center',  # Anchor point for x coordinate
            yanchor='top',  # Anchor point for y coordinate
            font=dict(
                size=40,
                color='white',
                family='Century Gothic'
            )
        ),
        yaxis_title='',
        height=550,
        showlegend=False,
        # Set bg 
        template=dict(layout=dict(
            plot_bgcolor='#1C1C1C',
            paper_bgcolor='#1C1C1C',
            margin=dict(t=100)  
        )),
        yaxis=dict(
            gridcolor='grey',
            gridwidth=0.001,
            zeroline=False,
            tickfont=dict(
                size=18,  # Adjust font size of y-axis ticks
                color='white',
                family='Century Gothic'
            ),
            title=dict(
                font=dict(
                    size=20,  # Adjust font size of y-axis title
                    color='white',
                    family='Century Gothic'
                )
            )
        ),
        xaxis=dict(
            tickfont=dict(
                size=22,  # Adjust font size of x-axis ticks
                color='white',
                family='Century Gothic'
            ),
            title=dict(
                font=dict(
                    size=18,  # Adjust font size of x-axis title
                    color='white',
                    family='Century Gothic'
                )
            )
        ),
        hoverlabel=dict(
            bgcolor='white',  
            font=dict(color='black',size = 18)  
        )
        
    )
    fig.add_annotation(
        x=0.28,  # adjust positition for label
        y=median_entry-7000,
        text=f'Median salary:<br> <i>{int(median_entry):,} USD</i>',
        showarrow=False,
        xanchor='center',
        yanchor='bottom',
        font=dict(color='white', 
                size=14,
                family='Century Gothic')
    )
    fig.add_annotation(
        x=1.28,  # adjust positition for label
        y=median_inter-6000,
        text=f'Median salary:<br> <i>{int(median_inter):,} USD</i>',
        showarrow=False,
        xanchor='center',
        yanchor='bottom',
        font=dict(color='white', 
                size=14,
                family='Century Gothic')
    )
    fig.add_annotation(
        x=2.28,  # adjust positition for label
        y=median_senior-7000,
        text=f'Median salary:<br> <i>{int(median_senior):,} USD</i>',
        showarrow=False,
        xanchor='center',
        yanchor='bottom',
        font=dict(color='white', 
                size=14,
                family='Century Gothic')
    )
    fig.add_annotation(
        x=3.28,  # adjust positition for label
        y=median_direct-7000,
        text=f'Median salary:<br> <i>{int(median_direct):,} USD</i>',
        showarrow=False,
        xanchor='center',
        yanchor='bottom',
        font=dict(color='white', 
                size=14,
                family='Century Gothic')
    )
    return fig

# Tree map
def return_fig4(input):
    datapath = Path(__file__).parent.parent/'data'/'clean.csv'
    df = pd.read_csv(datapath)
    selected_field = input
    dff = df[df['career'] == selected_field].copy()

    # Aggregating the data to get the percentage of count and median salary for each company size
    dff = dff.groupby('company_size').agg(
        count=('salary', 'size'),  # Count of records
        median_salary=('salary', 'median')  # Median salary
    ).reset_index()
    total_count = dff['count'].sum()
    dff['percentage'] = (dff['count'] / total_count) * 100

    # Label text inside treemap
    text_labels = dff.apply(lambda row: f"<b>{row['percentage']:.1f}% are in <br>{row['company_size'] } <br>companies</b><br>Median Salary: {row['median_salary']:,.0f} USD", axis=1)

    fig = go.Figure(go.Treemap(
        labels=dff['company_size'],
        parents=[""] * len(dff),  # No parents since all items are at the top level
        values=dff['median_salary'],
        hoverinfo='none',
        hoverlabel=dict(
            bgcolor='white',  # White background
            font=dict(size=18, color='black')  # Larger text size, black color, Century Gothic font
        ),
        text=text_labels,  
        textinfo="text",  
        textfont=dict(size=1, color='black',family='Century Gothic'),  
        insidetextfont=dict(size=20, color='black',family='Century Gothic'),  
        marker=dict(
            colors=dff['percentage'],  
            colorscale='Tealgrn', 
            showscale=True,  
            colorbar=dict(
                title=dict(text='Propotion', 
                        font=dict(size=18, 
                                    color='white',
                                    family='Century Gothic')),  
                tickfont=dict(size=16, 
                            color='white',
                            family='Century Gothic'),
                x=1.03 
            )  
        ),
        tiling=dict(pad=2)  
    ))
    fig.update_layout(
        title=dict(
            text=f'<b>Median Salary and Proportion by Company Size</b>',
            x=0.5,  
            y=0.93,  
            xanchor='center',  
            yanchor='top',  
            font=dict(
                size=30,
                color='white',
                family='Century Gothic'
            )
        ),
        # Set bg 
        template=dict(layout=dict(
            plot_bgcolor='#1C1C1C',
            paper_bgcolor='#1C1C1C',
            margin=dict(t=100)  
        )),
        height=550,
        margin=dict(t=100, l=25, r=25, b=25)  
    )
    return fig

# Remote piechart
def return_fig5(input):
    datapath = Path(__file__).parent.parent/'data'/'clean.csv'
    df = pd.read_csv(datapath)
    selected_field = input
    # Prepare data 
    dff = df[df['career'] == selected_field].copy()
    dff['remote_status'] = dff['remote_status'].map({0: 'On-site', 50: 'Hybrid', 100: 'Remote'})
    dff = dff['remote_status'].value_counts().reset_index()
    dff.columns = ['remote_status', 'count']
    total_count = dff['count'].sum()
    dff['percent'] = (dff['count'] / total_count) * 100
    dff = dff.drop(columns=['count'])
    # Build the fig
    fig = go.Figure(
        data=[go.Pie(labels=dff['remote_status'], 
                    values=dff['percent'],
                    insidetextorientation='horizontal',  
                    hovertemplate='<b>Remote Status:</b> %{label}<br><b>Percentage:</b> %{percent}<extra></extra>',
                    showlegend = False,
                    marker = dict(
                        colors = [fill4, fill3, fill2],
                        line=dict(
                            color='black',  # Border color
                            width=0.8  # Border width
                )
                    ) 
                    )])
    fig.update_traces(
        textposition='outside',  # To place labels outside of the pie chart
        textfont=dict(size=20, color='white')  
    )
    fig.update_layout(
        title=dict(
            text='<b>Percentage by Remote Work Status</b>',
            x=0.5,  # Center the title horizontally
            y=0.93,  # Adjust vertical position 
            xanchor='center',  # Anchor point for x coordinate
            yanchor='top',  # Anchor point for y coordinate
            font=dict(
                size=30,
                color='white',
                family='Century Gothic'
            )
        ),
        hoverlabel=dict(
            bgcolor='white',
            font=dict(size=18, 
                    color='black',
                    family = 'Arial')
        ),
        # Set bg 
        template=dict(layout=dict(
            plot_bgcolor='#1C1C1C',
            paper_bgcolor='#1C1C1C',
            margin=dict(t=100)  
        )),
        height = 550
    )
    fig.update_traces(
        textinfo='label+percent',  # Include both label and percent
        hoverinfo='text',  # Show hover info based on text template
        texttemplate='<b>%{label} </b><br> <i>%{percent:.1%}</i>',  
        textfont=dict(
            family='Century Gothic',  
            size=22,
            color='white'
        )
    )
    return fig


layout = html.Div([
    
    html.Div(style=dict(height='20px')),  

    dbc.Container([
        html.H3(html.B("Select your Job Title"), style=dict(fontSize='20px')),
        
        dcc.Dropdown(
            id='dbdropdown',
            options=[
                {'label': 'Data Scientist', 'value': 'Data Scientist'},
                {'label': 'Data Engineer', 'value': 'Data Engineer'},
                {'label': 'Data Analyst', 'value': 'Data Analyst'},
                {'label': 'Machine Learning Engineer', 'value': 'Machine Learning Engineer'},
                {'label': 'AI Engineer', 'value': 'AI Engineer'},
                {'label': 'Business Intelligence Analyst', 'value': 'Business Intelligence Analyst'}
            ],
            value='Data Scientist',  
            clearable=False,  
            style=dict(
                width='50%', 
                color='black'
            )  
        )
    ]),

    html.Div(children = 'Hover to learn more.',
             style=dict(
                 height='20px',
                 fontSize = '14px',
                 marginLeft = '100px')),

    dbc.Container([
        dbc.Row([
            dcc.Graph(
                id='fig1',
                figure={},
                style = dict(
                    marginTop = '10px')
                )
            ])
    ],fluid = True, style = dict(maxWidth = '90%')),
    
    html.Div(style=dict(height='30px')),  
    
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id='fig2',
                    figure={},
                    style=dict(
                        height='550px')  
                )
            ])
        ])
    ],fluid = True, style = dict(maxWidth = '90%')),
    
    html.Div(style=dict(height='30px')), 

    dbc.Container([
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id='fig3',
                    figure={},
                    style=dict(
                        height='550px')  
                )
            ])
        ])
    ],fluid = True, style = dict(maxWidth = '90%')),
    
    html.Div(style=dict(height='30px')), 

    dbc.Container([
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id='fig4',
                    figure={},
                    style = dict(height='550px')
                )
            ], width = 7),
            dbc.Col([
                dcc.Graph(
                    id='fig5',
                    figure={},
                    style = dict(height='550px')
                )
            ], width = 5)
        ])
    ],fluid = True, style = dict(maxWidth = '90%')),
    
    html.Div(style=dict(height='60px')),
    
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
            bottom='0', 
            width='100%', 
            zIndex='999'
        )
    )
])

# Callback to update selected role display
@callback(
    Output('fig1', 'figure'),
    Output('fig2', 'figure'),
    Output('fig3', 'figure'),
    Output('fig4', 'figure'),
    Output('fig5', 'figure'),
    Input('dbdropdown', 'value')
)
def update_selected_role(input):
    fig_1 = return_fig2(input)
    fig_2 = return_fig1(input)
    fig_3 = return_fig3(input)
    fig_4 = return_fig4(input)
    fig_5 = return_fig5(input)
    return fig_1, fig_2, fig_3, fig_4, fig_5

