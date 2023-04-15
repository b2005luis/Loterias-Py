
var jogos = [
   [7, 36, 38, 47, 50, 51],
   [19, 26, 39, 41, 57, 59],
   [11, 22, 28, 33, 39, 57],
   [1, 11, 12, 40, 42, 45],
   [26, 30, 36, 37, 41, 60],
   [14, 16, 21, 22, 39, 55],
   [1, 34, 36, 46, 47, 51]
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