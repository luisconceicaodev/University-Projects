#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 2 - lock_client.py
Grupo: 006
Números de aluno: 50036, 49050, 48303
"""
# Zona para fazer imports
import sys, socket
from lock_stub import ListStub

# argumentos da linha de comandos
if len(sys.argv) == 4:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    client_id = int(sys.argv[3])
else:
    print ("Erro: argumentos incorretos.")
    #dar ajuda no caso de o utilizador não saber os argumentos (print ("Ligação falhada: argumentos incorretos.\nPara ajuda, escreva 'HELP'."))
    sys.exit()


# Programa principal
stub = ListStub()
msg = ""
while True:
    print("\n(Escreve EXIT para sair do programa, ou HELP para ver os comandos)")
    msg = input("Comando : ")
    if msg.upper() == 'EXIT':
        print ("Conexão Terminada")
        sys.exit()
    
    elif msg.upper() == 'HELP':
        stub.helpTable()

    elif len(msg) == 0:
        print("Comando Vazio.")
    
    else:
        msg_split = msg.split()

        try:
            #lista a enviar para o servidor, ListStub
            
            #tratar comandos, erros
            if msg_split[0].upper() == "LOCK":
                if len(msg_split) != 3:
                    raise IndexError
                if client_id != int(msg_split[1]):
                    raise IndexError
                
                stub.append(10)
                stub.append(int(msg_split[1]))
                stub.append(int(msg_split[2]))
                
            elif msg_split[0].upper() == "RELEASE":
                if len(msg_split) != 3:
                    raise IndexError
                if client_id != int(msg_split[1]):
                    raise IndexError
                
                stub.append(20)
                stub.append(int(msg_split[1]))
                stub.append(int(msg_split[2]))
            
            elif msg_split[0].upper() == "TEST":
                if len(msg_split) != 2:
                    raise IndexError
                
                stub.append(30)
                stub.append(int(msg_split[1]))
            
            elif msg_split[0].upper() == "STATS":
                if len(msg_split) != 2:
                    raise IndexError
                
                stub.append(40)
                stub.append(int(msg_split[1]))
            
            elif msg_split[0].upper() == "STATS-Y":
                if len(msg_split) != 1:
                    raise IndexError
                
                stub.append(50)
            
            elif msg_split[0].upper() == "STATS-N":
                if len(msg_split) != 1:
                    raise IndexError
                
                stub.append(60)
            
            else:
                raise IndexError

            try:
                #criar ligação, socket
                stub.connect(HOST, PORT)
                #enviar a mensagem para o server
                resp = stub.send_receive_msg()
                #limbar a lista do comando
                stub.clear()
            
            #except erro de ligacao
            except:
                print ("Erro de ligação")
            
            stub.close()
            print (resp)
        except IndexError:
            print ("Unknown Command")
        except ValueError:
            print ("Unknown Command\nErro: o valor do id do cliente e o número do recurso tem de ser números inteiros.")
