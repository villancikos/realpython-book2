import sqlite3

with sqlite3.connect('newnum.db') as connection:
	c = connection.cursor()

	while True:

		users_answer = raw_input("""What would you like to do (enter the number):
		1. AVG numbers in table.
		2. MAX number in table.
		3. MIN number in table.
		4. SUM of numbers in table.
		Enter any other number if you want to exit.
		""")

		if users_answer in set(['1','2','3','4']):
			operation = {1: 'AVG', 2: 'MAX',3: 'MIN', 4: 'SUM'}[int(users_answer)]

			c.execute("SELECT {}(num) from numbers".format(operation))

			get = c.fetchone()

			print operation + " : %f" % get[0]

		else:
			print "Good bye"
			break
