import pyodbc
import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=..\Datasets\DW1.accdb;')

df = pd.read_sql_query("SELECT AñoCondena, SUM(Unidades) as TOTAL FROM hechos GROUP BY AñoCondena;",conn) 
fig=px.bar(df, x="AñoCondena", y="TOTAL")
print(df)
fig.show()

df2 = pd.read_sql_query("SELECT Unidades, Genero FROM hechos;",conn) 
fig2=px.pie(df2, values='Unidades', names='Genero', title= 'Condenas totales en hombres y mujeres del año 2013 al 2020')
print(df2)
fig2.show()

df3 = pd.read_sql_query("SELECT * FROM hechos;",conn)
print(df3)
app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("Variables:"),
    dcc.Dropdown(
        id='names', 
        value='Genero', 
        options=[{'value': x, 'label': x} 
                 for x in ['Genero', 'Nacionalidad', 'Edad', 'AñoCondena', 'CantidadDelitos']],
        clearable=False
    ),
    html.P("Cantidad de delitos cometidos:"),
    dcc.Dropdown(
        id='values', 
        value='Unidades', 
        options=[{'value': x, 'label': x} 
                 for x in ['Unidades']],
        clearable=False
    ),
    dcc.Graph(id="pie-chart"),
])

@app.callback(
    Output("pie-chart", "figure"), 
    [Input("names", "value"), 
     Input("values", "value")])
def generate_chart(names, values):
    fig3 = px.pie(df3, values=values, names=names)
    return fig3

app.run_server(debug=True)

'''
df3 = pd.read_sql_query("SELECT AñoCondena, SUM(Unidades) as TOTAL FROM hechos GROUP BY AñoCondena;",conn) 
fig3=px.bar(df, x="AñoCondena", y="TOTAL")
fig3.show()

df = pd.read_sql_query("SELECT AñoCondena, SUM(Unidades) as TOTAL FROM hechos GROUP BY AñoCondena;",conn) 
fig=px.bar(df, x="AñoCondena", y="TOTAL")
fig.show()

df = pd.read_sql_query("SELECT AñoCondena, SUM(Unidades) as TOTAL FROM hechos GROUP BY AñoCondena;",conn) 
fig=px.bar(df, x="AñoCondena", y="TOTAL")
fig.show()
'''