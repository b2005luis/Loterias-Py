# Loterias-Py

### Intridução

Nesse projeto, estamos desenvolvendo a ideia inteligente de números para jogar na loteria._

A lógica de funcionamento é basicamente em uma base de dados histórica que tem os resultados da Mega Sena desde 1995.ega 

Os jogos mais recentes são expurgados baseados em um parâ,etro com a quantidade, e retirado do modelo de chutes, que é a base de, no caso da Mega Sena, um conjunto de números que vai de 01 a 60.

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

Além disso todos os nímeros voltam para o globo para um novo sorteio.

Mesmo assim houveram duas aposta com 4 acertos, dando um total de +/- R$ 1.700,00

Veja algumas imagens do 1º teste:

![Resultado](./track-record/2022-08-25-Na-Pratica-Resultado-001.png)

![Aposta premiada](./track-record/2022-08-25-Na-Pratica-Resultado-002.png)

![Valor do prêmio](./track-record/2022-08-25-Na-Pratica-Resultado-003.png)

Veja algumas imagens do teste após várias regulagens de parâmetros:

![Resultado](./track-record/2022-08-25-Na-Pratica-Resultado-001.png)

![Resultado](./track-record/2022-08-25-Na-Pratica-Resultado-001.png)

![Resultado](./track-record/2022-08-25-Na-Pratica-Resultado-001.png)

### Dependências

* Pythom >= 3
* PyBrain3 >= 3.0.4
* Pamdas >= 1.4.1
