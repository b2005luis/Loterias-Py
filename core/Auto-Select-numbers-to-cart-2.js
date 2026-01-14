let jogos = [
   [5, 10, 15, 18, 26, 56],
   [5, 16, 25, 32, 33, 55],
   [10, 12, 18, 39, 53, 59],
   [6, 7, 13, 22, 32, 45],
   [5, 8, 18, 45, 52, 56],
   [4, 10, 33, 37, 48, 59],
   [5, 13, 20, 33, 48, 55],
   [3, 5, 7, 10, 18, 52],
   [11, 22, 33, 48, 51, 56],
   [5, 6, 12, 17, 21, 56]
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
    window.location.href = "https://www.loteriasonline.caixa.gov.br/silce-web/#/mega-sena/especial";
});
