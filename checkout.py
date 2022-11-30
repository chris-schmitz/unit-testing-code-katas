class Checkout:
    prices = {}
    items = []

    # def __int__(self):
    #     self.prices = {}
    #     self.items = []

    def add_item_price(self, name, price):
        self.prices[name] = price

    def add_item(self, name):
        self.items.append(name)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += self.prices[item]

        return total
