#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import groupby
import pylab

__author__ = "Luís Miguel Duarte Conceição, 48303"
__email__ = "fc48303@alunos.fc.ul.pt"

def participacoes(dados):
    """
    Cria uma lista com o número de participações dos atletas.
    Requires: dados é uma lista de tuplos com informações de atletas
    Ensures: Retorna uma lista com a quantidade de participações
    de cada atleta organizada por ordem alfabética

    O(n*log(n)), onde n representa a quantidade de atletas presentes na
    lista de tuplos (dados) uma vez que esta função recorre ao metodo .sort()

    Características e regiões:
    -lista de tuplos vazia: True, False
    -nº de atletas diferentes na lista de tuplos: 0, 1, 2, 3
    -nº de repetições de um atleta: 0, >1

    >>> participacoes([]) #True, 0, 0
    []
    >>> participacoes([('Ana', 'Lisboa', 42195, '10-18', 2224)]) #False, 1, 0
    [1]
    >>> participacoes([('Ana', 'Lisboa', 42195, '10-18', 2224), \
    ('Eva', 'Nova Iorque', 42195, '06-13', 2319)]) #False, 2, 0
    [1, 1]
    >>> participacoes([('Ana', 'Lisboa', 42195, '10-18', 2224), \
    ('Eva', 'Nova Iorque', 42195, '06-13', 2319), \
    ('Dulce', 'Toquio', 42195, '02-22', 2449)]) #False, 3, 0
    [1, 1, 1]
    >>> participacoes([('Ana', 'Lisboa', 42195, '10-18', 2224), \
    ('Eva', 'Nova Iorque', 42195, '06-13', 2319), \
    ('Ana', 'Toquio', 42195, '02-22', 2403)]) #False, 2, >1
    [2, 1]
    >>> participacoes([('Ana', 'Lisboa', 42195, '10-18', 2224), \
    ('Eva', 'Nova Iorque', 42195, '06-13', 2319), \
    ('Ana', 'Toquio', 42195, '02-22', 2403), \
    ('Eva', 'Sao Paulo', 21098, '04-12', 1182), \
    ('Ana', 'Sao Paulo', 21098, '04-12', 1096), \
    ('Dulce', 'Toquio', 42195, '02-22', 2449), \
    ('Ana', 'Boston', 42195, '04-20', 2187)]) #False, 3, >1
    [4, 1, 2]
    """
    ciclo = 0
    nomes = []
    while ciclo in range(0, len(dados)):
        nomes.append(dados[ciclo][0])
        ciclo += 1
    nomes.sort()
    return [len(list(group)) for key, group in groupby(nomes)]


def calorias_acumuladas(dados, nome):
    """
    Cria uma lista, apartir da informação do input dados, com as calorias
    acumuladas do atleta (nome).
    Requires: dados é uma lista de tuplos e nome é uma string representando
    o nome de um atleta
    Ensures: Retorna uma lista com as calorias que o atleta (nome) acumulou
    num ano

    O(n), onde n representa a quantidade de atletas presentes na lista de
    tuplos (dados) uma vez que esta função a percorre com um ciclo for.
    
    Características e regiões:
    -lista de tuplos vazia: True, False
    -nº de atleta diferentes na lista de tuplos: 0, 1, 2, 3, 4
    -nº de repetições de um atleta: 0, >1
    >>> calorias_acumuladas([], 'Ana') #True, 0, 0
    []
    >>> calorias_acumuladas([('Ana', 'Lisboa', 42195, '10-18', 2224)], 'Ana') #False, 1, 0
    [2224]
    >>> calorias_acumuladas([('Ana', 'Lisboa', 42195, '10-18', 2224), \
    ('Eva', 'Nova Iorque', 42195, '06-13', 2319)], 'Eva') #False, 2, 0
    [2319]
    >>> calorias_acumuladas([('Ana', 'Lisboa', 42195, '10-18', 2224), \
    ('Eva', 'Nova Iorque', 42195, '06-13', 2319), \
    ('Dulce', 'Toquio', 42195, '02-22', 2449)], 'Dulce') #False, 3, 0
    [2449]
    >>> calorias_acumuladas([('Ana', 'Lisboa', 42195, '10-18', 2224), \
    ('Eva', 'Nova Iorque', 42195, '06-13', 2319), \
    ('Ana', 'Toquio', 42195, '02-22', 2403)], 'Ana') #False, 2, >1
    [2224, 4627]
    >>> calorias_acumuladas([('Ana', 'Lisboa', 42195, '10-18', 2224), \
    ('Eva', 'Nova Iorque', 42195, '06-13', 2319), \
    ('Ana', 'Toquio', 42195, '02-22', 2403), \
    ('Eva', 'Sao Paulo', 21098, '04-12', 1182), \
    ('Ana', 'Sao Paulo', 21098, '04-12', 1096), \
    ('Dulce', 'Toquio', 42195, '02-22', 2449), \
    ('Ana', 'Boston', 42195, '04-20', 2187)], 'Eva') #False, 3, >1
    [2319, 3501]
    """
    lista = []
    cal = 0
    for tuplo in dados:
        if nome == tuplo[0]:
            cal += tuplo[4]
            lista.append(cal)
    return lista


def graficos(dados, nome):
    """
    Devolve dois graficos, um de barras com informações relativas aos atletas
    em geral e outro com informações sobre as calorias acumuladas do atleta
    introduzido no input nome
    Requires: dados é uma lista de tuploes e nome é uma string representando
    o nome de um atleta
    Ensures: retorna um gráfico de barras com o número de participações de
    cada atleta e um gráfico com as calorias acumuladas no atleta (nome)
    """
    Oy=calorias_acumuladas(dados,nome)
    Ox=sorted(zip(*(filter(lambda x:x[0]==nome,dados)))[3])
    etiquetas = []
    atletas = []
    area=0.89
    for tuplo in dados:
        if tuplo[0] == nome:
            etiquetas.append(tuplo[3])
        if tuplo[0] not in atletas:
            atletas.append(tuplo[0])
    etiquetas.sort()
    atletas.sort()
    escala_Ox=range(len(Ox))
    escala_Oy=range(len(atletas))
    pylab.figure(1)
    pylab.subplot(1,2,1)
    pylab.title(u'Participacoes')
    pylab.bar(escala_Oy,participacoes(dados),area)
    pylab.xticks(map(lambda escala_Ox: escala_Ox + area / 2.0, escala_Oy),atletas)
    pylab.subplot(1,2,2)
    pylab.title(u'Calorias acumuladas de ' + nome)
    pylab.xticks(escala_Ox,Ox)
    pylab.plot(escala_Ox, Oy,'-o')
    pylab.show()
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
