# GET data from Rotten Tomatoes, parse and write to database

import json, requests, sqlite3

API_KEY = 'm5549a8w6d7z9w7d4yugpezf'
url = requests.get("http://api.rottentomatoes.com/api/public/v1.0/"+
                   "lists/movies/in_theaters.json?apikey={}".format(API_KEY))

# convert data from feed to binary
binary = url.content
#print "This is binary\n"
#print binary

# decode the json feed
output = json.loads(binary)
#print "\nthis is output\n"
#print output

# grab the list of movies
movies = output["movies"]

with sqlite3.connect("movies.db") as connection:
    c = connection.cursor()

    # iterate through each movie and write to the database
    for movie in movies:
        c.execute("INSERT INTO new_movies VALUES (?,?,?,?,?,?,?)",
                  (movie["title"], movie["year"],
                   movie["mpaa_rating"],
                   movie["release_dates"]["theater"],
                   movie["runtime"], movie["ratings"]["critics_score"],
                   movie["ratings"]["audience_score"]))
    # retrieve data
    c.execute("SELECT * FROM new_movies ORDER BY title ASC")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        print "title "+str(r[0]), r[1], r[2], r[4], r[5], r[6]


