class FruitManager:
    def __init__(self):
        self.stock = {
            'Grapes': {'quantity': 50, 'price': 5},
            'kiwi': {'quantity': 25, 'price': 6},
            'Cherry': {'quantity': 25, 'price': 4}
        }

    def add_fruit_stock(self, fruit_name, quantity, price):
        if fruit_name in self.stock:
            self.stock[fruit_name]['quantity'] += quantity
        else:
            self.stock[fruit_name] = {'quantity': quantity, 'price': price}

    def view_fruit_stock(self):
        return self.stock

    def update_fruit_stock(self, fruit_name, quantity):
        if fruit_name in self.stock:
            self.stock[fruit_name]['quantity'] = quantity
            return True
        else:
            return False

    def get_fruit_price(self, fruit_name):
        if fruit_name in self.stock:
            return self.stock[fruit_name]['price']
        else:
            return 0.0

    def show_available_fruits(self):
        return self.stock.keys()




