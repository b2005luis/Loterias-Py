let jogos = [
    [3, 6, 7, 9, 20, 56],
    [4, 10, 16, 33, 41, 46],
    [7, 13, 17, 21, 27, 39],
    [17, 28, 33, 49, 58, 59]
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
