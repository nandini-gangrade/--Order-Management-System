# order_details.py

class OrderDetails:
    def __init__(self, orderDetailId, orderId, productId, quantity):
        self.orderDetailId = orderDetailId
        self.orderId = orderId
        self.productId = productId
        self.quantity = quantity

    # Getters
    def get_order_detail_id(self):
        return self.orderDetailId

    def get_order_id(self):
        return self.orderId

    def get_product_id(self):
        return self.productId

    def get_quantity(self):
        return self.quantity

    # Setters
    def set_order_id(self, orderId):
        self.orderId = orderId

    def set_product_id(self, productId):
        self.productId = productId

    def set_quantity(self, quantity):
        self.quantity = quantity
