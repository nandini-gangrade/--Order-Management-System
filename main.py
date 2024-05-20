from dao import OrderProcessor
from entity import User, Product

class OrderManagement:
    @staticmethod
    def main():
        order_processor = OrderProcessor()
        while True:
            print("\nOrder Management System")
            print("1. Create User")
            print("2. Create Product")
            print("3. Create Order")
            print("4. Cancel Order")
            print("5. Get All Products")
            print("6. Get Orders by User")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                OrderManagement.create_user(order_processor)

            elif choice == "2":
                OrderManagement.create_product(order_processor)

            elif choice == "3":
                OrderManagement.create_order(order_processor)

            elif choice == "4":
                OrderManagement.cancel_order(order_processor)

            elif choice == "5":
                OrderManagement.get_all_products(order_processor)

            elif choice == "6":
                OrderManagement.get_orders_by_user(order_processor)

            elif choice == "7":
                print("Exiting Order Management System.")
                break

            else:
                print("Invalid choice. Please enter a valid option.")

    @staticmethod
    def create_user(order_processor):
        user_id = int(input("Enter user ID: "))
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter role (Admin/User): ")
        user = User(user_id, username, password, role)
        order_processor.create_user(user)
        print("User created successfully.")

    @staticmethod
    def create_product(order_processor):
        product_id = int(input("Enter product ID: "))
        product_name = input("Enter product name: ")
        description = input("Enter description: ")
        price = float(input("Enter price: "))
        quantity_in_stock = int(input("Enter quantity in stock: "))
        type_ = input("Enter type (Electronics/Clothing): ")
        if type_ not in ['Electronics', 'Clothing']:
            print("Invalid product type. Please enter 'Electronics' or 'Clothing'.")
            return
        if type_ == 'Electronics':
            brand = input("Enter brand: ")
            warranty_period = int(input("Enter warranty period: "))
            product = Product(product_id, product_name, description, price, quantity_in_stock, type_, brand=brand, warranty_period=warranty_period)
        else:
            size = input("Enter size: ")
            color = input("Enter color: ")
            product = Product(product_id, product_name, description, price, quantity_in_stock, type_, size=size, color=color)
        order_processor.create_product(product)
        print("Product created successfully.")

    @staticmethod
    def create_order(order_processor):
        try:
            user_id = int(input("Enter user ID: "))
            num_products = int(input("Enter the number of products: "))
            products = []
            for _ in range(num_products):
                product_id = int(input("Enter product ID: "))
                quantity = int(input("Enter quantity: ")) 
                product = Product(product_id, None, None, None, None, None) 
                product.set_quantity(quantity)  
                products.append(product)
            
            order_processor.create_order(user_id, products)
            print("Order created successfully.")
        except Exception as e:
            print("Error creating order:", e)

    @staticmethod
    def cancel_order(order_processor):
        user_id = int(input("Enter user ID: "))
        order_id = int(input("Enter order ID: "))
        order_processor.cancel_order(user_id, order_id)
        print("Order cancelled successfully.")

    @staticmethod
    def get_all_products(order_processor):
        products = order_processor.get_all_products()
        print("\nAll Products:")
        for product in products:
            print(product)

    @staticmethod
    def get_orders_by_user(order_processor):
        user_id = int(input("Enter user ID: "))
        user = User(user_id, None, None, None) 
        orders = order_processor.get_order_by_user(user)
        print(f"\nOrders for User ID {user_id}:")
        for order in orders:
            print(order)

if __name__ == "__main__":
    OrderManagement.main()
