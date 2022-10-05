
var jogos = [];


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