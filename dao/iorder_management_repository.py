# iorder_management_repository.py

from abc import ABC, abstractmethod
from entity import User, Product

class IOrderManagementRepository(ABC):
    @abstractmethod
    def create_order(self, user: User, products: list):
        pass

    @abstractmethod
    def cancel_order(self, userId: int, orderId: int):
        pass

    @abstractmethod
    def create_product(self, user: User, product: Product):
        pass

    @abstractmethod
    def create_user(self, user: User):
        pass

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def get_order_by_user(self, user: User):
        pass
