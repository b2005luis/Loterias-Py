import requests


class MegaSenaDownload():

    def __init__(self):
        self.request = requests
        self.endpoint: str = "https://redeloteria.com.br/resultados/fc_imprime_relatorios.php?jogo=MegaSena"
        self.data: list

    def buscar_resultados(self):
        temp_data = self.request.get(
            self.endpoint,
            headers={
                "content-type": "application/json",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
        )
        json_response = temp_data.json()["data"]
        self.data = list(json_response)
