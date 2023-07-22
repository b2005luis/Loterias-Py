from repository.MySQLDatabase import MySQLDatabase


class MegaSenaResultadoRepository:

    def __init__(self, database: MySQLDatabase = None):
        self.database: MySQLDatabase = database

    def buscar_concurso(self, parametro: int):
        if self.database.is_connected():
            try:
                cursor = self.database.connection.cursor()
                cursor.execute(
                    operation="SELECT * FROM Resultados "
                              "WHERE Concurso = %s",
                    params=tuple([parametro])
                )
                result_set = cursor.fetchone()
                return result_set
            except Exception as erro:
                print(erro.__str__())
            finally:
                cursor.close()
        else:
            print("A base de dados não está conectada")

    def listar_resultados(self, colunas: str):
        if self.database.is_connected():
            try:
                cursor = self.database.connection.cursor()
                cursor.execute(
                    operation=f"SELECT {colunas} FROM Resultados ORDER BY Concurso ASC"
                )
                result_set = cursor.fetchall()
                return result_set
            except Exception as erro:
                print(erro.__str__())
            finally:
                cursor.close()
        else:
            print("A base de dados não está conectada")

    def listar_ultimo(self, colunas: str):
        if self.database.is_connected():
            try:
                cursor = self.database.connection.cursor()
                cursor.execute(
                    operation=f"SELECT TOP 1 {colunas} FROM Resultados ORDER BY Concurso DESC"
                )
                result_set = cursor.fetchone()
                return result_set
            except Exception as erro:
                print(erro.__str__())
            finally:
                cursor.close()
        else:
            print("A base de dados não está conectada")

    def cadastrar(self, parametros: list):
        if self.database.is_connected():
            try:
                cursor = self.database.connection.cursor()
                cursor.execute(
                    operation="INSERT INTO Resultados VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    params=parametros
                )
            except Exception as erro:
                print(erro.__str__())
            finally:
                cursor.close()
        else:
            print("A base de dados não está conectada")

    def deletar(self, concurso: int):
        if self.database.is_connected():
            try:
                cursor = self.database.connection.cursor()
                cursor.execute(
                    operation="DELETE FROM Resultados WHERE Concurso = %s",
                    params=tuple([concurso])
                )
            except Exception as error:
                print(error.__str__())
            finally:
                cursor.close()
        else:
            print("A base de dados não está conectada")
