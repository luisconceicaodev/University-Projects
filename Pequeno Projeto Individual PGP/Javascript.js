"use strict";

function addproject() {
    if (localStorage.getItem("valor_index") === null) {
        localStorage.setItem("valor_index", 0);
    }
    
    var nome = document.forms.novoProjeto.elements.nome.value,
    email = document.forms.novoProjeto.elements.email.value,
    tarefa1 = document.forms.novoProjeto.elements.tarefa1.value;
    
    if (document.getElementById('2') !== null) {
        var tarefa2 = document.forms.novoProjeto.elements.tarefa2.value;
    }
    if (document.getElementById('3') !== null) {
        var tarefa3 = document.forms.novoProjeto.elements.tarefa3.value;
    }
    if (document.getElementById('4') !== null) {
        var tarefa4 = document.forms.novoProjeto.elements.tarefa4.value;
    }
    if (document.getElementById('5') !== null) {
        var tarefa5 = document.forms.novoProjeto.elements.tarefa5.value;
    }
    
    
    localStorage.setItem("projeto_"  + localStorage.getItem("valor_index"), nome);
    localStorage.setItem("email_" + localStorage.getItem("valor_index"), email);
    localStorage.setItem("tarefa1_" + localStorage.getItem("valor_index"), tarefa1);
    localStorage.setItem("numberOfTarefas_" + localStorage.getItem("valor_index"), 1);
    if (tarefa2 !== null && tarefa2 !== "" && tarefa2 !== undefined) {
        localStorage.setItem("tarefa2_" + localStorage.getItem("valor_index"), tarefa2);
        localStorage.setItem("numberOfTarefas_" + localStorage.getItem("valor_index"), 2);
    }
    if (tarefa3 !== null && tarefa3 !== "" && tarefa3 !== undefined) {
        localStorage.setItem("tarefa3_" + localStorage.getItem("valor_index"), tarefa3);
        localStorage.setItem("numberOfTarefas_" + localStorage.getItem("valor_index"), 3);
    }
    
    if (tarefa4 !== null && tarefa4 !== "" && tarefa4 !== undefined) {
        localStorage.setItem("tarefa4_" + localStorage.getItem("valor_index"), tarefa4);
        localStorage.setItem("numberOfTarefas_" + localStorage.getItem("valor_index"), 4);
    }
    
    if (tarefa5 !== null && tarefa5 !== "" && tarefa5 !== undefined) {
        localStorage.setItem("tarefa5_" + localStorage.getItem("valor_index"), tarefa5);
        localStorage.setItem("numberOfTarefas_" + localStorage.getItem("valor_index"), 5);
    }
    localStorage.setItem("projeto_selecionado", localStorage.getItem("valor_index"));
    
    localStorage.setItem('valor_index', parseInt(localStorage.getItem('valor_index')) + 1);
    alert("Projeto e tarefas registadas.");
}

var clicks = 1;
function addTarefa() {
    clicks++;
    if (clicks <= 5) {
        var nova_label = document.createElement('label');
        var nova_tarefa = document.createElement('input');
        nova_label.innerHTML = "<p>Tarefa " + clicks + ":</p>";
        nova_tarefa.type = "text";
        nova_tarefa.name= "tarefa" + clicks;
        nova_label.for = "tarefa" + clicks;
        nova_tarefa.required = true;
        nova_tarefa.id = clicks;
        document.getElementById('new_tar_label').appendChild(nova_label);
        document.getElementById('new_tar_label').appendChild(nova_tarefa);
        if (clicks == 5) {
            document.getElementById("addtar").style.visibility = "hidden";
        }
    }
}

function enable(x) {
    var terminar_id = parseInt(x) + 5;
    document.getElementById(terminar_id).removeAttribute('disabled');
}

function disable_all(y) {
    var terminar_id = parseInt(y);
    var iniciar_id = parseInt(y) - 5;
    document.getElementById(terminar_id).disabled = true;
    document.getElementById(iniciar_id).disabled = true;
}

function start_date(t1) {
    var start_date_var = new Date();
    var date1_string = start_date_var.getDate() + "/" + (start_date_var.getMonth() + 1) + "/" + start_date_var.getFullYear() + " - " + start_date_var.getHours() + ":" + start_date_var.getMinutes() + ":" + start_date_var.getSeconds();
    var storage_string = start_date_var.getDate() + "/" + (start_date_var.getMonth() + 1) + "/" + start_date_var.getFullYear() + "/" + start_date_var.getHours() + "/" + start_date_var.getMinutes() + "/" + start_date_var.getSeconds();
    var p_start = document.createElement('p');
    p_start.innerHTML = "Tarefa " + t1 + " iniciada às: " + date1_string;
    document.getElementById('tempo').appendChild(p_start);
    localStorage.setItem("tarefa" + t1 + "_" + localStorage.getItem("projeto_selecionado") + "_start" , storage_string);
}

