import simulador
import controle


import time
import os
import sys


lista_f = controle.lista_f() # Lista com todas as filas de pacientes #

lista_p = controle.lista_p() # Lista com todas as pilhas de leitos #


t = 0  # Contador

while True :

	complemento_out_str = ''

	if t > 0:
		lista_alocados = controle.aloca(lista_f, lista_p) # Depois do primeiro ciclo aloca os pacientes aos leitos disponiveis #
		
		# Percorre a lista de filas para utilizar da função muda_estado (muda a condição de um paciente) #
		no_corrente = lista_f.get_primeiro()

		for i in range(lista_f.get_tamanho()):
			fila = no_corrente.get_dado()
			mudado = simulador.muda_estado(fila) # Paciente que mudou de condição #

			no_corrente = no_corrente.get_prox()	

			if mudado != None:
				controle.reatribui_p(mudado, lista_f) # Caso o paciente tenha mudado de condição essa função ira reatribuir o paciente à fila correta #

				complemento_out_str += "O {} | mudou de condição para {}\n".format(mudado, mudado.get_estado())



	paciente, p = simulador.gera_paciente() 	# Se p então houve requisição de leito por um paciente #

	leito, l = simulador.gera_leito()			# Se l então uma vaga de leito foi disponibilizada #

	if p:
		controle.atribui_p(paciente, lista_f)	# Envia o paciente para a sua fila #

	if l:
		controle.atribui_l(leito, lista_p)		# Coloca o leito disponivel em sua respectiva pilha #


	######### Organiza a impressão das filas de Pacientes #########

	out_str = "############# PACIENTES #############\n"



	no_corrente = lista_f.get_primeiro()
	for i in range(lista_f.get_tamanho()):
		fila = no_corrente.get_dado()
		if i == 0:
			out_str += "  NEONATAL  \n"
			out_str += "  ''''''''  \n"
		if i == 3:
			out_str += "  PEDIATRICO  \n"
			out_str += "  ''''''''''  \n"
		if i == 6:
			out_str += "  ADULTO  \n"
			out_str += "  ''''''  \n"

		out_str += str(fila) + "\n"					 


		no_corrente = no_corrente.get_prox()


	######### Organiza a impressão das pilhas de Leitos #########

	out_str += "############# LEITOS #############\n"

	no_corrente = lista_p.get_primeiro()
	for i in range(lista_p.get_tamanho()):
		pilha = no_corrente.get_dado()
		if i == 0:
			out_str += "  NEONATAL  \n"
			out_str += "  ''''''''  \n"
		if i == 1:
			out_str += "\n  PEDIATRICO  \n"
			out_str += "  ''''''''''  \n"
		if i == 2:
			out_str += "\n  ADULTO  \n"
			out_str += "  ''''''  \n"

		out_str += str(pilha)					 


		no_corrente = no_corrente.get_prox()


	######### Organiza a impressão dos pacientes que conseguiram vaga em um leito #########

	out_str += "\n#############  PACIENTES ENVIADOS PARA LEITO  #############\n"

	if t>0:
		p_atual = lista_alocados.get_primeiro()
		for i in range(lista_alocados.get_tamanho()//2):
			l_atual = p_atual.get_prox()
			out_str += "{} ------> {}\n".format(p_atual.get_dado(), l_atual.get_dado())
			p_atual = l_atual.get_prox()


	######### Organiza a impressão dos pacientes que tiveram sua condição alterada enquanto aguardavam em fila #########

	out_str += "\n#############  PACIENTES REALOCADOS #############\n"

	out_str += complemento_out_str



	######### Apaga o terminal à cada loop #########
	os.system('cls' if os.name == 'nt' else 'clear')


	print(out_str)

	#### Requer que o usúario aperte Enter para avançar o loop ####
	while True:
		key = str(input(""))
		if key == "":
			break

	t+=1





