# -*- coding: utf-8 -*-
import time, os.path, argparse, pickle
from datetime import datetime, timedelta

if __name__=='__main__':
	parser = argparse.ArgumentParser(description = 'leitura do ficheiro binário criado em pgrep')
	parser.add_argument('ficheiro', type = argparse.FileType('r'), nargs=1)
	args = parser.parse_args() #ficheiro


#dicionario com todos os parâmetros e respetivos valores
d = {'inicio':'','duracao':'','processo':[],'ficheiro':{},'tempo':{},'dimensao':{}, 'ocorrencias':{}}

while True:
    try:
        dicionario = pickle.load(args.ficheiro[0]) #ficheiro dado na linha de comandos vai ser colocado numa variável em formato dicionário
        if 'inicio' in dicionario.keys():
            d['inicio'] = dicionario['inicio']
        if 'duracao' in dicionario.keys():
            d['duracao'] = dicionario['duracao']
        else:
           
            if dicionario['processo'] not in d['processo']:
                d['processo'].append(dicionario['processo'])
            if dicionario['processo'] not in d['ficheiro'].keys():
                d['ficheiro'][dicionario['processo']] = [dicionario['ficheiro']]
            else:
                d['ficheiro'][dicionario['processo']].append(dicionario['ficheiro'])
			
            d['tempo'][dicionario['ficheiro']] = dicionario['tempo']
            d['dimensao'][dicionario['ficheiro']] = dicionario['dimensao']
            d['ocorrencias'][dicionario['ficheiro']] = dicionario['ocorrencias']
    
    except EOFError:
		break

print "Início da execução da pesquisa: %s" % d['inicio']
print "Duração da execução: %s" % d['duracao']

for process in d['processo']:
    print "Processo: %i" % process
    for fich in d['ficheiro'][process]:
        print "\tficheiro: %s" % fich
        print "\t\ttempo de pesquisa: %s" % d['tempo'][fich]
        print "\t\tdimensão do ficheiro: %s" % d['dimensao'][fich],"bytes."
        print "\t\tnúmero de ocorrências: %s" % d['ocorrencias'][fich]
