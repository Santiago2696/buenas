import sys
import pyodbc
conn= pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\cuc\Documents\database1.accdb;")
cursor=conn.cursor()
cursor.execute("SELECT * FROM tabla1")
for row in cursor.fetchall():
    print(row)
cursor.close
conn.close