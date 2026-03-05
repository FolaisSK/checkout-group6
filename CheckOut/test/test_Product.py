from unittest import TestCase

from models.product import Product


class ProductTest(TestCase):
    def test_that_the_product_name_and_price_is_entered_correctly(self):
        product = Product("Laptop", 150_000, 1)
        self.assertEqual("Laptop", product.get_name())


    def test_that_product_name_and_price_can_be_changed(self):
        product = Product("Laptop", 150_000, 1)
        self.assertEqual("Laptop", product.name)
        product.name = "Laptop"
        self.assertEqual("Laptop", product.name)

    def test_that_product_name_cannot_be_blank(self):
        with self.assertRaises(ValueError):
            Product("", 150_000, 1)


    def test_that_price_cannot_be_less_than_0(self):
        with self.assertRaises(ValueError):
            Product("Laptop", 0.00, 1)

    def test_that_price_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            Product("Laptop", -100.00, 1)


    def test_that_price_cannot_be_a_negative_input(self):
        with self.assertRaises(ValueError):
            Product("Laptop", -100.00, 0)
