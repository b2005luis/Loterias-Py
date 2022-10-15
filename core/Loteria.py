from random import sample


class Loteria:

    def __init__(self, quantidade_numeros: int = 6, quantidade_apostas: int = 7):
        self.quantidade_numeros = quantidade_numeros
        self.template_aposta: list = list()
        self.aposta_candidata: list = list()
        self.apostas: list = list()
        self.quantidade_apostas: int = quantidade_apostas

    def set_template_aposta(self, primeiro_numero: int = 1, ultimo_numero: int = 60):
        self.template_aposta = list(range(primeiro_numero, (ultimo_numero + 1), 1))

    def expurgar_template_chute(self, dataset: list, expurga_ultimos_jogos: int = 1):
        k = dataset.__len__()
        for j in dataset[(k - expurga_ultimos_jogos):]:
            for z in j[:self.quantidade_numeros]:
                if self.template_aposta.__contains__(z):
                    self.template_aposta.remove(z)
                    print(f"REMOVER {z}")
        print("\n")

    def gerar_aposta(self):
        aposta = sample(self.template_aposta, self.quantidade_numeros)
        return sorted(aposta, reverse=False)

    def mostrar_apostas_selecionadas(self):
        print("\n[")
        for aposta in self.apostas.__iter__():
            print(f"   {aposta},")
        print("]")
