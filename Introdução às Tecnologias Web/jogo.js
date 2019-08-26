"use strict";

//Var que contem 3 conjuntos de palavras para cada modo, fácil, intermédio e difícil.
var biblioteca_palavras = [["jogo", "batata",  "macaco", "casa", "segurança", "portugal", "rato", "computador", "samba", "pato", "arroz", "bola", "janota", "vida", "felicidade", "alcunha", "rosa", "fada", "princesa", "pimenta", "leite", "alfaiate"], ["permuta", "petiz", "justiça", "governo", "dedal", "teclado", "frutaria", "lacoste", "amizade", "titulares", "veiculo", "escocia", "luxemburgo", "gravata", "suporte", "lenço", "quinze", "andorinha", "feitiço", "pardal", "conjunto", "dezembro"], ["fugaz", "pedante", "criogenia", "terbio", "sensatez", "testosterona", "oftalmologista", "hidromedicina", "otorrinolaringologista", "atormentamento", "agulheta", "desodorizante", "rubicundo", "empedernido", "idiossincrasia", "metamorfismo", "ibuprofeno", "ametista", "oncologia", "tuberculose", "manteigueira", "posologia"]];

var chars = "abcdefghijlmnopqrstuvxz";
var resultado = [];
var resultado_vazio = [];
var modo = ["Fácil", "Intermédio", "Difícil"];
var tempo_dificuldade = [480, 240, 120];
var tentativas;
var vencer = 0;
var partes = 1;
var perdeu = false;
var venceu = false;
var duracao;
var modos_jogo_aleatorio;
var palavra;
var minutes;
var seconds;
var letra;
var palavraEscolhida;
var pontuacao = 0;
var certas = 0;

var teclado = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'x', 'z', 'ç'];

function terminar_sessao() { 
    localStorage.removeItem("Jogador_Actual");
    document.getElementById("Jogador_Actual").innerHTML = "Sessão terminada";
}

//função do tempo para o modo normal
function startTimer() {
    var display = document.querySelector("#time");
    var modos_jogo = document.getElementById("modos").options[modos.selectedIndex].value;
    duracao = tempo_dificuldade[modos_jogo];
    var timer = duracao;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            document.getElementById("tempo").innerHTML = "O tempo terminou!";
            document.getElementById(partes).style.display = 'none';
            tentativas = 0;
            document.getElementById("derrota").play();
            document.getElementById("hipoteses").innerHTML = "Tentativas Restantes: " + tentativas
            estado();
            document.getElementById("teclado").hidden = true; 
            document.getElementById("jogar").hidden = true;

            document.getElementById(11).style.display = 'block';
        }
    }, 1000);
}

//função do tempo para o modo aleatório
function startTimer_aleatorio() {
    var display = document.querySelector("#time");
    var modos_jogo = document.getElementById("modos").options[modos.selectedIndex].value;
    duracao = tempo_dificuldade[modos_jogo];
    var timer = duracao;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            document.getElementById("tempo").innerHTML = "O tempo terminou!";
            document.getElementById(partes).style.display = 'none';
            tentativas = 0;
            document.getElementById("derrota").play();
            document.getElementById("audio").pause();
            document.getElementById("hipoteses").innerHTML = "Tentativas Restantes: " + tentativas
            estado();
            document.getElementById("teclado").hidden = true; 
            document.getElementById("jogar").hidden = true;

            document.getElementById(11).style.display = 'block';
        }
    }, 1000);
}


// função main para escolher uma palavra qualquer consoante o modo de dificuldade, para o modo normal
function main() {
    var modos_jogo = document.getElementById("modos").options[modos.selectedIndex].value;
    palavra = biblioteca_palavras[modos_jogo];
    tentativas = 10;
    palavraEscolhida = palavra[Math.floor(Math.random() * palavra.length)];
    resultado = palavraEscolhida.split("");

    for (var elemento in resultado) {
        resultado_vazio.push("_");
    }
    
    document.getElementById("palavra").innerHTML = resultado_vazio.join(' '); // dá a palavra sem as virgulas
    document.getElementById("hipoteses").innerHTML = "Tentativas Restantes: " + tentativas; 
    document.getElementById("recomeçar").hidden = false; 
    document.getElementById("audio").play();
    document.getElementById("jogar").hidden = true;
    document.getElementById("modo_alt").hidden = true;
    document.getElementById("modos").hidden = true;
    document.getElementById("pontuacao").innerHTML ="Pontuação: 0";
}

