"""
Aplicações distribuídas - Projeto 2 - sock_utils.py
Grupo: 006
Números de aluno: 50036, 49050, 48303
"""

import socket as s

def create_tcp_server_socket(address, port, queue_size):
    HOST = address
    PORT = port
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(queue_size)
    return sock

def create_tcp_client_socket(address, port):
    HOST = address
    PORT = port
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.connect((HOST, PORT))
    return sock

def receive_all(socket, length) :
  return socket.recv(length)
