# -*- coding: utf-8 -*-
"""
Aplicações Distribuídas - Projeto 3
Grupo:
Números de aluno: 48303
"""

import os, requests, sys, json

from spotify import search_artist, search_album

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def error(httpStatus,details):
    answer = {}
    answer['httpStatus'] = httpStatus
    answer['detail'] = details
    return answer

start = """Enter your command,
HELP to get information, CLEAR to clear your terminal, EXIT to leave"""

cmd = "> "

help = """CHOOSE ONE OF THE OPTIONS:

ADD:
USER <NOME> <USERNAME> <PASSWORD>
BANDA <NOME> <ANO> <GENERO>
ALBUM <ID_BANDA> <NOME> <ANO_ALBUM>
<ID_USER> <ID_ALBUM> <RATE>

SHOW | REMOVE:
USER <ID_USER>
BANDA <ID_BANDA>
ALBUM <ID_ALBUM>
ALL <USERS | BANDAS | ALBUNS>
ALL ALBUNS_B <ID_BANDA>
ALL ALBUNS_U <ID_USER>
ALL ALBUNS <RATE>

UPDATE:
ALBUM <ID_USER> <ID_ALBUM> <RATE>
USER <ID_USER> <PASSWORD>
"""

list_add = ["USER", "BANDA", "ALBUM", "USERS", "BANDAS", "ALBUNS"]
list_rate = ["M", "MM", "S", "B", "MB"]

