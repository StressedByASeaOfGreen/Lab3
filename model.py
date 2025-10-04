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

    def has_order_for(self, seat):

        for items in self.orders[seat].items:
            if items.ordered == True:
                return True
        return False

    def order_for(self, seat):
        return self.orders[seat]

class Order:
    def __init__(self):
        pass

    def add_item(self, menu_item):
        return OrderItem(menu_item)

    def unordered_items(self):
        unordered_items = []
        for items in self.items:
            if items.ordered == False:
                unordered_items.append(items)
        return unordered_items

    def place_new_order(self):
        for items in self.items:
            items.mark_as_ordered()

    def remove_unordered_items(self):
        kept_items = []
        for item in self.items:
            if item.ordered:
                kept_items.append(item)
        self.items = kept_items

    def total_cost(self):
        total_cost = 0
        for items in self.items:
            if items.ordered: #this can be removed if needed
                total_cost += items.price
        return total_cost


class OrderItem:
    def __init__(self, menu_item):
        self.menu_item = menu_item
        self.ordered = False

    def mark_as_ordered(self):
        self.ordered = True

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
