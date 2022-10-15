from pandas._libs.writers import string_array_replace_from_nan_rep

from dataprovider.MegaSenaDownload import MegaSenaDownload
from mapper import ApostaMapper
from mapper.ApostaMapper import ApostaMapper
from repository.MySQLDatabase import MySQLDatabase
from repository.ResultadoRepository import MegaSenaResultadoRepository


def atualizar_base_historic(database: MySQLDatabase = None):
    download = MegaSenaDownload()
    download.buscar_resultados()

    if database is None:
        database = MySQLDatabase()

    repository = MegaSenaResultadoRepository(database=database)

    for item in download.data:
        concurso = int(item[0])
        aposta = repository.buscar_concurso(concurso)
        if aposta is None:
            entiry = ApostaMapper().to_entity(item)
            repository.cadastrar(entiry)
            print(item)

    database.connection.commit()
