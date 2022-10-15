
var jogos = [
    [5,	20,	25,	30,	33,	54],
    [2,	7,	10,	20,	26,	44],
    [5,	26,	42,	47,	49,	58],
    [21, 28, 30, 39, 42, 55],
    [7,	20,	30,	37,	50,	57],
    [3,	13,	33,	46,	51,	58],
    [9, 17, 27, 35, 36, 44]
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