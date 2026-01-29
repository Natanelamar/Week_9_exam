import mysql.connector
import os

class Sql_connector:
    def __init__(self):
        self.connection = mysql.connector.connect(
                host=os.getenv('MYSQL_HOST','mysql'),
                user=os.getenv('MYSQL_USER','root'),
                password=os.getenv('MYSQL_PASSWORD','rootpassword'),
                database = os.getenv('MYSQL_DATABASE','classicmodels'),
                use_pure=True
            )
        self.cursor = self.connection.cursor()

    def get_info(self, qury):
        self.cursor.execute(qury) 
        info = self.cursor.fetchall()
        self.cursor.close()
        return info
   
        