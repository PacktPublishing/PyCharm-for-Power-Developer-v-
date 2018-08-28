#  https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server
import pyodbc

server = 'den1.mssql5.gear.host'
db = 'testmenow'
usr = 'testmenow'
psword = 'TEST!!'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};'
                      'SERVER='+server+';DATABASE='+db+';UID='+usr+
                      ';PWD=' + psword)
c = cnxn.cursor()

c.execute('CREATE TABLE MySandwiches (meat TEXT, name TEXT, '
          'bread TEXT, my_charge INTEGER, my_cost REAL)')


menu = [
    ("Roast Beef", "Roasted B", "white", 10, 5.5),
    ("A", "Loaded Veggie", "wheat", 5, 2.5),
    ('B', "Hammy Lamby","white", 12, 7.5)
]
c.executemany('INSERT INTO MySandwiches(meat, name, bread, my_charge, '
              'my_cost) VALUES(?,?,?,?,?)', menu)

cnxn.commit()
cnxn.close()