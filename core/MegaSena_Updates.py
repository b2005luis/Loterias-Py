from dataprovider.MegaSenaDownload import MegaSenaDownload
from repository.ResultadoRepository import MegaSenaResultadoRepository

def atualizar_base_historic():
    download = MegaSenaDownload()
    download.buscar_resultados()

    repository = MegaSenaResultadoRepository()

    for item in download.data:
        concurso = int(item[0])
        aposta = repository.buscar_concurso(concurso)
        if aposta is None:
            repository.cadastrar(item)
            print(item)
