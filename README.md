# Loterias-Py

### Intridução

Nesse projeto, estamos desenvolvendo a ideia de um chutador inteligente de números para jogar na loteria._

A lógica de funcionamento é basicamente em uma base de dados histórica que tem os resultados da Mega Sena desde 1995.ega 

Os jogos mais recentes são expurgados do template de números chutáveis, baseados em um parâmetro com a quantidade, e retirado do modelo de chutes, que é a base de, no caso da Mega Sena, um conjunto de números que vai de 01 a 60.

Após isso, foi usada uma rede neural Back Propagation, com 6 pontos de entrada, uma camada de neurônios que ainda está em fase de teste e uma saída com a probabilidade que sinaliza se a aposta pode ou não ser uma ganhadora.

Após rodar o fit/treinamento do modelo, o script deve gerar um conjunto de 6 números aleatórios.

A validação se dá inicialmente pela ativação da rede, que por sua vez, dá uma probabilidade de aquela aposta ser ou não, um ganhador.

Ao Passar dessa fase de validação, a aposta passa por uma validação de duplicidade em apostas anteriores, por exemplo:

Uma aposta candidata: 01  02  03  04  05  06

Ao passar pela validação, não deve conter mais do que o parâmetro de limite de duplicidade de números em uma aposta já acorrida.

Se houvesse a aposta  01  02  10  11 12  13, a aposta candidata seria descartada, caso o limite de duplicidade fosse 1 ou 2.

Caso estas etapas sejam satisfatórias, a aposta é gravada em uma tabela de apostas candidatas.

### Track Record - Alguns resultados do uso

É bom deixar claro que a probabilidade de ocorrer um acerto é bem pequena, pois a estatística daria algo em torno de: 
60 * 59 * 58 * 57 * 56 * 55 =  36.045.979.200 de combinações possíveis para uma aposta.

Além disso todos os números voltam para o globo para um novo sorteio, o que faz retornar as possibilidades ao estado inicial.

Mesmo assim houveram duas apostas com 4 acertos, dando um total de +/- R$ 1.700,00

Veja algumas imagens do 1º teste:

Nesse primeiro caso, onde foi feita uma aposta na teimosinha com 8 recorrências, houve uma acertividade em torno de 8 para 1, totalizando as chances de 12,5% de ganhar algum prêmio.

<br>
![Resultado](/track-record/2022-06-25-1-Resultado.png)

![Aposta-premiada](/track-record/2022-06-25-2-Aposta-Premiada.png)

<br>
No segundo caso, onde foram feitas 5 apostas,  houve uma acertividade em torno de 5 para 1, totalizando as chances de 20,0% de ganhar algum prêmio.

![resuktadi-2](/track-record/2022-10-01-1-Resultado.png)

![aposta-premiada-2](/track-record/2022-10-01-2-Aposta-Premiada.png)

> Mais uma vez, é bom deixar claro que são 60 bolas, de mesmo tamanho, peso, e que retornam para o globo após cada sorteio, o que acaba não dando nenhuma garantia de que este método tenha êxito, pois a estatística prevalece.

### Dependências

* Pythom >= 3
  > [Instalar o Python 3](https://www.python.org/downloads)
* PyBrain3 >= 3.0.4
  > `python -m pip install pybrain3`
* Pamdas >= 1.4.1
  > `python -m pip install pandas`
* Requests >= 2.27.1
  > `python -m pip install requests`
* MySQL Connector Python 8.0.30
  > `python -m pip install mysql-connector-python`
