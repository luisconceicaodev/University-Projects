$(document).ready(function () {
    $(".fotos").hide();
    $(".efeito").hide();
    $(".registo").hide();
    $(".detalhes").hide();
    $(".detalhes1").hide();
    $(".regras").hide();
    $(".video").hide();
    $('.fotos').fadeIn(1000);
    $('.efeito').fadeIn(3000);
    $('.registo').fadeIn(1000);
    $('.detalhes').fadeIn(1000);
    $('.detalhes1').fadeIn(1000);
    $('.regras').fadeIn(1000);
    $('.video').fadeIn(1000);
    $('#terminar_sessao').hide();
    
    $("#aleatorio").hide();
    $("#modos").hide();
    $("#jogar").hide();
    $('#normal').click(function () {
        $("#modos").fadeIn('slow');
        $('#jogar').fadeIn('slow');
        $("#normal").hide();
        $("#modo_alt").hide();
    });
    
    $("#recomeçar").hide();
    $("#modos").hide();
    $("#jogar").hide();
    $("#aleatorio").hide();
    $('#modo_alt').click(function () {
        $("#modos").fadeIn('slow');
        $("#aleatorio").fadeIn();
        $("#normal").hide();
        $("#modo_alt").hide();
    });
    
    $("#recomeçar").hide();
    $("#jogo_detalhes").hide();
    $("#teclado").hide();
    $('#jogar').click(function () {
        $("#teclado").fadeIn(1000);
        $('#jogo_detalhes').fadeIn('slow');
        $("#modos").hide();
        $('#jogar').hide();
        $("#recomeçar").fadeIn('fast');
    });
    
     $("#jogo_detalhes").hide();
     $("#letra_al_nao").hide();
     $("#letra_al_sim").hide();
     $("#aleatoria").hide();
     $('#aleatorio').click(function () {
        $("#jogo_detalhes").fadeIn('slow');
        $("#letra_al_nao").fadeIn('slow');
        $("#letra_al_sim").fadeIn('slow');
        $("#aleatoria").fadeIn('slow');
        $("#modo_alt").hide();
        $("#normal").hide();
        $("#modos").hide();
        $("#aleatorio").hide();
        $("#recomeçar").fadeIn('fast'); 
    });
    
    
    $('#terminar_sessao').click(function(){
        $('#terminar_sessao').hide();
        $("Jogador_Actual").hide();
    });
    
});