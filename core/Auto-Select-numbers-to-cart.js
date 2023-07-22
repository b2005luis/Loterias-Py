
var jogos = [
    [1, 3, 9, 15, 26, 59],
    [3, 8, 15, 16, 47, 52],
    [2, 7, 31, 36, 40, 59],
    [5, 6, 20, 23, 51, 54],
    [3, 8, 12, 16, 22, 47],
    [1, 8, 15, 20, 46, 51],
    [6, 11, 41, 42, 47, 55]
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