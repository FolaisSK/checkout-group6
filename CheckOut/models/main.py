
from models.cart import Cart
from models.checkout import Checkout



checkout = Checkout()


def main_menu():
    new_cart = Cart()
    print("Welcome to FUDA Supermarket")
    isNo = True
    try:
        while(isNo):
            product_name = input("Enter Product Name: ")
            product_price = float(input("Enter Product Price: "))
            product_quantity = int(input("Enter Product Quantity: "))
            new_cart.add_to_cart(product_name, product_price, product_quantity)
            shop = input("Do you want to checkout another cart or shop? (Yes/No): ").lower()
            validate_user_response(shop)
            if shop.lower() == "no":
                isNo = False
        checkout.generate_invoice(new_cart)
    except Exception as e:
        print("Invalid Response")
    finally:
        main_menu()

def validate_user_response( response):
    if response.lower() not in ["yes","no"]:
        raise ValueError("Invalid Response")




main_menu()