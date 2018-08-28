import sqlite3

conn = sqlite3.connect("menu.db")
c = conn.cursor()

c.execute('CREATE TABLE Sandwiches (meat BLOB, name TEXT, bread TEXT, my_charge INTEGER, my_cost REAL)')

menu = [
    ("Roast Beef", "Roasted B", "white", 10, 5.5),
    ("A", "Loaded Veggie", "wheat", 5, 2.5),
    ('B', "Hammy Lamby","white", 12, 7.5)
]

c.executemany('INSERT INTO Sandwiches VALUES(?,?,?,?,?)', menu)


# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
