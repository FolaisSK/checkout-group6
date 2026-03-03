from datetime import datetime

from models.cart import Cart


class Checkout:
    name = ""
    VAT_RATE = 0.075


    def generate_invoice(self, cart:Cart):
        name = input("Dear FUDA attendant, Enter your name: ")
        print(f"\n ---- Invoice (by Attendant: {name}) ----")
        print("\t \tDate", self.date_and_time())
        print("\n ----------------------------------\n")
        products = cart.get_all_products()
        for item in products:
            print(f"{item.get_name()}: {item.get_price():.2f}")


        subtotal = self.calculate_subtotal(cart)
        print("-------------------------------------")
        print(f"Subtotal: ${subtotal:.2f}")
        print("\n")

        print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
        print(f"THIS IS NOT A RECEIPT, PLEASE PAY {subtotal} FOR RECEIPT GENERATION")
        amount = float(input(f"Attendant {name}, Enter amount paid: "))
        self.generate_receipt(amount,cart)



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

        print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
        print(f"VAT (7.5%): ${self.calculate_VAT(cart):.2f}")
        print(f"TOTAL: ${total:.2f}")
        print(f"Paid: ${amount_paid:.2f}")
        print(f"Balance: ${balance:.2f}\n\n")
        print("--- Thank you for shopping @FUDA, see you next time! ---")


    def calculate_balance(self, amount_paid,cart):
        if amount_paid < self.calculate_total(cart):
          raise ValueError("Not enough money")
        return amount_paid - self.calculate_total(cart)


    def date_and_time(self):
        return datetime.now().strftime("%d-%b-%Y %H:%M:%S")

