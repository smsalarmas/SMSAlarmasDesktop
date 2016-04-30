# -*- coding: latin-1 -*-
from PyQt4 import QtGui, QtCore, QtWebKit
from bd import BasedeDatos
import globalvars 
from QTSubVentanaMonitoreo import Ui_SubVentanaMonitoreo
from QTDialogProcesarSenal import Ui_Dialog
from QTDialogHombreMuerto import Ui_Dialog_HombreMuerto
from QTDialogDetalleSenal import Ui_Dialog_DetalleSenal
from modules.nuevosms import DialogNuevoSMS
from modules.nuevocorreo import DialogNuevoCorreo

import time, random, string
import datetime
import re
import base64
import subprocess
import webbrowser
import gc
from functools import partial
import urllib
import requests

class DialogHombreMuerto(QtGui.QDialog):
	def __init__(self,parent,hilotiempos):
		QtGui.QDialog.__init__(self,parent)
		self.DialogHombreMuerto = Ui_Dialog_HombreMuerto()
		self.DialogHombreMuerto.setupUi(self)
		self.parent = parent
		self.hilotiempos = hilotiempos

		#Que la ventana se Cargue sobre la otra ventana para que no tenga botones de cerrar ni nada
		#Se carga sobre la Ventana Padre
		#self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
		#self.setWindowModality(QtCore.Qt.ApplicationModal)
		#self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		#Para crear el Captcha
		self.captcha = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(4))

		#Para cargar el Captcha en el Label
		self.DialogHombreMuerto.label_Codigo.setText(str(self.captcha))

		#Conexiones
		self.connect(self.DialogHombreMuerto.pushButton_Aceptar, QtCore.SIGNAL("clicked()"), self.Cerrar)
		self.connect(self.DialogHombreMuerto.lineEdit_Codigo, QtCore.SIGNAL("textChanged(const QString&)"), self.ValidarCaptcha)
		#self.connect(self.DialogHombreMuerto.lineEdit_Codigo, QtCore.SIGNAL("returnPressed()"), self.Cerrar)
		
		#Crear el Objeto del Sonido del Hombre Muerto
		self.SonidoHombreMuerto = QtGui.QSound("sonidos/h_muerto.wav",self)
		self.ActivarSonidoHombreMuerto()

	def closeEvent(self,event):
		if self.DialogHombreMuerto.lineEdit_Codigo.text().toUpper() != self.captcha:
			event.ignore()
		else:
			event.accept()

	def ActivarSonidoHombreMuerto(self):
		if self.SonidoHombreMuerto.isFinished():
			self.SonidoHombreMuerto.setLoops(-1)
			self.SonidoHombreMuerto.play() 
		pass
	def ValidarCaptcha(self):
		Codigo = self.DialogHombreMuerto.lineEdit_Codigo.text().toUpper()
		if Codigo == '':
			self.DialogHombreMuerto.lineEdit_Codigo.setStyleSheet("border: 1px solid yellow;")
		elif Codigo == self.captcha:
			self.DialogHombreMuerto.lineEdit_Codigo.setStyleSheet("border: 1px solid green;")
		elif Codigo != self.captcha:
			self.DialogHombreMuerto.lineEdit_Codigo.setStyleSheet("border: 1px solid red;")
	def Cerrar(self):
		Codigo = self.DialogHombreMuerto.lineEdit_Codigo.text().toUpper()
		if Codigo == self.captcha:
			self.SonidoHombreMuerto.stop()
			del self.SonidoHombreMuerto
			self.close()
			self.hilotiempos.DialogHombreMuerto = None

class WebViewMapaCliente(QtWebKit.QWebView):
	def __init__(self, parent,latitudcliente,longitudcliente,iconocliente,nombreempresa,nombrecliente):
		super(WebViewMapaCliente, self).__init__()	
		self.load(QtCore.QUrl('mapprocesarsenal.html'))
		self.loadFinished.connect(self.on_loadFinished)
		self.page().mainFrame().addToJavaScriptWindowObject("VentanaPyQtCliente",self)
		self.parent= parent
		self.latitudcliente = latitudcliente
		self.longitudcliente = longitudcliente
		self.iconocliente = iconocliente
		self.nombreempresa = nombreempresa
		self.nombrecliente = nombrecliente
	@QtCore.pyqtSlot()
	def on_loadFinished(self):
		print 'Cargo el Mapa'
		#mapFrame = self.mainFrame()
		#self.page().mainFrame().evaluateJavaScript(getJsValue) 
		#ResultadoMapa = globalvars.BD.Querys('DatosClienteParaMapa',str(self.parent.Abonado))
		Latitud = str(self.latitudcliente)
		Longitud = str(self.longitudcliente)
		LatitudEmpresa = str(globalvars.DatosUsuario['Latitud'])
		LongitudEmpresa = str(globalvars.DatosUsuario['Longitud'])

		if Latitud == '' or Latitud == None or Longitud == '' or Longitud == None:
			Latitud = ''
			Longitud = ''
			Ubicacion = 0

		if LatitudEmpresa == '' or LongitudEmpresa == '' or LatitudEmpresa == None or LongitudEmpresa == None:
			LatitudEmpresa = ''
			LongitudEmpresa = ''

		Icono = self.iconocliente
		Ubicacion = 1
		NombreEmpresa = self.nombreempresa
		NombreCliente = self.nombrecliente

		self.page().mainFrame().evaluateJavaScript(QtCore.QString("SetVariables('"+str(Latitud)+"','"+str(Longitud)+"','"+str(Icono)+"','"+str(Ubicacion)+"','"+NombreEmpresa+"','"+NombreCliente+"','"+str(LatitudEmpresa)+"','"+str(LongitudEmpresa)+"'"+")"))

class DialogDetalleSenal(QtGui.QDialog):
	def __init__(self,parent,idtrama,cuentaynombre,evento):
		super(DialogDetalleSenal, self).__init__()
		self.DialogDetalleSenal = Ui_Dialog_DetalleSenal()
		self.DialogDetalleSenal.setupUi(self)
		self.idtrama = idtrama
		self.setAttribute(QtCore.Qt.WA_QuitOnClose,False)

		self.DialogDetalleSenal.tableWidget_Lista.verticalHeader().setVisible(False)
		self.DialogDetalleSenal.tableWidget_Lista.setShowGrid(False)
		self.DialogDetalleSenal.tableWidget_Lista.setAlternatingRowColors(True)
		self.DialogDetalleSenal.tableWidget_Lista.resizeColumnsToContents()
		self.DialogDetalleSenal.tableWidget_Lista.verticalHeader().setDefaultSectionSize(24)
		self.DialogDetalleSenal.tableWidget_Lista.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.header = self.DialogDetalleSenal.tableWidget_Lista.horizontalHeader()
		self.DialogDetalleSenal.tableWidget_Lista.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

		self.DialogDetalleSenal.label_Cliente.setText(cuentaynombre)
		self.DialogDetalleSenal.label_Evento.setText(evento)
		self.ListarObservaciones()
		self.AcomodarTamanoTablas()

	def AcomodarTamanoTablas(self):
		self.DialogDetalleSenal.tableWidget_Lista.setColumnWidth(0,165)
		self.DialogDetalleSenal.tableWidget_Lista.setColumnWidth(1,405)
		self.DialogDetalleSenal.tableWidget_Lista.setColumnWidth(2,100)

	def ListarObservaciones(self):
		Observaciones = globalvars.BD.Querys('SeleccionarObservacionesTramasProcesadas',str(self.idtrama))

		while self.DialogDetalleSenal.tableWidget_Lista.rowCount() > 0:
			self.DialogDetalleSenal.tableWidget_Lista.removeRow(0)
		
		for obser in Observaciones:
			Siguiente = self.DialogDetalleSenal.tableWidget_Lista.rowCount()
			self.DialogDetalleSenal.tableWidget_Lista.insertRow(Siguiente)
			columna = 0
			#Columna 0
			texto = QtGui.QTableWidgetItem(obser.fecha.strftime("%d %b %Y %H:%M:%S"))
			self.DialogDetalleSenal.tableWidget_Lista.setItem(Siguiente,columna,texto)	
			columna = 1
			texto = QtGui.QTableWidgetItem(obser.observacion)
			self.DialogDetalleSenal.tableWidget_Lista.setItem(Siguiente,columna,texto)
			columna = 2
			texto = QtGui.QTableWidgetItem(obser.nombre)
			self.DialogDetalleSenal.tableWidget_Lista.setItem(Siguiente,columna,texto)	

class DialogDetalleSenalProcesarSenal(QtGui.QDialog):
	def __init__(self,parent,idtrama,cuentaynombre,evento):
		super(DialogDetalleSenalProcesarSenal, self).__init__()
		self.DialogDetalleSenal = Ui_Dialog_DetalleSenal()
		self.DialogDetalleSenal.setupUi(self)
		self.idtrama = idtrama

		self.DialogDetalleSenal.tableWidget_Lista.verticalHeader().setVisible(False)
		self.DialogDetalleSenal.tableWidget_Lista.setShowGrid(False)
		self.DialogDetalleSenal.tableWidget_Lista.setAlternatingRowColors(True)
		self.DialogDetalleSenal.tableWidget_Lista.resizeColumnsToContents()
		self.DialogDetalleSenal.tableWidget_Lista.verticalHeader().setDefaultSectionSize(24)
		self.DialogDetalleSenal.tableWidget_Lista.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.header = self.DialogDetalleSenal.tableWidget_Lista.horizontalHeader()
		self.DialogDetalleSenal.tableWidget_Lista.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

		self.DialogDetalleSenal.label_Cliente.setText(cuentaynombre)
		self.DialogDetalleSenal.label_Evento.setText(evento)
		self.ListarObservaciones()
		self.AcomodarTamanoTablas()

	def AcomodarTamanoTablas(self):
		self.DialogDetalleSenal.tableWidget_Lista.setColumnWidth(0,165)
		self.DialogDetalleSenal.tableWidget_Lista.setColumnWidth(1,405)
		self.DialogDetalleSenal.tableWidget_Lista.setColumnWidth(2,100)

	def ListarObservaciones(self):
		Observaciones = globalvars.BD.Querys('SeleccionarObservacionesTramasProcesadas',str(self.idtrama))
		while self.DialogDetalleSenal.tableWidget_Lista.rowCount() > 0:
			self.DialogDetalleSenal.tableWidget_Lista.removeRow(0)
		
		for obser in Observaciones:
			Siguiente = self.DialogDetalleSenal.tableWidget_Lista.rowCount()
			self.DialogDetalleSenal.tableWidget_Lista.insertRow(Siguiente)
			columna = 0
			#Columna 0
			texto = QtGui.QTableWidgetItem(obser.fecha.strftime("%A, %d %b %Y %H:%M:%S"))
			self.DialogDetalleSenal.tableWidget_Lista.setItem(Siguiente,columna,texto)	
			columna = 1
			texto = QtGui.QTableWidgetItem(obser.observacion)
			self.DialogDetalleSenal.tableWidget_Lista.setItem(Siguiente,columna,texto)
			columna = 2
			texto = QtGui.QTableWidgetItem(obser.nombre)
			self.DialogDetalleSenal.tableWidget_Lista.setItem(Siguiente,columna,texto)


class LabelImageScaled(QtGui.QLabel):
	def __init__(self):
		super(LabelImageScaled, self).__init__()
		self.setFrameStyle(QtGui.QFrame.StyledPanel)
		self.pintar = False
	def CargarImagen(self,img):
		self.pixmap = QtGui.QPixmap(img)
		self.repaint()
	
	def paintEvent(self, event):
		#if self.pintar:
		try:
			size = self.size()
			painter = QtGui.QPainter(self)
			point = QtCore.QPoint(0,0)
			scaledPix = self.pixmap.scaled(size, QtCore.Qt.KeepAspectRatio, transformMode = QtCore.Qt.SmoothTransformation)
			# start painting the label from left upper corner
			point.setX((size.width() - scaledPix.width())/2)
			point.setY((size.height() - scaledPix.height())/2)
			#print point.x(), ' ', point.y()
			painter.drawPixmap(point, scaledPix)
		except:
			pass

