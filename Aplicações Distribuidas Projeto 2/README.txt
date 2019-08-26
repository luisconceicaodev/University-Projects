Aplicações Distribuídas : Projeto 2
Grupo 6
Nº 50036, 49050, 48303

Melhoramentos:

- lock_server foi implementado com o modulo Select para guardar a informação
dos diversos clientes

- Modelo de comunicação RPC implementado:

    - Stub foi implementado no ficheiro lock_stub

    - Skeleton foi implementado no ficheiro lock_skel

- O cliente agora envia listas com o codigo da operação ao servidor em vez de strings

- O servidor envia em resposta listas com o codigo da operação e o id do cliente acrescentado de 1 unidade
