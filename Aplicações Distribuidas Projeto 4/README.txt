Aplicações Distribuídas : Projeto 4
Grupo 6
Nº 48303, 49050

Software desenvolvido:
	Serviço para gerir um sistema de gestão de dados relativos a utilizadores, bandas, albuns e suas classificações
	recorrendo à API REST do Spotify para obter informação nas bandas e albuns e ao Github para realizar o OAuth2.

Limitações:
	Nomes de bandas e albuns com mais do que uma palavra devem ter um - entre
	as duas palavras (exemplo: ADD BANDA the-rolling-stones 1962 rock)

Operações suportadas pelo cliente:
	HELP to get information
	CLEAR to clear your terminal
	EXIT to leave

	ADD:
		USER <NOME> <USERNAME> <PASSWORD>
		BANDA <NOME> <ANO> <GENERO>
		ALBUM <ID_BANDA> <NOME> <ANO_ALBUM>
		<ID_USER> <ID_ALBUM> <RATE>

	SHOW | REMOVE:
		USER <ID_USER>
		BANDA <ID_BANDA>
		ALBUM <ID_ALBUM>
		ALL <USERS | BANDAS | ALBUNS>
		ALL ALBUNS_B <ID_BANDA>
		ALL ALBUNS_U <ID_USER>
		ALL ALBUNS <RATE>

	UPDATE:
		ALBUM <ID_USER> <ID_ALBUM> <RATE>
		USER <ID_USER> <PASSWORD>
		
Exemplos de utilização:
	ADD USER nome1 user1 123
	ADD USER nome2 user2 pass

	ADD BANDA metallica 1981 rock
	ADD BANDA aerosmith 1970 rock

	ADD ALBUM 1 metallica 1991
	ADD ALBUM 2 aerosmith 1976

	ADD 1 1 S
	ADD 2 2 B

	SHOW USER 1
	SHOW ALL USERS

	SHOW BANDA 1
	SHOW ALL BANDAS

	SHOW ALBUM 1
	SHOW ALL ALBUNS

	SHOW ALL ALBUNS_B 1
	SHOW ALL ALBUNS_U 2
	SHOW ALL ALBUNS S

	UPDATE ALBUM 1 1 M
	SHOW ALL ALBUNS M

	UPDATE USER 1 password
	SHOW USER 1