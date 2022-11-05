import c_paciente
import c_leito
import c_fila_paciente
import c_pilha_leito

import random

v_p    = 80 #Chance de gerar paciente em %
v_l    = 60 #Chance de gerar leito em %

### Gera um paciente aleatorio e único ###
def gera_paciente():
	### Gera o id SUS do paciente ###
	id = str(random.randrange(10**14, 10 ** 15)) 

	### Gera a faixa de idade do paciente  0 ---> Neonatal | 1 ---> Pediatrico | 2 ---> Adulto ###
	faixa = random.randint(0,2) 

	### Gera a condição do paciente  0 ---> Urgente | 1 ---> Muito urgente | 2 ---> Emergencia ###
	prioridade = random.randint(0,2) 

    ### Gera a idade do paciente de acordo com sua faixa etaria (obs: idade 0 significa que o paciente tem menos de um ano) ###
	if faixa == 0:
		idade = 0

	elif faixa == 1:
		idade = random.randint(1,13)

	elif faixa == 2:
		idade = random.randint(14,100)

	idade = "{:02d}".format(idade)	

	### Chama a classe paciente ###
	paciente = c_paciente.paciente(id, idade, prioridade)

	### Probabilidade do paciente ser gerado ###
	v = random.randrange(0, 100)//(100-v_p)
	if v == 0:
		gera = False
	else:
		gera = True


	return paciente, gera


### Gera leito aleatorio e unico ###
def gera_leito():
	### Gera o id do leito com seu respectivo hospital ###
	hospital = "{:02d}".format(random.randint(1, 50))
	id = hospital + "-" + "{:03d}".format(random.randint(1,200))

	### Gera a categoria do leito 0 ---> Neonatal | 1 ---> Pediatrico | 2 ---> Adulto ###
	categoria = random.randint(0,2)

	### Chama a classe leito ###
	leito = c_leito.leito(id, categoria, hospital)

    ### Probabilidade do leito ser gerado ###
	v = random.randrange(0, 100)//(100 - v_l)
	if v == 0:
		gera = False
	else:
		gera = True

	return leito, gera
			

### Função que muda a função de UM paciente ou NENHUMA de cada certa fila ###
def muda_estado(fila):
	### Variavel que diz se o paciente melhorou ou piorou ###
	melhora = False	
	piora   = False

	### Percorre a fila para talvez mudar a condição de um paciente ###
	no_corrente = fila.get_primeiro()
	for i in range (fila.size()):
		paciente   = no_corrente.get_dado()
		prioridade = paciente.get_prioridade()

		chance     = random.randint(0, 100)

		### Para pacientes em Emergencia chance de melhora 5% e de piora 15% ###
		if prioridade   == 2:
			if chance >= 95:
				melhora = True
			elif chance <= 15:
				piora = True

		### Para pacientes em Muito urgente chance de melhora 5% e de piora 10% ### 
		elif prioridade == 1:
			if chance >= 95:
				melhora = True
			elif chance <= 10:
				piora = True

		### Para pacientes em Urgente chance de melhora 10% e de piora 10% ###
		else:
			if chance >= 90:
				melhora = True
			elif chance == 10:
				piora = True

		### Caso o paciente sofra alteração de condição sua prioridade sera aumentada ou diminuida ###
		if melhora:
			prioridade -= 1
			break
		elif piora:
			prioridade += 1
			break

		no_corrente = no_corrente.get_prox()
		melhora = False	
		piora   = False

	### Retorna um paciente com condição alterada ###
	if (melhora or piora):
		paciente.set_prioridade(prioridade)
		return paciente

	else:
		return None



		






#def pandemia()

'''
pilha = c_pilha_leito.pilha()


for i in range (3):

	paciente = gera_leito()

	pilha.push(paciente)

print(pilha.size())

print(pilha)




x = pilha.pop()
pilha.pop()
pilha.pop()

print(x)
print(pilha)


fila = c_fila_paciente.fila()

for i in range(8):
	paciente = gera_paciente()
	fila.push(paciente)


print(fila)




muda_estado(fila)



print(fila)
'''

