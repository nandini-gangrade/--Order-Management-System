# db_property_util.py

class DBPropertyUtil:
    @staticmethod
    def get_connection_string():
        try:
            # Construct the connection string
            conn_str = (
                r"DRIVER={SQL Server};"
                r"SERVER=DESKTOP-K702Q3Q\SQLEXPRESS09;"
                r"DATABASE=Order_Management_System;"
                r"Trusted_Connection=yes;"
            )
            
            return conn_str
        except Exception as e:
            print("Error constructing connection string:", e)
            return None
