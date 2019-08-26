#!/usr/bin/env python
# -*- coding: utf-8 -*-

#zona de imports
from multiprocessing import Process, Semaphore, Value, Queue
import pickle
from datetime import datetime
import argparse
import re, mmap
import os
import sys
import time
import signal

time1 = time.time()
q = Queue() #inicialização da queue
process = [] #inicialização da lista de processos
go_ctrl = Value('b', True)
sem = Semaphore(1)
counter = Value('i', 0) #contabiliza o total de ficheiros processados
inicio = time.time()
data = datetime.utcnow().strftime('%d/%m/%Y, %H:%M:%S:%f') #formato da data


def pgrep(text_pattern):
	"""
	Conta o número de linhas onde o texto text_pattern aparece.
	Args:
		text_pattern(str): texto dado na linha de comandos, que é procurado no ficheiro.
	"""
	go = True
	sem.acquire()
	while go and go_ctrl.value:
		sem.release()
		if q.empty():  #caso a queue esteja vazia
			go = False
		else:
			sem.acquire() #serve para os processos não lerem mais que uma vez um mesmo ficheiro
			file_r = q.get(False)
			sem.release()			
			with open(file_r, 'r') as f:
				num_ocorrencias_fich = 0
				for _ in text_pattern: #para cada string na lista do conjunto de argumentos,
					
					output = f.readlines() #conteúdo do ficheiros em listas (cada linha representada por uma string)

					for linha in output: #string por linha

						palavras = list(set(linha.split('\n'))) #faz lista de todas as palavras (strings) da linha

						for palavra in palavras:

								procura = re.search(text_pattern, palavra) #procura a string text (dada na linha de comandos) na string palavra

								if procura is not None:
									print "\nNo ficheiro " + str(file_r) + " foi encontrada o texto '" + str(text_pattern) + "' na linha \n" + str(linha)
									sem.acquire()
									num_linhas.value += 1 #contabiliza o numero de linhas em que a palavra/letra aparece
									num_ocorrencias_fich += 1 #variável não partilhada que permite contabilizar as ocorrências de cada ficheiro
									sem.release()
									break
				counter.value += 1
				
				if args.bin_file is not None:
					dados_fich(file_r, num_ocorrencias_fich)


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


def dados_fich(nome, num_ocor):
	"""
	Escrever os dados de cada ficheiro e do respetivo processo que está a executar, para um ficheiro output.

	Args :
		nome - nome do ficheiro retirado da queue.
	"""
	now = time.time() - inicio
	
	with open(args.bin_file,"ab") as f:
		pickle.dump({'processo':os.getpid(),'ficheiro':nome,'tempo':time.strftime("%H:%M:%S:",time.gmtime(now))+str(now).split('.')[1],'dimensao':os.path.getsize(nome), 'ocorrencias':num_ocor}, f)


def handler(sig, NULL):
	"""
	Informações relativas ao número de linhas, número de ficheiros e tempo de execução.
	"""
	time3 = time.time()
	print "\nNúmero de linhas onde foi encontrado o texto é de " + str(num_linhas.value) + " e o número de ficheiros completamente processados é de " + str(counter.value) + " e o tempo decorrido até ao momento foi de " + str((time3-time1)*1000) + " microsegundos.\n"


def ctrlC(sig, NULL):
	"""
	Termina a execução do ficheiro atual e imprime a respetiva informação.
	"""
	sem.acquire()
	go_ctrl.value = False
	sem.release()
	print "A terminar de analisar o ficheiro corrente..."
	

signal.signal(signal.SIGINT, ctrlC)


if __name__ == '__main__':
	#argumentos a utilizar
	parser = argparse.ArgumentParser(prog='pgrep', description='Procura de palavras em ficheiros')
	parser.add_argument('-p', metavar='n', nargs='?', action='append', dest='process', const=True)
	parser.add_argument('-a', metavar='s', nargs='?', dest='time', const=True)
	parser.add_argument('ficheiros', nargs='*')
	parser.add_argument('-t', nargs='*', dest="text_pattern")
	parser.add_argument('-f', type = str, dest='bin_file')
	args = parser.parse_args()


	num_linhas = Value('i', 0) #inicialização da variável partilhada
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


	##### OPÇÕES #####
	#opção -t
	if args.text_pattern is None:
		print "Deve inserir o padrão de texto que pretende procurar utilizando a opção -t."
		sys.exit(1)
	else:
		if len(args.text_pattern) > 1:
			print "Por favor insira o texto a encontrar entre aspas."
			sys.exit(1)
	
		final_text = args.text_pattern[0]

	#opção -p
	if args.process is None: #se não for dado nenhum valor relativamente ao número de processos
		newP = Process(target=pgrep, args=(final_text,)) #cria um processo
		process.append(newP)
		newP.start() #executa os ficheiros apenas com um processo
	else: #se forem dados vários processos
		p = True
		for i in range(int(args.process[0])):
			newP = Process(target=pgrep, args=(final_text,))
			process.append(newP)
			newP.start()
	
	#opção -a
	if args.time is not None:
		signal.signal(signal.SIGALRM, handler)
		signal.setitimer(signal.ITIMER_REAL, float(args.time), float(args.time))
		
	#opção -f
	#escreve o header que varia de execução para execução
	if args.bin_file is not None:
		with open(args.bin_file,"ab") as f:
			duracao = time.time() - inicio
			pickle.dump({'inicio':data,'duracao':time.strftime("%H:%M:%S:",time.gmtime(duracao))+str(duracao).split('.')[1]}, f) #serializar objetos. escreve no ficheiro out o conteúdo do primeiro argumento
		
for p in process: #para cada processo na lista de procesos
	p.join() #cada processo espera que os restantes terminem


time.sleep(3) #tempo para que o processo pai não corra a função grep


print "O número de linhas com o texto '%s' é de %s." %(final_text, num_linhas.value) 
time2 = time.time()
print "O tempo que demorou a processar os ficheiros foi de " + str(time2-time1) + " segundos."
