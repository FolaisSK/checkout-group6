from datetime import datetime

from models.cart import Cart


class Checkout:
    name = ""
    VAT_RATE = 0.075


    def generate_invoice(self, cart:Cart):
        name = input("Dear FUDA attendant, Enter your name: ")
        print(f"\n ---- Invoice (by Attendant: {name}) ----")
        print("\tDate", self.date_and_time())
        print("\n-----------------------------------\n")

        products = cart.get_all_products()

        print(f"{'Product Name':<20}|{'Product Price':>13}|{'Product Quantity':>16}")
        print("-------------------------------------")

        for item in products:
            print(f"{item.get_name():<20}|{item.get_price():>13.2f}|{item.get_quantity():>16}")

        subtotal = self.calculate_subtotal(cart)
        vat = subtotal * self.VAT_RATE
        total = self.calculate_total(cart)

        print("-------------------------------------")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"VAT (7.5%): ${vat:.2f}")
        print(f"TOTAL: ${total:.2f}")
        print("\n")

        print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
        print(f"THIS IS NOT A RECEIPT, PLEASE PAY {total:.2f} FOR RECEIPT GENERATION")




    def calculate_subtotal(self, cart:Cart):
        products = cart.get_all_products()
        unit_price = 0
        for item in products:
            unit_price += item.get_price() * item.get_quantity()
        return unit_price


    def calculate_total(self,cart):
        return self.calculate_subtotal(cart)+ self.calculate_VAT(cart)



    def calculate_VAT(self,cart):
        return self.calculate_subtotal(cart) * self.VAT_RATE



    def generate_receipt(self,amount_paid,cart):
        total = self.calculate_total(cart)
        balance = self.calculate_balance(amount_paid,cart)
        print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
        print(f"\n--- Final Receipt ---\n")
        print("Date", self.date_and_time())

        print("\n$$$$$$$$$$$$$$$$$$$subtotal$$$$$$$$$$$$$$$$$$$$$\n")
        print(f"VAT (7.5%): ${self.calculate_VAT(cart):.2f}")
        print(f"TOTAL: ${total:.2f}")
        print(f"Paid: ${amount_paid:.2f}")
        print(f"Balance: ${balance:.2f}\n\n")
        print("--- Thank you for shopping @FUDA, see you next time! ---")


    def calculate_balance(self, amount_paid,cart):
        total = self.calculate_total(cart)

        if amount_paid < total:
          raise ValueError("Not enough money")

        balance = amount_paid - total
        return balance


    def date_and_time(self):
        return datetime.now().strftime("%d-%b-%Y %H:%M:%S")

