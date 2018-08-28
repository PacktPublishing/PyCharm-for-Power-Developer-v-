import sqlite3
import pandas as pd

conn = sqlite3.connect("menu.db")
c = conn.cursor()

###################################
## Key Words
###################################

print(pd.read_sql_query("SELECT * FROM Sandwiches", conn))

print("-------")
c.execute('UPDATE Sandwiches SET name="Veggie Explosion" WHERE name="Loaded Veggie"')
print(pd.read_sql_query("SELECT * FROM Sandwiches", conn))


# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
