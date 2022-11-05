import c_fila_paciente
import c_pilha_leito
import c_lista

### Cria as 9 filas de pacientes ###
def lista_f():
	lista_de_filas = c_lista.lista()
	for categoria in range(3):
		for prioridade in range(2, -1, -1):
			fila = c_fila_paciente.fila(prioridade, categoria)

			lista_de_filas.append(fila)

	return lista_de_filas

### Crias as 3 pilhas de leitos ###
def lista_p():
	lista_de_pilhas = c_lista.lista()
	for categoria in range(3):
		pilha = c_pilha_leito.pilha(categoria)
		lista_de_pilhas.append(pilha)

	return lista_de_pilhas

### Envia o paciente para a sua fila ###
def atribui_p(paciente, lista_de_filas):
	### Percorre a lista de filas ###
	no_corrente = lista_de_filas.get_primeiro()
	for i in range(9):
		fila = no_corrente.get_dado()

		### Caso o id e a categoria da fila e do paciente forem as mesmas, ele sera inserido na fila ###
		if (fila.get_categoria() == paciente.get_categoria()) and (fila.get_prioridade() == paciente.get_prioridade()): 
			fila.push(paciente)

		no_corrente = no_corrente.get_prox()

### Envia o leito para a sua pilha ###
def atribui_l(leito, lista_de_pilhas):
	### Percorre a lista de pilhas ###
	no_corrente = lista_de_pilhas.get_primeiro()
	for i in range(3):
		pilha = no_corrente.get_dado()

		### Caso o leito e a pilha tenham a mesma categoria, esse sera inserido na pilha ###
		if (pilha.get_categoria() == leito.get_categoria()):
			pilha.push(leito)

		no_corrente = no_corrente.get_prox()

### Caso estado do paciente mude, realoca o paciente para a fila correta ###
def reatribui_p(paciente, lista_de_filas):

	### Percorre as filas procurando o paciente ###
	no_corrente = lista_de_filas.get_primeiro()
	for i in range(9):
		fila = no_corrente.get_dado()

		if fila.remove(paciente): ### Se o paciente for achado será removido e o loop sera encerrado ###
			break

		no_corrente = no_corrente.get_prox()

	atribui_p(paciente, lista_de_filas)  ### Envia o paciente para a fila correta ###


### Cruza os dados de disponibilidade de leitos e requisição de vagas para alocar os pacientes aos leitos corretos ###
def aloca(lista_de_filas, lista_de_pilhas):

	lista_alocados = c_lista.lista() ### Cria uma lista com os pacientes que conseguiram vaga ###

	### Percorre a lista de pilhas###
	no_c_pilha = lista_de_pilhas.get_primeiro()
	for i in range(3):
		pilha = no_c_pilha.get_dado()
		categoria_pilha = pilha.get_categoria()

		if not (pilha.empty()): ### verifica se existem leitos disponiveis de certa categoria ###

		### Percorre a lista de filas ###
			no_c_fila = lista_de_filas.get_primeiro()
			for l in range (9):
				fila = no_c_fila.get_dado()
				categoria_fila = fila.get_categoria()

				if (categoria_pilha == categoria_fila) and not (fila.empty()): ### Verifica se a fila é da mesma categoria do leito e se tem pacientes na fila ###
					paciente = fila.pop() 
					leito    = pilha.pop()

					### Adiciona os pacientes e leitos na lista, em que o nó do paciente aponta para o nó de seu leito atribuido ###
					lista_alocados.append(paciente) 
					lista_alocados.append(leito)

					if pilha.empty(): ### Caso não existam mais vagas disponiveis para essa categoria, o loop é parado ###
						break

				no_c_fila = no_c_fila.get_prox()

		no_c_pilha = no_c_pilha.get_prox()

	return lista_alocados

	