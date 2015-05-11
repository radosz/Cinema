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
        if self.seats_availability[(row, col*2)] == 1:
            return False
        return True

    def choose_seat(self, row, col):
        if row > 10 or col > 10:
            return False
        self.seats_availability[(row, col*2)] = 1
        self.seats[row][col*2] = "X"
        return True

    def count_available_seats(self):
        count = 0
        for row in range(1, 11):
            for col in range(2, 21):
                if self.seats[row][col] == ".":
                    count += 1
        return count

mycinema = Cinema("cinema_map.txt")
print(mycinema.seats_availability)
mycinema.print_cinema()
print(mycinema.is_available(2, 3))
print(mycinema.is_available(4, 8))
print(mycinema.choose_seat(1, 1))
print(mycinema.choose_seat(5, 5))
print(mycinema.choose_seat(10, 10))
print(mycinema.choose_seat(15, 20))
print(mycinema.count_available_seats())
print("\n")
mycinema.print_cinema()
