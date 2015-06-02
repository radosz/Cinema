import sqlite3
from tabulate import tabulate
import sql
import class_Cinema as cinema
import sys


class res_m:
    messages1 = "Step 1 (User): Choose name :"
    messages2 = "Step 1 (User): Choose number of tickets :"
    messages3 = "Step 2 (Movie): Choose a movie :"
    messages4 = "Step 3 (Projection): Choose a projection :"
    messages5 = "Choose seat {}"
    final_messages = "This is your reservation:\nMovie : {} \n{} \nSeats : {}"


class Reservation:

    def __init__(self, databasename):
        self.conn = sqlite3.connect(databasename)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def show_movies(self):
        q = self.cursor.execute(sql.show_all_movies_query)
        head = ["movie_id", "name", "rating"]
        return self.__get_table(q, head)

    def show_reservation(self):
        q = self.cursor.execute(sql.cancel_reservation)
        head = ["id", "username", "movie", "type", "row", "col"]
        return self.__get_table(q, head)

    def get_reservation_rows(self):
        q = self.cursor.execute(sql.cancel_reservation)
        row_s = self.__get_table_row(q, "row")
        q = self.cursor.execute(sql.cancel_reservation)
        col_s = self.__get_table_row(q, "col")
        return (row_s, col_s)

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

    def get_projection_date_by_id(self, id):
        q = self.cursor.execute(sql.projection_date, (id,))
        return self.__get_table_row(q, "date")[0]

    def get_movie_name_rating_by_id(self, id):
        q = self.cursor.execute(sql.movie_by_id, (id,))
        name = self.__get_table_row(q, "name")[0]
        q = self.cursor.execute(sql.movie_by_id, (id,))
        rating = self.__get_table_row(q, "rating")[0]
        output = "{} ({})".format(name, rating)
        return output

    def load_reservation(self, id):
        rows = []
        cols = []
        q = self.cursor.execute(sql.reservation_where_prj_id, (id,))
        data = q.fetchall()
        for element in data:
            rows.append(element["row"])
            cols.append(element["col"])
        return (rows, cols)

    def get_date_time_types_by_id(self, id):
        q = self.cursor.execute(sql.projection, (id,))
        date = self.__get_table_row(q, "date")[0]
        q = self.cursor.execute(sql.projection, (id,))
        time = self.__get_table_row(q, "time")[0]
        output = "Date and time {} {}".format(date, time)
        return output

    def get_id_by_username_reservation(self, username):
        query = self.cursor.execute(sql.show_username_reservation, (username,))
        return self.__get_table_row(query, "reservation_id")[0]

    def delete_reservation(self, id):
        self.cursor.execute(sql.delete_reservation, (id,))
        self.conn.commit()


class Reservation_interface(Reservation):

    def __init__(self, databasename):
        super().__init__(databasename)
        cn = cinema.Cinema("cinema_map.txt")
        row_s, col_s = self.get_reservation_rows()
        all_tickets = cn.count_available_seats()
        username = input(res_m.messages1)
        self.show_movies()
        movie_id = input(res_m.messages3)
        self.get_projection_by_movie_id(movie_id)
        projection_id = input(res_m.messages4)
        self.reservation_load(projection_id, cn)
        tickets_num = input(res_m.messages2)
        seat_tuples = []
        if int(tickets_num) <= all_tickets:
            for i in range(int(tickets_num)):
                cn.print_cinema()
                row, col = self.choose(i)
                try:
                    cn.choose_seat(row, col)
                except cinema.SeatException:
                    while not cn.is_available(row, col):
                        row, col = self.choose(i)
                self.make_reservation(username, projection_id, row, col)
            seat_tuple = (row, col)
            seat_tuples.append(seat_tuple)
        print(res_m.final_messages.format(
            self.get_movie_name_rating_by_id(movie_id),
            self.get_date_time_types_by_id(projection_id),
            seat_tuples))

    def reservation_load(self, projection_id, cn):
        rows, cols = self.load_reservation(projection_id)
        for r, c in zip(rows, cols):
            cn.load_reservations(r, c)

    def choose(self, i):
        choose_o = input(res_m.messages5.format(i + 1) + ": ")
        lst_choose = choose_o.split(",")
        row = int(lst_choose[0])
        col = int(lst_choose[1])
        return (row, col)


def main():
    databasename = sys.argv[1]
    res = Reservation_interface(databasename)
if __name__ == '__main__':
    main()
