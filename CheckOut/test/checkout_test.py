import unittest

from models.cart import Cart
from models.checkout import Checkout


class MyTestCase(unittest.TestCase):
    def test_cart_is_empty_subtotal_is_zero(self):
        cart = Cart()
        self.assertEqual(cart.get_number_of_products(), 0)
        attendant = Checkout()
        self.assertEqual(attendant.calculate_subtotal(cart), 0)

    def test_cart_contains_one_item_cost_500_subtotal_is_500(self):
        cart = Cart()
        self.assertEqual(cart.get_number_of_products(), 0)
        cart.add_to_cart("Milk", 500, 1)
        attendant = Checkout()
        self.assertEqual(attendant.calculate_subtotal(cart), 500)

    def test_cart_contains_two_items_cost_500_each_subtotal_is_1000(self):
        cart = Cart()
        self.assertEqual(cart.get_number_of_products(), 0)
        cart.add_to_cart("Milk", 500, 1)
        cart.add_to_cart("Rice", 500, 1)
        attendant = Checkout()
        self.assertEqual(attendant.calculate_subtotal(cart), 1000)

    def test_cart_contains_one_product_quantity_3_cost_1000_subtotal_is_3000(self):
        cart = Cart()
        self.assertEqual(cart.get_number_of_products(), 0)
        cart.add_to_cart("Milk", 1000, 3)
        attendant = Checkout()
        self.assertEqual(attendant.calculate_subtotal(cart), 3000)

    def test_cart_contains_two_products_vat_is_calculated(self):
        cart = Cart()
        self.assertEqual(cart.get_number_of_products(), 0)
        cart.add_to_cart("Milk", 500, 1)
        cart.add_to_cart("Rice", 750, 1)
        attendant = Checkout()
        self.assertEqual(attendant.calculate_subtotal(cart), 1250)
        self.assertEqual(attendant.calculate_VAT(cart), 93.75)

    def test_cart_contains_three_products_vat_is_calculated(self):
        cart = Cart()
        self.assertEqual(cart.get_number_of_products(), 0)
        cart.add_to_cart("Milk", 200, 1)
        cart.add_to_cart("Rice", 700, 1)
        cart.add_to_cart("Eggs", 100, 5)
        attendant = Checkout()
        self.assertEqual(attendant.calculate_subtotal(cart), 1400)
        self.assertEqual(attendant.calculate_VAT(cart), 105)

    def test_cart_contains_two_items_subtotalIsCalculated_vatIsCalculated_totalIsCalculated(self):
        cart = Cart()
        self.assertEqual(cart.get_number_of_products(), 0)
        cart.add_to_cart("Milk", 200, 1)
        cart.add_to_cart("Rice", 700, 1)
        attendant = Checkout()
        self.assertEqual(attendant.calculate_subtotal(cart), 900)
        self.assertEqual(attendant.calculate_VAT(cart), 67.5)
        self.assertEqual(attendant.calculate_total(cart), 967.5)

    def test_amount_paid_is_more_than_total_cost_balance_is_given(self):
        cart = Cart()
        self.assertEqual(cart.get_number_of_products(), 0)
        cart.add_to_cart("Milk", 200, 1)
        cart.add_to_cart("Rice", 700, 1)
        attendant = Checkout()
        self.assertEqual(attendant.calculate_subtotal(cart), 900)
        self.assertEqual(attendant.calculate_VAT(cart), 67.5)
        self.assertEqual(attendant.calculate_total(cart), 967.5)
        amount_paid = 1000
        self.assertEqual(attendant.calculate_balance(amount_paid, cart), 32.5)

    def test_amount_paid_is_less_than_total_cost_i(self):
        cart = Cart()
        self.assertEqual(cart.get_number_of_products(), 0)
        cart.add_to_cart("Milk", 200, 1)
        cart.add_to_cart("Rice", 700, 1)
        attendant = Checkout()
        self.assertEqual(attendant.calculate_subtotal(cart), 900)
        self.assertEqual(attendant.calculate_VAT(cart), 67.5)
        self.assertEqual(attendant.calculate_total(cart), 967.5)
        amount_paid = 500
        with self.assertRaises(ValueError):
            self.assertEqual(attendant.calculate_balance(amount_paid, cart), 32.5)



if __name__ == '__main__':
    unittest.main()
