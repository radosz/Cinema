import sqlite3
from tabulate import tabulate
import sql


class Reservation:

    def __init__(self, databasename):
        self.conn = sqlite3.connect(databasename)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def show_movies(self):
        q = self.cursor.execute(sql.show_all_movies_query)
        head = ["movie_id", "name", "rating"]
        return self.__get_table(q, head)

    def __get_table(self, query, head):
        table = []
        for row in query:
            rows = [row[x] for x in head]
            table.append(rows)
        print(tabulate(table, headers=head, tablefmt="rst"))

    def __get_table_row(self, query, row_key):
        rows = []
        for row in query:
            rows.append(row[row_key])
        return rows

    def make_reservation(self, username, projection_id, row, col):
        # TODO : Make validate for row and col after Ticket class is done
        self.cursor.execute(
            sql.reservation_query, (username, projection_id, row, col))
        self.conn.commit()

    def get_id_show_movie(self, name):
        query = self.cursor.execute(sql.movie_id_query, (name,))
        return self.__get_table_row(query, "movie_id")[0]

    # take string date yyyy-mm-dd
    def get_projection_by_movie_id(self, movie_id, date=False):
        head = ("id", "movie", "rating", "type", "date", "time")
        if not date:
            q = self.cursor.execute(sql.projection_by_id_no_date, (movie_id,))
            return self.__get_table(q, head)
        date = "%" + date + "%"
        q = self.cursor.execute(sql.projection_by_id_date, (movie_id, date))
        return self.__get_table(q, head)


def main():
    res = Reservation("cinema.db")
    res.show_movies()
    print(res.get_id_show_movie("The Hunger Games: Catching Fire"))
    print(res.get_projection_by_movie_id(3))
    try:
        res.make_reservation("vlado", 2, 3, 4)
    except sqlite3.IntegrityError:
        pass
if __name__ == '__main__':
    main()
