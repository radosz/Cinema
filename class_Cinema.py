class Cinema:

    def __init__(self, filename):
        lines = open(filename).read().split("\n")
        lines = [line for line in lines if line.strip() != 0]
        self.seats = [[ch for ch in line] for line in lines]
        self.seats_availability = {}
        # self.col = 0
        # self.row = 0
        for i in range(1, 11):
            for j in range(2, 21):
                if self.seats[i][j] == "X":
                    self.seats_availability[(i, j)] = 1
                elif self.seats[i][j] == ".":
                    self.seats_availability[(i, j)] = 0

    def print_cinema(self):
        for x in self.seats:
            ss = ''.join(x)
            print(ss)

    def is_available(self, row, col):
        if self.seats_availability[(row, col * 2)] == 1:
            return False
        return True

    def choose_seat(self, row, col):
        if row > 10 or col > 10:
            return False
        if self.is_available(row, col):
            self.seats_availability[(row, col * 2)] = 1
            self.seats[row][col * 2] = "X"
        else:
            raise SeatException("This seat is busy")
        return True

    def count_available_seats(self):
        count = 0
        for row in range(1, 11):
            for col in range(2, 21):
                if self.seats[row][col] == ".":
                    count += 1
        return count

    def load_reservations(self, row, col):
        self.choose_seat(row, col)
        self.seats_availability[(row, col)] = 1


class SeatException(Exception):
    pass