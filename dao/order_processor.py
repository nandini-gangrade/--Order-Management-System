from entity import User, Product
from dao import IOrderManagementRepository
from util import DBConnUtil
from exception import UserNotFoundException, OrderNotFoundException

class OrderProcessor(IOrderManagementRepository):
    def create_order(self, user_id, products):
        try:
            connection = DBConnUtil.get_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM [User] WHERE userId = ?", user_id)
                user_count = cursor.fetchone()[0]
                if user_count == 0:
                    raise UserNotFoundException(f"User with ID {user_id} not found.")

                cursor.execute("INSERT INTO [Order] (UserId, status) OUTPUT INSERTED.OrderId VALUES (?, ?)", user_id, "pending")
                order_id = cursor.fetchone()[0]
                print("Order created successfully with ID:", order_id)
                
                order_product_data = [(order_id, product.get_product_id(), product.get_quantity()) for product in products]
                cursor.executemany("INSERT INTO OrderDetails (OrderId, ProductId, quantity) VALUES (?, ?, ?)", order_product_data)

                connection.commit()
                print("Order details added successfully.")

                print("Order created successfully.")
            else:
                print("Failed to connect to the database.")
        except UserNotFoundException as e:
            print("Error creating order:", e)
        except Exception as e:
            print("Error creating order:", e)
        finally:
            if connection:
                connection.close()


    def cancel_order(self, user_id, order_id):
        try:
            connection = DBConnUtil.get_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM [User] WHERE userId = ?", user_id)
                user_count = cursor.fetchone()[0]
                if user_count == 0:
                    raise UserNotFoundException(f"User with ID {user_id} not found.")

                cursor.execute("SELECT COUNT(*) FROM [Order] WHERE userId = ? AND orderId = ?", user_id, order_id)
                order_count = cursor.fetchone()[0]
                if order_count == 0:
                    raise OrderNotFoundException(f"Order with ID {order_id} not found for user {user_id}.")
                
                cursor.execute("DELETE FROM OrderDetails WHERE orderId = ?", order_id)
                
                cursor.execute("DELETE FROM [Order] WHERE userId = ? AND orderId = ?", user_id, order_id)
                connection.commit()
                print("Order cancelled successfully.")
            else:
                print("Failed to connect to database.")
        except UserNotFoundException as e:
            print("Error cancelling order:", e)
        except OrderNotFoundException as e:
            print("Error cancelling order:", e)
        except Exception as e:
            print("Error cancelling order:", e)
        finally:
            if connection:
                connection.close()

    def create_product(self, user, product):
        try:
            connection = DBConnUtil.get_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM [User] WHERE userId = ?", user.get_user_id())
                user_data = cursor.fetchone()
                if user_data:
                    user = User(user_data[0], user_data[1], user_data[2], user_data[3])
                    if user.get_role() != "Admin":
                        print("Error: User is not an admin.")
                        return
                    
                    cursor.execute("INSERT INTO [Product] (productId, productName, description, price, quantityInStock, type) VALUES (?, ?, ?, ?, ?, ?)",
                            product.get_product_id(), product.get_product_name(), product.get_description(), product.get_price(), product.get_quantity_in_stock(), product.get_type())
                    connection.commit()
                    print("Product created successfully.")
                else:
                    print("User not found.")
                    return None
            else:
                print("Failed to connect to database.")
                
        except Exception as e:
            print("Error creating product:", e)
        finally:
            if connection:
                connection.close()

    def create_user(self, user):
        try:
            connection = DBConnUtil.get_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM [User] WHERE userId = ?", user.get_user_id())
                user_count = cursor.fetchone()[0]
                if user_count > 0:
                    print(f"User with ID {user.get_user_id()} already exists.")
                    return
                cursor.execute("INSERT INTO [User] (userId, username, password, role) VALUES (?, ?, ?, ?)",
                               user.get_user_id(), user.get_username(), user.get_password(), user.get_role())
                connection.commit()
                print("User created successfully.")
            else:
                print("Failed to connect to database.")
        except Exception as e:
            print("Error creating user:", e)
        finally:
            if connection:
                connection.close()

    def get_all_products(self):
        try:
            connection = DBConnUtil.get_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM [Product]")
                products = cursor.fetchall()
                return products
            else:
                print("Failed to connect to database.")
                return []
        except Exception as e:
            print("Error retrieving products:", e)
            return []
        finally:
            if connection:
                connection.close()

    def get_order_by_user(self, user):
        try:
            connection = DBConnUtil.get_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM [Order] WHERE userId = ?", user.get_user_id())
                order = cursor.fetchall()
                return order
            else:
                print("Failed to connect to database.")
                return []
        except Exception as e:
            print("Error retrieving order:", e)
            return []
        finally:
            if connection:
                connection.close()

