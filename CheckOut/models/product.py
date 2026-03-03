class Product:
    def __init__(self, name, price, quantity):
        self.validate_name(name)
        self.validate_price(price)
        self.validate_quantity(quantity)
        self.name = name
        self.price = price
        self.quantity = quantity


    def get_name(self):
        return self.name

    def validate_price(self, price):
        if price <= 0:
            raise ValueError("Oga, Oga, Oga! Price cannot be less than 0!")
        self.price = price

        if price == 0:
            raise ValueError("Oga, Oga, Oga! Price cannot be 0, It's not free, Broke Boy!")

    def get_price(self):
        return self.price

    def validate_name(self, name):
        if name.strip() == "":
            raise ValueError("Oga, Oga, Oga! Name cannot be empty!")

        if not name.isalpha():
            raise ValueError("Oga, Oga! Name can only contain letters!")

    def validate_quantity(self, quantity):
        if quantity <= 0:
            raise ValueError("Oga, Oga, Oga! You've not picked anything!")

    def get_quantity(self):
        return self.quantity


        self.name = name
