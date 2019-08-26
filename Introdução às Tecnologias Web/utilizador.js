"use strict";

function terminar_sessao(){
    localStorage.removeItem("Jogador_Actual");
    document.getElementById("Jogador_Actual").innerHTML = "Sessão terminada";
}

window.onload = function(){
    if (localStorage.getItem("Jogador_Actual") !== null){
        document.getElementById("terminar_sessao").style.display = 'inline';
        document.getElementById("Jogador_Actual").innerHTML = "Jogador(a): " + localStorage.getItem("Jogador_Actual");
    }
    
    var tabela = document.getElementById("tabela_pontos");

    if (localStorage.getItem("Jogador_Actual") !== null) {
        for(var i = 0; i< localStorage.getItem("valor_pontuacoes"); i++){

            var row = tabela.insertRow(-1);

            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            var cell3 = row.insertCell(2);
            var cell4 = row.insertCell(3);
            var cell5 = row.insertCell(4);
            var cell6 = row.insertCell(5);
            cell1.innerHTML = localStorage.getItem("Jogador_actual" + i);
            cell2.innerHTML = localStorage.getItem("tempo_gasto" + i);
            cell3.innerHTML = localStorage.getItem("certas" +i);
            cell4.innerHTML = localStorage.getItem("pontos" +i);
            cell5.innerHTML = localStorage.getItem("pontuacao_total" + i);
            cell6.innerHTML = localStorage.getItem("modo_jogo" + i);
        }
    }
}
