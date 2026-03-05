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
        if price < 1:
            raise ValueError("Price cannot be lesser than 1 ")


    def get_price(self):
        return self.price

    def validate_name(self, name):
        if name.strip() == "":
            raise ValueError("Name cannot be left blank")


    def validate_quantity(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity of goods cannot be lesser than zero")

    def get_quantity(self):
        return self.quantity


