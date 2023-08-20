import requests

from enumerator.TipoLoteria import TipoLoteria


class LoteriaApi():

    def __init__(self, tipo_sorteio: TipoLoteria):
        self.endpoint: str = f"https://servicebus2.caixa.gov.br/portaldeloterias/api/{tipo_sorteio.value}"
        self.dadoa: dict = {}

    def buscar_resultado(self, numero_concurso=""):
        temp_data = requests.get(
            f"{self.endpoint}/{numero_concurso}",
            headers={
                "content-type": "application/json",
                "origin": "https://servicebus2.caixa.gov.br"
            },
            verify=False
        ).json()

        self.dadoa = {
            "numeroConcurso": temp_data["numero"],
            "ultimoConcurso": temp_data["ultimoConcurso"],
            "numeroConcursoAnterior": temp_data["numeroConcursoAnterior"],
            "numeroConcursoProximo": temp_data["numeroConcursoProximo"],
            "dataApuracao": temp_data["dataApuracao"],
            "listaDezenas": temp_data["listaDezenas"],
            "Ganhadores": {
                "Sena": {
                    "Acertos": temp_data["listaRateioPremio"][0]["numeroDeGanhadores"],
                    "Premio": float(temp_data["listaRateioPremio"][0]["valorPremio"])
                },
                "Quina": {
                    "Acertos": temp_data["listaRateioPremio"][1]["numeroDeGanhadores"],
                    "Premio": float(temp_data["listaRateioPremio"][1]["valorPremio"])
                },
                "Quadra": {
                    "Acertos": temp_data["listaRateioPremio"][2]["numeroDeGanhadores"],
                    "Premio": float(temp_data["listaRateioPremio"][2]["valorPremio"])
                }
            }
        }
        return self.dadoa
