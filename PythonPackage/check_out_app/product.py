from datetime import datetime

name_of_item = ""
number_of_items = 0
amount_of_item = 0.0
date = datetime.today()


class product:

    def __init__(self, name="", amount=0.0, quantity=0):
        self.name_of_item = name
        self.amount_of_item = amount
        self.number_of_items = quantity


def get_name_of_item(self, name):
    self.name_of_item = name
    return name_of_item


def get_amount_of_items(self):
    return self.amount_of_item


def get_quantity(self):
    if number_of_items > 0:
        return self.number_of_items


def calculate_amount_and_quantity() -> float:
    return amount_of_item * number_of_items


if __name__ == "__main__":
    amount_of_item = 200
    number_of_items = 2
    print(calculate_amount_and_quantity())
