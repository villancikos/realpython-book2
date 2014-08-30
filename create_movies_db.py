# Create a SQLite3 database and table
import sqlite3

with sqlite3.connect("movies.db") as connection:
  c = connection.cursor()

  # create table
  c.execute(""" CREATE TABLE new_movies
            (title TEXT, year INT, rating TEXT,
             release TEXT, runtime INT, critics_review INT,
             audience_review INT)""")


