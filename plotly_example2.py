import pandas as pd
import plotly.express as px
import numpy as np

# Load the CSV file
# Replace 'player_data.csv' with your actual file name
df = pd.read_csv('https://raw.githubusercontent.com/peasant98/TheNBACSV/refs/heads/master/nbaNew.csv')

# Create new columns
# Calculate AVGPTS as PTS divided by G
df['AVGPTS'] = df['PTS'] / df['G']

# Calculate TRBAST as sum of TRB and AST
df['TRBAST'] = df['TRB'] + df['AST']

# Calculate AVGTA as TRBAST divided by G
df['AVGTA'] = df['TRBAST'] / df['G']

# Convert FG% column to float by removing '%' character if present
df['FG%'] = df['FG%'].astype(str)
df['FG%'] = df['FG%'].str.replace('%', '').astype(float) / 100

# Convert new columns to numeric, setting errors='coerce'
df['AVGPTS'] = pd.to_numeric(df['AVGPTS'], errors='coerce')
df['AVGTA'] = pd.to_numeric(df['AVGTA'], errors='coerce')
df['MP'] = pd.to_numeric(df['MP'], errors='coerce')

# Remove rows where MP is less than 15
df = df[df['MP'] >= 15]

# Remove rows where FG%, AVGPTS, or AVGTA is NaN
df = df.dropna(subset=['FG%', 'AVGPTS', 'AVGTA'])

# Keep only the required columns
df = df[['SeasonStart', 'PlayerName', 'FG%', 'AVGPTS', 'AVGTA']]

# Create an animated scatter plot with a slider for years
fig = px.scatter(
    df, 
    x='FG%', 
    y='AVGPTS',
    animation_frame='SeasonStart',
    hover_name='PlayerName',
    size='AVGPTS',
    color='AVGTA',
    color_continuous_scale='Viridis',
    range_x=[0, df['FG%'].max() * 1.1],
    range_y=[0, df['AVGPTS'].max() * 1.1],
    title='NBA Player Field Goal Percentage vs. Average Points per Game (1960-2022)',
    labels={
        'FG%': 'Field Goal Percentage', 
        'AVGPTS': 'Avg Points per Game',
        'AVGTA': 'Avg TRB+AST per Game'
    }
)

# Improve layout
fig.update_layout(
    xaxis_title='Field Goal Percentage',
    yaxis_title='Avg Points per Game Start',
    coloraxis_colorbar_title='Avg TRB+AST',
    height=700,
    width=1000,
    template='plotly_white'
)

# Format x-axis as percentage
fig.update_xaxes(tickformat='.1%')

# Add animation controls
fig.update_layout(
    updatemenus=[{
        'type': 'buttons',
        'showactive': False,
        'buttons': [
            {
                'label': 'Play',
                'method': 'animate',
                'args': [None, {'frame': {'duration': 500, 'redraw': True}, 'fromcurrent': True}]
            },
            {
                'label': 'Pause',
                'method': 'animate',
                'args': [[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate'}]
            }
        ],
        'direction': 'left',
        'pad': {'r': 10, 't': 10},
        'x': 0.1,
        'y': 0
    }],
    sliders=[{
        'steps': [
            {
                'method': 'animate',
                'label': str(year),
                'args': [[str(year)], {'frame': {'duration': 300, 'redraw': True}, 'mode': 'immediate'}]
            } for year in sorted(df['SeasonStart'].unique())
        ],
        'currentvalue': {'prefix': 'Year: ', 'visible': True},
        'len': 0.9,
        'x': 0.1,
        'y': 0,
        'pad': {'b': 10, 't': 50},
    }]
)

# Show the figure
fig.show()