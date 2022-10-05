from repository.SQLiteDatabase import SQLiteDatabase


class ApostaCandidataRepository():

    def __init__(self):
        self.database: SQLiteDatabase = SQLiteDatabase("./../database/Mega-Sena.db")

    def cadastrar_aposta_candidata(self, parametros: list, previsao: any):
        self.database.inicializar_recursos()

        try:
            parametros_list: list = list()
            parametros_list.extend(parametros)
            parametros_list.append(previsao)

            self.database.cursor.execute(
                "INSERT INTO Apostas_Candidatas VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)",
                parametros_list
            )
        except Exception as erro:
            print(erro.__str__())
        finally:
            self.database.connection.commit()
            self.database.finalizar_recursos()
