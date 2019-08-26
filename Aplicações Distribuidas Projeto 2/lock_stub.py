#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 2 - lock_stub.py
Grupo: 6
Números de aluno: 50036, 49050, 48303
"""
import net_client

class ListStub:
    def __init__(self):
        self.conn_sock = None
        self.command = []

    def connect(self, address, port):
        self.conn_sock = net_client.server(address, port)
        self.conn_sock.connect()

    def close(self):
        self.conn_sock.close()
        self.conn_sock = None

    def send_receive_msg(self):
        msg = self.conn_sock.send_receive(self.command)
        return msg

    def list(self):
        return self.command

    def append(self, e):
        self.command.append(e)

    def clear(self):
        self.command = []

    def helpTable(self):
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
