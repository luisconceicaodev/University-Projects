#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Luís Miguel Duarte Conceição, 48303"

import csv
import numpy

def media_idades(nome_ficheiro_animais, nome_ficheiro_donos, nome_ficheiro_medias):
    """
    Requires: nome_ficheiro_animais é um ficheiro csv que contêm informações sobre os animais,
    nomeadamente nome, especie e idade
    nome_ficheiro_donos é um ficheiro csv que contêm informações sobre os donos, nomeadamente
    nome do dono e nome do animal
    nome_ficheiro_media é um ficheiro csv sem informações
    Ensures: escreve a média das idades (em unidades) de todos os animais de
    cada dono num ficheiro csv
    """
    fieldnames = ['Nome do dono', 'Media das idades']
    with open(nome_ficheiro_animais, 'rU') as ficheiro_csv:
        leitor_animais = csv.DictReader(ficheiro_csv,
                                fieldnames = None,
                                delimiter = ';')
        leitor_animais = [linha for linha in leitor_animais]
    
    with open(nome_ficheiro_donos, 'rU') as ficheiro_csv:
        leitor_donos = csv.DictReader(ficheiro_csv,
                                fieldnames = None,
                                delimiter = ';')
        leitor_donos = [linha for linha in leitor_donos]
    media = calcula_media(leitor_animais, leitor_donos)
    with open(nome_ficheiro_medias, 'w') as ficheiro_csv:
        writer = csv.DictWriter(ficheiro_csv, delimiter = ';', fieldnames=fieldnames)
        writer.writeheader()
        for line in media:
            writer.writerow(line)
    
def calcula_media(tabela_animais, tabela_donos):
    """
    Requires: tabela_animais é o conteudo de nome_ficheiro_animais da
    função media_idades em formato de tabela (lista de dicionários)
    tabela_donos é o conteudo de nome_ficheiro_donos da função media_idades
    em formato de tabela (lista de dicionários)
    Ensures: retorna uma tabela (lista de dicionários) em que as chaves são
    o nome dos donos e os valores são a média de idades de todos os animais
    pertencentes ao respetivo dono

    O(m + n*m + n*m + n), onde n representa a quantidade de dicionários nas tabelas tabela_animais
    e m representa a quantidade de cicionários na tabela tabela_donos uma vez que esta função percorre
    e cria listas e dicionários através destas com ciclos for

    Características e regiões:
    - tabelas vazias?: True, False
    - número de donos: 0, 1, >1
    - número de animais: 0, 1, >1

    >>> calcula_media([],[]) # True, 0, 0
    []
    
    >>> calcula_media([{'Idade': '57', 'Especie': 'Tartaruga', 'Nome do animal': 'Michelangelo'}], \
    [{'Nome do dono': 'Ana', 'Nome do animal': 'Michelangelo'}]) # False, 1, 1
    [{'Nome do dono': 'Ana', 'Media das idades': 57}]
    
    >>> calcula_media([{'Idade': '57', 'Especie': 'Tartaruga', 'Nome do animal': 'Michelangelo'}, \
    {'Idade': '45', 'Especie': 'Tartaruga', 'Nome do animal': 'Leonardo'}], \
    [{'Nome do dono': 'Ana', 'Nome do animal': 'Michelangelo'}, \
    {'Nome do dono': 'Ana', 'Nome do animal': 'Leonardo'}]) # False, 1, >1
    [{'Nome do dono': 'Ana', 'Media das idades': 51}]
    
    >>> calcula_media([{'Idade': '8', 'Especie': 'Gato', 'Nome do animal': 'Felix'}, \
    {'Idade': '57', 'Especie': 'Tartaruga', 'Nome do animal': 'Michelangelo'}, \
    {'Idade': '12', 'Especie': 'Cao', 'Nome do animal': 'Rantanplan'}, \
    {'Idade': '2', 'Especie': 'Peixe', 'Nome do animal': 'Nemo'}, \
    {'Idade': '45', 'Especie': 'Tartaruga', 'Nome do animal': 'Leonardo'}, \
    {'Idade': '9', 'Especie': 'Cao', 'Nome do animal': 'Milo'}, \
    {'Idade': '57', 'Especie': 'Tartaruga', 'Nome do animal': 'Raphael'}, \
    {'Idade': '4', 'Especie': 'Peixe', 'Nome do animal': 'Dory'}], \
    [{'Nome do dono': 'Ana', 'Nome do animal': 'Michelangelo'}, \
    {'Nome do dono': 'Eva', 'Nome do animal': 'Dory'}, \
    {'Nome do dono': 'Ada', 'Nome do animal': 'Rantanplan'}, \
    {'Nome do dono': 'Ana', 'Nome do animal': 'Leonardo'}, \
    {'Nome do dono': 'Eva', 'Nome do animal': 'Felix'}, \
    {'Nome do dono': 'Ana', 'Nome do animal': 'Raphael'}, \
    {'Nome do dono': 'Eva', 'Nome do animal': 'Nemo'}]) # False, >1, >1
    [{'Nome do dono': 'Eva', 'Media das idades': 5}, {'Nome do dono': 'Ana', 'Media das idades': 53}, {'Nome do dono': 'Ada', 'Media das idades': 12}]
    """
    nomes = []
    donos_animais = {}
    dic = {}
    resultado = []
    final = {}
    for item in tabela_donos:
        if item['Nome do dono'] in donos_animais:
            donos_animais[item['Nome do dono']].append(item['Nome do animal'])
        else:
            donos_animais[item['Nome do dono']] = [item['Nome do animal']]
        dic[item['Nome do dono']] = 0
    for item in tabela_animais:
        for key in donos_animais:
            if item['Nome do animal'] in donos_animais[key]:
                dic[key] += float(item['Idade'])
    for key in donos_animais:
        for key2 in dic:
            if key == key2:
                num = dic[key]/len(donos_animais[key])
                dic[key] = (int(numpy.mean(num)+0.5))
    for key in dic:
        final = {}
        final['Nome do dono'] = key
        final['Media das idades'] = dic[key]
        resultado.append(final)
    return resultado             

if __name__ == "__main__":
    import doctest
    doctest.testmod()
