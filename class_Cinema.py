class Cinema:
    def __init__(self, filename):
        lines = open(filename).read().split("\n")
        lines = [line for line in lines if line.strip() != 0]
        self.seats = [[ch for ch in line] for line in lines]
        self.seats_availability = {}
        # self.col = 0
        # self.row = 0
        for i in range(0, 10):
            for j in range(0, 10):
                if self.seats[i][j] == "X":
                    self.seats_availability[(i, j)] = 1
                else:
                    self.seats_availability[(i, j)] = 0

    def print_cinema(self):
        for x in self.seats:
            ss = ''.join(x)
            print(ss)

    def is_available(self, row, col):
        if self.seats_availability[(row, col)] == 1:
            return False
        return True

    def choose_seat(self, row, col):
        if row > 10 or col > 10:
            return False
        self.seats_availability[(row, col)] = 1
        self.seats[row][col] = "X"
        return True

mycinema = Cinema("cinema_map.txt")
print(mycinema.seats_availability)
mycinema.print_cinema()
print(mycinema.is_available(2, 3))
print(mycinema.is_available(3, 7))
print(mycinema.choose_seat(1, 3))
print("\n")
mycinema.print_cinema()
