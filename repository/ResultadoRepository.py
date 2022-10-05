from sqlite3 import Connection

from repository.SQLiteDatabase import SQLiteDatabase


class MegaSenaResultadoRepository:

    def __init__(self):
        self.database: SQLiteDatabase = SQLiteDatabase(pathname="./../database/Mega-Sena.db")

    def buscar_concurso(self, parametro: int):
        self.database.inicializar_recursos()

        if type(self.database.connection) == Connection:
            try:
                self.database.cursor.execute(
                    "SELECT * FROM Resultados "
                    "WHERE Concurso = ?",
                    [parametro]
                )
                result_set = self.database.cursor.fetchone()
                return result_set
            except Exception as erro:
                print(erro.__str__())
            finally:
                self.database.finalizar_recursos()

    def listar_resultados(self, colunas: str):
        self.database.inicializar_recursos()

        try:
            self.database.cursor.execute(f"SELECT {colunas} FROM Resultados ORDER BY Concurso ASC")
            result_set = self.database.cursor.fetchall()
            return result_set
        except Exception as erro:
            print(erro.__str__())
        finally:
            self.database.finalizar_recursos()

    def cadastrar(self, parametros: list):
        self.database.inicializar_recursos()

        try:
            self.database.cursor.execute(
                "INSERT INTO Resultados VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                parametros
            )
        except Exception as erro:
            print(erro.__str__())
        finally:
            self.database.connection.commit()
            self.database.finalizar_recursos()

    def deletar(self, concurso: any):
        self.database.inicializar_recursos()

        try:
            self.database.cursor.execute(
                "DELETE FROM Resultados WHERE Concurso = ?",
                [concurso]
            )
        except Exception as error:
            print(error.__str__())
        finally:
            self.database.connection.commit()
            self.database.finalizar_recursos()