cls()
print (start)
while True:
    command = input(cmd).split()
    answer = ""
    if len(command) != 0:
        if command[0] == "CLEAR":
            cls()
            print (start)
        elif command[0] == "HELP":
            print (help)
        elif command[0] == "EXIT":
            sys.exit(1)
        elif command[0] == "ADD":
            if command[1] in list_add:
                #-------------ADICIONA USER------------------------
                if command[1] == list_add[0]:
                    if len(command) == 5:
                        try:
                            answer = requests.post('http://localhost:5000/utilizadores/add', json = {'nome': command[2], 'username' : command[3], 'password': command[4]})
                        except:
                            answer = error(500, "Erro a ligar ao servidor")
                    else:
                        answer = error(400, "Dimensão errada do pedido (passwords e username sem espacos)")
                #-----------ADICIONA BANDA------------
                elif command[1] == list_add[1]:
                    nome_banda = None
                    ano_banda = None
                    genero_banda = None
                    if len(command) == 5:
                        try:
                            answer = requests.post('http://localhost:5000/bandas/add', json = {'nome': command[2], 'ano' : command[3], 'genero': command[4]})
                            artist = search_artist(command[2])
                            for dado in artist:
                                print (dado)
                        except:
                            answer = error(500, "Erro a ligar ao servidor")
                    else:
                        answer = error(400, "Dimensão errada do pedido")
                #-----------ADICIONA ALBUM------------
                elif command[1] == list_add[2]:
                    if command[-1].isdigit():
                        id_banda = command[2]
                        nome_album = command[3]
                        ano_album = command[4]
                        try:
                            answer = requests.post('http://localhost:5000/albuns/add', json = {'id_banda': int(command[2]), 'nome': command[3], 'ano_album' : int(command[4]) })
                            album = search_album(command[3])
                            for dado in album:
                                print (dado)
                        except:
                            answer = error(500, "Erro a ligar ao servidor")
                    else:
                        answer = error(400, "Input inválido ")
            elif len(command) == 4:
                if command[1].isdigit() and command[2].isdigit():
                    if command[3] in list_rate:
                        try:
                            answer = requests.post('http://localhost:5000/listas_albuns/add', json = {'id_user': int(command[1]), 'id_album' : int(command[2]), 'id_rate' : list_rate.index(command[3]) + 1})
                        except:
                            answer = error(500, "Erro a ligar ao servidor")
                    else:
                        answer = error(400, "O rating devem ser um dos seguintes: " + " | ".join(list_rate))
                else:
                    answer = error(400, "O id do User e do Album devem ser inteiros")
            else:
                answer = error(400, "Input invalido, verificar a ajuda")

    #------------------------------SHOW E REMOVE-------------------------------------------
        
        elif command[0] == "SHOW" or command[0] == "REMOVE":
    #----------------------COM ALL ---------------------
            if 3 <= len(command) <= 4:                
                if command[1] == "ALL": 
                    if command[0] == "SHOW":
        #------------so para o show all users/banda/album------------------
                        if len(command) == 3:
                            if command[2] in list_add:
                                if command[2] == list_add[3]:
                                    try:
                                        answer = requests.get('http://localhost:5000/utilizadores')
                                    except:
                                        answer = error(500, "Erro a ligar ao servidor")
                                elif command[2] == list_add[4]:
                                    try:
                                        answer = requests.get('http://localhost:5000/bandas')
                                    except:
                                        answer = error(500, "Erro a ligar ao servidor")
                                elif command[2] == list_add[5]:
                                    try:
                                        answer = requests.get('http://localhost:5000/albuns')
                                    except:
                                        answer = error(500, "Erro a ligar ao servidor")
                                else:
                                    answer = error(400, "Tem que ser uma dos seguintes commands, USERS | BANDAS | ALBUNS")
                            else:
                                answer = error(400, "Tem que ser uma dos seguintes commands, USERS | BANDAS | ALBUNS")

                        elif len(command) == 4:
                            if command[2] == "ALBUNS_B" and command[3].isdigit():
                                try:
                                    answer = requests.get('http://localhost:5000/listas_albuns/select_all/bandas/' + command[3])
                                except:
                                    answer = error(500, "Erro a ligar ao servidor")
                            elif command[2] == "ALBUNS_U" and command[3].isdigit():
                                try:
                                    answer = requests.get('http://localhost:5000/listas_albuns/select_all/utilizadores/' + command[3])
                                except:
                                    answer = error(500, "Erro a ligar ao servidor")
                            elif command[2] == "ALBUNS":
                                try:
                                    answer = requests.get('http://localhost:5000/listas_albuns/select_all/rates/' + str(list_rate.index(command[3])+1))
                                except:
                                    answer = error(500, "Erro a ligar ao servidor")
                            else:
                                answer = error(400, "Tem que escolher ALBUNS_B | ALBUNS_U | ALBUNS + o id que deseja")

                    elif command[0] == "REMOVE":
                        if len(command) == 3:
                            #REMOVE ALL USERS | BANDAS | ALBUNS
                            if command[2] in list_add:
                                if command[2] == list_add[3]:
                                    try:
                                        answer = requests.delete('http://localhost:5000/utilizadores/delete')
                                    except:
                                        answer = error(500, "Erro a ligar ao servidor")
                                elif command[2] == list_add[4]:
                                    try:
                                        answer = requests.delete('http://localhost:5000/bandas/delete')
                                    except:
                                        answer = error(500, "Erro a ligar ao servidor")
                                elif command[2] == list_add[5]:
                                    try:
                                        answer = requests.delete('http://localhost:5000/albuns/delete')
                                    except:
                                        answer = error(500, "Erro a ligar ao servidor")
                                else:
                                    answer = error(400, "Tem que ser uma dos seguintes commands, USERS | BANDAS | ALBUNS")
                            else:
                                answer = error(400, "o Terceiro argumento tem que ser USERS, BANDAS ou ALBUM, consulte a ajuda para mais informacoes")
                        elif len(command) == 4:
                            #REMOVE ALL ALBUNS_B | ALBUNS_U | ALBUNS
                            if command[2] == "ALBUNS_B" and command[3].isdigit():
                                try:
                                    answer = requests.delete('http://localhost:5000/listas_albuns/remove_all/bandas/' + command[3])
                                except:
                                    answer = error(500, "Erro a ligar ao servidor")
                            elif command[2] == "ALBUNS_U" and command[3].isdigit():
                                try:
                                    answer = requests.delete('http://localhost:5000/listas_albuns/remove_all/utilizadores/' + command[3])
                                except:
                                    answer = error(500, "Erro a ligar ao servidor")
                            elif command[2] == "ALBUNS":
                                try:
                                    answer = requests.delete('http://localhost:5000/listas_albuns/remove_all/rates/' + str(list_rate.index(command[3])+1))
                                except:
                                    answer = error(500, "Erro a ligar ao servidor")
                            else:
                                answer = error(400, "Tem que escolher ALBUNS_B | ALBUNS_U | ALBUNS + o id que deseja")

        #------------------- REMOVER S/ ALL ----------------------------------------

                elif command[1] in list_add: #CASO SEJA OS OUTROS DA list_add (USER, BANDA, ALBUM)
                    if len(command) == 3:
                        if command[0] == "SHOW": # mostrar , gets
                            if command[1] == list_add[0]: #para os users
                                if command[2].isdigit():
                                    try:
                                        answer = requests.get('http://localhost:5000/utilizadores/get/'+command[2])
                                    except:
                                        answer = error(500, "Erro a ligar ao servidor")
                                else:
                                    answer = error(400, "O ID do USER tem que ser um inteiro")
                            elif command[1] == list_add[1]: # para as BANDAS
                                if command[2].isdigit():
                                    try:
                                        answer = requests.get('http://localhost:5000/bandas/get/'+command[2])
                                    except:
                                        answer = error(500, "Erro a ligar ao servidor")
                                else:
                                    answer = error(400, "O ID da BANDA tem que ser um inteiro")
                            else: # para os episodios
                                if command[2].isdigit():
                                    try:
                                        answer = requests.get('http://localhost:5000/albuns/get/'+command[2])
                                    except:
                                        answer = error(500, "Erro a ligar ao servidor")
                                else:
                                    answer = error(400, "O ID da Banda tem que ser um inteiro")
                        elif command[0] == "REMOVE": #agora com os deletes
                            if command[1] == list_add[0]: #para os users
                                if command[2].isdigit():
                                    try:
                                        answer = requests.delete('http://localhost:5000/utilizadores/delete/'+command[2])
                                    except:
                                        answer = error(500, "Erro a ligar ao servidor")
                                else:
                                    answer = error(400, "O ID do USER tem que ser um inteiro")
                            elif command[1] == list_add[1]: # para as bandas
                                if command[2].isdigit():
                                    try:
                                        answer = requests.delete('http://localhost:5000/bandas/delete/'+command[2])
                                    except:
                                        answer = error(500, "Erro a ligar ao servidor")
                                else:
                                    answer = error(400, "O ID da BANDA tem que ser um inteiro")
                            else: # para os albums
                                if command[2].isdigit():
                                    try:
                                        answer = requests.delete('http://localhost:5000/albuns/delete/'+command[2])
                                    except:
                                        answer = error(500, "Erro a ligar ao servidor")
                                else:
                                    answer = error(400, "O ID do ALBUM tem que ser um inteiro")

                    else:
                        answer = error(400, "O Argumento Show [User, Banda, Album] tem que ter 3 argumentos")
                else:
                    answer = error(400, "Formato do pedido errado, por favor consulte a ajuda")
            else:
                answer = error(400, "Formato do pedido errado, por favor consulte a ajuda")
    
    #------------------------------UPDATE-------------------------------------------
        elif command[0] == "UPDATE":
            if len(command) == 4 or len (command) == 5:
                if command[1] == "ALBUM" or command[1] == "USER":
                    if command[1] == "USER":
                        if command[2].isdigit():
                            try:
                                answer = requests.put('http://localhost:5000/update/utilizadores/' + command[2], json = {'password' : command[3]})
                            except:
                                answer = error(500, "Erro a ligar ao servidor")
                        else:
                            answer = error(400, "O id Tem que ser um numero inteiro")
                    elif command[1] == "ALBUM":
                        if command[2].isdigit():
                            if command[3].isdigit():
                                if command[4] in list_rate:
                                    try:
                                        answer = requests.put('http://localhost:5000/update/listas_albuns', json = {'id_user': int(command[2]), 'id_album' : int(command[3]), 'id_rate' : list_rate.index(command[4]) + 1})
                                    except:
                                        answer = error(500, "Erro a ligar ao servidor")
                                else:
                                    error(400, "O rating tem que ser um dos seguintes" + " | ".join(list_rate))
                            else:
                                error(500, "O id do Album tem que ser um inteiro")
                        else:
                            error(500, "O id do utilizador tem que ser um inteiro")
                else:
                    error(500, "O Update tem que ser de users ou albuns")
            else:
                error(500, "Argumentos invalidos, ver ajuda para mais informacao")
        else:
            error(500, "Formato da mensagem errado, consultar Ajuda")
    else:
        error(500, "introduza um command")

    if answer != "":
        try:
            #print("Debbuger:",answer.content,"\n")
            resposta = json.loads(answer.content)
            if "mensagem" in resposta:
                #FUNCIONOU
                print ("Resposta {} - {}".format(resposta['httpStatus'], resposta['mensagem']))
                if "conteudo" in resposta:
                    if len(resposta['conteudo']) != 0:
                        if resposta['num_elementos'] == "unico":
                            print (" | ".join([str(i) for i in resposta['conteudo']]))
                        elif resposta['num_elementos'] == "muitos":
                            for i in resposta['conteudo']:
                                print (" | ".join([str(x) for x in i]))
                    else:
                        print ("Sem Elementos")

            else:
                #ERRO
                print ("Resposta {} - {}".format(resposta['httpStatus'], resposta['detail']))
                if ("ids" in resposta and resposta["ids"] != None):
                    print ("ID's Existentes:")
                    if len(resposta['ids']) != 0:
                        print (" | ".join([str(i) for i in resposta['ids']]))
                    else:
                        print ("Sem Elementos")
            print ("")
        except:
            resposta = answer
            print ("Resposta {} - {}".format(resposta['httpStatus'], resposta['detail']))
            print ("")
