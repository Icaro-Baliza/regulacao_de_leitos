import c_leito

class pilha:

# ************************************************************
# ************************************************************
	def __init__(self, categoria, maximo = 500):

		self.__vet__ 		= [0]*maximo
		self.__num_leitos__ = 0
		self.__top__ 		= None
		self.__categoria__  = categoria

# ************************************************************
# ************************************************************
	def __str__(self): 
		out_str = ""
		if self.empty():
			out_str += "\n"

		else:
			for i in range(self.__num_leitos__):
				leito = self.__vet__[i]
				out_str += "{:03d}º - {}\n".format(i+1, leito)	

		return out_str		

# ************************************************************
# ************************************************************
	def push(self, leito): 

		self.__top__ = leito
		self.__vet__[self.__num_leitos__] = leito
		self.__num_leitos__ += 1

# ************************************************************
# ************************************************************
	def pop(self): 

		if self.__num_leitos__ == 0:
			return None

		else:	
			removido = self.__top__
			self.__vet__[self.__num_leitos__ - 1]  = 0
			del(self.__top__)
			self.__num_leitos__ -= 1
			self.__top__ = self.__vet__[self.__num_leitos__ - 1]
			return removido

# ************************************************************
# ************************************************************
	def size(self): 
		return self.__num_leitos__

# ************************************************************
# ************************************************************
	def empty(self): 
		if self.__num_leitos__ == 0:
			return True

		else:
			return False

# ************************************************************
# ************************************************************
	def get_categoria(self):
		return self.__categoria__



	