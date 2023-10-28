
var jogos = [
    [5, 7, 10, 16, 18, 27],
    [3, 24, 36, 48, 54, 57],
    [3, 14, 16, 24, 49, 58],
    [6, 10, 17, 18, 22, 46],
    [3, 6, 31, 36, 38, 59],
    [3, 11, 12, 19, 36, 54],
    [36, 41, 45, 52, 53, 60],
    [4, 5, 12, 23, 32, 44]
];

async function marcarJogo(jogo) {

    jogo.map(function (n) {
        n = (n < 10) ? ("#n0" + n) : ("#n" + n);
        document.querySelector(n).click();
    });

    document.querySelector("#colocarnocarrinho").click();

}

jogos.map(await function (jogo) {
    marcarJogo(jogo);
});