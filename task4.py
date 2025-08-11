import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

#load data
df = pd.read_csv("pink_morsel_sales.csv")

#convert 'date' colomn to datetime object
df['date'] = pd.to_datetime(df['date'])

#aggregate data to get clean daily total data for sum sales for each day and region
df_agg = df.groupby(['date', 'region'], as_index=False)['sales'].sum()

#app init
app = dash.Dash(__name__)
server = app.server

#variables
COLORS = {
    'background':'#111111',
    'text': "#eaeaea",
    'chart_line': '#2631ca',
    'chart_grid': "#202020"
}

#app layout
app.layout = html.Div(style = {'backgroundColor': COLORS['background'], 'padding':'20px'}, children=[

    html.H1(
        children='Pink Morsel Sales Analysis',
        style={
            'textAlign' : 'center',
            'color': COLORS['text'],
            'fontFamily': 'sans-serif'
        }
    ),

    html.Div(
        children='Interactive dashboard to explore sales data by region',
        style={
            'textAlign':'center',
            'color': COLORS['text'],
            'fontFamily': 'sans-serif',
            'marginBottom': '20px'
        }
    ),

    dcc.RadioItems(
        id='region-filter',
        options=[
            {'label':'All Regions', 'value':'all'},
            {'label':'East', 'value':'east'},
            {'label':'West', 'value':'west'},
            {'label':'North', 'value':'north'},
            {'label':'South', 'value':'south'}
        ],
        value='all',
        labelStyle ={'display':'inline-block', 'marginRight':'20px'},
        style={
            'textAlign': 'center',
            'color': COLORS['text'],
            'fontFamily': ' sans-serif',
            'marginBottom': '30px'
        }
    ),

    dcc.Graph(
        id='sales-line-chart'
    )
])

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)

def update_graph(selected_region):
    if selected_region == 'all':
        # For 'all', sum up sales per day across all regions
        filtered_df = df_agg.groupby('date')['sales'].sum().reset_index()
        title = 'Total Pink Morsel Sales Over Time (All Regions)'
    else:
        #for selected region
        filtered_df = df_agg[df_agg['region'] == selected_region]
        title = f'Pink Morsel Sales Over Time in {selected_region}'

    fig = px.line(filtered_df, x='date', y='sales', title=title, labels={'sales': 'Total Sales ($)', 'date': 'Date'})

    fig.update_layout(
        plot_bgcolor=COLORS['background'],
        paper_bgcolor=COLORS['background'],
        font_color=COLORS['text'],
        xaxis_gridcolor=COLORS['chart_grid'],
        yaxis_gridcolor=COLORS['chart_grid'], 
        height=650,
        transition_duration=500
    )

    fig.update_traces(line_color=COLORS['chart_line'], line_width=2)

    return fig

#run
if __name__ == '__main__':
    app.run(debug=True)
