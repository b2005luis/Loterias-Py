from mysql.connector import connect, MySQLConnection


class MySQLDatabase():
    def __init__(self):
        self.host: str = "GZ690UD"
        self.username: str = "megasena_rw"
        self.password: str = "megasena"
        self.database: str = "megasena"
        self.connection: MySQLConnection = None

    def is_connected(self) -> bool:
        connection_status = False
        if self.connection is not None and self.connection.is_connected():
            connection_status = True

        return connection_status

    def open_connection(self):
        try:
            self.connection = connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database
            )
        except Exception as error:
            print(error.__str__())

    def close_connection(self):
        self.connection.close()
