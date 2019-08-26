# -*- coding: utf-8 -*-
"""
Aplicações Distribuídas - Projeto 3
Grupo: 
Números de aluno: 48303,
"""

import sqlite3
import json
from os.path import isfile

class database:
    def __init__(self, dbname):
        self.conn = None
        self.cursor = None
        db_is_created = isfile(dbname)
        self.conn = sqlite3.connect(dbname, check_same_thread = False)
        self.cursor = self.conn.cursor()
        if not db_is_created:
            query = open("create_db.sql", "r").read()
            self.cursor.executescript(query)
            self.conn.commit()
  
#---------------------------- QUERYS GERAIS -------------------------------
            
    #OBTER TODOS OS VALORES DE UMA TABELA
    def select_all(self, table):
        rows = self.cursor.execute('SELECT * FROM ' + table).fetchall()
        return rows
    
    #OBTER TODOS OS IDS
    def select_all_ids(self, table):
        rows = self.cursor.execute('SELECT id FROM ' + table).fetchall()
        return json.dumps(rows)

    #OBTER ELEMENTO POR ID
    def select_elementById(self, table, id):
        rows = self.cursor.execute('SELECT * FROM ' + table + ' WHERE id = ?', (id,)).fetchone()
        return rows

    #ELIMINAR ELEMENTO BY ID
    def remove_elementById(self, table, id):
        rows = self.cursor.execute('DELETE FROM ' + table + ' WHERE id = ?', (id,))
        self.conn.commit()

    #QUERY PARA APAGAR TUDO DE UMA TABELA
    def remove_all(self, table):
        rows = self.cursor.execute('DELETE FROM ' + table)
        self.conn.commit()

#---------------------------- ADD ----------------------------------------

    def add_user(self, dados):
        rows = self.cursor.execute('INSERT INTO utilizadores (nome, username, password) VALUES (?,?,?)',dados) 
        self.conn.commit()
        
    def add_banda(self, dados):
        rows = self.cursor.execute('INSERT INTO bandas (nome, ano, genero) VALUES (?,?,?)', dados)
        self.conn.commit()
    
    def add_album(self, dados):
        rows = self.cursor.execute('INSERT INTO albuns (id_banda, nome, ano_album) VALUES (?,?,?)', dados)
        self.conn.commit()

#------------------------- LISTAS ALBUNS ----------------------------------
        
    def select_all_ids_from_list_albuns(self):
        rows = self.cursor.execute('SELECT id_user , id_album, id_rate FROM listas_albuns').fetchall()
        return json.dumps(rows)

    def add_list_albuns(self, dados):
        rows = self.cursor.execute('INSERT INTO listas_albuns (id_user, id_album, id_rate) VALUES (?,?,?)', dados)
        self.conn.commit()

#---------------------------- SELECT ALBUNS ------------------------------
        
    def select_albuns_by_banda_id(self, id_banda):
        rows = self.cursor.execute('SELECT * FROM albuns WHERE id_banda = ? ', (id_banda,)).fetchall()
        return rows

    def select_albuns_by_id(self, id):
        rows = self.cursor.execute('SELECT * FROM albuns WHERE id = ? ', (id,)).fetchall()
        return rows
    
    def select_all_albuns_by_id_user(self,id_user):
        rows = self.cursor.execute('SELECT id_user , id_album, id_rate FROM listas_albuns WHERE id_user = ?', (id_user,)).fetchall()
        return rows

    def select_all_albuns_by_rate(self, rate):
        rows = self.cursor.execute('SELECT id_user, id_album, id_rate FROM listas_albuns WHERE id_rate = ?', (rate,)).fetchall()
        return rows

#---------------------------- REMOVE -------------------------------------
    def remove_all_albuns_with_id_user(self, id_user):
        rows = self.cursor.execute('DELETE FROM listas_albuns WHERE id_user = ?', (id_user,)).fetchall()
        self.conn.commit()

    def remove_all_albuns_with_id_banda(self, id_banda):
        rows = self.cursor.execute('DELETE FROM albuns WHERE id_banda = ?', (id_banda,)).fetchall()
        self.conn.commit()

    def remove_all_albuns_with_rate(self, rate):
        rows = self.cursor.execute('DELETE FROM listas_albuns WHERE id_rate = ?', (rate,)).fetchall()
        self.conn.commit()

    def remove_user(self, id_user):
        rows = self.cursor.execute('DELETE FROM utilizadores WHERE id = ?', (id_user,)).fetchall()
        self.conn.commit()

    def remove_banda(self, id_banda):
        rows = self.cursor.execute('DELETE FROM bandas WHERE id = ?', (id_banda,)).fetchall()
        self.conn.commit()

    def remove_album(self, id_album):
        rows = self.cursor.execute('DELETE FROM albuns WHERE id = ?', (id_album,)).fetchall()
        self.conn.commit()

#---------------------------- UPDATE -------------------------------------

    def update_user(self, dados):
        rows = self.cursor.execute('UPDATE utilizadores SET password = ? WHERE id = ? ',dados)
        self.conn.commit()

    def update_rate(self, dados):
        rows = self.cursor.execute('UPDATE listas_albuns SET id_rate = ? WHERE id_user = ? AND id_album = ?', dados)
        self.conn.commit()
