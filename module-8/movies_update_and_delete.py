#Jackie Scott 2/18/24 Module 8.2 Movies: Update & Deletes

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

def show_films(cursor, title):

    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' FROM film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    films = cursor.fetchall()

    print("\n -- {} --". format(title))

    for films in films:
         print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(films[0], films[1], films[2], films[3]))

show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

#inserting new record for 'film' table
#INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
#Values('Back to the Future', '1985', '116', 'Robert Zemeckis', '3', '2');

#update the film Alien to being a Horror film
#UPDATE film
#SET genre_id = 1
#WHERE film_name = 'Alien';
#SELECT * FROM film;

#delete the movie Gladiator
#DELETE FROM film WHERE film_name = 'Gladiator';