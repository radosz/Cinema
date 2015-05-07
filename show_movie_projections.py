from reservation import Reservation
import sys

res = Reservation("cinema.db")


def terminal_output():
    movie_id = sys.argv[1]
    try:
        date = sys.argv[2]
    except IndexError:
        res.get_projection_by_movie_id(movie_id)
        return True
    res.get_projection_by_movie_id(movie_id, date)


terminal_output()
