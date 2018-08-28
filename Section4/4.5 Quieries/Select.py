import sqlite3
import pandas as pd

conn = sqlite3.connect("menu.db")
c = conn.cursor()

print(pd.read_sql_query("SELECT * FROM Sandwiches", conn))
print("-------")
print(pd.read_sql_query("SELECT * FROM Sandwiches WHERE my_cost>5", conn))
print("-------")

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
