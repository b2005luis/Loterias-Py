
var jogos = [
    [1, 2, 14, 15, 26, 50],
    [2, 4, 11, 18, 29, 33],
    [6, 14, 26, 27, 57, 60],
    [7, 12, 18, 27, 50, 57],
    [12, 18, 50, 52, 57, 58],
    [13, 14, 24, 27, 29, 60],
    [18, 26, 50, 52, 54, 57]
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