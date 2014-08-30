# compact insert
import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	c.execute("INSERT INTO population VALUES ('Torreon', 'COAH', 499000)")
	c.execute("INSERT INTO population VALUES ('Durango', 'DGO', 301000)")
	