#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 2 - lock_skel.py
Grupo: 6
Números de aluno: 50036, 49050, 48303
"""
# Zona para fazer importação
import pickle, struct, sock_utils
from lock_pool import lock_pool

class ListSkeleton:
    def __init__(self, num_n, num_k, num_y, tempo):
        #self.resp = []
        #self.clientes = {}
        self.tempo = tempo
        self.pool = lock_pool(num_n, num_k, num_y, tempo)

    def clear_locks(self):
        self.pool.clear_expired_locks()
    
    def processing(self, msg):
        resp = []
        try:
            if msg[0] == 10:
                #command: LOCK <client_id> <resource_id>
                resp.append(msg[0] + 1)
                if self.pool.lock(msg[2], msg[1], self.tempo):
                    resp.append(True)
                else:
                    resp.append(False)
            
            elif msg[0] == 20:
                #command: RELEASE <client_id> <resource_id>
                resp.append(msg[0] + 1)
                if self.pool.release(msg[2], msg[1]):
                    resp.append(True)
                else:
                    resp.append(False)

            elif msg[0] == 30:
                #command: TEST <resource_id>
                resp.append(msg[0] + 1)
                if self.pool.stat(msg[1]) == arg_K:
                    resp.append("DISABLE")
                else:
                    if self.pool.test(msg[1]):
                        resp.append(True)
                    else:
                        resp.append(False)
            
            elif msg[0] == 40:
                #command: STATS <resource_id>
                resp.append(msg[0] + 1)
                resp.append(self.pool.stat(msg[1]))
                        
            elif msg[0] == 50:
                #command: STATS-Y
                resp.append(msg[0] + 1)
                resp.append(self.pool.stat_y())
            
            elif msg[0] == 60:
                #command: STATS-N
                resp.append(msg[0] + 1)
                resp.append(self.pool.stat_n())
        
        except IndexError:
            resp.append(None)

        return resp

    def toString(self):
        return self.pool.toString()