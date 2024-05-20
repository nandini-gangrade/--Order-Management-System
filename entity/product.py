class Product:
    def __init__(self, product_id, product_name, description, price, quantity_in_stock, type_, brand=None, warranty_period=None, size=None, color=None):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        self.type = type_
        self.brand = brand
        self.warranty_period = warranty_period
        self.size = size
        self.color = color
        self.quantity = 0  

    # Getter methods
    def get_product_id(self):
        return self.product_id

    def get_product_name(self):
        return self.product_name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get_quantity_in_stock(self):
        return self.quantity_in_stock

    def get_type(self):
        return self.type

    def get_brand(self):
        return self.brand

    def get_warranty_period(self):
        return self.warranty_period

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def get_quantity(self):
        return self.quantity

    # Setter methods
    def set_product_name(self, product_name):
        self.product_name = product_name

    def set_description(self, description):
        self.description = description

    def set_price(self, price):
        self.price = price

    def set_quantity_in_stock(self, quantity_in_stock):
        self.quantity_in_stock = quantity_in_stock

    def set_type(self, type_):
        self.type = type_

    def set_brand(self, brand):
        self.brand = brand

    def set_warranty_period(self, warranty_period):
        self.warranty_period = warranty_period

    def set_size(self, size):
        self.size = size

    def set_color(self, color):
        self.color = color

    def set_quantity(self, quantity):
        self.quantity = quantity
