let jogos = [
   [6, 37, 42, 50, 58, 59],
   [4, 6, 15, 36, 37, 51],
   [7, 22, 40, 52, 54, 56],
   [4, 5, 7, 21, 24, 41],
   [6, 9, 22, 29, 34, 38],
   [2, 4, 36, 38, 45, 46],
   [14, 15, 17, 37, 42, 43],
   [4, 15, 17, 31, 36, 56],
   [8, 11, 20, 48, 51, 53],
   [10, 18, 23, 25, 29, 33]
];

function marcarJogo(jogo) {
    jogo.map(function (n) {
        n = (n < 10) ? ("#n0" + n) : ("#n" + n);
        document.querySelector(n).click();
    });
}

jogos.forEach(function (jogo) {
    marcarJogo(jogo);
    document.querySelector("#colocarnocarrinho").click();
    window.location.href = "https://www.loteriasonline.caixa.gov.br/silce-web/#/mega-sena";
});
