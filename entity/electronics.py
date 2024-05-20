# electronics.py

from entity.product import Product

class Electronics(Product):
    def __init__(self, productId, productName, description, price, quantityInStock, type, brand, warrantyPeriod):
        super().__init__(productId, productName, description, price, quantityInStock, type)
        self.brand = brand
        self.warrantyPeriod = warrantyPeriod

    # Getters
    def get_brand(self):
        return self.brand

    def get_warranty_period(self):
        return self.warrantyPeriod

    # Setters
    def set_brand(self, brand):
        self.brand = brand

    def set_warranty_period(self, warrantyPeriod):
        self.warrantyPeriod = warrantyPeriod
