import sqlite3
import pandas as pd

conn = sqlite3.connect("menu.db")
c = conn.cursor()

###################################
## Key Words
###################################

print(pd.read_sql_query("SELECT * FROM Sandwiches", conn))

print("-------")
c.execute('ALTER TABLE Sandwiches ADD in_stock int')
print(pd.read_sql_query("SELECT * FROM Sandwiches", conn))

print("-------")
c.execute('ALTER TABLE Sandwiches DROP COLUMN in_stock')
print(pd.read_sql_query("SELECT * FROM Sandwiches", conn))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
