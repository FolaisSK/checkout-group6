
from CheckOut.models.product import Product


class Cart:
    def __init__(self):
        self.products = []


    def get_all_products(self):
        return self.products

    def add_to_cart(self,product_name:str,product_price: float,product_quantity:int):

        new_product = Product(product_name,product_price,product_quantity)

        self.products.append(new_product)


    def remove_form_cart(self,product_name:str):
        product = None
        product = self.find_product_by_name(product_name)

        if product is not None:
           self.products.remove(product)
        else:
            raise ValueError ("Product Not Found")



    def find_product_by_name(self,product_name:str):

        for item in self.products:
            if item.get_name() == product_name:
                return item

        return None


    def get_number_of_products(self):
        return len(self.products)