import sqlite3
import pandas as pd

menu = [
    ("Roast Beef", "Roasted B", "white", 10, 5.5),
    ("A", "Loaded Veggie", "wheat", 5, 2.5),
    ('B', "Hammy Lamby","white", 12, 7.5)
]


conn = sqlite3.connect("menu.db")
c = conn.cursor()

# INSERT INTO Sandwiches
# VALUES(
#     'Roast Beef',
#     'Roasted B',
#     'white,
#     10,
#     5.5
# ); etc.

c.executemany('INSERT INTO Sandwiches VALUES(?,?,?,?,?)', menu)


print(pd.read_sql_query("SELECT * FROM Sandwiches", conn))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
