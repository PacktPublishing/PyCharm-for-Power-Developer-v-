#  https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server
import pyodbc
import pandas as pd

server = 'den1.mssql5.gear.host'
db = 'testmenow'
usr = 'testmenow'
psword = 'TEST!!'


cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';'
                                                                              'DATABASE='+db+';UID='+usr+';PWD=' +  psword)
c = cnxn.cursor()

print(pd.read_sql_query("SELECT * FROM MySandwiches", cnxn))

cnxn.close()