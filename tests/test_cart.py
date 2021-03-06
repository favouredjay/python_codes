from unittest import TestCase

from PythonPackage.Tasks.check_out_app import cart, product


class cartTest(TestCase):
    item_list = []

    def test_that_cart_is_not_null(self):
        shopping_cart = cart
        self.assertIsNotNone(shopping_cart)

    def test_that_products_exist(self):
        item = product
        self.assertIsNotNone(item)

    def test_that_product_has_quantity_and_amount(self):
        product.number_of_items = 2
        product.amount_of_item = 200
        self.assertEqual(product.calculate_amount_and_quantity(), 400)

    def test_that_items_can_be_added_to_a_shopping_cart(self):
        shopping_cart = cart
        mango = product
        apple = product
        cart.add_items_to_cart(self, mango)
        cart.add_items_to_cart(self, apple)
        for i in shopping_cart.get_items_in_cart(self):
            print(i)
        self.assertEqual(cart.get_total_products(self), 2)

    def test_that_items_can_be_changed(self):
        shopping_cart = cart
        item_1 = product
        item_2 = product
        item_3 = product
        self.item_list.append(item_1)
        self.item_list.append(item_2)
        shopping_cart.change_item_in_a_cart(self, item_2, item_3)
        for i in self.item_list:
            print(i)
        self.assertEqual(shopping_cart.get_total_products(self), 2)

    def test_that_items_can_be_removed(self):
        shopping_cart = cart
        mango = product
        orange = product
        pampers = product
        self.item_list.append(mango)
        self.item_list.append(orange)
        self.item_list.append(pampers)
        self.assertEqual(shopping_cart.get_total_products(self), 3)
        shopping_cart.remove_items(self, pampers)
        self.assertEqual(shopping_cart.get_total_products(self), 2)
