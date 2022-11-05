import c_no
import c_paciente

### Classe fila de paciente ###
class fila:
# ********************************************************************
# ********************************************************************  
	def __init__(self, prioridade, categoria):
		self.__primeiro__ 		= None
		self.__num_pacientes__  = 0
		self.__ultimo__   		= None
		self.__prioridade__		= prioridade
		self.__categoria__		= categoria

# ********************************************************************
# ********************************************************************
	def __str__(self): 

		out_str = ""

		if self.__prioridade__ == 0:
			out_str += "|------Urgente------|\n"
		elif self.__prioridade__ == 1:
			out_str += "|---Muito urgente---|\n"
		elif self.__prioridade__ == 2:
			out_str += "|-----Emergencia----|\n"



		if self.empty():    		
			out_str += "\n"

		else:
			no_corrente = self.__primeiro__

			for i in range(self.__num_pacientes__):
				paciente = no_corrente.get_dado()
				out_str += "{:03d}º - {}\n".format(i+1, str(paciente))

				no_corrente = no_corrente.get_prox()

		return out_str		

# ********************************************************************
# ********************************************************************  
	def push(self,v): 
		novo_no = c_no.no(v)

		if (self.__num_pacientes__ == 0):
		  self.__primeiro__ = novo_no
		  self.__ultimo__   = novo_no

		else:
		  self.__ultimo__.set_prox(novo_no)
		  self.__ultimo__ = novo_no

		self.__num_pacientes__ +=1

# ********************************************************************
# ********************************************************************
	def pop(self): 
		if (self.__num_pacientes__ == 0):
			return None

		elif (self.__num_pacientes__ == 1):
			removido = self.__ultimo__.get_dado()
			del(self.__primeiro__)
			del(self.__ultimo__)
			self.__primeiro__ = None
			self.__ultimo__   = None
			self.__num_pacientes__ -= 1
			return removido

		else:
			removido = self.__primeiro__.get_dado()
			primeiro = self.__primeiro__
			self.__primeiro__ = self.__primeiro__.get_prox()
			del(primeiro)
			self.__num_pacientes__ -= 1
			return removido

# ********************************************************************
# ********************************************************************
	def remove(self, paciente):

		if not (self.busca(paciente)):
			return False

		else:
			id = paciente.get_id()
			no_corrente = self.__primeiro__
			for i in range(self.size()):
				id_atual = (no_corrente.get_dado()).get_id()

				if (id == id_atual):

					if (i == 0):
						primeiro = self.__primeiro__
						self.__primeiro__ = self.__primeiro__.get_prox()
						del(primeiro)
						self.__num_pacientes__ -= 1
						return True

					elif (i == self.size()-1):
						ultimo = self.__ultimo__
						no_anterior.set_prox(None)
						self.__ultimo__ = no_anterior
						del(ultimo)
						self.__num_pacientes__ -= 1
						return True

					else:
						no_prox = no_corrente.get_prox()
						no_anterior.set_prox(no_prox)
						atual = no_corrente
						del(atual)
						self.__num_pacientes__ -= 1
						return True

				no_anterior = no_corrente
				no_corrente = no_corrente.get_prox()


# ********************************************************************
# ********************************************************************
	def busca(self, paciente):
		if self.__num_pacientes__ > 0:
			id = paciente.get_id()
			no_corrente = self.__primeiro__
			while no_corrente != None:
				if id == (no_corrente.get_dado()).get_id():
					return True
				no_corrente = no_corrente.get_prox()


		return False					



# ********************************************************************
# ********************************************************************
	def size(self):  
		return self.__num_pacientes__

# ********************************************************************
# ********************************************************************
	def empty(self):
		if self.__num_pacientes__ == 0:
			return True

		else:
			return False

# ********************************************************************
# ********************************************************************			
	def get_primeiro(self):
		return self.__primeiro__

# ********************************************************************
# ********************************************************************	
	def get_categoria(self):
		return self.__categoria__

# ********************************************************************
# ********************************************************************	
	def get_prioridade(self):
		return self.__prioridade__









