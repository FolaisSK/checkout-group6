
from CheckOut.models.cart import Cart
from CheckOut.models.checkout import Checkout


class main:
    checkout = Checkout()


    def main_menu(self):
        self.new_cart = Cart()
        print("Welcome to FUDA Supermarket")
        isNo = True
        try:
            while(isNo):
                product_name = input("Enter Product Name: ")
                product_price = float(input("Enter Product Price: "))
                product_quantity = int(input("Enter Product Quantity: "))
                self.new_cart.add_to_cart(product_name, product_price, product_quantity)
                shop = input("Do you want to checkout another cart or shop? (Yes/No): ")
                self.validate_user_response(shop)
                if shop.lower() == "no":
                    isNo = False
            self.checkout.generate_invoice(self.new_cart)
        except Exception as e:
            print(e)
        finally:
            main().main_menu()

    def validate_user_response(self, response):
        if response != "yes" or response != "no":
            raise ValueError("Invalid Response")




print(main().main_menu())