from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv('pink_morsel_sales.csv')

fig = px.line(df, x='date', y='sales')
fig.update_layout(
    plot_bgcolor="#111",
    font_color="#2631ca",
    width=1400,
    height=650
)


app.layout=html.Div(
    style={
        "width":"full","height":"90vh","margin":"00px", 
        "font-family":"sans-serif","color":"#2631ca",
        "display":"flex","flex-direction":"column","align-items":"center",
        "justify-content":"center","gap":"10px", 
        "padding":"20px","background-color":"#111"},
    children=[
        html.H1(style={'textAlign': 'center',"font-family":"sans-serif","color":"#fff"},children='Pink Morsel Sales'),
        html.Div(style={'textAlign': 'center',"font-family":"sans-serif","color":"#fff"},children="Python Dash: A Web Application Framework"),
        dcc.Graph(style={'textAlign': 'center',"color":"#fff","background-color":"#111"}, id='pink-morsel-sales-graph', figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)