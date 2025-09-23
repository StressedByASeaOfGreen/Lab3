from model import Order


class Controller:
    """
    Do not modify this class, just its subclasses. Represents common behaviour of all
    Controllers. Python has a mechanism for explicitly dealing with abstract classes,
    which we haven't seen yet; raising RuntimeError gives a similar effect.
    """

    def __init__(self, view, restaurant):
        self.view = view
        self.restaurant = restaurant

    def add_item(self, item):
        raise RuntimeError('add_item: some subclasses must implement')

    def cancel(self):
        raise RuntimeError('cancel: some subclasses must implement')

    def create_ui(self):
        raise RuntimeError('create_ui: all subclasses must implement')

    def done(self):
        raise RuntimeError('done: some subclasses must implement')

    def place_order(self):
        raise RuntimeError('place_order: some subclasses must implement')

    def seat_touched(self, seat_number):
        raise RuntimeError('seat_touched: some subclasses must implement')

    def table_touched(self, table_index):
        raise RuntimeError('table_touched: some subclasses must implement')


class RestaurantController(Controller):

    def create_ui(self):
        self.view.create_restaurant_ui()

    def table_touched(self,table_number):
        table_controller = TableController(self.view, self.restaurant, self.restaurant.tables[table_number])
        self.view.set_controller(table_controller)

class TableController(Controller):
    def __init__(self, view, restaurant, table): #Besoin car table_index est initié
        super().__init__(view, restaurant) #besoin, car on a besoin de la class parent, qui est overide dans la ligne au-dessus
        self.table = table # Prend la table de la liste et la store

    def create_ui(self):
        self.view.create_table_ui(self.table)

    def seat_touched(self,seat_number):
        order = self.table.orders[seat_number]
        self.view.set_controller(OrderController(self.view, self.restaurant, self.table, order))

class OrderController(Controller):
    def __init__(self, view, restaurant, table, order): # Same que TableController()
        super().__init__(view, restaurant) # Same que TableController()
        self.table = table # Nécessaire pour savoir quelle table est utilisée
        self.order = order # Nécessaire pour savoir quel siège est utilisé

    def create_ui(self):
        self.view.create_order_ui(self.order)

    def add_item(self, menu_item):
        self.order.items.append(menu_item)

    def update_order(self):
        pass

    def cancel(self):
        self.order.remove_unordered_items()
        self.view.set_controller(TableController(self.view, self.restaurant, self.table))