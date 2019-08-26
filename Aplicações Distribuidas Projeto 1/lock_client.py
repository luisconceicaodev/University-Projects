#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_client.py
Grupo: 006
Números de aluno: 48303
"""
# Zona para fazer imports
import sys, socket
from net_client import *

# argumentos da linha de comandos
if len(sys.argv) == 4:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    client_id = int(sys.argv[3])
else:
    print ("Erro: argumentos incorretos.")
    #dar ajuda no caso de o utilizador não saber os argumentos (print ("Ligação falhada: argumentos incorretos.\nPara ajuda, escreva 'HELP'."))
    sys.exit()

# extras
def helpTable():
    print("+-------------------------------------------------------+----------------------------------------------------------+")
    print("|   COMANDO   |             FORMATO STRING              |                   RESPOSTA DO SERVIDOR                   |")
    print("+-------------+-----------------------------------------+----------------------------------------------------------+")
    print("| LOCK        | LOCK <id cliente> <numero recurso>      | OK, NOK or UNKNOWN RESOURCE                              |")
    print("| RELEASE     | RELEASE <id cliente> <numero recurso>   | OK, NOK or UNKNOWN RESOURCE                              |")
    print("| TEST        | TEST <numero recurso>                   | LOCKED, UNLOCKED, DISABLE or UNKNOWN RESOURCE            |")
    print("| STATS       | STATS <numero recurso>                  | <vezes que o recurso foi bloqueado> or UNKNOWN RESOURCE  |")
    print("| STATS-Y     | STATS-Y                                 | <recursos bloqueados em y>                               |")
    print("| STATS-N     | STATS-N                                 | <recursos disponíveis>                                   |")
    print("+-------------+-----------------------------------------+----------------------------------------------------------+")


# Programa principal
msg = ""
while True:
    print("\n(Escreve EXIT para sair do programa, ou HELP para ver os comandos)")
    msg = input("Comando : ")
    if msg.upper() == 'EXIT':
        print ("Conexão Terminada")
        sys.exit()
    
    elif msg.upper() == 'HELP':
        helpTable()
    
    else:
        msg_split = msg.split()

        try:
            #lista a enviar para o servidor
            send_server = []
            
            #tratar comandos, erros
            if msg_split[0].upper() in ["LOCK", "RELEASE"]:
                if len(msg_split) != 3:
                    raise IndexError
                if client_id != int(msg_split[1]):
                    raise IndexError
                send_server = [msg_split[0].upper(), int(msg_split[1]), int(msg_split[2])]
            
            elif msg_split[0].upper() in ["TEST", "STATS"]:
                if len(msg_split) != 2:
                    raise IndexError
                send_server = [msg_split[0].upper(), int(msg_split[1])]
            
            elif msg_split[0].upper() in ["STATS-Y", "STATS-N"]:
                if len(msg_split) != 1:
                    raise IndexError
                send_server = [msg_split[0].upper()]
            
            else:
                raise IndexError

            #criar ligação, socket
            sock = server(HOST, PORT)

            try:
                sock.connect()
                resp = sock.send_receive(send_server)
            
            #except erro de ligacao
            except:
                print ("Erro de ligação")
            
            sock.close()
            print (resp)
        except IndexError:
            print ("Unknown Command")
        except ValueError:
            print ("Unknown Command\nErro: o valor do id do cliente e o número do recurso tem de ser números inteiros.")