function end_date(t2) {
    var date_end = new Date();
    var p_end = document.createElement('p');
    var date2_string = date_end.getDate() + "/" + (date_end.getMonth() + 1) + "/" + date_end.getFullYear() + " - " + date_end.getHours() + ":" + date_end.getMinutes() + ":" + date_end.getSeconds();
    var storage_string = date_end.getDate() + "/" + (date_end.getMonth() + 1) + "/" + date_end.getFullYear() + "/" + date_end.getHours() + "/" + date_end.getMinutes() + "/" + date_end.getSeconds();
    p_end.innerHTML = "Tarefa " + (parseInt(t2) - 5) + " terminada às: " + date2_string;
    document.getElementById('tempo').appendChild(p_end);
    
    localStorage.setItem("tarefa" + (parseInt(t2) -5) + "_" + localStorage.getItem("projeto_selecionado") + "_end" , storage_string);
    var time1 = localStorage.getItem("tarefa" + (parseInt(t2) - 5) + "_" + localStorage.getItem("projeto_selecionado") + "_start");
    var split = time1.split("/");
    var date_start = new Date(split[1]+"/"+split[0]+"/"+split[2]+" "+split[3]+":"+split[4]+":"+split[5]);
    
    // get total seconds between the times
    var delta = Math.abs(date_end - date_start) / 1000;

    // calculate (and subtract) whole days
    var days = Math.floor(delta / 86400);
    delta -= days * 86400;

    // calculate (and subtract) whole hours
    var hours = Math.floor(delta / 3600) % 24;
    delta -= hours * 3600;

    // calculate (and subtract) whole minutes
    var minutes = Math.floor(delta / 60) % 60;
    delta -= minutes * 60;

    // what's left is seconds
    var seconds = Math.round(delta % 60);
    
    localStorage.setItem("tarefa" + (parseInt(t2) - 5 + "_" + localStorage.getItem("projeto_selecionado") + "_total"), days + "/" + hours + ":" + minutes + ":" + seconds);  
    var p_total = document.createElement('p');
    if (days == 0) {
        p_total.innerHTML = "O utilizador " + localStorage.getItem(parseInt(t2) - 5) + " realizou a tarefa " + (parseInt(t2) - 5) + " em " + hours + " horas " + " , " + minutes + "minutos, " + seconds + ".";
        p_total.style = "font-weight: bold";
        if (hours == 0) {
            p_total.innerHTML = "O utilizador " + localStorage.getItem(parseInt(t2) - 5) + " realizou a tarefa " + (parseInt(t2) - 5) + "  em " + + minutes + "minutos, " + seconds + ".";
            p_total.style = "font-weight: bold";
            if (minutes == 0) {
                p_total.innerHTML = "O utilizador " + localStorage.getItem(parseInt(t2) - 5) + " realizou a tarefa " + (parseInt(t2) - 5) + " em " + + seconds + " segundos.";
                p_total.style = "font-weight: bold";
            }
        }
    }
    document.getElementById('tempo').appendChild(p_total);
    
    
    if (localStorage.getItem("total_projeto_" + localStorage.getItem("projeto_selecionado")) === null) {
        localStorage.setItem("total_projeto_" + localStorage.getItem("projeto_selecionado"), Math.round((Math.abs(date_end - date_start) / 1000)));
    }else{
        var total_before = localStorage.getItem("total_projeto_" + localStorage.getItem("projeto_selecionado"));
        var total_now = parseInt(total_before) + Math.round((Math.abs(date_end - date_start) / 1000));
        localStorage.setItem("total_projeto_" + localStorage.getItem("projeto_selecionado"), total_now);
    }
    
    document.getElementById("total_proj").innerHTML = "Tempo total gasto no projeto: " + localStorage.getItem("total_projeto_" + localStorage.getItem("projeto_selecionado")) + " segundos";  
}

