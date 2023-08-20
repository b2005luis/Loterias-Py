from repository.MySQLDatabase import MySQLDatabase


class ApostaCandidataRepository():

    def __init__(self, database: MySQLDatabase = None):
        self.database: MySQLDatabase = database

    def cadastrar_aposta_candidata(self, parametros: list, previsao: any):
        if self.database.is_connected():
            try:
                parametros_list: list = list()
                parametros_list.append(None)
                parametros_list.extend(parametros)
                parametros_list.append(previsao)

                cursor = self.database.connection.cursor()
                cursor.execute(
                    operation="INSERT INTO Apostas_Candidatas "
                              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    params=tuple(parametros_list)
                )
            except Exception as erro:
                print(erro.__str__())
            finally:
                self.database.connection.commit()
                cursor.close()
        else:
            print("A base de dados não esta conectada")
