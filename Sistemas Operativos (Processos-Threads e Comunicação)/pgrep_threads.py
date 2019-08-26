#!/usr/bin/env python
# -*- coding: utf-8 -*-

#zona de imports
from Queue import Queue
from threading import Thread
import argparse
import re, mmap
import os
import sys
import time

q = Queue() #inicialização da queue
threads = [] #inicialização da lista de threads


def pgrep(text_pattern):
	"""
	Conta o número de linhas onde o texto text_pattern aparece.
	Args:
		text_pattern(str): texto dado na linha de comandos, que é procurado no ficheiro.
	"""
	global num_linhas
	go = True
	while go:

		if q.empty():  #caso a queue esteja vazia
			go = False
		else:
			file_r = q.get()
			with open(file_r, 'r') as f:

				for text in text_pattern: #para cada string na lista do conjunto de argumentos,

					output = f.readlines() #conteúdo do ficheiros em listas (cada linha representada por uma string)

					for linha in output: #string por linha

						palavras = list(set(linha.split('\n'))) #faz lista de todas as palavras (strings) da linha

						for palavra in palavras:

								procura = re.search(text, palavra) #procura a string text (dada na linha de comandos) na string palavra

								if procura is not None:
									print "No ficheiro " + str(file_r) + " foi encontrada o texto '" + str(text_pattern) + "' na linha \n" + str(linha)
									num_linhas += 1 #contabiliza o numero de linhas em que a palavra/letra aparece
									break

def verFiles(list_files):
	"""
	Lê os ficheiros dados na linha de comandos (que se encontram numa lista list_files) e verifica se eles existem.

	Args :
		list_files - lista de ficheiros.
	"""
	for f in list_files:
	    if not os.path.isfile(f):
	        print 'O ficheiro %s não existe' % f
	    else:
			q.put(f)


if __name__ == '__main__':
	# argumentos a utilizar
	parser = argparse.ArgumentParser(prog='pgrep', description='Search files for matching words')
	parser.add_argument('-p', metavar='n', nargs='?', action='append', dest='threads', const=True)
	parser.add_argument('ficheiros', nargs='*')
	parser.add_argument('-t', nargs='*', dest="text_pattern")
	args = parser.parse_args()

	num_linhas = 0
	#verificação de argumentos
	p = False
	list_files = []

	for i in args.ficheiros:
		list_files.append(i)

	#se não forem dados ficheiros na linha de comandos, pede ao utilizador
	while len(list_files) == 0:
		files = raw_input("Indique o/(s) nome/(s) do/(s) ficheiro/(s): ")
		list_files = files.split(' ')

	verFiles(list_files)

	if len(args.text_pattern) > 1:
		print ("Por favor insira o texto a encontrar entre aspas.")
		sys.exit(1)

	final_text = args.text_pattern[0]

	if args.threads is None: #se não for dado nenhum valor relativamente ao número de processos
		newT = Thread(target=pgrep, args=(args.text_pattern,)) #cria uma processo
		newT.start() #executa os ficheiros apenas com um processo
	else: #se forem dados vários processos
		p = True
		for i in range(int(args.threads[0])):
			newT = Thread(target=pgrep, args=(args.text_pattern,))
			threads.append(newT)
			newT.start()
	for p in threads: #para cada processo na lista de procesos
		p.join() #cada processo espera que os restantes terminem

	time.sleep(2) #tempo para que o processo pai não corra a função pgrep

print "O número de linhas com o texto '%s' é de %s." %(final_text, num_linhas)
