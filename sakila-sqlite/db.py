import sqlite3
def get_actors():
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        results = cursor.execute("SELECT * FROM actor;")
        # print(results.fetchone())
        # print(results.fetchone())
        actors = results.fetchall()
        print(actors)
        return actors

if __name__ == "__main__":
    get_actors()