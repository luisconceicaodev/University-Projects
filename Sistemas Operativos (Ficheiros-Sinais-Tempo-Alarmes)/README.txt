Sistemas Operativos (2018/2019) - Trabalho prático de avaliação 2
	Grupo 017:
	Beatriz Martins, 48757
	Tiago Santos, 48286
	Luís Conceição, 48303

O objetivo deste trabalho prático é desenvolver dois scripts de programação Python, envolvendo a manipulação de ficheiros e o tratamento de sinais, tempo e alarmes, 
que visam procurar padrões de texto dados pelo o utilizador, em determinados ficheiros. Este trabalho é um incremento de funcionalidades relativamente ao trabalho anterior.


Implementação do trabalho:

Utilizou-se Python 2.7 para a realização do trabalho.
Na implementação desenvolveram-se duas funções:
	
	pgrep(text_pattern)
		Para além das funções anteriormente desenvolvidas no trabalho prático de aval. 1, acresce as seguintes alterações:
		- Adição de semáforos que visam a sincronização entre os processos aquando acessos aos ficheiros.
		
	verFiles(list_files)
		Função permanece igual, sem qualquer alteração, relativamente ao trabalho prático de avaliação 1.
	
	dados_fich(nome, num_ocor)
		- Escreve para um ficheiro binário toda a informação relativa ao processo e ao respetivo/(s) ficheiro/(s).
	
	handler(sig, NULL)
		- Emite um alarme periódico, dado pelo utilizador, através da opção -a.
	
	ctrlC(sig, NULL)
		- Alterar uma variável partilhada com intuito de resolver a função do Ctrl-C.
		- Os processos terminam a pesquisa nos ficheiros correntes e, após tal acontecimento, o processo-pai escreve para stdout o número das linhas onde foi 
		encontrado o padrão de texto.

Correções relativas ao projeto anterior:
	- Foi feito o tratamento de erros para a opção -t, caso o utilizador não escreva nenhum padrão de texto.
		
Comunicação entre Processos:
	Uso de memória partilhada:
		- Função Value(), importada do módulo multiprocessing. Cria três variáveis partilhadas, por todos os processos:
			-num.linhas: contabiliza o número de linhas cujo o padrão foi detectado. 
			-counter: contabiliza o número de ficheiros totalmente processados.
			-go_ctrl: utilizada para sincronizar os processos, após o utilizador executar Ctrl-C.
			
	Armazenamento de ficheiros:
		- Função Queue(), abordada no ficheiro README.txt do trabalho anterior.
		
	Sincronização de processos:
		- Função Semaphore(), importada pelo módulo multiprocessing. Sincroniza os processos, atribuindo acesso de cada um à zona crítica, de forma não simultânea.
	
	Serialização dos dados dos ficheiros:
		-Função pickle, serializa todos os dados dos ficheiros e coloca-os num ficheiro binário, criado anteriormente.



Padrão de utilização:
	python pgrep.py -p [número de processos] -a [tempo do alarme] -f [nome do ficheiro output] [ficheiros] -t [padrão de texto]
	
	-> -p [número de processos]: se esta opção for omitida, o programa executa com um processo/thread, por definição. O valor de [número de processos] pode ser superior ou
	igual a 1.
	
	-> -a [tempo do alarme]: esta opção é opcional. É enviada uma mensagem após o [tempo do alarme] com informações relativas ao número de linhas, número de ficheiros 
	totalmente processados e tempo de execução.
	
	-> -f [nome do ficheiro output]: escreve todas as informações relativas a cada ficheiro e processo para um ficheiro com o nome [nome do ficheiro output].
	
	-> [ficheiros]: ficheiro ou conjunto de ficheiros separados por um espaço. No caso de o/(s) ficheiro/(s) não for/(em) dado/(s), então o programa envia a mensagem 
	"Indique o/(s) nome/(s) do/(s) ficheiro/(s): " ao utilizador.
	
	-> -t [padrão de texto]: o utlizador deve inserir no espaço [padrão de texto] um caracter ou um conjunto de caracteres a procurar no/(s) ficheiro/(s) dado/(s). Se esta 
	opção for omitida, o número de linhas será 0 (zero).
	
Exemplos de instruções:
	Existem dois a2.txt e b2.txt ficheiros na diretoria com o seguinte conteúdo:
	
	-a2.txt
	ola
	oi oi oi ami
	ole
	olu
	oli
	ola
	
	-b2.txt
	sistemas operativos
	si
	sa
	su
	ola
	oi amigoooos
	ol
	
	1) python pgrep.py -p 2 a2.txt b2.txt 
	
	Output: 
		Deve inserir o padrão de texto que pretende procurar utilizando a opção -t.

	
	2) python pgrep.py -a 0.05 -f file1 a2.txt b2.txt -t ola 
	
	Output: 
		No ficheiro a2.txt foi encontrada o texto 'ola' na linha 
		ola


		No ficheiro a2.txt foi encontrada o texto 'ola' na linha 
		ola

		Número de linhas onde foi encontrado o texto é de 2 e o número de ficheiros completamente processados é de 1 e o tempo decorrido até ao momento foi de 22.3250389099 microsegundos.


		No ficheiro b2.txt foi encontrada o texto 'ola' na linha 
		ola


		Número de linhas onde foi encontrado o texto é de 3 e o número de ficheiros completamente processados é de 2 e o tempo decorrido até ao momento foi de 27.2798538208 microsegundos.


		Número de linhas onde foi encontrado o texto é de 3 e o número de ficheiros completamente processados é de 2 e o tempo decorrido até ao momento foi de 32.4289798737 microsegundos.

		O número de linhas com o texto 'ola' é de 3.
		O o tempo que demorou a processar os ficheiros foi de 0.0325129032135 segundos.

	
	
	3) python lgrep.py file1
	
	Output: 
		Início da execução da pesquisa: 30/11/2018, 15:14:45:663768
		Duração da execução: 00:00:00:00529813766479
		Processo: 2996
			ficheiro: a2.txt
				tempo de pesquisa: 00:00:00:00682520866394
				dimensão do ficheiro: 32 bytes.
				número de ocorrências: 2
			ficheiro: b2.txt
				tempo de pesquisa: 00:00:00:0114071369171
				dimensão do ficheiro: 48 bytes.
				número de ocorrências: 1

	
	
	4) python pgrep.py a2.txt b2.txt -t ola (NOTA: para realizar este teste, foi utilizado um time.sleep(5), dado que os ficheiros a2.txt e b2.txt são muito pequenos)
	
	Output: 
		No ficheiro a2.txt foi encontrada o texto 'ola' na linha 
		ola


		No ficheiro a2.txt foi encontrada o texto 'ola' na linha 
		ola

		No ficheiro b2.txt foi encontrada o texto 'ola' na linha 
		ola

		^CA terminar de analisar o ficheiro corrente...
		A terminar de analisar o ficheiro corrente...
		A terminar de analisar o ficheiro corrente...
		O número de linhas com o texto 'ola' é de 3.
		O o tempo que demorou a processar os ficheiros foi de 15.5209429264 segundos.

	
	