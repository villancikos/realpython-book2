import sqlite3

with sqlite3.connect("movies.db") as connection:
  c = connection.cursor()

  movies = c.execute("SELECT * FROM new_movies")
  for movie in movies:
    print "Name: "+movie[0]
    print "Year: "+str(movie[1])
    print "Rating: "+movie[2]
    print "Release: "+str(movie[3])
    print "Runtime: "+str(movie[4])
    print "Critics Score: "+str(movie[5])
    print "People Score: "+str(movie[6])
    print "---------------------------------------------"
