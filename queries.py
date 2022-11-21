"""
Your database code for Task 1 goes here.
"""

import sqlite3

from pydantic import create_model_from_namedtuple

def get_actors():
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM actor;")
        results = cursor.fetchall()
        print(results)
        return results

# TODO: Add more functions below. 

##### START HERE -> 20 "def" created, but I still have to do WHERE/LIMIT/DELETE/UPDATE/INSERT INTO/JOIN and other commands as requested.

def get_cities():
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT city FROM city;")
        results = cursor.fetchall()
        # print(results)
        cities = []
        for city in results:
            cities.append(city[0])
        return cities

def get_rental_rate():
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT rental_rate, film_id, title FROM film ORDER BY rental_rate ASC;")
        results = cursor.fetchall()
        print(results)
        return results

def get_cheap_rental_rate():
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT rental_rate, film_id, title FROM film WHERE rental_rate like '%0.99%';")
        results = cursor.fetchall()
        print(results)
        return results

def get_pg13_rating():
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT rating, title FROM film WHERE rating like '%PG-13%';")
        results = cursor.fetchall()
        print(results)
        return results

def get_limited_list():
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT length, film_id, title FROM film LIMIT 9,16;")
        results = cursor.fetchall()
        print(results)
        return results

def get_category_id():
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT film_id, category_id FROM film_category JOIN category USING (category_id)")
        results = cursor.fetchall()
        categories = []
        for category in results:
            categories.append(category[1])
        return categories

def get_repeated_actor_list():
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT actor_id, first_name, last_name FROM actor INNER JOIN film_actor USING (actor_id);")
        results = cursor.fetchall()
        main_counter = []
        for repeated_list in results:
            main_counter.append(repeated_list[0])
        return main_counter

def address_list():
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT address, city_id, country_id FROM address JOIN city USING (city_id);")
        results = cursor.fetchall()
        add_list = []
        for city_id in results:
            add_list.append(city_id[0])
        return add_list

def get_film_titles():
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM film_text;")
        results = cursor.fetchall()
        films = []
        for film in results:
            films.append(film[0])
        return films

def get_staff_email():
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM staff;")
        results = cursor.fetchall()
        print(results)
        return results

def get_district():
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT district FROM address;")
        results = cursor.fetchall()
        districts = []
        for dist in results:
            districts.append(dist[0])
        return results

def get_postal_code():
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT postal_code FROM address;")
        results = cursor.fetchall()
        print(results)
        return results

def get_phone():
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT phone FROM address;")
        results = cursor.fetchall()
        print(results)
        return results

def update_film_category(param1, param2):
    print(param1)
    print(param2)
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE category SET name = ? where name = ?", [param1, param2])
        results = cursor.fetchall()
        print(results)
        return results

def delete_country(deleted_country):
    print(deleted_country)
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM country WHERE country = ?;", [deleted_country])
        conn.commit()
    return ("Deleted successfully.")

def insert_country(country_name):
    print(country_name)
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        # "?" will pull data from country_name entered into json
        cursor.execute("INSERT INTO country (country, last_update) VALUES (?, datetime());", [country_name])
        conn.commit()
        #return id from last execution (insert into above)
        # https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta
        print(cursor.lastrowid)
        return cursor.lastrowid

def insert_language(new_language):
    print(new_language)
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO language (name, last_update) VALUES (?, datetime());", [new_language])
        conn.commit()
        print(cursor.lastrowid)
        return cursor.lastrowid

def insert_auckland():
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO city VALUES (601, 'Auckland', '68', '2022-11-15 04:34:33');")
        results = cursor.fetchall()
        print(results)
        return results

def insert_tv_series():
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO category VALUES (17, 'TV Series', '2022-11-15 04:34:33');")
        results = cursor.fetchall()
        print(results)
        return results

def insert_new_actor(actor1, actor2):
    print(actor1)
    print(actor2)
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO actor (first_name, last_name, last_update) VALUES (?, ?, datetime()) RETURNING *;", [actor1, actor2])
        item = cursor.fetchone()
        print(item)
        return item

if __name__ == "__main__":
    get_actors()
    get_rental_rate()
    get_cheap_rental_rate()
    get_pg13_rating()
    get_limited_list()
    get_category_id()
    get_repeated_actor_list()
    get_staff_email()
    get_cities()
    get_district()
    get_postal_code()
    get_phone()    
    get_film_titles()
    address_list()
    delete_country()
    update_film_category()
    insert_country()
    insert_new_actor()
    insert_language()
    insert_auckland()
    insert_tv_series()
