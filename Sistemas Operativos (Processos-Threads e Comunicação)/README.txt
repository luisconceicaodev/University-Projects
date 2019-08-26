Sistemas Operativos (2018/2019) - Trabalho prático de avaliação 1
	Grupo 017:
	Beatriz Martins, 48757
	Tiago Santos, 48286
	Luís Conceição, 48303

O objetivo deste trabalho prático é desenvolver dois scripts de programação Python, envolvendo a criação de processos/threads 
e a comunicação entre processos/threads, que visam procurar padrões de texto dados pelo o utilizador, em determinados ficheiros.

Implementação do trabalho:

Utilizou-se Python 2.7 para a realização do trabalho.
Na implementação desenvolveu-se duas funções:
	
	pgrep(text_pattern)
		- Retorna as linhas onde aparece o padrão de texto dado na linha de comandos.
		- Retorna o número de linhas em que o texto ocorre no(s) ficheiro(s). Ambos os parâmetro referidos são dados pelo utilizador, na linha de comandos.
	
	verFiles(list_files)
		- Verifica se os ficheiros existem.
		- Ira colocar os ficheiros numa Queue para que se controlem os acessos aos mesmos.

Comunicação entre Processos:
	Uso de memória partilhada:
		- Função Value(), importada do modulo multiprocessing. Cria uma variável partilhada, por todos os processos, que contabiliza o número de linhas cujo o 
		padrão foi detectado.
	Armazenamento de ficheiros:
		- Função Queue(), importada do modulo multiprocessing para guardar os ficheiros dados na linha de comandos. Tem como objetivo, fazer com que os processos 
		não executem sobre o mesmo ficheiro.

Comunicação entre Threads:
	Armazenamento de ficheiros:
		- Função Queue(), importada do modulo multiprocessing para guardar os ficheiros dados na linha de comandos. Tem como objetivo, fazer com que os processos 
		não executem sobre o mesmo ficheiro.
		Não foi usada Memória Partilhada visto que as Threads partilham dados e heap, portanto apenas foi necessário definir a váriavel global (num_linhas)
		 entre as diversas Threads.



Padrão de utilização:
	python pgrep.py -p [número de processos] [ficheiros] -t [padrão de texto]
	
	-> -p [número de processos]: se esta opção for omitida, o programa executa com um processo/thread, por definição. O valor de [número de processos] pode ser superior ou
	igual a 1.
	
	-> [ficheiros]: ficheiro ou conjunto de ficheiros separados por um espaço. No caso de o/(s) ficheiro/(s) não for/(em) dado/(s), então o programa envia a mensagem 
	"Indique o/(s) nome/(s) do/(s) ficheiro/(s): " ao utilizador.
	
	-> -t [padrão de texto]: o utlizador deve inserir no espaço [padrão de texto] um caracter ou um conjunto de caracteres a procurar no/(s) ficheiro/(s) dado/(s). Se esta 
	opção for omitida, o número de linhas será 0 (zero).
	
Exemplos de instruções:
	Existem dois a.txt e b.txt ficheiros na diretoria com o seguinte conteúdo:
	
	-a.txt
	ola
	oi oi oi 
	ole
	olu
	oli
	ola
	
	-b.txt
	sistemas operativos
	si
	sa
	su
	ola
	ol
	
	1) python pgrep.py -p 2 a.txt b.txt -t ola 
	
	Output: 
		No ficheiro a.txt foi encontrada o texto 'ola' na linha 
		ola

		No ficheiro a.txt foi encontrada o texto 'ola' na linha 
		ola
		No ficheiro b.txt foi encontrada o texto 'ola' na linha 
		ola

		O número de linhas com o texto 'ola' é de 3.

	
	2) python pgrep_threads.py -p 2 a.txt b.txt -t ola 
	
	Output: 
		No ficheiro a.txt foi encontrada o texto 'ola' na linha 
		ola

		No ficheiro a.txt foi encontrada o texto 'ola' na linha 
		ola
		No ficheiro b.txt foi encontrada o texto 'ola' na linha 
		ola


		O número de linhas com o texto 'ola' é de 3.
	
	
	3) python pgrep.py a.txt b.txt -t ola
	
	Output: 
		No ficheiro a.txt foi encontrada o texto 'ola' na linha 
		ola


		No ficheiro a.txt foi encontrada o texto 'ola' na linha 
		ola

		No ficheiro b.txt foi encontrada o texto 'ola' na linha 
		ola

		O número de linhas com o texto ola é de 3.
	
	
	4) python pgrep_threads.py a.txt b.txt -t ola
	
	Output: 
		No ficheiro a.txt foi encontrada o texto 'ola' na linha 
		ola

		No ficheiro a.txt foi encontrada o texto 'ola' na linha 
		ola
		No ficheiro b.txt foi encontrada o texto 'ola' na linha 
		ola

		O número de linhas com o texto 'ola' é de 3.
	
	
	5) python pgrep.py -t ola
	
	Output: 
		Indique o/(s) nome/(s) do/(s) ficheiro/(s): a.txt b.txt
		
		No ficheiro a.txt foi encontrada o texto 'ola' na linha 
		ola


		No ficheiro a.txt foi encontrada o texto 'ola' na linha 
		ola

		No ficheiro b.txt foi encontrada o texto 'ola' na linha 
		ola

		O número de linhas com o texto 'ola' é de 3.
	
	
	6) python pgrep_threads.py -t ola
	
	Output: 
		Indique o/(s) nome/(s) do/(s) ficheiro/(s): a.txt b.txt
		
		No ficheiro a.txt foi encontrada o texto 'ola' na linha 
		ola

		No ficheiro a.txt foi encontrada o texto 'ola' na linha 
		ola
		No ficheiro b.txt foi encontrada o texto 'ola' na linha 
		ola

		O número de linhas com o texto 'ola' é de 3.
		
	
	7) python pgrep_threads.py a.txt b.txt -t ola ola
	
	Output:
		Por favor insira o texto a encontrar entre aspas.
		
	
	8) python pgrep_threads.py a.txt b.txt -t "oi oi"
	
	Output:
		No ficheiro a.txt foi encontrada o texto 'oi oi' na linha 
		oi oi oi 

		O número de linhas com o texto 'oi oi' é de 1.
	
	9) python pgrep.py a.txt b.txt -t "oi oi"
	
	Output:
		No ficheiro a.txt foi encontrada o texto 'oi oi' na linha 
		oi oi oi 

		O número de linhas com o texto 'oi oi' é de 1.

	
	10) python pgrep.py a.txt b.txt -t "ola"
	
	Output:
		No ficheiro a.txt foi encontrada o texto 'ola' na linha 
		ola
		
		
		No ficheiro a.txt foi encontrada o texto 'ola' na linha 
		ola
		
		No ficheiro b.txt foi encontrada o texto 'ola' na linha 
		ola
		
		O número de linhas com o texto 'ola' é de 3.