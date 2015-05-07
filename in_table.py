from tabulate import tabulate


class View:

    def __init__(self, table, headers):
        self.table = table
        self.headers = headers

    def __str__(self):
        return self.__make_table()

    def __repr__(self):
        return self.__str__()

    def __make_table(self):
        table = self.table
        return tabulate(table, headers=self.headers, tablefmt="fancy_grid")
