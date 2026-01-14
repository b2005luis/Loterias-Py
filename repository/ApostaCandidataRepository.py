from repository.MySQLDatabase import MySQLDatabase


class ApostaCandidataRepository():

    def __init__(self, database: MySQLDatabase = None):
        self.database: MySQLDatabase = database

    def cadastrar_aposta_candidata(self, aposta_candidata: list, previsao: any):
        if self.database.is_connected():
            cursor = self.database.connection.cursor()
            try:
                parametros: list = list()
                parametros.extend(aposta_candidata)
                parametros.append(previsao)

                cursor.execute(
                    operation="INSERT INTO Apostas_Candidatas "
                              "(Coluna1, Coluna2, Coluna3, Coluna4, Coluna5, Coluna6, Previsao) "
                              "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    params=tuple(parametros)
                )
            except Exception as erro:
                print(erro.__str__())
            finally:
                self.database.connection.commit()
                cursor.close()
        else:
            print("A base de dados não esta conectada")