function check_if_done(i) {
    if ((localStorage.getItem("tarefa" + i + "_" + localStorage.getItem("projeto_selecionado") + "_total")) !== null) {
        var timex = localStorage.getItem("tarefa" + (i) + "_" + localStorage.getItem("projeto_selecionado") + "_total");
        var split1 = timex.split("/");
        var hms = split1[1];
        var hms_split = hms.split(":");
        var diasx = split1[0];
        var horasx = hms_split[0];
        var minutosx = hms_split[1];
        var segundosx = hms_split[2];
        var t_total = document.createElement('p');
        if (diasx == 0) {
            t_total.innerHTML = "O utilizador " + localStorage.getItem(i) + " realizou a tarefa " + i + " em " + horasx + " horas " + " , " + minutosx + "minutos, " + segundosx + ".";
            t_total.style = "font-weight: bold";
            document.getElementById(i).disabled = true;
            document.getElementById('tempo').appendChild(t_total);
            if (horasx == 0) {
                t_total.innerHTML = "O utilizador " + localStorage.getItem(i) + " realizou a tarefa " + i + "  em " + + minutosx + "minutos, " + segundosx + ".";
                t_total.style = "font-weight: bold";
                document.getElementById(i).disabled = true;
                if (minutosx == 0) {
                    t_total.innerHTML = "O utilizador " + localStorage.getItem(i) + " realizou a tarefa " + (i) + " em " + + segundosx + " segundos.";
                    t_total.style = "font-weight: bold";
                    document.getElementById(i).disabled = true;
                }
            }
        }
        var proj_total = localStorage.getItem("total_projeto_" + localStorage.getItem("projeto_selecionado"));
        document.getElementById("total_proj").innerHTML = "Tempo total gasto no projeto: " + proj_total + " segundos"; 
        document.getElementById('tempo').appendChild(t_total);
        
        
        var startdate = localStorage.getItem("tarefa" + i + "_" + localStorage.getItem("projeto_selecionado") + "_start");
        var enddate = localStorage.getItem("tarefa" + i + "_" + localStorage.getItem("projeto_selecionado") + "_end");
        var splitS = startdate.split("/");
        var splitE = enddate.split("/");
        var anoS = splitS[2],
        mesS = splitS[1],
        diaS = splitS[0],
        horaS = splitS[3],
        minutoS = splitS[4],
        segundoS = splitS[5];
        var anoE = splitE[2],
        mesE = splitE[1],
        diaE = splitE[0],
        horaE = splitE[3],
        minutoE = splitE[4],
        segundoE = splitE[5];
        
        var startstring = diaS + "/" + mesS + "/" + anoS + " - " + horaS + ":" + minutoS + ":" + segundoS;
        var endstring = diaE + "/" + mesE + "/" + anoE + " - " + horaE + ":" + minutoE + ":" + segundoE;
        
        var p_start = document.createElement('p');
        p_start.innerHTML = "Tarefa " + i + " iniciada às: " + startstring;
        document.getElementById('tempo').appendChild(p_start);
        var p_end = document.createElement('p');
        p_end.innerHTML = "Tarefa " + i + " terminada às: " + endstring;
        document.getElementById('tempo').appendChild(p_end);
    }
}

window.onload = function () {
    "use strict";
    var path = window.location.pathname.split("/").pop();
    if (path == "selecionarprojeto.html") {
        for (var i = 0; i < localStorage.getItem("valor_index") ;i++) {
             if (localStorage.getItem("projeto_" + i) !== null) {
                var a = document.createElement('a');
                a.innerHTML = "<p>Projeto " + localStorage.getItem("projeto_" + i) + "</p>";
                a.href="projeto.html";
                a.setAttribute("onclick","localStorage.setItem('projeto_selecionado',"+i+")");
                 document.getElementById('projetos').appendChild(a);
            }
        }
    }
    
    if (path == "projeto.html") {
        document.getElementById('nome').innerHTML = localStorage.getItem('projeto_' + localStorage.getItem('projeto_selecionado'));
        document.getElementById('email').innerHTML = localStorage.getItem('email_' + localStorage.getItem('projeto_selecionado'));
        var cycle = localStorage.getItem("numberOfTarefas_" + localStorage.getItem("projeto_selecionado"));
        for (var i = 0; i <= parseInt(cycle) ;i++) {
             if (localStorage.getItem("tarefa" + i + "_" + localStorage.getItem('projeto_selecionado')) !== null) {
                var p = document.createElement('p');
                p.innerHTML = "<p>Tarefa " + (i) + ": " + localStorage.getItem("tarefa" + i + "_" + localStorage.getItem('projeto_selecionado')) + "</p>";
                 document.getElementById('tarefas').appendChild(p);
                 var button_start = document.createElement('button');
                 var button_finish = document.createElement('button');
                 button_start.id = i;
                 button_finish.id = i+5;
                 button_finish.disabled = true;
                 if ((localStorage.getItem("tarefa" + i + "_" + localStorage.getItem('projeto_selecionado') + "_" + "start") !== null) && (localStorage.getItem("tarefa" + i + "_" + localStorage.getItem('projeto_selecionado') + "_" + "end")) == undefined) {
                     button_start.disabled = true;
                     button_finish.removeAttribute('disabled');
                     var startdate = localStorage.getItem("tarefa" + i + "_" + localStorage.getItem("projeto_selecionado") + "_start");
                     var splitS = startdate.split("/");
                     var anoS = splitS[2],
                         mesS = splitS[1],
                         diaS = splitS[0],
                         horaS = splitS[3],
                         minutoS = splitS[4],
                         segundoS = splitS[5];
                     var startstring = diaS + "/" + mesS + "/" + anoS + " - " + horaS + ":" + minutoS + ":" + segundoS;
                     var p_start = document.createElement('p');
                     p_start.innerHTML = "Tarefa " + i + " iniciada às: " + startstring;
                     document.getElementById('tempo').appendChild(p_start);
                 }
                 button_start.setAttribute("onclick","var userid = prompt('De modo a identificar quem realizou a tarefa, insira o nº do seu cartão:', '48303');localStorage.setItem(this.id,userid);enable(this.id);start_date(this.id);");
                 button_finish.setAttribute("onclick","alert('Tarefa terminada às: " + Date() + "');disable_all(this.id);end_date(this.id);");
                 button_start.innerHTML = "Começar tarefa " + i;
                 button_finish.innerHTML = "Terminar tarefa " + i;
                 document.getElementById('tarefas').appendChild(button_start);
                 document.getElementById('tarefas').appendChild(button_finish);
                 
                 check_if_done(i);
            }
        }   
    }
}