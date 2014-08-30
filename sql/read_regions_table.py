import sqlite3

with sqlite3.connect('new.db') as connection:
	c = connection.cursor()
reapython 
	c.execute("SELECT * FROM regions ORDER BY region ASC")

	rows = c.fetchall()

	for r in rows:
		print r[0],r[1]