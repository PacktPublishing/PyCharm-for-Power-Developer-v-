import sqlite3

conn = sqlite3.connect("menu.db")
c = conn.cursor()

# CREATE TABLE Sandwiches (
#     meat TEXT,
#     name TEXT,
#     bread TEXT,
#     my_charge INTEGER,
#     my_cost REAL
# );
c.execute('CREATE TABLE Sandwiches (meat BLOB, name TEXT, bread TEXT, my_charge INTEGER, my_cost REAL)')


# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