class DialogProcesarSenal(QtGui.QDialog):
	def __init__(self,parent,idtrama):
		super(DialogProcesarSenal, self).__init__()
		self.DialogProcesarSenal = Ui_Dialog()
		self.DialogProcesarSenal.setupUi(self)
		self.idtrama = idtrama
		self.parent = parent
		self.parent.ProcesandoSenal = True
		self.setAttribute(QtCore.Qt.WA_QuitOnClose,False)

		#print self.idtrama
		# Formato de Tabla de Contactos de Emergencia
		self.DialogProcesarSenal.tableWidget_ContactosEmergencia.verticalHeader().setVisible(False)
		self.DialogProcesarSenal.tableWidget_ContactosEmergencia.setShowGrid(False)
		self.DialogProcesarSenal.tableWidget_ContactosEmergencia.setAlternatingRowColors(True)
		self.DialogProcesarSenal.tableWidget_ContactosEmergencia.resizeColumnsToContents()
		#self.DialogProcesarSenal.tableWidget_ContactosEmergencia.verticalHeader().setDefaultSectionSize(24)
		self.DialogProcesarSenal.tableWidget_ContactosEmergencia.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.header = self.DialogProcesarSenal.tableWidget_ContactosEmergencia.horizontalHeader()
		self.DialogProcesarSenal.tableWidget_ContactosEmergencia.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows);

		#Zonas
		self.DialogProcesarSenal.tableWidget_Zonas.verticalHeader().setVisible(False)
		self.DialogProcesarSenal.tableWidget_Zonas.setShowGrid(False)
		self.DialogProcesarSenal.tableWidget_Zonas.setAlternatingRowColors(True)
		self.DialogProcesarSenal.tableWidget_Zonas.resizeColumnsToContents()
		#self.DialogProcesarSenal.tableWidget_Zonas.verticalHeader().setDefaultSectionSize(24)
		self.DialogProcesarSenal.tableWidget_Zonas.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.header = self.DialogProcesarSenal.tableWidget_Zonas.horizontalHeader()
		self.DialogProcesarSenal.tableWidget_Zonas.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows);

		#Usuarios
		self.DialogProcesarSenal.tableWidget_Usuarios.verticalHeader().setVisible(False)
		self.DialogProcesarSenal.tableWidget_Usuarios.setShowGrid(False)
		self.DialogProcesarSenal.tableWidget_Usuarios.setAlternatingRowColors(True)
		self.DialogProcesarSenal.tableWidget_Usuarios.resizeColumnsToContents()
		#self.DialogProcesarSenal.tableWidget_Usuarios.verticalHeader().setDefaultSectionSize(24)
		self.DialogProcesarSenal.tableWidget_Usuarios.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.header = self.DialogProcesarSenal.tableWidget_Usuarios.horizontalHeader()
		self.DialogProcesarSenal.tableWidget_Usuarios.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows);

		self.DialogProcesarSenal.tableWidget_SenalesPendientes.verticalHeader().setVisible(False)
		self.DialogProcesarSenal.tableWidget_SenalesPendientes.setShowGrid(False)
		self.DialogProcesarSenal.tableWidget_SenalesPendientes.setAlternatingRowColors(True)
		self.DialogProcesarSenal.tableWidget_SenalesPendientes.resizeColumnsToContents()
		#self.DialogProcesarSenal.tableWidget_SenalesPendientes.verticalHeader().setDefaultSectionSize(24)
		self.DialogProcesarSenal.tableWidget_SenalesPendientes.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.header = self.DialogProcesarSenal.tableWidget_SenalesPendientes.horizontalHeader()
		self.DialogProcesarSenal.tableWidget_SenalesPendientes.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows);

		self.DialogProcesarSenal.tableWidget_TimeLine.verticalHeader().setVisible(False)
		self.DialogProcesarSenal.tableWidget_TimeLine.setShowGrid(False)
		self.DialogProcesarSenal.tableWidget_TimeLine.setAlternatingRowColors(True)
		self.DialogProcesarSenal.tableWidget_TimeLine.resizeColumnsToContents()
		#self.DialogProcesarSenal.tableWidget_TimeLine.verticalHeader().setDefaultSectionSize(24)
		self.DialogProcesarSenal.tableWidget_TimeLine.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.header = self.DialogProcesarSenal.tableWidget_TimeLine.horizontalHeader()
		self.DialogProcesarSenal.tableWidget_TimeLine.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows);

		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.verticalHeader().setVisible(False)
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setShowGrid(False)
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setAlternatingRowColors(True)
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.resizeColumnsToContents()
		#self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.verticalHeader().setDefaultSectionSize(24)
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.header = self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.horizontalHeader()
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows);

		#Senales
		self.DialogProcesarSenal.tableWidget_Senales.verticalHeader().setVisible(False)
		self.DialogProcesarSenal.tableWidget_Senales.setShowGrid(False)
		self.DialogProcesarSenal.tableWidget_Senales.setAlternatingRowColors(True)
		self.DialogProcesarSenal.tableWidget_Senales.verticalHeader().setDefaultSectionSize(26)
		self.DialogProcesarSenal.tableWidget_Senales.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.DialogProcesarSenal.tableWidget_Senales.setSortingEnabled(False)
		self.DialogProcesarSenal.tableWidget_Senales.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows);
		self.DialogProcesarSenal.tableWidget_Senales.horizontalHeader().setStyleSheet(self.styleSheet())

		self.connect(self.DialogProcesarSenal.comboBox_FechaHistorialSenales, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.ListarSenales)
		#Para activar busqueda avanzada
		self.connect(self.DialogProcesarSenal.pushButton_SelectorBusqueda, QtCore.SIGNAL("clicked()"), self.CambiarBusqueda)
		self.connect(self.DialogProcesarSenal.pushButton_BuscarAvanzado, QtCore.SIGNAL("clicked()"), self.ListarSenalesAvanzada)	
		#Para exportar las senales a XLS
		self.connect(self.DialogProcesarSenal.tableWidget_Senales, QtCore.SIGNAL("cellDoubleClicked(int,int)"), self.AbrirDetalleSenalProcesada)

		self.iconocam =QtGui.QIcon()
		self.iconocam.addPixmap(QtGui.QPixmap(":/iconos/ico/CCTVICON.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

		#Agrego el comentario de senal tomada por operador
		ObservacionTomada = 'Señal tomada por el Operador'
		globalvars.BD.Querys('InsertarObservacionTrama',str(self.idtrama),ObservacionTomada.decode("utf-8"),str(globalvars.DatosUsuario['IDPersonal']))



		self.CargarTabCierreSenal()
		self.CargarIconosSMSCorreo()
		## TAB DATOS CLIENTE ##
		self.connect(self.DialogProcesarSenal.pushButton_Procesar, QtCore.SIGNAL("clicked()"), self.ProcesarSenal)
		self.connect(self.DialogProcesarSenal.pushButton_Procesar_2, QtCore.SIGNAL("clicked()"), self.ProcesarSenalesCierreRapido)

		self.connect(self.DialogProcesarSenal.pushButton_Cancelar, QtCore.SIGNAL("clicked()"), self.Cerrar)
		self.connect(self.DialogProcesarSenal.pushButton_Pendiente, QtCore.SIGNAL("clicked()"), self.PonerPendienteGuardarObservacion)

		## RADIO BUTTONS CIERRE RAPIDO ##
		self.connect(self.DialogProcesarSenal.radioButton_SenalesSeleccionadas, QtCore.SIGNAL("clicked()"), self.CargarCierreRapido)
		self.connect(self.DialogProcesarSenal.radioButton_PorCliente, QtCore.SIGNAL("clicked()"), self.CargarCierreRapido)
		self.connect(self.DialogProcesarSenal.radioButton_PorCodigoAlarma, QtCore.SIGNAL("clicked()"), self.CargarCierreRapido)
		self.connect(self.DialogProcesarSenal.radioButton_PorCodigodeEvento, QtCore.SIGNAL("clicked()"), self.CargarCierreRapido)
		self.connect(self.DialogProcesarSenal.radioButton_TodasLasSenales, QtCore.SIGNAL("clicked()"), self.CargarCierreRapido)


		self.connect(self.DialogProcesarSenal.tabWidget_CierreSenal, QtCore.SIGNAL("currentChanged(int)"), self.DetectarTabCargar)
		self.MapaCargado = False
		self.DatosClientesCargados = False
		self.SenalesCargadas = False

		gc.collect()

		self.CargarTimeLineSenal()
		self.CargarMensajesPredefinidos()
		self.CargarTablaSenalesCliente()
		self.CargarDiccionariosCierreRapido()

		Notas = globalvars.BD.Querys('NotasCliente',str(self.IDCliente))
		if Notas:
			if Notas[0].NotaFija.strip():
				self.DialogProcesarSenal.textEdit_NotaFija.setText(Notas[0].NotaFija)
				self.DialogProcesarSenal.tabWidget_CierreSenal.setCurrentIndex(7)
			if Notas[0].NotaTemp.strip():
				self.DialogProcesarSenal.textEdit_NotaTemp.setText(Notas[0].NotaTemp)
				self.DialogProcesarSenal.label_FechaInicio.setText(Notas[0].FechaIni.strftime("%d %b %Y %H:%M:%S"))
				self.DialogProcesarSenal.label_FechaFin.setText(Notas[0].FechaFin.strftime("%d %b %Y %H:%M:%S"))
				self.DialogProcesarSenal.tabWidget_CierreSenal.setCurrentIndex(7)
		else:
			self.DialogProcesarSenal.tabWidget_CierreSenal.removeTab(7)

		#Cargar Imagen Cliente
		ImagenCliente = globalvars.DictSenales[str(self.idtrama)]['imagencliente']
		if ImagenCliente:
			try:
				self.LabelImage = LabelImageScaled()
				self.DialogProcesarSenal.horizontalLayout_Imagen.addWidget(self.LabelImage)
				self.UrlImage = str(globalvars.WEBServer)+'/img/img_c/'+str(ImagenCliente)
				self.data = urllib.urlopen(self.UrlImage).read()
				#Creamos el Label de la Imagen Proporcional
				self.ImageUser = QtGui.QImage()
				self.ImageUser.loadFromData(self.data)
				self.LabelImage.pintar = True
				self.LabelImage.CargarImagen(self.ImageUser)
			except:
				pass
		
	def CargarIconosSMSCorreo(self):

		#Si hay telefono y correo de la cuenta como tal

		self.menusms = QtGui.QMenu(self)
		self.DialogProcesarSenal.pushButton_sms.setMenu(self.menusms)
		self.DialogProcesarSenal.pushButton_sms.setStyleSheet('QPushButton::menu-indicator { image: none; }')
		if globalvars.DictSenales[str(self.idtrama)]['movil']:
			self.action = QtGui.QAction(self)
			self.action.setText('Cuenta')
			self.menusms.addAction(self.action)
			self.action.triggered.connect(partial(self.AbrirEnviarSMS,str(globalvars.DictSenales[str(self.idtrama)]['movil']),self.IDCliente))

		

		self.menucorreo = QtGui.QMenu(self)
		self.DialogProcesarSenal.pushButton_mail.setMenu(self.menucorreo)
		self.DialogProcesarSenal.pushButton_mail.setStyleSheet('QPushButton::menu-indicator { image: none; }')
		if globalvars.DictSenales[str(self.idtrama)]['correo']:
			self.action = QtGui.QAction(self)
			self.action.setText('Cuenta')
			self.menucorreo.addAction(self.action)
			self.action.triggered.connect(partial(self.AbrirEnviarCorreo,str(globalvars.DictSenales[str(self.idtrama)]['correo']),self.IDCliente))


		self.ResultadoUsuarios = globalvars.BD.Querys2('UsuariosClienteProcesarSenal',str(self.IDCliente))

		#Si hay correos y telefonos para los usuarios
		if self.ResultadoUsuarios:
			self.menuuserssms = QtGui.QMenu(self.menusms)
			self.menuuserssms.setTitle("Usuarios")
			self.menusms.addMenu(self.menuuserssms)
			for reuser in self.ResultadoUsuarios:
				if reuser.movil:
					self.action = QtGui.QAction(self)
					self.action.setText(reuser.nombre)
					self.menuuserssms.addAction(self.action)
					self.action.triggered.connect(partial(self.AbrirEnviarSMS,reuser.movil,self.IDCliente))

		if self.ResultadoUsuarios:
			self.menuuserscorreo = QtGui.QMenu(self.menucorreo)
			self.menuuserscorreo.setTitle("Usuarios")
			self.menucorreo.addMenu(self.menuuserscorreo)
			for reuser in self.ResultadoUsuarios:
				if reuser.email:
					self.action = QtGui.QAction(self)
					self.action.setText(reuser.nombre)
					self.menuuserscorreo.addAction(self.action)
					self.action.triggered.connect(partial(self.AbrirEnviarCorreo,reuser.email,self.IDCliente))

		#Si hay correos y telefonos para los contactos de emergencia
		self.NumerosEmergencia = globalvars.BD.Querys('NumerosEmergenciaMonitoreo',str(self.IDCliente))


		if self.NumerosEmergencia:
			self.menucontactsms = QtGui.QMenu(self.menusms)
			self.menucontactsms.setTitle("Contactos")
			self.menusms.addMenu(self.menucontactsms)
			for recontact in self.NumerosEmergencia:
				if recontact.numero:
					self.action = QtGui.QAction(self)
					self.action.setText(recontact.descript)
					self.menucontactsms.addAction(self.action)
					self.action.triggered.connect(partial(self.AbrirEnviarSMS,recontact.numero,self.IDCliente))



	def AbrirEnviarCorreo(self,numero,idcliente):
		self.DialogNuevoCorreo = DialogNuevoCorreo(self,numero,idcliente)
		self.DialogNuevoCorreo.show()

	def AbrirEnviarSMS(self,numero,idcliente):
		self.DialogNuevoSMS = DialogNuevoSMS(self,numero,idcliente)
		self.DialogNuevoSMS.show()
	def closeEvent(self,event):

		self.parent.ProcesandoSenal = False

	def CargarTimeLineSenal(self):
		
		TimeLine = globalvars.BD.Querys('TimeLineSenal',str(self.idtrama))

		rows = len(TimeLine)
		self.DialogProcesarSenal.tableWidget_TimeLine.setRowCount(rows)
		fila = 0
		columna = 0

		for senaltl in TimeLine:
			columna = 0
			for num in senaltl:
				#print signal
				#print type(signal)
				if columna <= 2:
					if num == None:
						num = ''
					if columna == 0:
						num = num.strftime("%d %b %Y %H:%M:%S")
					texto = QtGui.QTableWidgetItem(num)
					self.DialogProcesarSenal.tableWidget_TimeLine.setItem(fila,columna,texto)
				else:
					break
				columna = columna + 1
			fila = fila + 1

		self.DialogProcesarSenal.tableWidget_TimeLine.setColumnWidth(0,80)
		self.DialogProcesarSenal.tableWidget_TimeLine.setColumnWidth(1,200)
		self.DialogProcesarSenal.tableWidget_TimeLine.setColumnWidth(2,120)

	def Cerrar(self):
		self.close()


	def DetectarTabCargar(self,indextab):
		if indextab == 4 and self.MapaCargado == False:
			self.CargarMapa()
			self.MapaCargado = True
		if indextab == 1 and self.DatosClientesCargados == False:
			self.CargarTabDatosCliente()
		if indextab == 2 and self.SenalesCargadas == False:
			self.CargarTabSenales()
		if indextab == 3:
			self.CargarTabCCTV()

	def CargarTabSenales(self):

		#Agrego al ComboBox la Opcion de Ultimas 20
		self.DialogProcesarSenal.comboBox_FechaHistorialSenales.addItem("Ultimas 20")

		#Ahora Busco que dias tiene Senalesss
		Resultado = globalvars.BD.Querys('DiasSenalesCliente',str(self.IDCliente))
		#Lo pinto en el ComboBox
		for i in Resultado:
			self.DialogProcesarSenal.comboBox_FechaHistorialSenales.addItem(i.fechaSalida.strftime('%d/%m/%Y'))
		#Ahora Tomamos los Datos del Combo
		self.indexHistorialSenales = self.DialogProcesarSenal.comboBox_FechaHistorialSenales.currentIndex()
		self.fechasenalespordefecto = self.DialogProcesarSenal.comboBox_FechaHistorialSenales.itemText(self.indexHistorialSenales)

		self.ListarSenales(self.fechasenalespordefecto)


		#Escondemos por defecto la busqueda avanzada
		self.DialogProcesarSenal.dateEdit_FechaHasta.hide()
		self.DialogProcesarSenal.dateEdit_FechaDesde.hide()
		self.DialogProcesarSenal.comboBox_Eventos.hide()
		self.DialogProcesarSenal.label_12.hide()
		self.DialogProcesarSenal.label_14.hide()
		self.DialogProcesarSenal.label_22.hide()
		self.DialogProcesarSenal.pushButton_BuscarAvanzado.hide()

		#Le coloco la fecha de Hoy a los rangos de fecha de la bsuqeuda avanzada
		self.DialogProcesarSenal.dateEdit_FechaHasta.setDate(QtCore.QDate.currentDate())	
		self.DialogProcesarSenal.dateEdit_FechaDesde.setDate(QtCore.QDate.currentDate())

		#Cargo los grupos de codigos de Alarma  en la busqueda Avanzada
		Resultado = globalvars.BD.Querys('GruposdeAlarmas')
		listadegrupos = []
		self.dictgruposid = {}
		for grupo in Resultado:
			listadegrupos.append(str(grupo.Descript))
			self.dictgruposid[str(grupo.Descript)] = str(grupo.idGrupo)
			
		self.DialogProcesarSenal.comboBox_Eventos.addItems(listadegrupos)
		self.SenalesCargadas = True




	def CargarTabDatosCliente(self):



		rows = len(self.NumerosEmergencia)
		self.DialogProcesarSenal.tableWidget_ContactosEmergencia.setRowCount(rows)
		fila = 0
		columna = 0

		for numem in self.NumerosEmergencia:
			columna = 0
			for num in numem:
				#print signal
				#print type(signal)
				if type(num) == str or type(num) == unicode:
					num = num.encode('Latin-1')
				if columna <= 2:
					if num == None:
						num = ''
					texto = QtGui.QTableWidgetItem(str(num))
					self.DialogProcesarSenal.tableWidget_ContactosEmergencia.setItem(fila,columna,texto)
				else:
					break
				columna = columna + 1
			fila = fila + 1
		self.DialogProcesarSenal.tableWidget_ContactosEmergencia.setColumnWidth(0,100)
		self.DialogProcesarSenal.tableWidget_ContactosEmergencia.setColumnWidth(1,110)
		self.DialogProcesarSenal.tableWidget_ContactosEmergencia.setColumnWidth(2,110)


		ZonasPuntos = globalvars.BD.Querys('ZonasPuntosCliente',str(self.IDCliente))
		rows = len(ZonasPuntos)
		self.DialogProcesarSenal.tableWidget_Zonas.setRowCount(rows)
		fila = 0
		columna = 0
		#print ZonasPuntos
		for zona in ZonasPuntos:
			columna = 0
			valor = ''
			for item in range((len(zona)/3)*4):
				if columna <= 2:
					if zona[item] == None:
						valor = '-----'
					elif type(zona[item]) == int or type(zona[item]) == float:
						valor = str(zona[item])
					else:
						valor = zona[item].encode('latin-1')
					texto = QtGui.QTableWidgetItem(str(valor))
					self.DialogProcesarSenal.tableWidget_Zonas.setItem(fila,columna,texto)
					columna = columna + 1
			fila = fila + 1	
		self.DialogProcesarSenal.tableWidget_Zonas.setColumnWidth(0,30)
		self.DialogProcesarSenal.tableWidget_Zonas.setColumnWidth(1,190)
		self.DialogProcesarSenal.tableWidget_Zonas.setColumnWidth(2,260)

		rows = len(self.ResultadoUsuarios)
		self.DialogProcesarSenal.tableWidget_Usuarios.setRowCount(rows)
		fila = 0
		columna = 0
		#print Resultado
		for user in self.ResultadoUsuarios:
			columna = 0
			valor = ''
			for item in range((len(user)/5)*6):
				if columna <= 4:
					if user[item] == None:
						valor = '-----'
					elif type(user[item]) == int or type(user[item]) == float:
						valor = str(user[item])
					else:
						valor = user[item].encode('latin-1')
					texto = QtGui.QTableWidgetItem(str(valor))
					self.DialogProcesarSenal.tableWidget_Usuarios.setItem(fila,columna,texto)
					columna = columna + 1
				else:
					pass
			fila = fila + 1	
		self.DialogProcesarSenal.tableWidget_Usuarios.setColumnWidth(0,30)
		self.DialogProcesarSenal.tableWidget_Usuarios.setColumnWidth(1,130)
		self.DialogProcesarSenal.tableWidget_Usuarios.setColumnWidth(2,130)
		self.DialogProcesarSenal.tableWidget_Usuarios.setColumnWidth(3,130)
		self.DialogProcesarSenal.tableWidget_Usuarios.setColumnWidth(4,100)



	def CargarTabCierreSenal(self):
		#DatosCliente = globalvars.BD.Querys('DatosClienteSenalMonitoreo',str(self.idtrama))[0]

		self.IDCliente = str(globalvars.DictSenales[str(self.idtrama)]['idcliente'])

		self.PrefijoCuenta = globalvars.DictSenales[str(self.idtrama)]['prefijocuenta']
		if self.PrefijoCuenta == None:
			self.PrefijoCuenta = ''

		self.NombreCliente = globalvars.DictSenales[str(self.idtrama)]['nombrecliente']
		if self.NombreCliente == None:
			self.NombreCliente = ''

		self.Fecha = globalvars.DictSenales[str(self.idtrama)]['fecha']
		if self.Fecha == None or self.Fecha == 'None':
			self.Fecha = ''
		else:
			self.Fecha =self.Fecha.strftime("%d %b %Y %H:%M:%S")

		self.Direccion = globalvars.DictSenales[str(self.idtrama)]['direccion']
		if self.Direccion == None:
			self.Direccion = ''		

		self.Referencia = globalvars.DictSenales[str(self.idtrama)]['referencia']
		if self.Referencia == None:
			self.Referencia = ''

		self.EstatusPanel = globalvars.DictSenales[str(self.idtrama)]['estatuspanel']
		if self.EstatusPanel == None:
			self.EstatusPanel = ''

		self.FechaEstatus = globalvars.DictSenales[str(self.idtrama)]['fechastatus']
		if self.FechaEstatus == 'None' or self.FechaEstatus == None:
			self.FechaEstatus = ''
		else:
			self.FechaEstatus = self.FechaEstatus.strftime("%d %b %Y %H:%M:%S")

		self.Evento = str(globalvars.DictSenales[str(self.idtrama)]['evento'])
		if self.Evento == None:
			self.Evento = ''

		self.NombreEmpresa = globalvars.DictSenales[str(self.idtrama)]['nombreempresa']
		if self.NombreEmpresa == None:
			self.NombreEmpresa = ''

		self.TelefonoLocal = globalvars.DictSenales[str(self.idtrama)]['telefonolocal']
		if self.TelefonoLocal == None:
			self.TelefonoLocal = ''

		self.TelefonoMovil = globalvars.DictSenales[str(self.idtrama)]['movil']
		if self.TelefonoMovil == None:
			self.TelefonoMovil = ''

		self.ClaveMaster = globalvars.DictSenales[str(self.idtrama)]['clavemaster']
		if self.ClaveMaster == None:
			self.ClaveMaster = ''

		if self.ClaveMaster:
			self.action_clavemaster = QtGui.QAction(self)
			self.action_clavemaster.setText(self.ClaveMaster)
			self.menu_clavemaster = QtGui.QMenu(self)
			self.menu_clavemaster.addAction(self.action_clavemaster)
			self.DialogProcesarSenal.pushButton_clavemaster.setMenu(self.menu_clavemaster)
			self.DialogProcesarSenal.pushButton_clavemaster.setStyleSheet('QPushButton::menu-indicator { image: none; }')
		else:
			self.DialogProcesarSenal.pushButton_clavemaster.setEnabled(False)


		self.DescripcionEvento = globalvars.DictSenales[str(self.idtrama)]['descripcionevento']
		if self.DescripcionEvento == None:
			self.DescripcionEvento = ''

		self.ZonaUsuario = globalvars.DictSenales[str(self.idtrama)]['zonausuario']
		if self.ZonaUsuario == None:
			self.ZonaUsuario = ''

		self.ColorEvento = globalvars.DictSenales[str(self.idtrama)]['webcolor']
		if self.ColorEvento == None:
			self.ColorEvento = ''

		self.NumZonaUser = globalvars.DictSenales[str(self.idtrama)]['numzonauser']

		self.TipoEvento = globalvars.DictSenales[str(self.idtrama)]['tipoevent']


		self.Llave = globalvars.DictSenales[str(self.idtrama)]['llave']
		if self.Llave:
			self.action_llave = QtGui.QAction(self)
			self.action_llave.setText(self.Llave)
			self.menu_llave = QtGui.QMenu(self)
			self.menu_llave.addAction(self.action_llave)
			self.DialogProcesarSenal.pushButton_key.setMenu(self.menu_llave)
			self.DialogProcesarSenal.pushButton_key.setStyleSheet('QPushButton::menu-indicator { image: none; }')
		else:
			self.DialogProcesarSenal.pushButton_key.setEnabled(False)

		#Aqui cuando desarrolle lo de la foto. ############OJO#################
		self.DialogProcesarSenal.pushButton_pic.setEnabled(False)


		#### TAB CIERRE SENAL ####

		if self.EstatusPanel.strip() == 'APE':
			self.EstatusPanel = 'Desarmado'
			self.ColorEstatus = '#3379B5'
		elif self.EstatusPanel.strip() == 'CIE':
			self.EstatusPanel = 'Armado'
			self.ColorEstatus = '#DF0101'
		else:
			self.ColorEstatus = '#3379B5'

		self.DialogProcesarSenal.label_NombreCuenta.setText(self.PrefijoCuenta+' - '+self.NombreCliente)
		self.DialogProcesarSenal.label_Fecha.setText(self.Fecha)
		self.DialogProcesarSenal.label_Evento.setText(self.Evento+' - '+self.DescripcionEvento+' - '+self.ZonaUsuario)
		self.DialogProcesarSenal.label_Evento.setStyleSheet('color : '+ self.ColorEvento+'; font: bold 10pt "Calibri";}');

		self.DialogProcesarSenal.label_Direccion.setText(self.Direccion)

		self.DialogProcesarSenal.label_Referencia.setText(self.Referencia)
		self.DialogProcesarSenal.label_Estatus.setText(self.EstatusPanel)
		self.DialogProcesarSenal.label_Estatus.setStyleSheet('color : '+ self.ColorEstatus+'; font: bold 10pt "Calibri";}');
		self.DialogProcesarSenal.label_FechaEstatus.setText(self.FechaEstatus)

		self.DialogProcesarSenal.label_Empresa.setText(self.NombreEmpresa)
		self.DialogProcesarSenal.label_Telefono.setText(str(self.TelefonoLocal)+' / '+str(self.TelefonoMovil))


		self.connect(self.DialogProcesarSenal.comboBox_MensajesPredefinidos, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.AgregarMensajePredefinido)
		self.connect(self.DialogProcesarSenal.comboBox_MensajesPrefefinidosCierreRapido, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.AgregarMensajePredefinidoCierreSenal)

		if str(self.TipoEvento) == str(1): #Solo si es evento de Zona o Punto puede tener camara relacionada
			self.CargarCamarasRelacionadas()
		else:
			self.DialogProcesarSenal.pushButton_cam.setEnabled(False)

	def CargarCamarasRelacionadas(self):

		self.ResultadoCamRelacionadas = globalvars.BD.Querys2('SeleccionarCamarasClienteZona',str(self.NumZonaUser),str(self.IDCliente),str(self.NumZonaUser),str(self.IDCliente))

		if self.ResultadoCamRelacionadas:
			self.menu_camararelacionadas = QtGui.QMenu(self)
			self.DialogProcesarSenal.pushButton_cam.setMenu(self.menu_camararelacionadas)
			self.DialogProcesarSenal.pushButton_cam.setStyleSheet('QPushButton::menu-indicator { image: none; }')			
			for camrel in self.ResultadoCamRelacionadas:
				if camrel.tipo == 'IP':
					self.action = QtGui.QAction(self)
					self.action.setText(camrel.nombredvr+'-'+camrel.nombrecam)
					self.menu_camararelacionadas.addAction(self.action)
					self.action.triggered.connect(partial(self.AbrirCamaraTCPIP,camrel.ip,camrel.puerto))
				elif camrel.tipo == 'RTSP':
					self.action = QtGui.QAction(self)
					self.action.setText(camrel.nombredvr+'-'+camrel.nombrecam)
					self.menu_camararelacionadas.addAction(self.action)
					self.action.triggered.connect(partial(self.AbrirCamaraRTCP,str(camrel.channel),str(camrel.ip),str(camrel.puerto),str(camrel.usuario),str(camrel.clave),str(camrel.id_modelo)))
		else:
			self.DialogProcesarSenal.pushButton_cam.setEnabled(False)
		

	def CargarTablaSenalesCliente(self):


		fila = 0
		columna = 0
		self.dictchecksenalesmismocliente = {}
		for sgnal in globalvars.DictSenales:
			if str(globalvars.DictSenales[sgnal]['idcliente']) == str(self.IDCliente):
				self.DialogProcesarSenal.tableWidget_SenalesPendientes.insertRow(0)
				columna = 0
				#Columna 0
				check = QtGui.QCheckBox()
				check.setText(' ')
				self.dictchecksenalesmismocliente[str(globalvars.DictSenales[sgnal]['idtrama'])] = check
				self.DialogProcesarSenal.tableWidget_SenalesPendientes.setCellWidget(fila, columna, self.dictchecksenalesmismocliente[str(globalvars.DictSenales[sgnal]['idtrama'])])
				#Columna 1
				columna = columna + 1
				texto = QtGui.QTableWidgetItem(globalvars.DictSenales[sgnal]['fecha'].strftime("%d %b %Y %H:%M:%S"))
				self.DialogProcesarSenal.tableWidget_SenalesPendientes.setItem(fila,columna,texto)
				#Columna 2
				columna = columna + 1
				texto = QtGui.QTableWidgetItem(globalvars.DictSenales[sgnal]['evento']+' - '+globalvars.DictSenales[sgnal]['descripcionevento']+' - '+globalvars.DictSenales[sgnal]['zonausuario'])
				self.DialogProcesarSenal.tableWidget_SenalesPendientes.setItem(fila,columna,texto)
				#Colocar el Color
				colorfila = QtGui.QColor(str(globalvars.DictSenales[sgnal]['webcolor']))
				for columnacolor in range(2):
					self.DialogProcesarSenal.tableWidget_SenalesPendientes.item(fila,columnacolor+1).setTextColor(colorfila)
				check.setStyleSheet('color : '+ str(globalvars.DictSenales[sgnal]['webcolor'])+'; font: bold 10pt "Calibri";}');
		self.DialogProcesarSenal.tableWidget_SenalesPendientes.setColumnWidth(0,15)
		self.DialogProcesarSenal.tableWidget_SenalesPendientes.setColumnWidth(1,130)
		self.DialogProcesarSenal.tableWidget_SenalesPendientes.setColumnWidth(2,270)
	def ListarSenalesAvanzada(self):
		self.ListaIDTramas = []

		self.BusquedaAvanzada = True
		FechaInicio = self.DialogProcesarSenal.dateEdit_FechaDesde.date().toPyDate()
		FechaFin = self.DialogProcesarSenal.dateEdit_FechaHasta.date().toPyDate()
		Evento = str(self.DialogProcesarSenal.comboBox_Eventos.currentText())
		
		self.ResultadoBusquedaAvanzada =globalvars.BD.Querys('SenalesBusquedaAvanzada',str(self.IDCliente),FechaInicio,FechaFin,str(self.dictgruposid[Evento]))
		rows = len(self.ResultadoBusquedaAvanzada)
		self.DialogProcesarSenal.tableWidget_Senales.setRowCount(rows)
		fila = 0
		columna = 0
		for sen in self.ResultadoBusquedaAvanzada:
			columna = 0
			for item in sen:
				if columna < 4:
					if item == None:
						item = ''
					else:
						if columna == 2 or columna == 3:
							item = item.strftime("%A, %d %b %Y %H:%M:%S")
						else:
							item = item.encode('latin-1')
					texto = QtGui.QTableWidgetItem(str(item))
					self.DialogProcesarSenal.tableWidget_Senales.setItem(fila,columna,texto)
				else:
					if columna == 4:
						colorfila = QtGui.QColor(str(item))
						for columnacolor in range(4):
							self.DialogProcesarSenal.tableWidget_Senales.item(fila,columnacolor).setTextColor(colorfila)
						pass
					elif columna == 5:
						self.ListaIDTramas.append(str(item))
				columna = columna + 1
			fila = fila + 1
		#Esta variable es para saber si la ultima busqueda fue avanzada o normal para
		#Crear los reportes en Excel y PDF. Y saber que variable buscar si la de self.ResultadoBusquedaAvanzada o
		#self.ResultadoBusqueda
		self.DialogProcesarSenal.tableWidget_Senales.setColumnWidth(0,215)
		self.DialogProcesarSenal.tableWidget_Senales.setColumnWidth(1,215)
		self.DialogProcesarSenal.tableWidget_Senales.setColumnWidth(2,210)
		self.DialogProcesarSenal.tableWidget_Senales.setColumnWidth(3,210)
	def ListarSenales(self,fecha):
		self.ListaIDTramas = []

		self.BusquedaAvanzada = False
		#Solo si hay alguna fecha en la que hay mensajes
		if fecha != '':
			if fecha != "Ultimas 20":
				fecha = datetime.datetime.strptime(str(fecha), "%d/%m/%Y").date()
				#Ahora busco los mensajes en Base de Datos
				self.ResultadoBusquedaNormal = globalvars.BD.Querys('SenalesClienteFecha',str(self.IDCliente),fecha)
				rows = len(self.ResultadoBusquedaNormal)
				self.DialogProcesarSenal.tableWidget_Senales.setRowCount(rows)
				fila = 0
				columna = 0
				for sen in self.ResultadoBusquedaNormal:
					columna = 0
					for item in sen:
						if columna < 4:
							if item == None:
								item = ''
							else:
								if columna == 2 or columna == 3:
									item = item.strftime("%A, %d %b %Y %H:%M:%S")
								else:
									item = item.encode('latin-1')
							texto = QtGui.QTableWidgetItem(str(item))
							self.DialogProcesarSenal.tableWidget_Senales.setItem(fila,columna,texto)
						else:
							if columna == 4:
								colorfila = QtGui.QColor(str(item))
								for columnacolor in range(4):
									self.DialogProcesarSenal.tableWidget_Senales.item(fila,columnacolor).setTextColor(colorfila)
								pass
							elif columna == 5:
								self.ListaIDTramas.append(str(item))
						columna = columna + 1
					fila = fila + 1
			else:
				#Ahora busco los mensajes en Base de Datos
				self.ResultadoBusquedaNormal = globalvars.BD.Querys2('SenalesUltimas20Cliete',str(self.IDCliente))
				rows = len(self.ResultadoBusquedaNormal)
				self.DialogProcesarSenal.tableWidget_Senales.setRowCount(rows)
				fila = 0
				columna = 0
				for sen in self.ResultadoBusquedaNormal:
					columna = 0
					for item in sen:
						if columna < 4:
							if item == None:
								item = ''
							else:
								if columna == 2 or columna == 3:
									item = item.strftime("%A, %d %b %Y %H:%M:%S")
								else:
									item = item.encode('latin-1')
							texto = QtGui.QTableWidgetItem(str(item))
							self.DialogProcesarSenal.tableWidget_Senales.setItem(fila,columna,texto)
						else:
							if columna == 4:
								colorfila = QtGui.QColor(str(item))
								for columnacolor in range(4):
									self.DialogProcesarSenal.tableWidget_Senales.item(fila,columnacolor).setTextColor(colorfila)
								pass
							elif columna == 5:
								self.ListaIDTramas.append(str(item))
						columna = columna + 1
					fila = fila + 1
		#Esta variable es para saber si la ultima busqueda fue avanzada o normal para
		#Crear los reportes en Excel y PDF. Y saber que variable buscar si la de self.ResultadoBusquedaAvanzada o
		#self.ResultadoBusqueda

		self.DialogProcesarSenal.tableWidget_Senales.setColumnWidth(0,215)
		self.DialogProcesarSenal.tableWidget_Senales.setColumnWidth(1,215)
		self.DialogProcesarSenal.tableWidget_Senales.setColumnWidth(2,210)
		self.DialogProcesarSenal.tableWidget_Senales.setColumnWidth(3,210)
	def CambiarBusqueda(self):
		seleccionactual = str(self.DialogProcesarSenal.pushButton_SelectorBusqueda.text())

		if seleccionactual == "Busqueda Sencilla":
			self.DialogProcesarSenal.pushButton_SelectorBusqueda.setText("Busqueda Avanzada")
			#Motramos
			self.DialogProcesarSenal.label_FechaHistorialSenales.show()
			self.DialogProcesarSenal.comboBox_FechaHistorialSenales.show()
			#Escondemos
			self.DialogProcesarSenal.dateEdit_FechaHasta.hide()
			self.DialogProcesarSenal.dateEdit_FechaDesde.hide()
			self.DialogProcesarSenal.comboBox_Eventos.hide()
			self.DialogProcesarSenal.label_12.hide()
			self.DialogProcesarSenal.label_14.hide()
			self.DialogProcesarSenal.label_22.hide()
			self.DialogProcesarSenal.pushButton_BuscarAvanzado.hide()

		elif seleccionactual == "Busqueda Avanzada":
			self.DialogProcesarSenal.pushButton_SelectorBusqueda.setText("Busqueda Sencilla")
			#Mostramos
			self.DialogProcesarSenal.dateEdit_FechaHasta.show()
			self.DialogProcesarSenal.dateEdit_FechaDesde.show()
			self.DialogProcesarSenal.comboBox_Eventos.show()
			self.DialogProcesarSenal.label_12.show()
			self.DialogProcesarSenal.label_14.show()
			self.DialogProcesarSenal.label_22.show()
			self.DialogProcesarSenal.pushButton_BuscarAvanzado.show()
			#Escondemos
			self.DialogProcesarSenal.label_FechaHistorialSenales.hide()
			self.DialogProcesarSenal.comboBox_FechaHistorialSenales.hide()

	def AbrirDetalleSenalProcesada(self,fila,columna):
		idtrama = self.ListaIDTramas[fila]
		cuentaynombre = self.PrefijoCuenta + '-'+self.NombreCliente
		evento = self.DialogProcesarSenal.tableWidget_Senales.item(fila,0).text()
		self.DialogDetalleSenalProcesarSenal = DialogDetalleSenalProcesarSenal(self,idtrama,cuentaynombre,evento)
		self.DialogDetalleSenalProcesarSenal.show()
	def CargarCierreRapido(self):
		if self.DialogProcesarSenal.radioButton_SenalesSeleccionadas.isChecked():
			pass
		elif self.DialogProcesarSenal.radioButton_PorCliente.isChecked():
			self.CierreRapidoPorCliente()
		elif self.DialogProcesarSenal.radioButton_PorCodigoAlarma.isChecked():
			self.CierreRapidoCodigoAlarma()
		elif self.DialogProcesarSenal.radioButton_PorCodigodeEvento.isChecked():
			self.CierreRapidoCodigoEvento()
		elif self.DialogProcesarSenal.radioButton_TodasLasSenales.isChecked():
			self.CierreRapidoTodasLasSenales()
	def CargarModoCCTV(self):
		self.DictModoCCTV = {}
		ResultadoModoCCTV = globalvars.BD.Querys('SeleccionarModoCCTV')
		for modocctv in ResultadoModoCCTV:
			self.DictModoCCTV[modocctv.id_modo] = {'id':modocctv.id_modo,'descripcion':modocctv.descripcion}		
	def CargarTipoCCTV(self):
		self.DictTipoCCTV = {}
		ResultadoTipoCCTV = globalvars.BD.Querys('SeleccionarSubTiposCCTV')
		for tipocam in ResultadoTipoCCTV:
			self.DictTipoCCTV[tipocam.id_subtipo] = {'id':tipocam.id_subtipo,'descripcion':tipocam.descripcion}
	def CargarTabCCTV(self):
		self.DictCCTV = {}
		ResultadoCamaras = globalvars.BD.Querys('SeleccionarCamarasCliente',str(self.IDCliente))
		for cam in ResultadoCamaras:
			self.DictCCTV[cam.id_cctv] = {'descripcion':cam.descripcion,'idtipo':cam.id_tipo,'ip':cam.ip,'puerto':cam.puerto,'usuario':cam.usuario,'clave':cam.clave,'idmodo':cam.id_modo,'idcctv':cam.id_cctv,'marca':cam.id_marca,'modelo':cam.id_modelo}
		self.CargarModoCCTV()
		self.CargarTipoCCTV()
		self.ListarCCTV()
		self.TabCCTVCargados = True


	def ListarCCTV(self):

		#Borro lo que tenga
		self.DialogProcesarSenal.treeWidget_Camaras.clear()
		self.DictItems = {}  #Se creo este diccionario para buscar luego el ID por el Objeto, si duda ver EditarCCTV
		self.ListaItemsChilds = [] #Para saber cuando se hace doble click a un hijo y que no pase nada
		fila = 0
		columna = 0
		for idcctv,datos in self.DictCCTV.iteritems():
			if datos["idmodo"] == 1: #IP DOMINIO
				texto = QtGui.QTreeWidgetItem(self.DialogProcesarSenal.treeWidget_Camaras)
				texto.setText(0, datos["descripcion"])
				for tipo in self.DictTipoCCTV:
					if self.DictTipoCCTV[tipo]['id'] == datos["idtipo"]:
						desctipo = self.DictTipoCCTV[tipo]['descripcion']
						break
				texto.setText(1, desctipo)
				for modo in self.DictModoCCTV:
					if self.DictModoCCTV[modo]['id'] == datos["idmodo"]:
						modo = self.DictModoCCTV[modo]['descripcion']
						break
				texto.setText(2, modo)
				widget = QtGui.QWidget()
				layout = QtGui.QHBoxLayout()
				btncamara = QtGui.QPushButton(self.DialogProcesarSenal.treeWidget_Camaras)
				btncamara.setFlat(True)
				btncamara.setIcon(self.iconocam)
				btncamara.clicked.connect(partial(self.AbrirCamaraTCPIP,datos["ip"],datos["puerto"]))
				layout.addWidget(btncamara)				
				layout.addStretch()
				widget.setLayout(layout)
				layout.setContentsMargins(0,0,0,0)
				self.DialogProcesarSenal.treeWidget_Camaras.setItemWidget(texto,3,widget)
				self.DialogProcesarSenal.treeWidget_Camaras.insertTopLevelItem(columna,texto)
				columna = columna + 1
			elif datos["idmodo"] == 2: #RTSP
				texto = QtGui.QTreeWidgetItem(self.DialogProcesarSenal.treeWidget_Camaras)
				texto.setText(0, datos["descripcion"])
				for tipo in self.DictTipoCCTV:
					if self.DictTipoCCTV[tipo]['id'] == datos["idtipo"]:
						desctipo = self.DictTipoCCTV[tipo]['descripcion']
						break
				texto.setText(1, desctipo)
				for modo in self.DictModoCCTV:
					if self.DictModoCCTV[modo]['id'] == datos["idmodo"]:
						modo = self.DictModoCCTV[modo]['descripcion']
						break
				texto.setText(2, modo)
				self.DialogProcesarSenal.treeWidget_Camaras.insertTopLevelItem(columna,texto)
				ResultadoCanalesRTSP = globalvars.BD.Querys('SeleccionarCanalesIDCCTV',str(datos["idcctv"]))
				for Channel in ResultadoCanalesRTSP:
					widgethijo = QtGui.QWidget()
					Hijo = QtGui.QTreeWidgetItem(texto)  #Texto es la columna Padre
					Hijo.setText(0, 'Camara ' + str(Channel.channel) + ' - ' + str(Channel.descripcion))
					Hijo.setText(1, 'Camara')
					Hijo.setText(2, 'RTSP')
					layouthijo = QtGui.QHBoxLayout()
					btncamara = QtGui.QPushButton()
					btncamara.setFlat(True)
					btncamara.setIcon(self.iconocam)
					btncamara.clicked.connect(partial(self.AbrirCamaraRTCP,str(Channel.channel),str(datos["ip"]),str(datos["puerto"]),str(datos["usuario"]),str(datos["clave"]),str(datos["modelo"])))
					layouthijo.addWidget(btncamara)
					widgethijo.setLayout(layouthijo)
					layouthijo.addStretch()
					layouthijo.setContentsMargins(0,0,0,0)
					self.DialogProcesarSenal.treeWidget_Camaras.setItemWidget(Hijo,3,widgethijo)
					self.ListaItemsChilds.append(Hijo)
					#texto.addChild(widgethijo)
				columna = columna + 1
			self.DictItems[texto] = datos['idcctv']

		self.DialogProcesarSenal.treeWidget_Camaras.setColumnWidth(0,100)
		self.DialogProcesarSenal.treeWidget_Camaras.setColumnWidth(1,100)
		self.DialogProcesarSenal.treeWidget_Camaras.setColumnWidth(2,100)
		self.DialogProcesarSenal.treeWidget_Camaras.setColumnWidth(3,100)
	def AbrirCamaraTCPIP(self,ip,puerto):

		Direccion = ip+':'+puerto
		print Direccion
		webbrowser.open(Direccion)
	def AbrirCamaraRTCP(self,canal,ip,puerto,usuario,clave,idmodelo):

		#Busco el String de Conexion a la camara RTSP segun su Modelo
		ResultadoMarcasCCTV = globalvars.BD.Querys('SeleccionarStringPorModelo',str(idmodelo))[0]

		#Reemplazamos la IP y el Puerto por los Seleccionados

		String = str(ResultadoMarcasCCTV.string_acceso)

		for i in range(10):
			if '[encode]' in String:
				if String is not None:
					resp=re.search('\[encode\].{1,90}\[/encode\]',String)
					if resp is not None:
						substring = String[resp.start():resp.end()]
						resp=re.search('\[fn\].{1,20}\[/fn\]',String)
						encode = String[resp.start():resp.end()]
						encode = encode.replace('[fn]','')
						encode = encode.replace('[/fn]','')
						resp = re.search('\[val\].{1,20}\[/val\]',String)
						valor = String[resp.start():resp.end()]
						valor = valor.replace('[val]','')
						valor = valor.replace('[/val]','')
						if encode == None:
							break
						else:
							valor = valor.replace('#user#',usuario)
							valor = valor.replace('#clave#',clave)
							valor = valor.replace('#channel#',canal)
							if encode == 'base64_encode':
								valor = base64.b64encode(valor)
						######Aqui agregamos mas si vamos a utilizar otros encode######
						String = String.replace(substring,valor)
			else:
				break

		String = String.replace('#user#',usuario)
		String = String.replace('#clave#',clave)
		String = String.replace('#channel#',canal)
		String = String.replace('#ip#',ip)

		String = String.replace('#puerto#',puerto)
		try:
			subprocess.Popen('"C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe" %s'%String)
		except:
			subprocess.Popen('"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe" %s'%String)
	def CierreRapidoCodigoEvento(self):
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.removeColumn(3)

		while self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.rowCount() > 0:
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.removeRow(0)

		#Acomodar la Tabla por Codigo de Evento
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.clear()
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.clearContents()




		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setHorizontalHeaderLabels(('Selecciona','Codigo','Descripcion'))
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignLeft)
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setColumnWidth(0,15)
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setColumnWidth(1,120)
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setColumnWidth(2,687)
		fila = 0
		columna = 0
		self.dictchecksenalescodigoevento = {}
		for codigo,descrip in self.dictcodigoeventodescrip.iteritems():
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.insertRow(0)
			columna = 0
			#Columna 0
			check = QtGui.QCheckBox()
			check.setText(' ')
			self.dictchecksenalescodigoevento[str(codigo)] = check
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setCellWidget(fila, columna, self.dictchecksenalescodigoevento[str(codigo)])
			#Columna 1
			columna = columna + 1
			texto = QtGui.QTableWidgetItem(str(codigo))
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setItem(fila,columna,texto)
			#Columna 2
			columna = columna + 1
			texto = QtGui.QTableWidgetItem(descrip[0])
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setItem(fila,columna,texto)
			#Colocar el Color
			colorfila = QtGui.QColor(str(descrip[1]))
			for columnacolor in range(2):
				self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.item(fila,columnacolor+1).setTextColor(colorfila)
			check.setStyleSheet('color : '+ str(descrip[1])+'; font: bold 10pt "Calibri";}');
	def CierreRapidoCodigoAlarma(self):
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.removeColumn(3)

		#Acomodar la Tabla por Codigo de Evento
		while self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.rowCount() > 0:
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.removeRow(0)

		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.clear()
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.clearContents()

		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setHorizontalHeaderLabels(('Selecciona','Codigo','Descripcion'))
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignLeft)

		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setColumnWidth(0,15)
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setColumnWidth(1,120)
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setColumnWidth(2,687)
		fila = 0
		columna = 0
		self.dictchecksenalescodigoalarma = {}
		for codigo,descrip in self.dictcodigoalarmadescrip.iteritems():
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.insertRow(0)
			columna = 0
			#Columna 0
			check = QtGui.QCheckBox()
			check.setText(' ')
			self.dictchecksenalescodigoalarma[str(codigo)] = check
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setCellWidget(fila, columna, self.dictchecksenalescodigoalarma[str(codigo)])
			#Columna 1
			columna = columna + 1
			texto = QtGui.QTableWidgetItem(str(codigo))
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setItem(fila,columna,texto)
			#Columna 2
			columna = columna + 1
			texto = QtGui.QTableWidgetItem(descrip[0])
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setItem(fila,columna,texto)
			#Colocar el Color
			colorfila = QtGui.QColor(str(descrip[1]))
			for columnacolor in range(2):
				self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.item(fila,columnacolor+1).setTextColor(colorfila)
			check.setStyleSheet('color : '+ str(descrip[1])+'; font: bold 10pt "Calibri";}');
	def CierreRapidoPorCliente(self):
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.removeColumn(3)

		#Acomodar la Tabla por Codigo de Evento
		while self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.rowCount() > 0:
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.removeRow(0)

		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.clear()
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.clearContents()

		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setHorizontalHeaderLabels(('Selecciona','ID','Nombre'))
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignLeft)

		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setColumnWidth(0,20)
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setColumnWidth(1,80)
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setColumnWidth(2,687)
		fila = 0
		columna = 0
		self.dictchecksenalesporcliente = {}
		for codigo,descrip in self.dictporclientedatos.iteritems():
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.insertRow(0)
			columna = 0
			#Columna 0
			check = QtGui.QCheckBox()
			check.setText(' ')
			self.dictchecksenalesporcliente[str(codigo)] = check
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setCellWidget(fila, columna, self.dictchecksenalesporcliente[str(codigo)])
			#Columna 1
			columna = columna + 1
			texto = QtGui.QTableWidgetItem(str(codigo))
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setItem(fila,columna,texto)
			#Columna 2
			columna = columna + 1
			if descrip == None:
				descrip = ''
			texto = QtGui.QTableWidgetItem(descrip)
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setItem(fila,columna,texto)
	def CierreRapidoTodasLasSenales(self):
		#Acomodar la Tabla por Codigo de Evento
		while self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.rowCount() > 0:
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.removeRow(0)

		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.clear()
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.clearContents()
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.insertColumn(3)
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setHorizontalHeaderLabels(('ID','Nombre','Senal','Fecha'))
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignLeft)

		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setColumnWidth(0,80)
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setColumnWidth(1,220)
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setColumnWidth(2,267)
		self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setColumnWidth(3,220)

		fila = 0
		columna = 0
		for codigo,descrip in self.dicttodassenalesdatos.iteritems():
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.insertRow(0)
			columna = 0
			#Columna 0
			if descrip[0] == None:
				descrip[0] = ''
			texto = QtGui.QTableWidgetItem(str(descrip[0]))
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setItem(fila,columna,texto)
			#Columna 1
			columna = columna + 1
			if descrip[1] == None:
				descrip[1] = ''
			texto = QtGui.QTableWidgetItem(descrip[1])
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setItem(fila,columna,texto)
			#Columna 2
			columna = columna + 1
			if descrip[2] == None:
				descrip[2] = ''
			texto = QtGui.QTableWidgetItem(descrip[2])
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setItem(fila,columna,texto)		
			#Columna 3
			columna = columna + 1
			if descrip[3] == None:
				descrip[3] = ''
			texto = QtGui.QTableWidgetItem(descrip[3].strftime("%d %b %Y %H:%M:%S"))
			self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.setItem(fila,columna,texto)
			#Colocar el Color
			colorfila = QtGui.QColor(str(descrip[4]))
			for columnacolor in range(4):
				self.DialogProcesarSenal.tableWidget_SeleccionQueSenales.item(fila,columnacolor).setTextColor(colorfila)
	def CargarDiccionariosCierreRapido(self):
		#Los diccionarios del cierre rapido lo cargo en el init de este objeto
		#Para cerrar solo senales que existan en el momento de hacer doble click en la senal a editar
		#Y no senales nuevas que el operador no ha visto.

		#Los de Codigo de Evento
		self.dictcodigoeventodescrip = {}
		self.dictcodigoeventoidtrama = {}
		for sig in globalvars.DictSenales:
			if globalvars.DictSenales[sig]['evento'] in self.dictcodigoeventoidtrama:
				self.dictcodigoeventoidtrama[str(globalvars.DictSenales[sig]['evento'])].append(globalvars.DictSenales[sig]['idtrama'])
			else:
				self.dictcodigoeventoidtrama[str(globalvars.DictSenales[sig]['evento'])] = [globalvars.DictSenales[sig]['idtrama']]
			if not globalvars.DictSenales[sig]['evento'] in self.dictcodigoeventodescrip:
				self.dictcodigoeventodescrip[globalvars.DictSenales[sig]['evento']] = [globalvars.DictSenales[sig]['descripcionevento'],globalvars.DictSenales[sig]['webcolor']]

		#Los de Codigo de Alarma
		self.dictcodigoalarmadescrip = {}
		self.dictcodigoalarmaidtrama = {}
		for sig in globalvars.DictSenales:
			if globalvars.DictSenales[sig]['codigoalarma'] in self.dictcodigoalarmaidtrama:
				self.dictcodigoalarmaidtrama[str(globalvars.DictSenales[sig]['codigoalarma'])].append(globalvars.DictSenales[sig]['idtrama'])
			else:
				self.dictcodigoalarmaidtrama[str(globalvars.DictSenales[sig]['codigoalarma'])] = [globalvars.DictSenales[sig]['idtrama']]
			if not globalvars.DictSenales[sig]['codigoalarma'] in self.dictcodigoalarmadescrip:
				self.dictcodigoalarmadescrip[globalvars.DictSenales[sig]['codigoalarma']] = [globalvars.DictSenales[sig]['descripcioncodigoalarma'],globalvars.DictSenales[sig]['webcolor']]

		#Por Cliente
		self.dictporclientedatos = {}
		self.dictporclienteidtramas = {}
		for sig in globalvars.DictSenales:
			if str(globalvars.DictSenales[sig]['idcliente']) in self.dictporclienteidtramas:
				self.dictporclienteidtramas[str(globalvars.DictSenales[sig]['idcliente'])].append(globalvars.DictSenales[sig]['idtrama'])
			else:
				self.dictporclienteidtramas[str(globalvars.DictSenales[sig]['idcliente'])] = [globalvars.DictSenales[sig]['idtrama']]
			if not globalvars.DictSenales[sig]['idcliente'] in self.dictporclientedatos:
				self.dictporclientedatos[globalvars.DictSenales[sig]['idcliente']] = globalvars.DictSenales[sig]['nombrecliente']

		self.dicttodassenalesdatos = {}
		self.listatodaslassenales = []
		for sig in globalvars.DictSenales:
			self.listatodaslassenales.append(str(globalvars.DictSenales[sig]['idtrama']))
			self.dicttodassenalesdatos[str(globalvars.DictSenales[sig]['idtrama'])] = [str(globalvars.DictSenales[sig]['idcliente']),globalvars.DictSenales[sig]['nombrecliente'],str(globalvars.DictSenales[sig]['idtrama']),globalvars.DictSenales[sig]['fecha'],str(globalvars.DictSenales[sig]['webcolor'])]
			
	def CargarMensajesPredefinidos(self):
		MensajesPredefinidos = globalvars.BD.Querys('MensajesPredefinidosMonitoreo',str(self.idtrama))

		for menpre in MensajesPredefinidos:
			self.DialogProcesarSenal.comboBox_MensajesPredefinidos.addItem(menpre[0])
			self.DialogProcesarSenal.comboBox_MensajesPrefefinidosCierreRapido.addItem(menpre[0])

		#Colocamos Los dos ComboBox de Mensajes Predefinidos con nungun mensaje por defecto
		self.DialogProcesarSenal.comboBox_MensajesPrefefinidosCierreRapido.setCurrentIndex(-1)
		self.DialogProcesarSenal.comboBox_MensajesPredefinidos.setCurrentIndex(-1)

	def AgregarMensajePredefinido(self,texto):
		self.DialogProcesarSenal.textEdit_Comentarios.setText(texto)

	def AgregarMensajePredefinidoCierreSenal(self,texto):
		self.DialogProcesarSenal.textEdit_ComentarioCierreRapido.setText(texto)

	def CargarMapa(self):
		self.WebViewMapaCliente = WebViewMapaCliente(self,globalvars.DictSenales[str(self.idtrama)]['latitud'],globalvars.DictSenales[str(self.idtrama)]['longitud'],globalvars.DictSenales[str(self.idtrama)]['imagentipocliente'],globalvars.DictSenales[str(self.idtrama)]['nombreempresa'],globalvars.DictSenales[str(self.idtrama)]['nombrecliente'])
		self.DialogProcesarSenal.gridLayout_14.addWidget(self.WebViewMapaCliente, 0, 0, 1, 1)

	def PonerPendienteGuardarObservacion(self):
		senalesapendientesadicionales = []
		for i in self.dictchecksenalesmismocliente:
			if self.dictchecksenalesmismocliente[i].isChecked():
				senalesapendientesadicionales.append(str(i))

		for senalapendiente in senalesapendientesadicionales:
			globalvars.BD.Querys('ActualizarTramaPendiente',str(senalapendiente))
			if self.DialogProcesarSenal.textEdit_Comentarios.toPlainText() != '':
				globalvars.BD.Querys('InsertarObservacionTrama',str(senalapendiente),str(self.DialogProcesarSenal.textEdit_Comentarios.toPlainText().toLatin1()),str(globalvars.DatosUsuario['IDPersonal']))

		#La colocamos en Pendiente
		globalvars.BD.Querys('ActualizarTramaPendiente',str(self.idtrama))
		#Si tiene Observacion la Guardamos
		if self.DialogProcesarSenal.textEdit_Comentarios.toPlainText() != '':
			globalvars.BD.Querys('InsertarObservacionTrama',str(self.idtrama),str(self.DialogProcesarSenal.textEdit_Comentarios.toPlainText().toLatin1()),str(globalvars.DatosUsuario['IDPersonal']))
		self.close()

	def ProcesarSenal(self):
		#Verificamos si aparte de la trama abierta, seleccionamos otra trama en la tabla de tramas del mismo
		#Cliente
		senalesaprocesaradicionales = []
		for i in self.dictchecksenalesmismocliente:
			if self.dictchecksenalesmismocliente[i].isChecked():
				senalesaprocesaradicionales.append(str(i))

		QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))

		for senalaprocesar in senalesaprocesaradicionales:
			if self.DialogProcesarSenal.textEdit_Comentarios.toPlainText() != '':
				globalvars.BD.Querys('InsertarObservacionTrama',str(senalaprocesar),str(self.DialogProcesarSenal.textEdit_Comentarios.toPlainText().toLatin1()),str(globalvars.DatosUsuario['IDPersonal']))
			globalvars.BD.Querys('InsertarTramaProcesada',str(self.DialogProcesarSenal.textEdit_Comentarios.toPlainText().toLatin1()),str(globalvars.DatosUsuario['IDPersonal']),str(senalaprocesar))
	
		#Si tiene Observacion la Guardamos
		if self.DialogProcesarSenal.textEdit_Comentarios.toPlainText() != '':
			globalvars.BD.Querys('InsertarObservacionTrama',str(self.idtrama),str(self.DialogProcesarSenal.textEdit_Comentarios.toPlainText().toLatin1()),str(globalvars.DatosUsuario['IDPersonal']))
		self.close()
		#Ahora de aqui en adelante es la trama a la que hicimos doble click, la principal se guarda y se le pone la observacion
		globalvars.BD.Querys('InsertarTramaProcesada',str(self.DialogProcesarSenal.textEdit_Comentarios.toPlainText().toLatin1()),str(globalvars.DatosUsuario['IDPersonal']),str(self.idtrama))
		QtGui.QApplication.restoreOverrideCursor()

	def ProcesarSenalesCierreRapido(self):
		QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))

		listasenalesaprocesar = []
		if self.DialogProcesarSenal.radioButton_SenalesSeleccionadas.isChecked():
			pass
		elif self.DialogProcesarSenal.radioButton_PorCliente.isChecked():
			for i in self.dictchecksenalesporcliente:
				if self.dictchecksenalesporcliente[i].isChecked():
					if type(self.dictporclienteidtramas[str(i)]) == list or type(self.dictporclienteidtramas[str(i)]) == tuple:
						for i in self.dictporclienteidtramas[str(i)]:
							listasenalesaprocesar.append(str(i))
					else:
						listasenalesaprocesar.append(str(self.dictporclienteidtramas[str(i)]))
		elif self.DialogProcesarSenal.radioButton_PorCodigoAlarma.isChecked():
			for i in self.dictchecksenalescodigoalarma:
				if self.dictchecksenalescodigoalarma[i].isChecked():
					if type(self.dictcodigoalarmaidtrama[str(i)]) == list or type(self.dictcodigoalarmaidtrama[str(i)]) == tuple:
						for i in self.dictcodigoalarmaidtrama[str(i)]:
							listasenalesaprocesar.append(str(i))
					else:
						listasenalesaprocesar.append(str(self.dictcodigoalarmaidtrama[str(i)]))
		elif self.DialogProcesarSenal.radioButton_PorCodigodeEvento.isChecked():
			for i in self.dictchecksenalescodigoevento:
				if self.dictchecksenalescodigoevento[i].isChecked():
					if type(self.dictcodigoeventoidtrama[str(i)]) == list or type(self.dictcodigoeventoidtrama[str(i)]) == tuple:
						for i in self.dictcodigoeventoidtrama[str(i)]:
							listasenalesaprocesar.append(str(i))
					else:
						listasenalesaprocesar.append(str(self.dictcodigoeventoidtrama[str(i)]))
		elif self.DialogProcesarSenal.radioButton_TodasLasSenales.isChecked():
			for i in self.listatodaslassenales:
				listasenalesaprocesar.append(str(i))

		for senalaprocesar in listasenalesaprocesar:
			if self.DialogProcesarSenal.textEdit_ComentarioCierreRapido.toPlainText() != '':
				globalvars.BD.Querys('InsertarObservacionTrama',str(senalaprocesar),str(self.DialogProcesarSenal.textEdit_ComentarioCierreRapido.toPlainText().toLatin1()),str(globalvars.DatosUsuario['IDPersonal']))
			globalvars.BD.Querys('InsertarTramaProcesada',str(self.DialogProcesarSenal.textEdit_ComentarioCierreRapido.toPlainText().toLatin1()),str(globalvars.DatosUsuario['IDPersonal']),str(senalaprocesar))
		QtGui.QApplication.restoreOverrideCursor()

		self.close()
		
