#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_server.py
Grupo: 006
Números de aluno: 48303
"""

# Zona para fazer importação
import time
import sys
import socket as s
import pickle, struct

###############################################################################
#################################### TABLE ####################################
class MilkyTable:
    def __init__(self, headers = [], columns = 0, column_length = [], lines = []):
        self.headers = []
        self.columns = columns
        self.column_length = column_length
        self.lines = lines

    def verify_columns(self, list_elements):
        if self.columns == 0:
            self.columns = len(list_elements)
            for i in range(self.columns):
                try:
                    self.column_length[i] = len(str(list_elements[i]))
                except IndexError:
                    self.column_length.append(len(str(list_elements[i])))
            return True
        elif self.columns != len(list_elements):
            print ("List invalid: different number of columns.")
            return False
        else:
            for i in range(self.columns):
                if self.column_length[i] < len(str(list_elements[i])):
                    self.column_length[i] = len(str(list_elements[i]))
            return True

    def verify_column_length(self, column_index, element):
        if self.column_length[column_index] < len(str(element)):
            self.column_length[column_index] = len(str(element))

    def add_lines(self, list_elements):
        """
        list_elements is a list or tuple with the elements - strings or ints - of a line (e.g. list_elements = ['ID', 'NAME', 'DATE', 'DESCRIPTION', 'CATEGORY'])
        list_elements can also be a list of lists or tuples
        """
        #verify if list_elements is a list of elements or a list of lists
        if isinstance(list_elements[0], list) or isinstance(list_elements[0], tuple):
            #list_elements is a list of lists
            for l in list_elements:
                if self.verify_columns(l):
                    i = 0
                    for e in l:
                        self.verify_column_length(i, e)
                        i+=1
                self.lines.append(list(l))
        else:
            if self.verify_columns(list_elements):
                i = 0
                for e in list_elements:
                    self.verify_column_length(i, e)
                    i+=1
            self.lines.append(list(list_elements))

    def add_headers(self, list_headers):
        if self.verify_columns(list_headers):
            i = 0
            for e in list_headers:
                self.verify_column_length(i, e)
                i+=1
        if self.headers == []:
            self.headers = list(list_headers)
        else:
            print ("Headers list invalid.")

    def create_str_line(self, list_elements):
        i = 0
        line = "|"
        for l in list_elements:
            #print (self.column_length, list_elements)
            #print (len(self.column_length), len(list_elements))
            #print (line)
            spaces_len = self.column_length[i] - len(str(l))
            spaces = ""
            for n in range(spaces_len):
                spaces += " "

            line += " " + str(l) + spaces + " |"
            i+=1
        return line

    def toString(self):
        table = ""
        separator = "+"
        for k in self.column_length:
            spaces_len = k + 2
            spaces = ""
            for i in range(spaces_len):
                spaces += "-"
            separator += spaces + "+"

        #print headers
        table += separator + "\n" + self.create_str_line(self.headers) + "\n" + separator
        #print (separator)
        #print (self.create_str_line(self.headers))
        #print (separator)

        #print lines
        for line in self.lines:
            #print (self.create_str_line(line))
            table += "\n" + self.create_str_line(line)
        
        table += "\n" + separator
        return table #separator
###############################################################################
###############################################################################

class resource_lock:
    def __init__(self):
        """
        Define e inicializa as características de um LOCK num recurso.

        status, indica o estado do recurso, pode ser ['bloqueado', 'desbloqueado', 'inativo']
        blocks, indica o número de vezes que o recurso já foi bloqueado
        client_id, o id do cliente que bloqueia um recurso ou -1 no caso de estar 'desbloqueado' ou 'inativo'
        expire_time, tempo em que o bloqueio expira
        """
        self.status = "desbloqueado"
        self.blocks = 0
        self.client_id = -1
        self.expire_time = 0

    def lock(self, client_id, time_limit):
        """
        Bloqueia o recurso se este não estiver bloqueado ou inativo, ou mantém o bloqueio
        se o recurso estiver bloqueado pelo cliente client_id. Neste caso renova
        o bloqueio do recurso até time_limit.
        Retorna True se bloqueou o recurso ou False caso contrário.
        """
        if self.status == "desbloqueado":
            #pode bloquear
            self.status = "bloqueado"
            self.client_id = client_id
            self.expire_time = time.time() + time_limit
            self.blocks += 1
            return True
        elif self.status == "bloqueado":
            if self.client_id == client_id:
                #o mesmo cliente que bloqueou o recurso quer bloquear de novo, extede-se o tempo e adiona-se um block
                self.expire_time = time.time() + time_limit
                self.blocks += 1
                return True
        
        #retorna False se o recurso tem estado 'inativo' e se um cliente tentar bloquear um recurso já bloqueado por outro cliente
        return False

        

    def urelease(self):
        """
        Liberta o recurso incondicionalmente, alterando os valores associados
        ao bloqueio.
        """
        self.status = "desbloqueado"
        self.client_id = -1
        self.expire_time = 0

    def release(self, client_id):
        """
        Liberta o recurso se este foi bloqueado pelo cliente client_id,
        retornando True nesse caso. Caso contrário retorna False.
        """
        if self.client_id == client_id:
            self.urelease()
            return True
        
        return False


    def test(self):
        """
        Retorna o estado de bloqueio do recurso ou inativo, caso o recurso se 
        encontre inativo.
        """
        return self.status
    
    def stat(self):
        """
        Retorna o número de vezes que este recurso já foi bloqueado em k.
        """
        return self.blocks

    def disable(self):
        """
        Coloca o recurso inativo/indisponível incondicionalmente, alterando os 
        valores associados à sua disponibilidade.
        """
        self.status = "inativo"
        self.client_id = -1
        self.expire_time = 0

    def toList(self, id):
        """
        Coloca os atributos do recurso numa lista, de modo a ser facilmente 
        impressa.
        """
        result = [id, self.status, self.client_id, self.blocks, time.ctime(self.expire_time)]
        return result


        
###############################################################################

class lock_pool:
    def __init__(self, N, K, Y, T):
        """
        Define um array com um conjunto de locks para N recursos. Os locks podem
        ser manipulados pelos métodos desta classe.
        Define K, o número máximo de bloqueios permitidos para cada recurso. Ao 
        atingir K, o recurso fica indisponível/inativo.
        Define Y, o número máximo permitido de recursos bloqueados num dado 
        momento. Ao atingir Y, não é possível realizar mais bloqueios até que um 
        recurso seja libertado.
		Define T, o tempo máximo de concessão de bloqueio.
        """
        self.lock_pool = [] #definir melhor
        
        for n in range (N): #cria uma lista com N recursos, onde cada posicao ja tem iniciado um resource_look
            self.lock_pool.append(resource_lock())

        self.value_K = K
        self.value_Y = Y
        self.value_T = T
       
        
    def clear_expired_locks(self):
        """
        Verifica se os recursos que estão bloqueados ainda estão dentro do tempo
        de concessão do bloqueio. Liberta os recursos caso o seu tempo de
        concessão tenha expirado.
        """
        time_now = time.time()
        for r in self.lock_pool:
            if r.test() == "bloqueado" and r.expire_time < time_now: #recurso bloqueado com um tempo inferior ao de agora, significa que o bloqueio terminou
                if r.blocks == self.value_K: #recurso atengiu o limite, logo indisponivel
                    r.disable()
                else:
                    r.urelease()
        
        if self.stat_y == self.value_Y:
            print ("Número máximo de recursos bloqueados foi atingido.")
            

    def lock(self, resource_id, client_id, time_limit):
        """
        Tenta bloquear o recurso resource_id pelo cliente client_id, até ao
        instante time_limit.
        O bloqueio do recurso só é possível se o recurso estiver ativo, não 
        bloqueado ou bloqueado para o próprio requerente, e Y ainda não foi 
        excedido. É aconselhável implementar um método __try_lock__ para
        verificar estas condições.
        Retorna True em caso de sucesso e False caso contrário.
        """
        r = self.lock_pool[resource_id]

        if self.stat_y() < self.value_Y and self.stat(resource_id) < self.value_K:
            #o recurso pode ser bloqueado
            # return r.lock(client_id, time_limit)
            if r.lock(client_id, time_limit):
                return True
        
        elif self.stat(resource_id) == self.value_K:
            r.disable()
        
        return False
        

    def release(self, resource_id, client_id):
        """
        Liberta o bloqueio sobre o recurso resource_id pelo cliente client_id.
        True em caso de sucesso e False caso contrário.
        """
        return self.lock_pool[resource_id].release(client_id)

    def test(self,resource_id):
        """
        Retorna True se o recurso resource_id estiver bloqueado e False caso 
        esteja bloqueado ou inativo.
        """
        if self.lock_pool[resource_id].test() == "bloqueado":
            return True
        return False

    def stat(self,resource_id):
        """
        Retorna o número de vezes que o recurso resource_id já foi bloqueado, dos 
        K bloqueios permitidos.
        """
        return self.lock_pool[resource_id].stat()

    def stat_y(self):
        """
        Retorna o número de recursos bloqueados num dado momento do Y permitidos.
        """
        resources_blocked = 0
        i = 0
        for i in range(len(self.lock_pool)):
            if self.test(i):
                resources_blocked += 1
        return resources_blocked

    def stat_n(self):
        """
        Retorna o número de recursos disponíneis em N.
        """
        n = len(self.lock_pool) - self.stat_y()
        return n
		
    def toString(self):
        """
        Representação da classe para a saída standard. A string devolvida por
        esta função é usada, por exemplo, se uma instância da classe for
        passada à função print.
        """
        headers = ["ID RESOURCE", "STATUS", "ID CLIENT", "BLOCKS", "TIME LIMIT"]
        table = MilkyTable([], 0, [], [])

        table.add_headers(headers)
        
        i=0
        for r in self.lock_pool:
            table.add_lines(r.toList(i))
            i+=1
        
        return table.toString()
        #output = ""
        #
        # Acrescentar na output uma linha por cada recurso bloqueado, da forma:
        # recurso <número do recurso> bloqueado pelo cliente <id do cliente> até
        # <instante limite da concessão do bloqueio>
        #
        # Caso o recurso não esteja bloqueado a linha é simplesmente da forma:
        # recurso <número do recurso> desbloqueado
        # Caso o recurso não esteja inativo a linha é simplesmente da forma:
        # recurso <número do recurso> inativo
        #
        #return output

###############################################################################

# código do programa principal

#comandos = ["LOCK", "RELEASE", "TEST", "STATS", "STATS-Y", "STATS-N"]


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

#criacao do lock_pool
pool = lock_pool(arg_N, arg_K, arg_Y, arg_time)

#criacao do socket
#usar sock_utils

sock = s.socket(s.AF_INET, s.SOCK_STREAM)
sock.bind(('', PORT))
sock.listen(1)

while True:
    (conn_sock, addr) = sock.accept()
    print ('Ligado a %s', addr)
    resp = ''

    #limpar recursos
    pool.clear_expired_locks()


    size_bytes = conn_sock.recv(4)
    size = struct.unpack("!i", size_bytes)[0]
    msg_bytes = conn_sock.recv(size)
    msg = pickle.loads(msg_bytes)
    print (msg)

    #tratar do lock_pool
    try:
        if msg[0] == "LOCK":
            #command: LOCK <client_id> <resource_id>
            if pool.lock(msg[2], msg[1], arg_time):
                resp = "OK"
            else:
                resp = "NOK"
        
        elif msg[0] == "RELEASE":
            #command: RELEASE <client_id> <resource_id>
            if pool.release(msg[2], msg[1]):
                resp = "OK"
            else:
                resp = "NOK"

        elif msg[0] == "TEST":
            #command: TEST <resource_id>
            if pool.stat(msg[1]) == arg_K:
                resp = "DISABLE"
            else:
                if pool.test(msg[1]):
                    resp = "LOCKED"
                else:
                    resp = "UNLOCKED"
        
        elif msg[0] == "STATS":
            #command: STATS <resource_id>
            resp = pool.stat(msg[1])
                    
        elif msg[0] == "STATS-Y":
            #command: STATS-Y
            resp = pool.stat_y()
        
        elif msg[0] == "STATS-N":
            #command: STATS-N
            resp = pool.stat_n()
    
    except IndexError:
        resp = "UNKNOWN RESOURCE"
    
    #tabela de recursos
    print (pool.toString())

    msg_bytes = pickle.dumps(resp, -1)
    size_bytes = struct.pack("!i", len(msg_bytes))

    conn_sock.sendall(size_bytes)
    conn_sock.sendall(msg_bytes)
    
    conn_sock.close()

sock.close()
