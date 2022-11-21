"""
Your FastAPI code for Task 2 goes here.
"""
from fastapi import FastAPI
from pyparsing import countedArray
import queries
import hashlib


# uvicorn main:app --reload --port 15688

app = FastAPI(docs_url='/')

@app.get("/hello")
def hi():
    return "Obiwan: Hello there."

# TODO: Add more below.

# Run "uvicorn main:app --refresh" 

@app.get("/cities")
def get_cities():
    cities = queries.get_cities()
    return cities

@app.get("/rental_rate")
def get_rental_rate():
    rate = queries.get_rental_rate()
    rental_rate_result = []
    for data in rate:
        print(data)
        rental_rate = {}
        rental_rate["rate"] = data[0]
        rental_rate["title"] = data[2]
        rental_rate_result.append(rental_rate)
    return rental_rate_result

@app.get("/cheap_rental_rate")
def get_cheap_rental_rate():
    movie_list = queries.get_cheap_rental_rate()
    return movie_list

@app.get("/get_pg13_rating")
def get_pg13_rating():
    pg13_list = queries.get_pg13_rating()
    movie_list = []
    for data in pg13_list:
        print(data)
        rating = data[1]
        movie_list.append(rating)
    return movie_list

@app.get("/get_limited_list")
def get_limited_list():
    short_list = queries.get_limited_list()
    movie_list = []
    for data in short_list:
        print(data)
        id_name = {}
        id_name["movie_id"] = data[1]
        id_name["movie_title"] = data[2]
        movie_list.append(id_name)
    return movie_list

@app.get("/get_category_id")
def get_category_id():
    categories = queries.get_category_id()
    return categories

@app.get("/get_repeated_actor_list")
def get_repeated_actor_list():
    counter = queries.get_repeated_actor_list()
    return counter 

@app.get("/address_list")
def address_list():
    add_list = queries.address_list()
    return add_list

@app.get("/get_film_titles")
def get_film_titles():
    titles = queries.get_film_titles()
    return titles

@app.get("/get_staff_email")
def get_staff_email():
    emails = queries.get_staff_email()
    return emails

@app.get("/get_district")
def get_district():
    dist_list = queries.get_district()
    districts = []
    for data in dist_list:
        district = data[0]
        districts.append(district)
    return districts

@app.get("/get_postal_code")
def get_postal_code():
    post_code = queries.get_postal_code()
    return post_code

@app.get("/get_phone")
def get_phone():
    phones = queries.get_phone()
    return phones

@app.delete("/delete_country")
async def delete_country(country):
    deleted_country = queries.delete_country(deleted_country=country)
    return deleted_country

@app.put("/new_film_cat")
async def film_category(new_film_cat_name, film_cat):
    updated_cat = queries.update_film_category(param1=new_film_cat_name, param2=film_cat)
    return updated_cat

@app.post("/insert_country")
async def insert_country(new_country):
    new_country_id = queries.insert_country(country_name=new_country)
    return new_country_id

@app.post("/insert_language")
async def insert_language(language):
    new_lang = queries.insert_language(new_language=language)
    return new_lang

@app.post("/insert_new_actor")
async def insert_new_actor(first_name, last_name):
    new_actor = queries.insert_new_actor(actor1=first_name, actor2=last_name)
    return new_actor

@app.post("/hash_password")
async def hash_password(p_word):
    pw = bytes(p_word, 'utf-8')
    print(pw)
    hash = hashlib.sha256()
    hash.update(pw)
    return hashlib.sha256(pw).hexdigest()