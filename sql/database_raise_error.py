# import CSV

#import csv library
import csv

import sqlite3

path = '/Users/villancikos/Google_Drive/Learning_Shit/Python/RealPython/book2/sql/book2-exercises/sql/employees.csv'

conn = sqlite3.connect("new.db")

cursor = conn.cursor()

try:
	cursor.execute("INSERT INTO populations VALUES ('New York','NY',8200000)")
	cursor.execute("INSERT INTO populations VALUES ('San Francisco','CA', 800000)")

	conn.commit()
except sqlite3.OperationalError as e:
	print "Whooops! Something went wrong.",e.args[0]

conn.close()