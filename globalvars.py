
from bd import BasedeDatos
import socket, threading
from urllib2 import urlopen
from Crypto.Cipher import XOR
from base64 import b64encode, b64decode
from ConfigParser import ConfigParser

def initvars():
	global Logueado
	Logueado = False
	config = ConfigParser()
	config.read("conf/config.ini")
	tipo = config.get('CUENTA', 'Tipo')
	ps = b64decode('MjAxMDE3MzMtOTYwOTkyNg==')
	xorps = XOR.new(str(ps))
	global Tipo
	Tipo = xorps.decrypt(b64decode(str(tipo)))
	webserver = config.get('WEB', 'srv')
	ps = b64decode('MjAxMDE3MzMtOTYwOTkyNg==')
	xorps = XOR.new(str(ps))
	global WEBServer
	WEBServer = xorps.decrypt(b64decode(str(webserver)))
	print WEBServer
	global DatosUsuario
	DatosUsuario = {}
	global DictSenales
	DictSenales = {}
	global BD
	BD = BasedeDatos()
	BD.Conectar()
	global DictColaResultados
	DictColaResultados = {}
	t = threading.Thread(target=GetIps)
	t.start()



def GetIps(): 
	global IPLocal
	IPLocal = ''
	IPLocal = socket.gethostbyname(socket.gethostname())
	global IPPublica
	IPPublica = ''
	IPPublica = urlopen('http://ip.42.pl/raw').read().encode('utf8')




