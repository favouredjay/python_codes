from PythonPackage.check_out_app import product


class cart:
    item = product
    item_list = []


def __init__(self, items):
    self.item = items


def get_items(self):
    return self.item


def get_items_in_cart(self):
    return self.item_list


def find_item(self, item):
    return self.item_list.index(item)


def get_item_by_name(self, name):
    position = self.find_item(name)
    if position >= 0:
        return self.item_list.index(position)
    else:
        return None


def add_items_to_cart(self, name, amount, quantity):
    item = product
    self.item_list.append(item)


def change_item_in_a_cart(self, old_item=product, new_item=product):
    found_item = self.find_item(old_item)
    if found_item < 0:
        print("Choose what's in your cart")
        return False
    else:
        self.item_list.remove(old_item)
        self.item_list.append(new_item)
        return True


def remove_items(self, item):
    position = self.find_item(item)
    if position <= 0:
        print(product.name_of_item, " not found")
        return False
    self.item_list.remove(position)
    print(product.name_of_item, " was deleted")
    return True


def calculate_total(self):
    for i in range(len(self.item_list)):
        total = sum.__get__(product.calculate_amount_and_quantity())
        return total


def get_total_products(self):
    return len(self.item_list)


def print_items(self):
    for i in range(len(self.item_list)):
        print(i.__eq__(product.get_name_of_item(self)), " - ", i.__eq__(product.get_quantity(self)), " - ",
              i.__eq__(product.get_amount_of_items(self)))
