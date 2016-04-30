

class GuardarTXT(object):
	def __init__(self):
		pass

	def GuardarTXTFail(self,error):
		self.TramasFail=open('Error.dat','a')
		self.TramasFail.write(error+"\n")
		self.TramasFail.close()

SaveError= GuardarTXT()