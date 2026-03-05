from models.cart import Cart
from models.checkout import Checkout

checkout = Checkout()

def main():
    cart = Cart()
    print("Welcome to FUDA Supermarket")
    isRunning = True

    while isRunning:
        product_name = input("Enter Product Name: ")
        while True:
            try:
                product_price = float(input("Enter Product Price: "))
            except Exception:
                print("Please enter a valid price")
                continue
            break
        while True:
            try:
                product_quantity = int(input("Enter Product Quantity: "))
            except Exception:
                print("Please enter a valid quantity")
                continue
            break
        cart.add_to_cart(product_name, product_price, product_quantity)
        shop = input("Do you want to checkout another cart or shop? (Yes/No): ").lower()
        try:
            validate_user_response(shop)
        except ValueError:
            print("Please enter a valid choice")
            continue
        if shop == "no":
            isRunning = False

    checkout.generate_invoice(cart)
    subtotal = checkout.calculate_subtotal(cart)

    while True:
        try:
            amount_paid = float(input("Enter Amount Paid: "))
        except Exception:
            print("Please enter a valid amount")
            continue
        if amount_paid < subtotal:
            print("Insufficient funds")
            continue
        break

    checkout.generate_receipt(amount_paid, cart)



def validate_user_response( response):
    if response.lower() not in ["yes","no"]:
        raise ValueError("Invalid Response")

main()