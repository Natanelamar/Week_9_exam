import mysql.connector

class Sql_connector:
    def __init__(self):
        self.connection = mysql.connector.connect(
                host='mysql',
                user='root',
                password='rootpassword',
                use_pure=True
            )
        self.cursor = self.connection.cursor()
        