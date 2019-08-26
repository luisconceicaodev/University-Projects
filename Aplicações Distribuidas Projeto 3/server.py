# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 3
Grupo: 
Números de aluno: 48303
"""

from flask import Flask, request, make_response, jsonify, Response
#make_response - sends requests in JSON
#jsonify - reads JSON messages

import json
import database as db

#inicialização da aplicacao
app = Flask(__name__)

#criacao da base de dados
info = db.database("albuns.db")



#SOS----------------------------------------------------------------------------
def formato_mensagem(dados):
    send_msg = make_response(json.dumps(dados))
    send_msg.headers["Content-Type"] = "application/json"
    return send_msg
    
def mensagem_erro(describedBy, httpStatus, title, detail, ids = None):
    resposta = {
        "describedBy": describedBy,
        "httpStatus": httpStatus,
        "title": title,
        "detail": detail,
        "ids" : ids
        }
    return resposta




#-------------------------------------------------------------------------------
#app
#-------------------------utilizadores-------------------------------------------

@app.route("/utilizadores", methods = ["GET", "OPTIONS"]) # PARA O SHOW ALL
@app.route("/utilizadores/add", methods = ["POST", "OPTIONS"])
@app.route("/utilizadores/delete", methods = ["DELETE", "OPTIONS"])
@app.route("/utilizadores/get/<int:id_user>", methods = ["GET", "OPTIONS"])
@app.route("/utilizadores/delete/<int:id_user>", methods = ["DELETE", "OPTIONS"])
def utilizadores(id_user = None):
    resposta = {}
    if id_user == None:
        if request.method == "GET":
            print (info.select_all("utilizadores"))
            resposta["mensagem"] = "Todos os utilizadores." #informa o que esta a mandar
            resposta["conteudo"] = info.select_all("utilizadores")
            resposta["num_elementos"] = "muitos" # para no futuro se forem mts, separar
            resposta["httpStatus"] = 200 #it works
            
        elif request.method == "POST":
            try:
                dados = json.loads(request.data)
                info.add_user((dados["nome"], dados["username"], dados["password"]))
                resposta["mensagem"] = "Utilizador " + dados["nome"] + " adicionado com sucesso!"
                resposta["httpStatus"] = 201
            except:
                resposta = mensagem_erro("localhost:5000/utilizadores/add", 400, "Formato incorreto. ", "JSON Invalido. ")
                
        elif request.method == "DELETE":
            info.remove_all("utilizadores")
            resposta["mensagem"] = "Todos os utilizadores apagados com sucesso."
            resposta["httpStatus"] = 204
    else:
        ids = [x[0] for x in json.loads(info.select_all_ids("utilizadores"))]
        if request.method == "GET":
            if id_user in ids:
                resposta["mensagem"] = "Utilizador encontrado."
                resposta["conteudo"] = info.select_elementById("utilizadores", id_user)
                resposta["num_elementos"] = "unico"
                resposta["httpStatus"] = 200
            else:
                resposta = mensagem_erro("localhost:5000/utilizadores/get", 404, "Utilizador nao existente. ", "Este utilizador nao existe na BD ", ids)
        
        elif request.method == "DELETE":
            if id_user in ids:
                info.remove_elementById("utilizadores", id_user)
                resposta["mensagem"] = "Utilizador com id " + str(id_user) + " removido."
                resposta["httpStatus"] = 202
            else:
                resposta = mensagem_erro("localhost:5000/utilizadores/get", 204, "Utilizador ja apagado ou inexistente. ", "O utilizador que tentou apagar, ja foi apagado ou nao existe ", ids)

    r = formato_mensagem(resposta)
    return r

#-------------------------------bandas-------------------------------

@app.route("/bandas", methods = ["GET", "OPTIONS"])
@app.route("/bandas/add", methods = ["POST", "OPTIONS"])
@app.route("/bandas/delete", methods = ["DELETE", "OPTIONS"])
@app.route("/bandas/get/<int:id_banda>", methods = ["GET", "OPTIONS"])
@app.route("/bandas/delete/<int:id_banda>", methods = ["DELETE", "OPTIONS"])
def bandas(id_banda = None):
    resposta = {}

    if id_banda == None:
        if request.method == "GET":
            resposta["mensagem"] = "Todas as bandas."
            resposta["conteudo"] = info.select_all("bandas")
            resposta["num_elementos"] = "muitos"
            resposta["httpStatus"] = 200 
            
        elif request.method == "POST":
            try:
                dados = json.loads(request.data)
                info.add_banda((dados["nome"], dados["ano"], dados["genero"]))
                resposta["mensagem"] = "Banda " + dados["nome"] + " adicionada com sucesso!"
                resposta["httpStatus"] = 201
            except:
                resposta = mensagem_erro("localhost:5000/bandas/add", 400, "Formato incorreto. ", "JSON Invalido. ")
                
        elif request.method == "DELETE":
            info.remove_all("bandas")
            resposta["mensagem"] = "Todas as bandas apagadas com sucesso."
            resposta["httpStatus"] = 204
    else:
        ids = [x[0] for x in json.loads(info.select_all_ids("bandas"))]

        if request.method == "GET":
            if id_banda in ids:
                resposta["mensagem"] = "banda encontrada."
                resposta["conteudo"] = info.select_elementById("bandas", id_banda)
                resposta["num_elementos"] = "unico"
                resposta["httpStatus"] = 200
            else:
                resposta = mensagem_erro("localhost:5000/bandas/get", 404, "banda nao existente. ", "Esta banda nao existe na BD ", ids)
        elif request.method == "DELETE":
            if id_banda in ids:
                info.remove_elementById("bandas", id_banda)
                resposta["mensagem"] = "banda com id " + str(id_banda) + " removida."
                resposta["httpStatus"] = 202
            else:
                resposta = mensagem_erro("localhost:5000/bandas/get", 204, "banda ja apagada ou inexistente. ", "A banda que tentou apagar ja foi apagada ou nao existe ", ids)

    r = formato_mensagem(resposta)
    return r

#---------------------------------album--------------------------------

@app.route("/albuns", methods = ["GET", "OPTIONS"])
@app.route("/albuns/add", methods = ["POST", "OPTIONS"])
@app.route("/albuns/delete", methods = ["DELETE", "OPTIONS"])
@app.route("/albuns/get/<int:id_album>", methods = ["GET", "OPTIONS"])
@app.route("/albuns/delete/<int:id_album>", methods = ["DELETE", "OPTIONS"])
def album(id_album = None):
    resposta = {}

    if id_album == None:
        if request.method == "GET":
            resposta["mensagem"] = "Todos os albuns."
            resposta["conteudo"] = info.select_all("albuns")
            resposta["num_elementos"] = "muitos"
            resposta["httpStatus"] = 200 
            
        elif request.method == "POST":
            try:
                dados = json.loads(request.data)
                ids = [x[0] for x in json.loads(info.select_all_ids("bandas"))]
                if dados["id_banda"] in ids:
                    info.add_album((dados["id_banda"], dados["nome"], dados["ano_album"]))
                    resposta["mensagem"] = "Album " + dados["nome"] + " adicionado com sucesso!"
                    resposta["httpStatus"] = 201
                else:
                    resposta = mensagem_erro("localhost:5000/albuns/add", 404, "banda Inexistente. ", "A banda com o Id nao existe, usar um dos seguintes", ids)
            except:
                resposta = mensagem_erro("localhost:5000/albuns/add", 400, "Formato incorreto. ", "Mau formato do JSON. ")
                
        elif request.method == "DELETE":
            info.remove_all("albuns")
            resposta["mensagem"] = "Todos os albuns apagados com sucesso."
            resposta["httpStatus"] = 204
    else:
        ids = [x[0] for x in json.loads(info.select_all_ids("albuns"))]

        if request.method == "GET":
            if id_album in ids:
                resposta["mensagem"] = "Album encontrado."
                resposta["conteudo"] = info.select_elementById("albuns", id_album)
                resposta["num_elementos"] = "unico"
                resposta["httpStatus"] = 200
            else:
                resposta = mensagem_erro("localhost:5000/albuns/get", 404, "Album nao existente. ", "O Album ja nao existe na BD ", ids)
        elif request.method == "DELETE":
            if id_album in ids:
                info.remove_elementById("albuns", id_album)
                resposta["mensagem"] = "Album com id " + str(id_album) + " removido."
                resposta["httpStatus"] = 202
            else:
                resposta = mensagem_erro("localhost:5000/albuns/get", 204, "Album ja apagado ou inexistente. ", "O Album que tentou apagar ja foi apagado ou nao existe ", ids)

    r = formato_mensagem(resposta)
    return r
#--------------------------------------------------------------
#--------------------------LISTA-albuns------------------------
@app.route('/listas_albuns', methods = ["GET", "OPTIONS"])
@app.route('/listas_albuns/add', methods = ["POST", "OPTIONS"])
@app.route('/listas_albuns/delete', methods = ["DELETE", "OPTIONS"])
#para todos os show all
@app.route('/listas_albuns/select_all/utilizadores/<int:id_user>', methods = ["GET", "OPTIONS"])
@app.route('/listas_albuns/select_all/bandas/<int:id_album>', methods = ["GET", "OPTIONS"])
@app.route('/listas_albuns/select_all/rates/<int:id_rate>', methods = ["GET", "OPTIONS"])
#para todos os delete all
@app.route('/listas_albuns/remove_all/utilizadores/<int:id_user>', methods = ["DELETE", "OPTIONS"])
@app.route('/listas_albuns/remove_all/bandas/<int:id_album>', methods = ["DELETE", "OPTIONS"])
@app.route('/listas_albuns/remove_all/rates/<int:id_rate>', methods = ["DELETE", "OPTIONS"])
def listas_album(id_user = None, id_album = None, id_rate = None):
    resposta = {}
    ids_albuns = [x[0] for x in json.loads(info.select_all_ids('albuns'))]
    ids_utilizadores = [x[0] for x in json.loads(info.select_all_ids('utilizadores'))]
    lista_com_ids_da_lista_albuns = json.loads(info.select_all_ids_from_list_albuns())

    if id_user == None and id_album == None and id_rate == None:
        if request.method == "GET":
            resposta['mensagem'] = "Todos os albuns com ratings"
            resposta['conteudo'] = info.select_all('list_albuns')
            resposta['httpStatus'] = 200
            resposta['num_elementos'] = "varios"

        elif request.method == "POST":
            try:
                dados = json.loads(request.data)
                if dados['id_user'] in ids_utilizadores and dados['id_user']:
                    if dados['id_album'] in ids_albuns:
                        if [dados['id_user'],dados['id_album']] not in [[x[0],x[1]] for x in lista_com_ids_da_lista_albuns]:
                            info.add_list_albuns((dados['id_user'],dados['id_album'],dados['id_rate']))
                            resposta['mensagem'] = "Adicionado a lista com sucesso o album com o id " + str(dados['id_album'])
                            resposta['httpStatus'] = 201
                        else:
                            resposta = mensagem_erro("localhost:5000/listas_albuns/add/", 409, "Elemento ja existente", "O cliente ja tem um rating para o album, por favor faca update")
                    else:
                        resposta = mensagem_erro("localhost:5000/albuns/get/", 404, "albun inexistente", "A banda nao existe na base de dados", ids_bandas)
                else:
                    resposta = mensagem_erro("localhost:5000/utilizadores/get/", 404, "utilizador inexistente", "O utilizador nao existe na base de dados", ids_utilizadores)
            except:
                resposta = mensagem_erro("localhost:5000/lista_albuns/add", 400, "Formato Incorrecto", "Mal formato do JSON")

        elif request.method == "DELETE":
            try:
                info.remove_all('list_bandas')
                resposta['mensagem'] = "Lista de bandas apagadas com sucesso"
                resposta['httpStatus'] = 204
            except:
                resposta = mensagem_erro("localhost:5000/lista_albuns/add", 404, "Impossivel apagar", "Não existe list album")

    else:
        ids_dos_users_das_listas = [x[0] for x in lista_com_ids_da_lista_albuns]
        ids_dos_albuns = [x[0] for x in json.loads(info.select_all_ids('albuns'))]
        list_rate = ["M", "MM", "S", "B", "MB"]

        if id_user != None:
            if request.method == "GET":
                dados = info.select_all_albuns_by_id_user(id_user)
                rates = []
                for i in range(len(dados)):
                    rates.append(list_rate[int(dados[i][2])-1])
                conteudo = info.select_all_albuns_by_id_user(id_user) + (rates)
                if id_user in ids_dos_users_das_listas:
                    resposta['mensagem'] = "Rating do utilizador encontrados"
                    resposta['conteudo'] = conteudo
                    resposta['httpStatus'] = 200
                    resposta['num_elementos'] = "muitos"
                else:
                    resposta = mensagem_erro("localhost:5000/lista_albuns/select_all/utilizadores/", 404, "O cliente nao tem avaliou", "Nao existem avalicacoes deste cliente ou cliente inexistente")

            elif request.method == "DELETE":
                try:
                    info.remove_all_albuns_with_id_user(id_user)
                    resposta['mensagem'] = "Lista de rates do user apagada"
                    resposta['httpStatus'] = 202
                except:
                    resposta = mensagem_erro("localhost:5000/lista_albuns/add", 404, "User não tem albuns rated", "Sem albuns para eliminar")

        if id_rate != None:
            rate_dos_albuns = info.select_all_albuns_by_rate(id_rate)
            dados = info.select_all_albuns_by_rate(id_rate)
            albuns = []
            for i in range(len(dados)):
                    albuns.append(info.select_albuns_by_id(dados[i][1]))
            conteudo = rate_dos_albuns + (albuns)
            if request.method == "GET":
                if len(rate_dos_albuns) == 0:
                    resposta = mensagem_erro("localhost:5000/lista_albuns/select_all/rate/", 404, "Sem esse rate", "Nao existem albuns com esse rate")
                else:
                    resposta['mensagem'] = "Albuns com o rate encontrados"
                    resposta['conteudo'] = conteudo
                    resposta['httpStatus'] = 200
                    resposta['num_elementos'] = "muitos"

            elif request.method == "DELETE":
                try:
                    info.remove_all_albuns_with_rate(id_rate)
                    resposta['mensagem'] = "Lista Albuns com rate inserido apagados com sucesso"
                    resposta['httpStatus'] = 202
                except:
                    resposta = mensagem_erro("localhost:5000/lista_albuns/select_all/rate/", 404, "Sem esse rate", "Nao existem rates com esse rate")

        elif id_album != None:
            bandas = info.select_albuns_by_banda_id(id_album)
            if request.method == "GET":
                if len(bandas) == 0:
                    resposta = mensagem_erro("localhost:5000/lista_albuns/select_all/rate/", 404, "Sem essa banda", "Nao existem bandas com esse id")
                else:
                    resposta['mensagem'] = "Todos os albuns da banda"
                    resposta['conteudo'] = bandas
                    resposta['httpStatus'] = 200
                    resposta['num_elementos'] = "muitos"

            elif request.method == "DELETE":
                try:
                    info.remove_all_albuns_with_id_banda(id_album)
                    resposta['mensagem'] = "albuns Apagados"
                    resposta['httpStatus'] = 202
                except:
                    resposta = mensagem_erro("localhost:5000/lista_albuns/remove_all/bandas/", 404, "Não existente", "albuns dessa banda")
    r = formato_mensagem(resposta)
    return r

#----------------------------------------------------------------------------
#-----------------------------PARA OS UPDATES-------------------------------
@app.route('/update/utilizadores/<int:id_user>', methods = ["PUT", "OPTIONS"])
def update_utilizador(id_user = None):
    resp = {}
    if request.method == "PUT":
        try:
            dados = json.loads(request.data)
            ids_utilizadores = [x[0] for x in json.loads(info.select_all_ids('utilizadores'))]
            if id_user in ids_utilizadores:
                info.update_user((dados['password'], id_user))
                resp["mensagem"] = "Alterado utilizador com id " + str(id_user) + " com sucesso"
                resp['httpStatus'] = 200
            else:
                resp = mensagem_erro("localhost:5000/update/utilizadores/", 204, "Utilizador não existente", "O utilizador que tentou fazer update não existe")
        except:
            resp = mensagem_erro("localhost:5000/update/utilizadores/", 400, "Formato Incorrecto", "Mal formato do JSON")
    r = formato_mensagem(resp)
    return r

@app.route('/update/listas_albuns', methods = ["PUT", "OPTIONS"])
def update_listas_albuns():
    try:
        resp = {}
        dados = json.loads(request.data)
        lista_com_ids_da_lista_albuns = json.loads(info.select_all_ids_from_list_albuns())
        resp = mensagem_erro("localhost:5000/update/listas_albuns", 204, "Utilizador ou album nao existente", "O utilizador ou album nao existe")
        for i in lista_com_ids_da_lista_albuns:
            if [dados['id_user'],dados['id_album']] == [i[0], i[1]]:
                if dados['id_rate'] + 1 != int(i[1]):
                    info.update_rate((dados['id_rate'] , dados['id_user'], dados['id_album']))
                    resp["mensagem"] = "Alterado a classificacao do utilizador e album com id " + str((dados['id_user'], dados['id_album'])) + " respetivamente com sucesso"
                    resp['httpStatus'] = 200
                else:
                    resp = mensagem_erro("localhost:5000/update/banda", 204, "Rating Igual", "Nao pode dar o mesmo rating que ja esta defenido")
    except:
        resp = mensagem_erro("localhost:5000/update/listas_albuns", 400, "Formato Incorrecto", "Mal formato do JSON")
    r = formato_mensagem(resp)
    return r

if __name__ == "__main__":
    app.run(debug = True)
