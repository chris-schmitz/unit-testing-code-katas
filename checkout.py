from typing import Dict


# https://www.udemy.com/course/unit-testing-and-tdd-in-python/learn/lecture/8419080#overview

#  TODO: consider refactor
# * in the lesson the concept of whether or not an item qualifies for a discount and the total calculated
# * happen in Checkout, but if we already have a Discount class it seems like concepts like `qualifies_for_discount`
# * and maybe `get_discounted_total` (returning discount total and remaining count???) belong in this class.
class Discount:
    def __init__(self, count: int, discount_price: int):
        self.qualifying_count = count
        self.discount_price = discount_price


class NoPriceException(Exception):
    pass


class Checkout:
    # ! note that we can't really use just class level attributes here.
    # ? if we uncomment these and remove the init then all of the instances of checkout
    # ? will share the data within these properties; class level attributes are created once
    # ? when the first instance of the class is created and they're shared between all instances.
    # ? if we do use the class level attributes here and run all of our tests we'll find that the
    # ? latter tests will start to fail because they have data stored in them from the earlier tests.
    #
    # ? If we use just the instance attributes via the init function we're fine b/c the instance
    # ? attributes take precedent over matching class level attributes unless you manually set the underlying
    # ? class level attributes.
    # discounts: Dict[str, Discount] = {}
    # prices: Dict[str, int] = {}
    # items: Dict[str, int] = {}

    def __init__(self):
        self.discounts: Dict[str, Discount] = {}
        self.prices: Dict[str, int] = {}
        self.items: Dict[str, int] = {}

    def add_item_price(self, name: str, price: int):
        self.prices[name] = price

    def add_item(self, name: str):
        if name not in self.prices:
            raise NoPriceException
        if name in self.items:
            self.items[name] += 1
        else:
            self.items[name] = 1

    def add_discount(self, item: str, count: int, discount_price: int):
        self.discounts[item] = Discount(count, discount_price)

    def calculate_total(self):
        # TODO: this is giong to need _heavy_ refactoring.
        # * If they don't cover that in the lession, swing back and take a stab at it
        # * and apply the 99 bottles methodologies to refactor
        total = 0
        for item, count in self.items.items():
            total += self.calculate_total_for_item(item, count)
        return total

    def calculate_total_for_item(self, item: str, count: int):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]

            if count >= discount.qualifying_count:
                number_of_discounts = count / discount.qualifying_count
                remainder_items = count % discount.qualifying_count

                total += number_of_discounts * discount.discount_price
                total += remainder_items * self.prices[item]
            else:
                total += self.prices[item] * count
        else:
            total += self.prices[item] * count

        return total

    def calculate_items_discount_total(self, item, count, discount):
        pass
