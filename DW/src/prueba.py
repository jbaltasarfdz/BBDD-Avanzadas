import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*mdb, *.accdb)};DBQ=C:\DW.accdb;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM Hechos: Cantidad delincuentes')

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()