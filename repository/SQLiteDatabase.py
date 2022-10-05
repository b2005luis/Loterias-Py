import sqlite3
from sqlite3 import Connection, Cursor


class SQLiteDatabase:

    def __init__(self, pathname: str):
        self.pathname = pathname
        self.connection: Connection
        self.cursor = Cursor

    def inicializar_recursos(self):
        try:
            self.connection = sqlite3.connect(self.pathname)
            self.cursor = self.connection.cursor()
        except Exception as error:
            print(error.__str__())

    def finalizar_recursos(self):
        self.cursor.close()
        self.connection.close()