// funçãao main para escolher uma palavra qualquer consoante o modo de dificuldade, para o modo aleatório
function modo_aleatorio() {
    var modos_jogo = document.getElementById("modos").options[modos.selectedIndex].value;
    palavra = biblioteca_palavras[modos_jogo];
    tentativas = 10;
    palavraEscolhida = palavra[Math.floor(Math.random() * palavra.length)]
    resultado = palavraEscolhida.split("");
    console.log(palavraEscolhida);
    for (var elemento in resultado) {
        resultado_vazio.push("_");
    }
    
    document.getElementById("palavra").innerHTML = resultado_vazio.join(' '); // da a palavra sem as virgulas
    document.getElementById("hipoteses").innerHTML = "Tentativas Restantes: " + tentativas; // adiciona o numero de tentativas as tentativas
    document.getElementById("audio").play();
    var chars = "abcdefghijlmnopqrstuvxz";
    letra = (chars.substr( Math.floor(Math.random() * chars.length), 1));
    document.getElementById("aleatoria").innerHTML = "Tentar a letra " + letra + "?";
    document.getElementById("pontuacao").innerHTML ="Pontuação: 0";
}

// função que dá a letra aleatória no modo aleatório
function letra_aleatoria() {
    letra = (chars.substr( Math.floor(Math.random() * chars.length), 1));
    while (document.getElementById("aleatoria").innerHTML === "Tentar a letra " + letra + "?"){
            letra = (chars.substr( Math.floor(Math.random() * chars.length), 1));
    }
    document.getElementById("aleatoria").innerHTML = "Tentar a letra " + letra + "?";
    if (perdeu == true || venceu == true) {
        document.getElementById("aleatoria").innerHTML = "";
    }
    
}

function letra_aleatoria_aceite() {
    var tryer = 0;
    for (var i = 0; i < resultado.length; i++) {
        if (resultado[i] === letra) {
            resultado_vazio[i] = letra;
            tryer++;
            vencer++;
            var index = chars.indexOf(letra);
            chars = chars.replace(letra,"");
            pontuacao += 10;
            certas += 1;
        }
    }
        if (tryer === 0) {
            chars = chars.replace(letra,"");
            partes += 1;
            tentativas--;
            document.getElementById("hipoteses").innerHTML = "Tentativas Restantes: " + tentativas;
            document.getElementById(partes - 1).hidden = true;
            document.getElementById(partes).hidden = false;
            if(pontuacao !== 0){
                pontuacao -= 1;
            }
        }
        if (tentativas === 0) {
            perdeu = true;
            document.getElementById("aleatoria").innerHTML = "";
            estado();
        }
    document.getElementById("palavra").innerHTML = resultado_vazio.join(' ');
    document.getElementById("pontuacao").innerHTML ="Pontuação: " + pontuacao;
    estado();
}

//função para criar o teclado
function teclado_html(){
    var localTeclado = document.getElementById("teclado");
    for (var i = 0; i < teclado.length; i++) {
        var z = document.createElement('div');
        z.className = "letra";
        z.id = teclado[i];
        z.innerHTML = teclado[i];

        z.onclick = function () {
            verLetra(this.id); //cada clique de uma letra faz com que se execute esta função
        }
        localTeclado.appendChild(z);
    }
}

