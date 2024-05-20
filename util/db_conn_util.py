# db_conn_util.py

import pyodbc
from util.db_property_util import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection():
        try:
            conn_str = DBPropertyUtil.get_connection_string()
            if conn_str:
                conn = pyodbc.connect(conn_str)
                return conn
            else:
                return None
        except pyodbc.Error as e:
            print("Error connecting to the database:", e)
            return None
