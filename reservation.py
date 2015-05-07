import sqlite3
show_all_movies_query = """SELECT * FROM Movies
"""


class Reservation:

    def __init__(self, databasename):
        self.conn = sqlite3.connect(databasename)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def show_movies(self):
        r = self.cursor.execute(show_all_movies_query)
        for row in r:
            print("{}||{}||{}".format(row["id"], row["name"], row["rating"]))

    def make_reservation(self):
        pass

    def get_id_show_movies(self):
        pass

    def get_projection_by_movie_id(self):
        pass
