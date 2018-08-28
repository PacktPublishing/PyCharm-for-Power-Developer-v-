import sqlite3
import pandas as pd

conn = sqlite3.connect("menu.db")
c = conn.cursor()

print(pd.read_sql_query("SELECT * FROM Sandwiches", conn))
print("-------")
print(pd.read_sql_query("SELECT name, my_cost FROM Sandwiches WHERE my_cost>5", conn))
print("-------")

x = pd.read_sql_query("SELECT name, my_cost FROM Sandwiches WHERE my_cost>5", conn)
print(x['name'])
print('-')
print(x['my_cost'][0])


# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
