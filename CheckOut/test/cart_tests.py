import unittest

from CheckOut.models.cart import Cart


class MyTestCase(unittest.TestCase):
    def test_cart_is_initially_empty(self):
        cart = Cart()
        self.assertEqual(cart.get_number_of_products(), 0)

    def test_item_can_be_added_to_cart(self):
        cart = Cart()
        self.assertEqual(cart.get_number_of_products(), 0)
        cart.add_to_cart("Milk", 200, 1)
        self.assertEqual(cart.get_number_of_products(), 1)

    def test_two_items_are_added_to_cart_remove_one_products_are_one(self):
        cart = Cart()
        self.assertEqual(cart.get_number_of_products(), 0)
        cart.add_to_cart("Milk", 200, 1)
        cart.add_to_cart("Rice", 500, 2)
        self.assertEqual(cart.get_number_of_products(), 2)

    def test_item_cannot_be_added_to_cart_with_negative_price(self):
        cart = Cart()
        self.assertEqual(cart.get_number_of_products(), 0)
        with self.assertRaises(ValueError):
            cart.add_to_cart("Milk", -100, 1)

    def test_item_cannot_be_added_to_cart_with_negative_quantity(self):
        cart = Cart()
        self.assertEqual(cart.get_number_of_products(), 0)
        with self.assertRaises(ValueError):
            cart.add_to_cart("Milk", 100, -1)

    def test_item_cannot_be_added_to_cart_with_empty_name(self):
        cart = Cart()
        self.assertEqual(cart.get_number_of_products(), 0)
        with self.assertRaises(ValueError):
            cart.add_to_cart("", 100, 1)


if __name__ == '__main__':
    unittest.main()
