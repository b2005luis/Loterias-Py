
let jogos = [
   [3, 11, 13, 18, 32, 36],
   [1, 3, 8, 16, 42, 48],
   [1, 10, 18, 39, 45, 46],
   [4, 13, 17, 37, 46, 53],
   [2, 5, 14, 18, 21, 55],
   [13, 36, 41, 43, 48, 57]
];

async function marcarJogo(jogo) {
    setTimeout(() => {
        jogo.map(function (n) {
            n = (n < 10) ? ("#n0" + n) : ("#n" + n);
            document.querySelector(n).click();
        });
        document.querySelector("#colocarnocarrinho").click();
    }, 5000);
}

jogos.map(function (jogo) {
    return marcarJogo(jogo);
});
