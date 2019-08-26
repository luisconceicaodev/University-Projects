"use strict";
if(localStorage.getItem("valor_index") === null ){
    localStorage.setItem("valor_index", 0);
}

function registo(){
    var utilizador = document.forms.registration.elements.userid.value;
    var password = document.forms.registration.elements.passid.value;
    var email = document.forms.registration.elements.email.value;
    var genero = document.forms.registration.elements.genero.value;
    
    localStorage.setItem("utilizador_"+localStorage.getItem("valor_index"), utilizador);
    localStorage.setItem("password_" + localStorage.getItem("valor_index"), password);
    localStorage.setItem("email_" + localStorage.getItem("valor_index"), email);
    localStorage.setItem("genero_" + localStorage.getItem("valor_index"), genero);
    
    localStorage.setItem('valor_index', parseInt(localStorage.getItem('valor_index')) + 1 );
    alert("Já estás registado/a, agora é só fazeres o login.");

}