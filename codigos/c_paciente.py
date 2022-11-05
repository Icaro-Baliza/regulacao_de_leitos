class paciente:

# ***************************************************************************
# ***************************************************************************
	def __init__(self, id, idade, prioridade):

		self.__id__         = id
		self.__idade__      = idade
		self.__prioridade__ = prioridade

# ***************************************************************************
# ***************************************************************************
	def __str__(self):
		return "Paciente: {} | Idade: {}".format(self.__id__, self.__idade__)		

# ***************************************************************************
# ***************************************************************************
	def get_id(self):
		return self.__id__

# ***************************************************************************
# ***************************************************************************
	def get_idade(self):
		return self.__idade__

# ***************************************************************************
# ***************************************************************************
	def get_prioridade(self):
		return self.__prioridade__

# ***************************************************************************
# ***************************************************************************
	def set_prioridade(self, v):
		self.__prioridade__ = v

# ***************************************************************************
# ***************************************************************************
	def get_categoria(self):
		if int(self.__idade__) == 0:
			return 0
		elif int(self.__idade__) <= 13:
			return 1
		else:
			return 2

# ***************************************************************************
# ***************************************************************************
	def get_estado(self):

		if self.__prioridade__ > 2:
			return "Falecido"

		elif self.__prioridade__ == 2:
			return "Emergencia"

		elif self.__prioridade__ == 1:
			return "Muito urgente"

		elif self.__prioridade__ == 0:
			return "Urgente"	

		elif self.__prioridade__ == -1:
			return "Pouco urgente"

		elif self.__prioridade__ == -2:
			return "Nao Urgente"

		else:
			return "Alta hospitalar" 	 

