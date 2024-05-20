# order.py

from datetime import datetime

class Order:
    def __init__(self, orderId, userId, orderDate=None, status=None):
        self.orderId = orderId
        self.userId = userId
        self.orderDate = orderDate or datetime.now()
        self.status = status

    # Getters
    def get_order_id(self):
        return self.orderId

    def get_user_id(self):
        return self.userId

    def get_order_date(self):
        return self.orderDate

    def get_status(self):
        return self.status

    # Setters
    def set_user_id(self, userId):
        self.userId = userId

    def set_order_date(self, orderDate):
        self.orderDate = orderDate

    def set_status(self, status):
        self.status = status
