import sqlite3
from tabulate import tabulate
import sql
from class_Cinema import Cinema


class res_m:
    messages1 = "Step 1 (User): Choose name :"
    messages2 = "Step 1 (User): Choose number of tickets :"
    messages3 = "Step 2 (Movie): Choose a movie :"
    messages4 = "Step 3 (Projection): Choose a projection :"
    messages5 = "Choose seat {}"
    final_messages = "This is your reservation:{} {} {}"


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
            print(row[row_key])
            rows.append(row[row_key])
        return rows

    def reservation_interface(self):
        cn = Cinema("cinema_map.txt")
        all_tickets = cn.count_available_seats()
        username = input(res_m.messages1)
        self.show_movies()
        movie_id = input(res_m.messages3)
        self.get_projection_by_movie_id(movie_id)
        projection_id = input(res_m.messages4)
        tickets_num = input(res_m.messages2)
        if int(tickets_num) <= all_tickets:
            for i in range(1, int(tickets_num)):
                choose = input(res_m.messages5.format(i) + ": ")
                lst_choose = choose.split(",")
                row = lst_choose[0]
                col = lst_choose[1]
                cn.choose_seat(int(row), int(col))
                cn.print_cinema()
        #Repair print 
        print(res_m.final_messages.format("end","end","end"))
        return self.make_reservation(username, projection_id, int(row), int(col))

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

    def get_id_by_username_reservation(self, username):
        query = self.cursor.execute(sql.show_username_reservation, (username,))
        return self.__get_table_row(query, "reservation_id")[0]

    def delete_reservation(self, id):
        self.cursor.execute(sql.delete_reservation, (id,))
        self.conn.commit()


def main():
    res = Reservation("cinema.db")
#    res.show_movies()
#    print(res.get_id_show_movie("The Hunger Games: Catching Fire"))
#    print(res.get_projection_by_movie_id(3))
#    try:
#        res.make_reservation("vlado", 2, 3, 4)
#    except sqlite3.IntegrityError:
#        pass
#    print(res.get_id_by_username_reservation("vlado"))
    res.reservation_interface()
if __name__ == '__main__':
    main()
