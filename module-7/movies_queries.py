#Jackie Scott 2/17/24 Module 7.2 Movies: Table Queries

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Frogg3r$2839",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)

cursor = db.cursor()

#query 1 studio 
studio_name = "Studio"
print("--DISPLAYING {} RECORDS--".format(studio_name))

cursor.execute("SELECT * FROM studio")
studio = cursor.fetchall()
for row in studio:
    print("Studio ID: {}\nStudio Name: {}\n".format(row[0], row[1]))
    
#query 2 genre 
genre_name = "Genre"
print("-- DISPLAYING {} RECORDS --".format(genre_name))

cursor.execute("SELECT * FROM genre")
genre = cursor.fetchall()
for row in genre:
    print("Genre ID: {}\nGenre Name: {}\n".format(row[0], row[1]))

#query 3 movies names for run time less than two hours
short_films = "Short Film"
print("-- DISPLAYING {} RECORDS --".format(short_films))

cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;")
film = cursor.fetchall()
for row in film:
    print("Film Name: {}\nRuntime: {}\n".format(row[0], row[1]))


#query 4 list of film names and directors grouped by director
directors = "Director"
print("-- DISPLAYING {} RECORDS in ORDER --".format(directors))

cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
order_director = cursor.fetchall()
for row in order_director:
    print("Film Name: {}\nDirector: {}\n".format(row[0], row[1]))