class SubVentanaMonitoreo(QtGui.QWidget):
	def __init__(self,parent):
		super(SubVentanaMonitoreo, self).__init__()
		self.SubVentanaMonitoreo = Ui_SubVentanaMonitoreo()
		self.SubVentanaMonitoreo.setupUi(self)
		#Para que se cierre el Monitoreo si se cierra el Software
		self.setAttribute(QtCore.Qt.WA_QuitOnClose,False)
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)
		#Modo Pause por Defecto Desabilitado
		self.ModoPause = False
		self.ModoSilenciar = False
		self.ProcesandoSenal = False

		#Escondo el Frame que sale cuando estoy en pause
		self.SubVentanaMonitoreo.frame_ModoPause.hide()

		#Tabla de Senales por Procesar
		self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.verticalHeader().setVisible(False)
		self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.setShowGrid(False)
		self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.setAlternatingRowColors(True)
		self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.resizeColumnsToContents()
		self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.verticalHeader().setDefaultSectionSize(24)
		self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.header = self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.horizontalHeader()
		self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
		#self.header.setResizeMode(QtGui.QHeaderView.Stretch)

		self.connect(self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar, QtCore.SIGNAL("cellDoubleClicked(int,int)"), self.AbrirProcesarSenal)

		#Tabla de Senales Pendientes
		self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.verticalHeader().setVisible(False)
		self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.setShowGrid(False)
		self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.setAlternatingRowColors(True)
		self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.resizeColumnsToContents()
		self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.verticalHeader().setDefaultSectionSize(24)
		self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.header = self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.horizontalHeader()
		self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows);
		#self.header.setResizeMode(QtGui.QHeaderView.Stretch)

		self.connect(self.SubVentanaMonitoreo.tableWidget_SenalesPendientes, QtCore.SIGNAL("cellDoubleClicked(int,int)"), self.AbrirProcesarSenalPendiente)

		#Tabla de Todas las Senales
		self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.verticalHeader().setVisible(False)
		self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.setShowGrid(False)
		self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.setAlternatingRowColors(True)
		self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.resizeColumnsToContents()
		self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.verticalHeader().setDefaultSectionSize(24)
		self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.header = self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.horizontalHeader()
		self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows);
		#self.header.setResizeMode(QtGui.QHeaderView.Stretch)

		#Tabla de Senales Procesadas
		self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.verticalHeader().setVisible(False)
		self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.setShowGrid(False)
		self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.setAlternatingRowColors(True)
		self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.resizeColumnsToContents()
		self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.verticalHeader().setDefaultSectionSize(24)
		self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.header = self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.horizontalHeader()
		self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
		#self.header.setResizeMode(QtGui.QHeaderView.Stretch)
		self.connect(self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas, QtCore.SIGNAL("cellDoubleClicked(int,int)"), self.AbrirDetalleSenalProcesada)



		#Cargo Los Iconos para alternar.
		self.iconoplay = QtGui.QIcon()
		self.iconoplay.addPixmap(QtGui.QPixmap(":/iconos/ico/play128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.iconopause = QtGui.QIcon()
		self.iconopause.addPixmap(QtGui.QPixmap(":/iconos/ico/pause41.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.iconosonidoact = QtGui.QIcon()
		self.iconosonidoact.addPixmap(QtGui.QPixmap(":/iconos/ico/sound35.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.iconosonidodesact = QtGui.QIcon()
		self.iconosonidodesact.addPixmap(QtGui.QPixmap(":/iconos/ico/speaker113.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.SonidoAlarmaNueva = QtGui.QSound("sonidos/Alarm.wav",self)
		self.SonidoAlarmaPendiente = QtGui.QSound("sonidos/pendiente.wav",self)

		self.HiloMonitoreo = HiloMonitoreo(self,self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar,self.SubVentanaMonitoreo.tableWidget_SenalesPendientes,self.SubVentanaMonitoreo.tableWidget_TodasLasSenales,self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas)
		self.HiloMonitoreo.start()

		self.HiloTiempos = HiloTimers(self)
		self.HiloTiempos.start()

		self.connect(self.SubVentanaMonitoreo.pushButton_Pause, QtCore.SIGNAL("clicked()"), self.ModoPauseFunction)
		self.connect(self.SubVentanaMonitoreo.pushButton_Silenciar, QtCore.SIGNAL("clicked()"), self.ModoSilenciarFunction)
		self.connect(self.SubVentanaMonitoreo.tabWidget_Monitoreo, QtCore.SIGNAL("currentChanged(int)"), self.CargarTabSeleccionado)


		#Para captar el evento cuando muevo el mouse por encima de las Tablas, hay que hacerlo con viewport tambien
		self.installEventFilter(self)
		self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.installEventFilter(self)
		self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.viewport().installEventFilter(self)
		self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.installEventFilter(self)
		self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.viewport().installEventFilter(self)
		self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.installEventFilter(self)
		self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.viewport().installEventFilter(self)
		self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.installEventFilter(self)
		self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.viewport().installEventFilter(self)


		self.setMouseTracking(True)
		self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.setMouseTracking(True)
		self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.setMouseTracking(True)
		self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.setMouseTracking(True)
		self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.setMouseTracking(True)
		
		#Inicio Hombre Muerto
		self.emit(QtCore.SIGNAL("IniciarTempHM"))

		#self.CargarTablasEstaticamente()
		self.connect(self.SubVentanaMonitoreo.pushButton_aqui, QtCore.SIGNAL("clicked()"), self.ModoPauseFunction)
		
		#Invento mio para solucionar el Bug con que si esta activado el rezize de las tablas\
		#Con el resize de la ventana no se le puede colocar un tamano por defecto
		self.Resize1 =  False
		self.Resize = False



	def CargarTablasEstaticamente(self):

		self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.setColumnWidth(0,65)
		self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.setColumnWidth(1,330)
		self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.setColumnWidth(2,330)
		self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.setColumnWidth(3,330)
		self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.setColumnWidth(4,120)
		self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.setColumnWidth(5,65)

		self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.setColumnWidth(0,65)
		self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.setColumnWidth(1,330)
		self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.setColumnWidth(2,330)
		self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.setColumnWidth(3,330)
		self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.setColumnWidth(4,120)
		self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.setColumnWidth(5,65)

		self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.setColumnWidth(0,65)
		self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.setColumnWidth(1,330)
		self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.setColumnWidth(2,330)
		self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.setColumnWidth(3,330)
		self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.setColumnWidth(4,120)
		self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.setColumnWidth(5,65)

		self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.setColumnWidth(0,65)
		self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.setColumnWidth(1,250)
		self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.setColumnWidth(2,250)
		self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.setColumnWidth(3,50)
		self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.setColumnWidth(4,50)
		self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.setColumnWidth(5,50)
		self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.setColumnWidth(6,50)

	def CargarTabSeleccionado(self,tab):
		if tab == 0:
			self.emit(QtCore.SIGNAL("SenalesPorProcesar"))
		elif tab == 1:
			self.emit(QtCore.SIGNAL("SenalesPendientes"))
		elif tab == 2:
			self.emit(QtCore.SIGNAL("TodasLasSenales"))
		elif tab == 3:
			self.emit(QtCore.SIGNAL("SenalesProcesadas"))
		self.ArreglarTamanoTablas()




	def eventFilter(self, source, event):
		if event.type() == QtCore.QEvent.MouseMove:
			self.emit(QtCore.SIGNAL("DetenerTempHM"))
			self.emit(QtCore.SIGNAL("IniciarTempHM"))
		if event.type() == QtCore.QEvent.WindowStateChange:
			self.ArreglarTamanoTablas()
		return QtGui.QWidget.eventFilter(self, source, event)

		#if (event.type() == QtCore.QEvent.MouseMove and
		#	source is self.label):
		#	pos = event.pos()
		#	print('mouse move: (%d, %d)' % (pos.x(), pos.y()))
		#return QtGui.QWidget.eventFilter(self, source, event)

	def resizeEvent(self,resizeEvent):
		if self.Resize1 == True:
			self.ArreglarTamanoTablas()
		self.Resize1 = True
		pass

	def ArreglarTamanoTablas(self):

		if self.Resize == True:
			print 'Aqui Adentro'
			self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.setColumnWidth(0,self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.width()/20)
			self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.setColumnWidth(1,self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.width()/3.8)
			self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.setColumnWidth(2,self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.width()/3.8)
			self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.setColumnWidth(3,self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.width()/3.8)
			self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.setColumnWidth(4,self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.width()/10)
			self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.setColumnWidth(5,self.SubVentanaMonitoreo.tableWidget_SenalesPorProcesar.width()/20)
			
			self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.setColumnWidth(0,self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.width()/20)
			self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.setColumnWidth(1,self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.width()/3.8)
			self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.setColumnWidth(2,self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.width()/3.8)
			self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.setColumnWidth(3,self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.width()/3.8)
			self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.setColumnWidth(4,self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.width()/10)
			self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.setColumnWidth(5,self.SubVentanaMonitoreo.tableWidget_SenalesPendientes.width()/20)

			self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.setColumnWidth(0,self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.width()/20)
			self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.setColumnWidth(1,self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.width()/3.8)
			self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.setColumnWidth(2,self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.width()/3.8)
			self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.setColumnWidth(3,self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.width()/3.8)
			self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.setColumnWidth(4,self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.width()/10)
			self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.setColumnWidth(5,self.SubVentanaMonitoreo.tableWidget_TodasLasSenales.width()/20)

			self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.setColumnWidth(0,self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.width()/20)
			self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.setColumnWidth(1,self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.width()/5.3)
			self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.setColumnWidth(2,self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.width()/5.3)
			self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.setColumnWidth(3,self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.width()/10)
			self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.setColumnWidth(4,self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.width()/4)
			self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.setColumnWidth(5,self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.width()/10)
			self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.setColumnWidth(6,self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.width()/10)
		self.Resize = True
	def AbrirProcesarSenal(self,fila,columna):
		idtrama = self.HiloMonitoreo.ListaTramasPorProcesar[fila]
		self.DialogProcesarSenal = DialogProcesarSenal(self,idtrama)
		self.DialogProcesarSenal.show()
		if not self.SonidoAlarmaNueva.isFinished():
			self.SonidoAlarmaNueva.stop()

	def AbrirProcesarSenalPendiente(self,fila,columna):
		idtrama = self.HiloMonitoreo.ListaTramasPendientes[fila]
		self.DialogProcesarSenal = DialogProcesarSenal(self,idtrama)
		self.DialogProcesarSenal.show()
		if not self.SonidoAlarmaNueva.isFinished():
			self.SonidoAlarmaNueva.stop()

	def AbrirDetalleSenalProcesada(self,fila,columna):
		idtrama = self.HiloMonitoreo.ListaTramasProcesadas[fila]
		cuentaynombre = self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.item(fila,0).text() + ' - ' + self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.item(fila,1).text()
		evento = self.SubVentanaMonitoreo.tableWidget_SenalesProcesadas.item(fila,2).text()
		self.DialogDetalleSenal = DialogDetalleSenal(self,idtrama,cuentaynombre,evento)
		self.DialogDetalleSenal.show()



	def closeEvent(self,event):
		self.HiloMonitoreo.terminate()
		self.SonidoAlarmaNueva.stop()
		del self.SonidoAlarmaNueva
		self.SonidoAlarmaPendiente.stop()
		del self.SonidoAlarmaPendiente
		del self.HiloMonitoreo
		self.HiloTiempos.terminate()
		del self.HiloTiempos
		event.accept()

	def ModoPauseFunction(self):
		if self.ModoPause == False:
			self.emit(QtCore.SIGNAL("signalModoPause"))
			self.ModoPause = True
			self.SubVentanaMonitoreo.pushButton_Pause.setIcon(self.iconoplay)
			self.SubVentanaMonitoreo.frame_ModoPause.show()
		else:
			self.emit(QtCore.SIGNAL("signalModoNormal"))
			self.ModoPause = False
			self.SubVentanaMonitoreo.pushButton_Pause.setIcon(self.iconopause)
			self.SubVentanaMonitoreo.frame_ModoPause.hide()


	def ModoSilenciarFunction(self):
		if self.ModoSilenciar == False:
			#self.emit(QtCore.SIGNAL("signalModoPause"))
			self.ModoSilenciar = True
			self.SubVentanaMonitoreo.pushButton_Silenciar.setIcon(self.iconosonidoact)
		else:
			#self.emit(QtCore.SIGNAL("signalModoNormal"))
			self.ModoSilenciar = False

			self.SubVentanaMonitoreo.pushButton_Silenciar.setIcon(self.iconosonidodesact)

		print self.ModoSilenciar

	def ActivarSonidoAlarmaNueva(self):
		if self.SonidoAlarmaNueva.isFinished():
			self.SonidoAlarmaNueva.setLoops(-1)
			self.SonidoAlarmaNueva.play()

	def ActivarSonidoAlarmaPendiente(self):
		if self.SonidoAlarmaPendiente.isFinished():
			self.SonidoAlarmaPendiente.setLoops(-1)
			self.SonidoAlarmaPendiente.play()

class HiloMonitoreo(QtCore.QThread):
	def __init__(self,parent,tablasenalesporprocesar,tablasenalespendientes,tablatodaslassenales,tablasenalesprocesadas):
		QtCore.QThread.__init__(self)
		self.parent = parent
		self.tablasenalesporprocesar = tablasenalesporprocesar
		self.tablasenalespendientes = tablasenalespendientes
		self.tablatodaslassenales = tablatodaslassenales
		self.tablasenalesprocesadas = tablasenalesprocesadas

		self.EstatusMonitoreo = 1
		self.SenalesPorProcesar = False
		self.SenalesEnEspera = False

		self.connect(self.parent, QtCore.SIGNAL("signalModoPause"), self.ActivarModoPause)
		self.connect(self.parent, QtCore.SIGNAL("signalModoNormal"), self.ActivarModoNormal)
 ###Senales para que la Base de datos busque segun el tab seleccionado ###
		self.connect(self.parent, QtCore.SIGNAL("SenalesPorProcesar"), self.BuscarPorProcesarFunction)
		self.connect(self.parent, QtCore.SIGNAL("SenalesPendientes"), self.BuscarPendientesFunction)
		self.connect(self.parent, QtCore.SIGNAL("TodasLasSenales"), self.BuscarTodasLasSenalesFunction)
		self.connect(self.parent, QtCore.SIGNAL("SenalesProcesadas"), self.BuscasProcesadasFunction)

		self.DesactivarBusquedaSenales() #Por defecto para que cuando cargue el tab busque solo las por procesar
		self.BuscarPorProcesar = True
		
		#Lista Para saber cuando una Trama por procesar es Nueva
		self.ListaTramasPorProcesarOld = []
		self.ListaTramasPorProcesar = []
		self.ListaTramasPendientes = []
		self.ListaTramasProcesadas = []
	def BuscarPorProcesarFunction(self):
		#Se usaba para que buscara las senales por procesar
		#self.DesactivarBusquedaSenales()
		#self.BuscarPorProcesar = True
		pass

	def BuscarPendientesFunction(self):
		self.DesactivarBusquedaSenales()
		self.BuscarPendientes = True

	def BuscarTodasLasSenalesFunction(self):
		self.DesactivarBusquedaSenales()
		self.BuscarTodasLasSenales = True

	def BuscasProcesadasFunction(self):
		self.DesactivarBusquedaSenales()
		self.BuscarProcesadas = True

	def DesactivarBusquedaSenales(self):
		self.BuscarPorProcesar = False
		self.BuscarPendientes = False
		self.BuscarTodasLasSenales = False
		self.BuscarProcesadas = False

	def ActivarModoPause(self):
		self.EstatusMonitoreo = 3
	def ActivarModoNormal(self):
		self.EstatusMonitoreo = 2


	def ConectarBD(self):
		try:
			self.BD = BasedeDatos()
			self.BD.Conectar()
		except:
			del self.BD
			self.ConectarBD()
			time.sleep(5)

	def DepurarDictSenales(self):
		TramasPorEliminar = []
		for idtrama in globalvars.DictSenales:
			if not str(idtrama) in self.ListaTramasPorProcesar and not str(idtrama) in self.ListaTramasPendientes:
				TramasPorEliminar.append(str(idtrama))

		for tramadel in TramasPorEliminar:
			del globalvars.DictSenales[tramadel]

		print str(self.ListaTramasPorProcesar) +' Por Procesar'
		print str(self.ListaTramasPendientes) +' Pendientes'
		print str(TramasPorEliminar) + ' Por Eliminar'


	def CargarSenalesPorProcesar(self):
		#self.parent.ArreglarTamanoTablas()
		print 'Buscando Senales por Procesar'
		#Buscar las senales por procesar por primera vez
		
		try:
			ResultadoTPP = self.BD.Querys('TramasPorProcesarOperador',globalvars.DatosUsuario['IDPersonal'])
		except:
			self.BD.Desconectar()
			self.ConectarBD()
			self.CargarSenalesPorProcesar()

		rows = len(ResultadoTPP)
		self.tablasenalesporprocesar.setRowCount(rows)
		fila = 0
		columna = 0


		self.ListaTramasPorProcesar = []

		for signalpp in ResultadoTPP:
			columna = 0
			globalvars.DictSenales[str(signalpp.id_trama)] = {'prefijocuenta':signalpp.cuen,'idcliente':signalpp.id_cliente, 'nombrecliente':signalpp.NameCliente, 'zonausuario':signalpp.UserZona, 'fecha':signalpp.fecha, 'webcolor': signalpp.web_color, 'idtrama' : signalpp.id_trama, 'webcolorbackground':signalpp.web_colorBg, 'protocolo':signalpp.protocolo,  'linea':signalpp.Linea, 'descripcion' : signalpp.descrip, 'tipoevento':signalpp.type_evento, 'evento':signalpp.evento, 'cliente' : signalpp.cliente, 'variante':signalpp.Variante, 'color':signalpp.color, 'colorBg':signalpp.colorBg, 'obsevacion':signalpp.Obser, 'idgrupo' :signalpp.idGrupo, 'status':signalpp.status, 'idempresa':signalpp.id_empresa,'direccion':signalpp.direccion,'referencia':signalpp.referencia,'latitud':signalpp.latitud,'longitud':signalpp.longitud,'clavemaster':signalpp.clavemaster,'idtipocliente':signalpp.id_type_cliente,'imagentipocliente':signalpp.img,'telefonolocal':signalpp.telf_local,'imagencliente':signalpp.pic,'codigoalarma':signalpp.codAlrm,'descripcioncodigoalarma':signalpp.codDesc,'estatuspanel':signalpp.staPanel,'fechastatus':signalpp.fechaStatusp,'nombreempresa':signalpp.nombreempresa,'movil':signalpp.movil,'descripcionevento':signalpp.StrEvento,'numzonauser':signalpp.numzonausuario,'tipoevent':signalpp.tipoevent,'llave':signalpp.llave,'correo':signalpp.email}
			for signal in signalpp:
				#print signal
				#print type(signal)
				if columna <= 4:
					if signal == None:
						signal = ''
					else:
						#if columna > 0 and columna < 3:
						#	signal = signal.encode('latin-1')
						if columna == 4:
							signal = signal.strftime("%d %b %Y %H:%M:%S")
						if type(signal) == int:
							signal = str(signal)
					texto = QtGui.QTableWidgetItem(signal)
					self.tablasenalesporprocesar.setItem(fila,columna,texto)
				elif columna == 5:
					colorfila = QtGui.QColor(str(signal))
					for columnacolor in range(5):
						self.tablasenalesporprocesar.item(fila,columnacolor).setTextColor(colorfila)
				elif columna == 6:
					self.ListaTramasPorProcesar.append(str(signal))
				else:
					break
				columna = columna + 1
			fila = fila + 1

		if ResultadoTPP:
			self.SenalesPorProcesar = True
		else:
			self.SenalesPorProcesar = False

		if self.ListaTramasPorProcesar:
			#for tramacomp in self.ListaTramasPorProcesar:
			#	if tramacomp in self.ListaTramasPorProcesarOld:
			#		pass
			#	else:
			if self.parent.ProcesandoSenal == False:
				self.parent.ActivarSonidoAlarmaNueva()
				pass
		else:
			if "self.SonidoAlarmaNueva" in locals():
				if not self.SonidoAlarmaNueva.isFinished():
					self.parent.SonidoAlarmaNueva.stop()

		self.ListaTramasPorProcesarOld = self.ListaTramasPorProcesar


	def CargarSenalesPendientes(self):
		print 'Buscando Senales Pendientes'
		#Buscar las senales por procesar por primera vez
		try:
			ResultadoTP = self.BD.Querys('TramasPendientesOperador',globalvars.DatosUsuario['IDPersonal'])
		except:
			self.BD.Desconectar()
			self.ConectarBD()
			self.CargarSenalesPendientes()
		rows = len(ResultadoTP)
		self.tablasenalespendientes.setRowCount(rows)
		fila = 0
		columna = 0

		self.ListaTramasPendientes = []

		for signalpp in ResultadoTP:
			columna = 0
			globalvars.DictSenales[str(signalpp.id_trama)] = {'prefijocuenta':signalpp.cuen,'idcliente':signalpp.id_cliente, 'nombrecliente':signalpp.NameCliente, 'zonausuario':signalpp.UserZona, 'fecha':signalpp.fecha, 'webcolor': signalpp.web_color, 'idtrama' : signalpp.id_trama, 'webcolorbackground':signalpp.web_colorBg, 'protocolo':signalpp.protocolo,  'linea':signalpp.Linea, 'descripcion' : signalpp.descrip, 'tipoevento':signalpp.type_evento, 'evento':signalpp.evento, 'cliente' : signalpp.cliente, 'variante':signalpp.Variante, 'color':signalpp.color, 'colorBg':signalpp.colorBg, 'obsevacion':signalpp.Obser, 'idgrupo' :signalpp.idGrupo, 'status':signalpp.status, 'idempresa':signalpp.id_empresa,'direccion':signalpp.direccion,'referencia':signalpp.referencia,'latitud':signalpp.latitud,'longitud':signalpp.longitud,'clavemaster':signalpp.clavemaster,'idtipocliente':signalpp.id_type_cliente,'imagentipocliente':signalpp.img,'telefonolocal':signalpp.telf_local,'imagencliente':signalpp.pic,'codigoalarma':signalpp.codAlrm,'descripcioncodigoalarma':signalpp.codDesc,'estatuspanel':signalpp.staPanel,'fechastatus':signalpp.fechaStatusp,'nombreempresa':signalpp.nombreempresa,'movil':signalpp.movil,'descripcionevento':signalpp.StrEvento,'numzonauser':signalpp.numzonausuario,'tipoevent':signalpp.tipoevent,'llave':signalpp.llave,'correo':signalpp.email}
			for signal in signalpp:
				#print signal
				#print type(signal)
				if columna <= 4:
					if signal == None:
						signal = ''
					else:
						if columna > 0 and columna < 3:
							signal = signal.encode('latin-1')
						if columna == 4:
							signal = signal.strftime("%d %b %Y %H:%M:%S")
						if type(signal) == int:
							signal = str(signal)
					texto = QtGui.QTableWidgetItem(signal)
					self.tablasenalespendientes.setItem(fila,columna,texto)
				elif columna == 5:
					colorfila = QtGui.QColor(str(signal))
					for columnacolor in range(5):
						self.tablasenalespendientes.item(fila,columnacolor).setTextColor(colorfila)
				elif columna == 6:
					self.ListaTramasPendientes.append(str(signal))
				else:
					break
				columna = columna + 1
			fila = fila + 1

		if ResultadoTP:
			self.SenalesEnEspera = True
		else:
			self.SenalesEnEspera = False

	def CargarLogSenales(self):
		print 'Buscando Log Senales'
		#Buscar las senales por procesar por primera vez
		

		try:
			ResultadoLS = self.BD.Querys('MonitoreoEstatico',str(globalvars.DatosUsuario['IDEmpresa']))
		except:
			self.BD.Desconectar()
			self.ConectarBD()
			self.CargarLogSenales()

		rows = len(ResultadoLS)
		self.tablatodaslassenales.setRowCount(rows)
		fila = 0
		columna = 0
		for signalpp in ResultadoLS:
			columna = 0
			for signal in signalpp:
				#print signal
				#print type(signal)
				if columna <= 4:
					if signal == None:
						signal = ''
					else:
						if columna > 0 and columna < 3:
							signal = signal
						if columna == 4:
							signal = signal.strftime("%d %b %Y %H:%M:%S")
						if type(signal) == int:
							signal = str(signal)
					texto = QtGui.QTableWidgetItem(signal)
					self.tablatodaslassenales.setItem(fila,columna,texto)
				elif columna == 5:
					colorfila = QtGui.QColor(str(signal))
					for columnacolor in range(5):
						self.tablatodaslassenales.item(fila,columnacolor).setTextColor(colorfila)
				else:
					break
				columna = columna + 1
			fila = fila + 1

	def CargarProcesadas(self):
		print 'Buscando Senales Procesadas'
		#Buscar las senales por procesar por primera vez
		
		try:
			ResultadoSP = self.BD.Querys('TramasProcesadas',str(globalvars.DatosUsuario['IDEmpresa']))
		except:
			self.BD.Desconectar()
			self.ConectarBD()
			self.CargarProcesadas()		




		rows = len(ResultadoSP)
		self.tablasenalesprocesadas.setRowCount(rows)
		fila = 0
		columna = 0

		self.ListaTramasProcesadas = []

		for signalpp in ResultadoSP:
			columna = 0
			for signal in signalpp:
				#print signal
				#print type(signal)
				if columna <= 6:
					if signal == None:
						signal = ''
					else:
						if columna > 0 and columna < 3:
							signal = signal.encode('latin-1')
						if columna == 5 or columna == 6:
							signal = signal.strftime("%d %b %Y %H:%M:%S")
						if type(signal) == int:
							signal = str(signal)
						texto = QtGui.QTableWidgetItem(signal)
						self.tablasenalesprocesadas.setItem(fila,columna,texto)

				elif columna == 7:
					colorfila = QtGui.QColor(str(signal))
					for columnacolor in range(7):
						self.tablasenalesprocesadas.item(fila,columnacolor).setTextColor(colorfila)
				elif columna == 8:
					self.ListaTramasProcesadas.append(str(signal))
				else:
					break
				columna = columna + 1
			fila = fila + 1

	def ValidarExistenciaOperadorSession(self):
		ExisteOperadorSession = self.BD.Querys('ComprobarExisteOperadorSession',str(globalvars.DatosUsuario['IDPersonal']))
		if not ExisteOperadorSession:
			if globalvars.IPPublica:
				self.BD.Querys('InsertarOperadorSession',str(globalvars.DatosUsuario['IDPersonal']),str(globalvars.DatosUsuario['IDPersonal']),globalvars.IPPublica,'1','1')
			else:
				self.BD.Querys('InsertarOperadorSession',str(globalvars.DatosUsuario['IDPersonal']),str(globalvars.DatosUsuario['IDPersonal']),globalvars.IPLocal,'1','1')

			
	def EnviarHeartBeat(self):
		if globalvars.IPPublica:
			self.BD.Querys('ActualizarHeartBeatOperador',globalvars.IPPublica,str(self.EstatusMonitoreo),str(globalvars.DatosUsuario['IDPersonal']))
		else:
			self.BD.Querys('ActualizarHeartBeatOperador',globalvars.IPLocal,str(self.EstatusMonitoreo),str(globalvars.DatosUsuario['IDPersonal']))
		

	def ActualizarFechaDesocupado(self):
		if self.EstatusMonitoreo == 2:
			if not self.SenalesPorProcesar and not self.SenalesEnEspera:
				self.EstatusMonitoreo = 1

				self.BD.Querys('ActualizarFechaDesocupado',str(globalvars.DatosUsuario['IDPersonal']))
		elif self.EstatusMonitoreo == 1:
			if self.SenalesPorProcesar or self.SenalesEnEspera:
				self.EstatusMonitoreo = 2


	def Iniciar(self):
		self.ConectarBD()
		self.ValidarExistenciaOperadorSession()




		
		try:
			while True:
				#if self.BuscarPorProcesar:
				self.CargarSenalesPorProcesar()
				self.DepurarDictSenales()
				if self.BuscarPendientes:
					self.CargarSenalesPendientes()
					self.DepurarDictSenales()
				time.sleep(0.5)
				self.ActualizarFechaDesocupado()
				time.sleep(0.5)
				self.EnviarHeartBeat()
				time.sleep(0.5)
				if self.BuscarTodasLasSenales:
					self.CargarLogSenales()
					time.sleep(0.5)
				if self.BuscarProcesadas:
					self.CargarProcesadas()
					time.sleep(0.5)
		except:
			self.BD.Desconectar()
			self.ConectarBD()
			self.Iniciar()		




	def run(self):
		self.Iniciar()

class HiloTimers(QtCore.QThread):
	def __init__(self,parent):
		QtCore.QThread.__init__(self)
		self.parent = parent

		self.TiempoHombreMuerto = QtCore.QTimer(self)
		if globalvars.DatosUsuario['TiempoHM'] == 'None' or globalvars.DatosUsuario['TiempoHM'] == '':
			globalvars.DatosUsuario['TiempoHM'] == 500000
		self.TiempoHombreMuerto.setInterval(int(globalvars.DatosUsuario['TiempoHM']))


		self.TiempoAlertaPendientes = QtCore.QTimer(self)
		if globalvars.DatosUsuario['TiempoAlerta'] == 'None' or globalvars.DatosUsuario['TiempoAlerta'] == '':
			globalvars.DatosUsuario['TiempoAlerta'] == 500000
		self.TiempoAlertaPendientes.setInterval(int(globalvars.DatosUsuario['TiempoAlerta']))

		self.TiempoNotificacionHM = QtCore.QTimer(self)
		if globalvars.DatosUsuario['TiempoNotificacionHM'] == 'None' or globalvars.DatosUsuario['TiempoNotificacionHM'] == '':
			globalvars.DatosUsuario['TiempoNotificacionHM'] == 1000000
		self.TiempoNotificacionHM.setInterval(int(globalvars.DatosUsuario['TiempoNotificacionHM']))


		self.connect(self.TiempoHombreMuerto, QtCore.SIGNAL("timeout()"), self.TimeoutHombreMuerto)
		self.connect(self.TiempoAlertaPendientes, QtCore.SIGNAL("timeout()"), self.TimeoutPendientes)
		self.connect(self.TiempoNotificacionHM, QtCore.SIGNAL("timeout()"), self.TimeoutNotificacionHombreMuerto)

		self.connect(self.parent, QtCore.SIGNAL("IniciarTempHM"), self.IniciarTempHombreMuerto)
		self.connect(self.parent, QtCore.SIGNAL("IniciarTempPendientes"), self.IniciarTempPendientes)
		self.connect(self.parent, QtCore.SIGNAL("IniciarTempNotificarHM"), self.IniciarTempNotificacionHM)

		#self.connect(self.parent, QtCore.SIGNAL("DetenerTempHM"), self.DetenerTempHombreMuerto)
		#self.connect(self.parent, QtCore.SIGNAL("DetenerTempPendientes"), self.DetenerTempPendientes)
		#self.connect(self.parent, QtCore.SIGNAL("DetenerTempNotificarHM"), self.DetenerTempNotificacionHM)
		self.DialogHombreMuerto = None

	def IniciarTempHombreMuerto(self):
		if int(globalvars.DatosUsuario['TiempoHM']) != 0:
			self.TiempoHombreMuerto.start()
	def IniciarTempPendientes(self):
		#if int(globalvars.DatosUsuario['TiempoAlerta']) != 0:
		#	self.TiempoAlertaPendientes.start()
		pass
	def IniciarTempNotificacionHM(self):
		#if int(globalvars.DatosUsuario['TiempoNotificacionHM']) != 0:
		#	self.TiempoNotificacionHM.start()
		pass
	def DetenerTempHombreMuerto(self):
		#if int(globalvars.DatosUsuario['TiempoHM']) != 0:
		#	self.TiempoHombreMuerto.stop()
		pass
	def DetenerTempPendientes(self):
		#if int(globalvars.DatosUsuario['TiempoAlerta']) != 0:
		#	self.TiempoAlertaPendientes.stop()
		pass
	def DetenerTempNotificacionHM(self):
		#if int(globalvars.DatosUsuario['TiempoNotificacionHM']) != 0:
		#	self.TiempoNotificacionHM.stop()
		pass
	def TimeoutHombreMuerto(self):
		if self.DialogHombreMuerto ==  None:
			self.DialogHombreMuerto = DialogHombreMuerto(self.parent,self)
			self.DialogHombreMuerto.exec_()
			#self.DialogHombreMuerto.show()

	def TimeoutPendientes(self):
		print 'TimeoutPendientes'

	def TimeoutNotificacionHombreMuerto(self):
		print 'TimeoutNOTIFI'

	def run(self):
		print 'Inicieeeeeeeeeeeeeeeee'

