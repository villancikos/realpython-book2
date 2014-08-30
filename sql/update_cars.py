import sqlite3

with sqlite3.connect('cars.db') as connection:
	c = connection.cursor()

	c.execute("UPDATE inventory set quantity = 191391 WHERE model = 'Malibu'")
	c.execute("UPDATE inventory set quantity = 342323 WHERE model = 'GT'")

	c.execute("SELECT * from inventory")
	cars = c.fetchall()

	for car in cars:
		print car[0],car[1],car[2]

	print "\nNOW just FORD\n"

	c.execute("SELECT * from inventory where Make = 'Ford'")
	cars = c.fetchall()
	for car in cars:
		print car[0],car[1]