# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - net_client.py
Grupo: 006
Números de aluno: X, Y, 48303
"""

# zona para fazer importação

from sock_utils import create_tcp_client_socket
import pickle, struct

# definição da classe server 

class server:
    """
    Classe para abstrair uma ligação a um servidor TCP. Implementa métodos
    para estabelecer a ligação, para envio de um comando e receção da resposta,
    e para terminar a ligação
    """
    def __init__(self, address, port):
        """
        Inicializa a classe com parâmetros para funcionamento futuro.
        """
        self.HOST = address
        self.PORT = port
        self.sock = None
        
    def connect(self):
        """
        Estabelece a ligação ao servidor especificado na inicialização do
        objeto.
        """
        try:
            self.sock = create_tcp_client_socket(self.HOST, self.PORT)
        except:
            print("Ligação ao servidor falhou")
        

    def send_receive(self, data):
        """
        Envia os dados contidos em data para a socket da ligação, e retorna a
        resposta recebida pela mesma socket.
        """
        try:
            msg_bytes = pickle.dumps(data, -1)
            size_bytes = struct.pack('!i',len(msg_bytes))
            self.sock.sendall(size_bytes)
            self.sock.sendall(msg_bytes)
            size_bytes = self.sock.recv(4)
            size = struct.unpack('!i',size_bytes)[0]  
            msg_bytes = self.sock.recv(size)
            res = pickle.loads(msg_bytes)
            return res
        except:
            return "O envio da mensagem falhou"

    def close(self):
        """
        Termina a ligação ao servidor.
        """
        try:
            self.sock.close()
        except:
            print("Terminar a ligação com o servidor falhou")
        
