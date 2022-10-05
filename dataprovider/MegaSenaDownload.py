import requests


class MegaSenaDownload():

    def __init__(self):
        self.request = requests
        self.endpoint: str = "https://redeloteria.com.br/rotinas_01/arquivos_txt/tx_megasena_todos_resultados.txt"
        self.data: list

    def buscar_resultados(self):
        temp_data = self.request.get(
            self.endpoint,
            headers={"content-type": "application/json"}
        )
        self.data = temp_data.json()["data"]
