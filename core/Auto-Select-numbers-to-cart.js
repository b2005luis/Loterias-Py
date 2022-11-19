
var jogos = [
    [2,	10,	12,	47,	57,	60],
    [4,	8, 15,	50,	53,	60],
    [13, 14, 20, 27, 30, 56],
    [5,	6, 7, 22, 28, 42],
    [2, 5, 7, 26, 44, 52],
    [6, 10,	17,	35, 37,	46],
    [10, 24, 29, 38, 42, 48]
];

function marcarJogo(jogo) {

    jogo.map(function (n) {
        n = (n < 10) ? ("#n0" + n) : ("#n" + n);
        document.querySelector(n).click();
    });

    document.querySelector("#colocarnocarrinho").click();

}


jogos.map(function (jogo) {
    marcarJogo(jogo);
});