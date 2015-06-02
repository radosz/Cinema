from magic_reservation_system import Reservation
import sys

res = Reservation("cinema.db")


def terminal_output():
    try:
        reservation_id = sys.argv[1]
        res.delete_reservation(reservation_id)
        print("reservation {} is cancelled".format(reservation_id))
    except IndexError:
        res.show_reservation()


terminal_output()
