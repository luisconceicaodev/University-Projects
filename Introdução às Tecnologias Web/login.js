"use strict";

function validate() {
    var utilizador = document.getElementById("utilizador").value;
    var password = document.getElementById("password").value;
    if (utilizador !== "" && password !== "") {
        for (var i = 0; i < localStorage.getItem("valor_index"); i++) {
            var username_storage = localStorage.getItem("utilizador_" + [i]);
            var password_storage = localStorage.getItem("password_" + [i]);

            if (username_storage === utilizador && password_storage === password) {
                localStorage.setItem("Jogador_Actual", utilizador);
                alert("Bem vindo/a " + utilizador);
                document.getElementById("Jogador_Actual").innerHTML = "Jogador: " + localStorage.getItem("Jogador_Actual");
                document.getElementById("terminar_sessao").style.display = 'inline';
            }
        }
        if (localStorage.getItem("Jogador_Actual") === "") {
            alert("Jogador não encontrado ou dados incorrectos.");
        }
    } 
    else {
        alert("Por favor preencher todos os dados necessários para o login.");
    }
}