#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 2 - lock_server.py
Grupo: 006
Números de aluno: 50036, 49050, 48303
"""

# Zona para fazer importação

import sys
import socket as s
import pickle, struct
from lock_skel import ListSkeleton
from sock_utils import receive_all
import select

# código do programa principal


# argumentos da linha de comandos
if len(sys.argv) == 6:
    PORT = int(sys.argv[1])
    arg_N = int(sys.argv[2])
    arg_K = int(sys.argv[3])
    arg_Y =int(sys.argv[4])
    arg_time = int(sys.argv[5])
else:
    print ("Erro: argumentos incorretos.")
    #dar ajuda no caso de o utilizador não saber os argumentos (print ("Ligação falhada: argumentos incorretos.\nPara ajuda, escreva 'HELP'."))
    sys.exit()

#criacao do ListSkeleton
skel = ListSkeleton(arg_N, arg_K, arg_Y, arg_time)


ListenSocket = s.socket(s.AF_INET, s.SOCK_STREAM)
ListenSocket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)

try:
    ListenSocket.bind(('', PORT))
except s.error as err:
    print ("Error: " + err)
    exit(1)

#ListenSocket.listen(1)
ListenSocket.listen(4)

SocketList = [ListenSocket, sys.stdin]

while True:
    R, W, X = select.select(SocketList, [], [])
    for socket in R:
        if socket is ListenSocket:
            conn_sock, addr = ListenSocket.accept()
            addr, port = conn_sock.getpeername()
            print ('Novo cliente conectado -> %s:%d' % (addr, port))
            SocketList.append(conn_sock)
            
        else:
            #limpar recursos
            skel.clear_locks()

            size_bytes = receive_all(socket, 4)
            if not size_bytes:
                socket.close()
                SocketList.remove(socket)
                print('Client closed connection.')
                    
            else:
                size = struct.unpack("!i", size_bytes)[0]
                msg_bytes = receive_all(socket, size)
                if not msg_bytes:
                    socket.close()
                    SocketList.remove(socket)
                    print('Client closed connection.')
                        
                else:
                    msg = pickle.loads(msg_bytes)
                    try:
                        resp = skel.processing(msg)
                    except:
                        resp = "Error: Something went wrong."

                #tabela de recursos
                print (skel.toString())
                    
                #envio para o cliente
                msg_bytes = pickle.dumps(resp, -1)
                size_bytes = struct.pack("!i", len(msg_bytes))

                socket.sendall(size_bytes)
                socket.sendall(msg_bytes)

ListenSocket.close()
