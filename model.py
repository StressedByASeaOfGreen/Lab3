from constants import TABLES, MENU_ITEMS


class Restaurant:

    def __init__(self):
        self.tables = [Table(seats, loc) for seats, loc in TABLES]
        self.menu_items = [MenuItem(name, price) for name, price in MENU_ITEMS]


class Table:

    def __init__(self, seats, location):
        self.n_seats = seats
        self.location = location
        self.orders = [Order() for _ in range(seats)]


class Order:
    pass


class OrderItem:
    pass


class MenuItem:
    #todo (par Abderr) creer un init pour cette classe conformant a l'appellation a la ligne 8 de ce file
    pass
