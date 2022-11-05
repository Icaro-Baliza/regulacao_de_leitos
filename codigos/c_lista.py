import c_no

class lista:  ### Classe de lista fixa

	def __init__(self):

		self.__primeiro__ = None
		self.__num_obj__  = 0
		self.__ultimo__   = None

	def append(self, v):
		novo_no = c_no.no(v)

		if (self.__num_obj__ == 0):
		  self.__primeiro__ = novo_no
		  self.__ultimo__   = novo_no

		else:
		  self.__ultimo__.set_prox(novo_no)
		  self.__ultimo__ = novo_no

		self.__num_obj__ +=1

	def get_tamanho(self):
		return self.__num_obj__

	def get_primeiro(self):
		return self.__primeiro__

	











