
var jogos = [
    [5, 8, 16, 23, 30, 42],
    [6, 9, 20, 24, 30, 43],
    [3, 15, 19, 24, 47, 55],
    [2, 5, 9, 18, 20, 48],
    [1, 7, 16, 19, 25, 60],
    [4, 9, 12, 22, 30, 39]
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