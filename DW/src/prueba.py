import pyodbc
import pandas as pd
import plotly.express as px 

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=..\Datasets\DW1.accdb;')

df = pd.read_sql_query("SELECT AñoCondena, SUM(Unidades) as TOTAL FROM hechos GROUP BY AñoCondena;",conn) 
fig=px.bar(df, x="AñoCondena", y="TOTAL")
fig.show()

df2 = pd.read_sql_query("SELECT Unidades, Genero FROM hechos;",conn) 
fig2=px.pie(df2, values='Unidades', names='Genero', title= 'Condenas totales en hombres y mujeres del año 2013 al 2020')
fig2.show()

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