import pyodbc
import pandas as pd

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=..\Datasets\DW1.accdb;')
cursor = conn.cursor()
cursor.execute('SELECT * FROM hechos')
   
for row in cursor.fetchall():
    print (row)