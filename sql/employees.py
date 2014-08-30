# import CSV

#import csv library
import csv

import sqlite3

path = '/Users/villancikos/Google_Drive/Learning_Shit/Python/RealPython/book2/sql/book2-exercises/sql/employees.csv'
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	#open csv and assign to variable
	employees = csv.reader(open(path,"rU"))

	#create table employees
	c.execute("CREATE TABLE employees(firstname,lastname)")

	#insert data into table
	c.executemany("INSERT INTO employees(firstname, lastname) values (?,?)", employees)
	