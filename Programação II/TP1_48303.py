#!/usr/local/bin/python
# coding: utf-8

__author__ = "Luís Miguel Duarte Conceição, 48303"
__email__ = "fc48303@alunos.fc.ul.pt"

dict = {'2': 'A', '22': 'B','222': 'C','3': 'D', '33': 'E','333': 'F', 
        '4': 'G', '44': 'H', '444': 'I', '5': 'J', '55':'K', '555':'L', 
        '6': 'M', '66': 'N', '666': 'O', '7': 'P', '77':'Q', '777':'R', 
        '7777':'S', '8':'T', '88': 'U', '888': 'V', '9': 'W', '99': 'X', 
        '999': 'Y', '9999': 'Z'}

def teclas_para_palavra(string):                                                                          
    """
    Converte sequências de números em letras como num teclado númerico.
    Requires: string é uma string de sequência de números entre 2 a 9.
    Ensures: converte uma string de sequências de números inteiros
    nas letras que equivalem as sequências num teclado númerico
    
    O(n), onde n representa a quantidade de números no parâmetro string
    porque esta função percorre com um for cada sequência de números não
    separados por um espaço.
    
    Características e regiões:
    -string vazia: True, False
    -quantidade de espaços vazios na string: 0, 1, >1
    -números "7" ou "9": 0, 1, >1
    -números restantes: 0, 1, >1
    -sequências de números diferentes sem espaço entre si: 0, 1, >1
    -números "7" ou "9" repetidos mais do que 4 vezes: True, False
    -números restantes repetidos mais do que 3 vezes: True, False
    
    >>> teclas_para_palavra("") # True, 0, 0, 0, 0, False, False
    ''
    >>> teclas_para_palavra("3") # False, 0, 0, 1, 0, False, False
    'D'
    >>> teclas_para_palavra("3333") #False, 0, 0, >1, 0, False, True
    'D'
    >>> teclas_para_palavra("9") # False, 0, 1, 0, 0, False, False
    'W'
    >>> teclas_para_palavra("999999999") # False, 0, >1, 0, 0, True, False
    'W'
    >>> teclas_para_palavra("77777") # False, 0, >1, 0, 0, True, False
    'P'
    >>> teclas_para_palavra("777777777") # False, 0, >1, 0, 0, True, False
    'P'
    >>> teclas_para_palavra("222 2") # False, 1, 0, >1, 0, False, False
    'CA'
    >>> teclas_para_palavra("222 2333 33") # False, >1, 0, >1, 1, False, False
    'CAFE'
    >>> teclas_para_palavra("8888822") # False, 0, 0, >1, 1, False, True
    'UB'
    >>> teclas_para_palavra("2277777") # False, 0, >1, >1, 1, True, False
    'BP'
    >>> teclas_para_palavra("224444         7799999") # False, >1, >1, >1, >1, True, True
    'BGQW'
    """
    string = string.split()
    msg =  ""   
    for item in string:
        if (item == len(item) * item[0]) == (True):
            msg += repetidos(item)
        else:
            msg += misturados(item)
    return msg
    
def repetidos(item):
    """
    Retorna a letra correspondente, em teclado númerico,
    à sequência de números iguais.
    Requires: item é uma string de números todos iguais.
    Ensures: retorna a letra correspondente à sequência de
    números iguais.
    
    O(n), onde n representa o comprimento do parâmetro item,
    uma vez que na presente função existe um range() que depende
    do comprimento de item.
    """
    word = ""
    if (item[0] == '7' or item[0] == '9') and len(item) > 4:
        n = 4
        item = [item[i:i+n] for i in range(0, len(item), n)]
        word += dict[item[-1]]
    elif (item[0] == '7' or item[0] == '9') and len(item) <= 4:
        word += dict[item]
    else:
        n = 3
        item = [item[i:i+n] for i in range(0, len(item), n)]
        word += dict[item[-1]]  
    return word

def misturados(item): 
    """
    Requires: item é uma string de tamanho variável constituida por
    2 números diferentes.
    Ensures: separa a string item por números iguais entre si
    e posteriormente retorna as suas letras equivalentes em teclado númerico.
    
    O(n**2), onde n representa a quantidade de números diferentes
    no parâmetro item porque na presente função existe um ciclo for,
    dentro de outro ciclo for, que percorre o parâmetro item.
    """
    split = ""
    split2 = ""
    splited_words = ""
    for word in item:
        for word2 in item:
            if word == word2:
                split += word
                break
            else:
                split2 += word
                break
    if (split[0] == '7' or split[0] == '9') and len(split) > 4:
        n = 4
        split = [split[i:i+n] for i in range(0, len(split), n)]
        split = split[-1]
    if (split2[0] == '7' or split2[0] == '9') and len(split2) > 4:
        n = 4
        split2 = [split2[i:i+n] for i in range(0, len(split2), n)]
        split2 = split2[-1]
    if (split[0] == '2' or split[0] == '3' or split[0] == '4' or split[0] == '5' \
         or split[0] == '6' or split[0] == '8') and len > 3:
        n = 3
        split = [split[i:i+n] for i in range(0, len(split), n)]
        split = split[-1]
    if (split2[0] == '2' or split2[0] == '3' or split2[0] == '4' or split2[0] == '5' \
         or split2[0] == '6' or split2[0] == '8') and len > 3:
        n = 3
        split2 = [split2[i:i+n] for i in range(0, len(split2), n)]
        split2 = split2[-1]
    splited_words += dict[split] + dict[split2]
    return splited_words

if __name__ == "__main__":
    import doctest
    doctest.testmod()
