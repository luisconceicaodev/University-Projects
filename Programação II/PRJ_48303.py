#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Universidade de Lisboa
Faculdade de Ciências
Departamento de Informática
Licenciatura em Tecnologias da Informação
2015/2016

Programação II

Projeto de programação:
Crime numa grande cidade
"""

__author__ = "Luís Conceição, 48303; Inês Lino, 48311"

import csv
from math import radians, cos, sin, asin, sqrt, pi
from itertools import groupby
import pylab
import matplotlib.pyplot as plt

def crimes(nome_ficheiro):
    """
    Esta função recebe o nome de um ficheiro como parâmetro,
    e traça uma figura com quatro gráficos.

    Requires: nome_ficheiro é uma string do nome de um ficheiro CSV
    Ensures: traça uma figura com quatro gráficos com dados relativos
    ao ficheiro CSV
    """
    
    pylab.figure(1)
    pylab.suptitle("O crime na cidade de Baltimore")
    traca_crimes_por_data(ler_tabela_de_csv(nome_ficheiro))
    traca_crimes_por_hora(ler_tabela_de_csv(nome_ficheiro))
    traca_crimes_por_tipo(ler_tabela_de_csv(nome_ficheiro))
    traca_crimes_por_distancia(ler_tabela_de_csv(nome_ficheiro),100)

    pylab.show()


def traca_crimes_por_data(grafico):
    """
    Esta função recebe uma lista de listas com a informação sobre os
    crimes (lida diretamente de um ficheiro CSV descarregado do Data
    Search Baltimore, e inalterada) e devolve dados essenciais para traçar
    o seu respetivo grafico na função crimes.

    Requires: grafico é uma lista de listas, uma lista representando
    as abcissas e outra representando as ordenadas.
    Ensures: retorna dados essenciais para traçar o seu respetivo grafico na função
    crimes.
    """
    coordenadas_graf1 = crimes_por_data(grafico)
    x1 = coordenadas_graf1[0]
    y1 = coordenadas_graf1[1]
    range_x1 = range(len(coordenadas_graf1[0]))

    pylab.subplot(2, 2, 1)
    pylab.title(u"Número de crimes por dia")
    pylab.xticks([182,548,913,1278,1644,2009], [2011,2012,2013,2014,2015,2016])
    plt.xlim(0, 2230)
    pylab.plot(range_x1, y1, color='blue')
    pylab.ylabel(u'#Crimes')
    pylab.xlabel(u'Anos')
    

def traca_crimes_por_hora(grafico):
    """
    Esta função recebe uma lista de listas com a informação sobre os
    crimes (lida diretamente de um ficheiro CSV descarregado do Data
    Search Baltimore, e inalterada) e devolve dados essenciais para traçar
    o seu respetivo grafico na função crimes.

    Requires: grafico é uma lista de listas, uma lista representando
    as abcissas e outra representando as ordenadas.
    Ensures: retorna dados essenciais para traçar o seu respetivo grafico na função
    crimes.
    """
    largura = 1
    coordenadas_graf2 = crimes_por_hora(grafico) #
    x2 = coordenadas_graf2[0]
    y2 = coordenadas_graf2[1]
    range_x2 = range(len(coordenadas_graf2[0]))
    range_y2 = range(len(coordenadas_graf2[1]))

    pylab.subplot(2, 2, 2)
    pylab.title(u'Número de crimes por hora')   
    pylab.bar(range_x2, y2, largura, color='blue')
    pylab.xticks(map(lambda range_x2: range_x2 + largura / 2.0, range_y2), x2)
    plt.xlim([0, 24])
    pylab.ylabel(u'#Crimes')
    pylab.xlabel(u'Horas')

def traca_crimes_por_tipo(grafico):
    """
    Esta função recebe uma lista de listas com a informação sobre os
    crimes (lida diretamente de um ficheiro CSV descarregado do Data
    Search Baltimore, e inalterada) e devolve dados essenciais para traçar
    o seu respetivo grafico na função crimes.

    Requires: grafico é uma lista de listas, uma lista representando
    as abcissas e outra representando as ordenadas.
    Ensures: retorna dados essenciais para traçar o seu respetivo grafico na função
    crimes.
    """
    largura = 1
    coordenadas_graf3 = crimes_por_tipo(grafico)
    range_x3 = range(len(coordenadas_graf3[0]))
    range_y3 = range(len(coordenadas_graf3[1]))
    
    x3 = coordenadas_graf3[0]
    y3 = coordenadas_graf3[1]

    pylab.subplot(2, 2, 3)
    pylab.title(u'Número de crimes por tipo')   
    pylab.bar(range_x3, y3, largura, color='blue')
    pylab.xticks(map(lambda range_x3: range_x3 + largura / 2.0, range_y3), x3, rotation=90)
    plt.xlim([0, 15])
    pylab.ylabel(u'#Crimes')

def traca_crimes_por_distancia(grafico, distancia_maxima):
    """
    Esta função recebe uma lista de listas com a informação sobre os
    crimes (lida diretamente de um ficheiro CSV descarregado do Data
    Search Baltimore, e inalterada) e devolve dados essenciais para traçar
    o seu respetivo grafico na função crimes

    Requires: grafico é uma lista de listas, uma lista representando
    as abcissas e outra representando as ordenadas e distancia_maxima é um inteiro
    representando a distancia máxima a que a coroa pode demonstrar dados.
    Ensures: retorna dados essenciais para traçar o seu respetivo grafico na função
    crimes.
    """
    coordenadas_graf4 = crimes_por_distancia(grafico)
    x4 = coordenadas_graf4[0]
    y4 = coordenadas_graf4[1]
    range_x4 = range(len(x4))
    range_distancia = range(0, distancia_maxima+1, 20)
    pylab.subplot(2, 2, 4)
    pylab.title(u"Número de crimes por distância ao centro")
    pylab.xticks(range_distancia, range_distancia)
    plt.xlim(0, 100)
    pylab.plot(range_x4, y4, color='blue')
    pylab.ylabel(u'#Crimes por km2')
    pylab.xlabel(u'Distância (x 100m)')
    

def crimes_por_data(tabela):
    """
    Esta função recebe uma lista de dicionários e devolve um par de listas:
    abcissas e ordenadas. As abcissas contêm as datas dos crimes por ordem
    crescente; as ordenadas contêm o número de crimes que ocorreram em cada data.

    Requires: tabela é uma lista de dicionários representando os dados
    de um ficheiro CSV com dados sobre crimes.
    Ensures: retorna um par de listas: abcissas e ordenadas.
    """
    coordenadas = []
    abcissas = []
    ordenadas = []
    
    for item in tabela:
        soma = 0
        x = item["CrimeDate"]
        x = x.replace("/","")
        novo_formato = ""
        novo_formato += x[4:]
        novo_formato += x[:2]
        novo_formato += x[2:4]  
        abcissas.append(novo_formato)
    abcissas.sort()
    ordenadas = [len(list(group)) for key, group in groupby(abcissas)]
    abcissas = sorted(set(abcissas))
    coordenadas.append(abcissas)
    coordenadas.append(ordenadas)
    return coordenadas
            
            
    
    
def crimes_por_hora(tabela):
    """
    Esta função recebe uma lista de dicionários e devolve um par de listas:
    abcissas e ordenadas. As abcissas contêm uma lista ordenada de horas
    entre 0 e 23 ; as ordenadas contêm o total de crimes, independentemente
    da data de ocorrência destes, nas horas correspondentes na lista das abcissas.

    Requires: tabela é uma lista de dicionários representando os dados
    de um ficheiro CSV com dados sobre crimes.
    Ensures: retorna um par de listas: abcissas e ordenadas.
    """
    coordenadas = []
    abcissas = range(0,24)
    ordenadas = []
    horas = []
    for item in tabela:
        hora = item["CrimeTime"]
        hora = ((hora.split(":"))[0])
        if len(hora) == 2:
            horas.append(hora)
    horas.sort()
    ordenadas = [len(list(group)) for key, group in groupby(horas)]
    coordenadas.append(abcissas)
    coordenadas.append(ordenadas)
    return coordenadas 
    

def crimes_por_tipo(tabela):
    """
    Esta função recebe uma lista de dicionários e devolve um par de
    listas: abcissas e ordenadas. As abcissas contêm o tipo do crime,
    dado por um valor do tipo string constante no campo Description
    do ficheiro CSV); as ordenadas contêm o número de crimes que ocorreram
    para o tipo correspondente.

    Requires: tabela é uma lista de dicionários representando os dados
    de um ficheiro CSV com dados sobre crimes.
    Ensures: retorna um par de listas: abcissas e ordenadas.
    """
    coordenadas = []
    abcissas = []
    ordenadas = []
    filtro = []
    for item in tabela:
        tipo_crime = item["Description"]
        filtro.append(tipo_crime)
        if tipo_crime not in abcissas:
            abcissas.append(tipo_crime)
    filtro.sort()
    abcissas.sort()
    ordenadas = [len(list(group)) for key, group in groupby(filtro)]
    coordenadas.append(abcissas)
    coordenadas.append(ordenadas)
    return coordenadas

def crimes_por_distancia(tabela):
    """
    Esta função recebe uma lista de dicionários e devolve um par de
    listas: abcissas e ordenadas. As abcissas contêm distâncias múltiplos
    de 100m ao centro da cidade.
    As ordenadas contêm a densidade dos crimes em cada coroa circular.

    Requires: tabela é uma lista de dicionários representando os dados
    de um ficheiro CSV com dados sobre crimes.
    Ensures: retorna um par de listas: abcissas e ordenadas.
    """
    centro = [39.289444, -76.616667]
    latitudes = []
    longitudes = []
    abcissas = range(0,100)
    ordenadas = []
    coordenadas = []
    metros = []
    ciclo1 = 0.1
    ciclo2 = 0
    for item in tabela:
        local = item["Location 1"]
        if len(local.split(",")) == 2:
            lat1 = float((local.split(","))[0].replace("(",""))
            lon1 = float((local.split(","))[1].replace(")",""))
            distancia = int(haversine(lat1, lon1, centro[0], centro[1]))
            if len(str(distancia)) == 5:
                if str(distancia)[0] == 1:
                    metros.append(100)
            elif len(str(distancia)) > 5:
                pass
            else:
                metros.append(distancia//100)
    metros.sort()
    ocorrencia = [len(list(group)) for key, group in groupby(metros)]
    for item in ocorrencia:
        ordenadas.append(item / (pi * (ciclo1**2) - pi *(ciclo2**2)))
        ciclo1 += 0.1
        ciclo2 += 0.1
    coordenadas.append(abcissas)
    coordenadas.append(ordenadas)
    return coordenadas
           

def haversine(lat1, lon1, lat2, lon2):
    """
    Returns the great circle distance between two GPS points given in degrees.
    See:
        http://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
        http://www.movable-type.co.uk/scripts/latlong.html
    """
    lat1, lat2, dlat, dlon = map(radians, [lat1, lat2, lat2 - lat1, lon2 - lon1])
    a = sin(dlat / 2.0) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2.0) ** 2
    c = 2 * asin(sqrt(a))
    raio_da_terra_em_metros = 6371000
    return c * raio_da_terra_em_metros


def ler_tabela_de_csv(nome_ficheiro_csv):
    """
    Requires: o nome de um ficheiro CSV com cabeçalho na primeira linha.
    Ensures: retorna uma tabela no formato de lista de dicionários.
    """
    with open(nome_ficheiro_csv, 'rU') as ficheiro_csv:
        leitor = csv.DictReader(ficheiro_csv, delimiter=',')
        return [linha for linha in leitor]


### Verificando o tempo que leva a construir os dados dos gráficos

from timeit import timeit

# Uma string representando o nome do ficheiro CSV contendo os dados de
# interesse para o trabalho. Coloquem aqui o nome do vosso ficheiro.
ficheiro_dados_crimes = 'BPD_Part_1_Victim_Based_Crime_Data.csv'

def go_time():
    """Ensures: Devolve o tempo de execução da função dados_crimes()
    quando aplicada ao ficheiro ficheiro_dados_crimes.
    """
    return timeit("dados_crimes(ficheiro_dados_crimes)",
            "from PRJ_48303 import dados_crimes", number = 1)

def dados_crimes(nome_ficheiro):
    """Esta função não deve levar mais do que um determinado tempo
    quando executada numa máquina do laboratório do Departamento de
    Informática. O tempo em questão será anunciado na semana 9 de maio
    de 2016.

    Requires: nome_ficheiro é uma string representando o nome de um
    ficheiro CSV com dados sobre crimes.
    
    Ensures: Devolve um quadrúplo com os dados referentes a cada um dos
    quatro gráficos, de acordo com o enunciado do projeto.
    """
    t = ler_tabela_de_csv(nome_ficheiro)
    return crimes_por_data(t), crimes_por_hora(t), \
           crimes_por_tipo(t), crimes_por_distancia(t)
