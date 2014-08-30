import sqlite3

with sqlite3.connect('cars.db') as connection:
	c = connection.cursor()
	cars = [('Ford', 'Malibu', 2010),
			('Ford', 'Mustang' , 2015),
			('Ford', 'GT', 2020),
			('Honda', 'Civic', 2010),
			('Honda', 'Accord', 2010)]
	
	c.executemany("INSERT INTO inventory VALUES(?,?,?)",cars)