//indica o estado - se o jogador ganhou ou perdeu
function estado() {
    if (vencer === resultado.length) {
        if(localStorage.getItem("valor_pontuacoes") === null ){
            localStorage.setItem("valor_pontuacoes", 0);
        }
        document.getElementById("audio").pause();
        document.getElementById("aleatoria").innerHTML = "";
        document.getElementById("vencer").innerHTML = "Parabéns, ganhou o jogo!";
        venceu = true;
        document.getElementById("ganhou").play();
        document.getElementById("verPontos").hidden = false;
        var minutos = minutes;
        var segundos = seconds;
        var TJogo = duracao - (minutos * 60 + segundos);
        document.getElementById("tempo").innerHTML = "Voce demorou " + (Math.floor(TJogo/60)) + " minutos " + (TJogo%60) + " segundos" ;
        document.getElementById('letra_al_sim').style.display = "none";
        document.getElementById('letra_al_nao').style.display = "none";
        
        localStorage.setItem("Jogador_actual" + localStorage.getItem("valor_pontuacoes"), localStorage.getItem("Jogador_Actual"));
        localStorage.setItem("tempo_gasto" + localStorage.getItem("valor_pontuacoes"),(Math.floor(TJogo/60)) + " minutos " + (TJogo%60) + " segundos");
        localStorage.setItem("certas" + localStorage.getItem("valor_pontuacoes"), certas);
        localStorage.setItem("pontuacao_total" + localStorage.getItem("valor_pontuacoes"), pontuacao);
        localStorage.setItem("modo_jogo" + localStorage.getItem("valor_pontuacoes"), modo[document.getElementById("modos").options[modos.selectedIndex].value]);
        localStorage.setItem("pontos" + localStorage.getItem("valor_pontuacoes"), 10 - tentativas);                 
        localStorage.setItem('valor_pontuacoes', parseInt(localStorage.getItem('valor_pontuacoes')) + 1 );      
    }
    if (tentativas === 0) {  
        document.getElementById("aleatoria").innerHTML = "";
        document.getElementById("perder").innerHTML = "Ups, parece que PERDESTE :( a palavra correta era " + palavraEscolhida;
        document.getElementById('jogar').hidden = true;
        document.getElementById("audio").pause();
        document.getElementById("derrota").play();
        document.getElementById("tempo").innerHTML = "";
        document.getElementById('letra_al_sim').style.display = "none";
        document.getElementById('letra_al_nao').style.display = "none";
    }
}

//verifica se a letra que se escolheu corresponde a palavra
function verLetra(id_da_letra) {
    if(venceu === true || perdeu === true){
        alert("Desculpa o jogo já acabou, no entanto podes jogar de novo :)");
    }
    else{
        var x = id_da_letra;
        var elementoId = document.getElementById(x);
        elementoId.onclick = ''; // remove o on click da determinada letra
        var tryer = 0;
        for (var i = 0; i < resultado.length; i++) {
            if (resultado[i] === x) {
                resultado_vazio[i] = x;
                elementoId.className = "letra_vista_certa";
                tryer++;
                vencer++;
                pontuacao += 10;
                certas += 1;
            }
        }
        if (tryer === 0) {
            partes += 1;
            tentativas--;
            if(pontuacao !== 0){
                pontuacao -= 1;
            }
            elementoId.className = "letra_vista_errada";
            document.getElementById("hipoteses").innerHTML = "Tentativas Restantes: " + tentativas;
            document.getElementById(partes - 1).hidden = true;
            document.getElementById(partes).hidden = false;
        }

        if (tentativas === 0) {
            perdeu = true;
        }
        document.getElementById("palavra").innerHTML = resultado_vazio.join(' ');
        document.getElementById("pontuacao").innerHTML ="Pontuação: " + pontuacao;
        estado();
    }
}

function reset(){
    main();
}

//quando a janela carregar tudo executa estas primeiras funções
window.onload = function(){
    teclado_html();
    if (localStorage.getItem("Jogador_Actual") !== null){
        document.getElementById("terminar_sessao").style.display = 'inline';
        document.getElementById("Jogador_Actual").innerHTML = "Jogador: " + localStorage.getItem("Jogador_Actual");
    }
    else{
        alert("Você pode jogar sem iniciar sessão, porém as suas pontuações não serão guardadas na tabela das pontuações.");
    }
}