# -*- coding: latin1 -*-
### Solo para las conversiones de la interfaz ###
from PyQt4 import QtGui, QtCore, QtWebKit
import datetime, time, re
from functools import partial

from QTSubVentanaNuevoGrupoClientes import Ui_SubVentanaNuevoGrupoClientes
from QTSubVentanaGrupoClientes import Ui_SubVentanaGruposdeClientes
from QTDialogConfigurarAccesoWebClientes import Ui_Dialog_ConfigurarDatosLoginWebUsuarios
from QTSubVentanaVehiculos import Ui_SubVentanaVehiculos
from QTSubVentanaEnvioSMS import Ui_SubVentanaEnvioSMS

from QTDialogCuentasGrupo import Ui_DialogCuentasGrupo

import globalvars 


############ CONFIGURACIONES ###############








from QTSubVentanaDiasFeriados import Ui_SubVentanaDiasFeriados


################# REPORTES ###################





################## REPORTES PROGRAMACION #######################################



##################################################################################




class SubVentanaDiasFeriados(QtGui.QWidget):
	def __init__(self):
		super(SubVentanaDiasFeriados, self).__init__()
		self.SubVentanaDiasFeriados = Ui_SubVentanaDiasFeriados()
		self.SubVentanaDiasFeriados.setupUi(self)

class DialogConfigurarDatosLoginWebUsuarios(QtGui.QWidget):
	def __init__(self):
		super(DialogConfigurarDatosLoginWebUsuarios, self).__init__()
		self.DialogConfigurarDatosLoginWebUsuarios = Ui_Dialog_ConfigurarDatosLoginWebUsuarios()
		self.DialogConfigurarDatosLoginWebUsuarios.setupUi(self)

class SubVentanaVehiculos(QtGui.QWidget):
	def __init__(self):
		super(SubVentanaVehiculos, self).__init__()
		self.SubVentanaVehiculos = Ui_SubVentanaVehiculos()
		self.SubVentanaVehiculos.setupUi(self)

###################################################################################



class SubVentanaGruposdeClientes(QtGui.QWidget):
	def __init__(self):
		super(SubVentanaGruposdeClientes, self).__init__()
		self.SubVentanaGruposdeClientes = Ui_SubVentanaGruposdeClientes()
		self.SubVentanaGruposdeClientes.setupUi(self)
		self.iconaddtogroup = QtGui.QIcon()
		self.iconaddtogroup.addPixmap(QtGui.QPixmap(":/iconos/ico/Box Add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		
		self.ListarGruposClientes()
		self.connect(self.SubVentanaGruposdeClientes.pushButton_AgregarGrupoCliente, QtCore.SIGNAL("clicked()"), self.AgregarGrupo)
		#Busqueda
		self.connect(self.SubVentanaGruposdeClientes.lineEdit_Buscar, QtCore.SIGNAL("textEdited(const QString&)"), self.BuscarGrupos)
		
		#Acomodar Tablas
		self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.verticalHeader().setVisible(False)
		self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.setShowGrid(False)
		self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.setAlternatingRowColors(True)
		#self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.resizeColumnsToContents()
		self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.verticalHeader().setDefaultSectionSize(26)
		self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.setSortingEnabled(False)
		self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
	
		self.Resize1 =  False
		self.Resize = False	
		self.installEventFilter(self)

		self.CargarTablasEstaticamente()

	def CargarTablasEstaticamente(self):

		self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.setColumnWidth(0,100)
		self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.setColumnWidth(1,100)
		self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.setColumnWidth(2,100)
		self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.setColumnWidth(3,100)

	def eventFilter(self, source, event):
		if event.type() == QtCore.QEvent.WindowStateChange:
			self.ArreglarTamanoTablas()
		return QtGui.QWidget.eventFilter(self, source, event)
	def resizeEvent(self,resizeEvent):
		if self.Resize1 == True:
			self.ArreglarTamanoTablas()
		self.Resize1 = True
		pass

	def ArreglarTamanoTablas(self):

		if self.Resize == True:
			self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.setColumnWidth(0,self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.width()/2.9)
			self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.setColumnWidth(1,self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.width()/2.9)
			self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.setColumnWidth(2,self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.width()/10)
			self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.setColumnWidth(3,self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.width()/5)
			
		self.Resize = True
	def BuscarGrupos(self,busqueda=""):
		self.ListarGruposClientes()
		busqueda = self.SubVentanaGruposdeClientes.lineEdit_Buscar.text()
		#print busqueda
		#for letra in busqueda:
		ResultadoBusqueda = self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.findItems(busqueda,QtCore.Qt.MatchContains)
		#print ResultadoBusqueda
		#for i in ResultadoBusqueda:
			#print i.text()
		listafilasresultado = []
		for r in ResultadoBusqueda:
			listafilasresultado.append(self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.row(r))
		#print listafilasresultado
		filasentotal = self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.rowCount()
		for eliminar in reversed(range(filasentotal)):
				if eliminar in listafilasresultado:
					pass
				else:
					self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.removeRow(eliminar)
	def AgregarGrupo(self):
		self.emit(QtCore.SIGNAL("signalAbrirAgregarGrupo"),self)

	def ListarGruposClientes(self):
		Resultado = globalvars.BD.Querys('DatosAsociados',globalvars.DatosUsuario['IDEmpresa'])
		rows = len(Resultado)
		self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.setRowCount(rows)
		fila = 0
		columna = 0
		self.filaboton = {}
		filadict = {}
		#print Resultado
		for asoc in Resultado:
			columna = 0
			for item in asoc:
				if columna <= 2:
					#print type(item)

					if item == None:
						item = '-----'
					elif item == True:
						item = 'Activo'
					elif item == False:
						item = 'No Activo'
					#else:
						#item = item.encode('latin-1')
					texto = QtGui.QTableWidgetItem(str(item))
					self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.setItem(fila,columna,texto)
					columna = columna + 1
				elif columna == 3:
					ResultadoQtyAsoAbo = globalvars.BD.Querys('CantidadAsociadosAbonados',item,globalvars.DatosUsuario['IDEmpresa'])
					texto = 'Cuentas: ' + str(ResultadoQtyAsoAbo[0][0])
					btn = QtGui.QPushButton(self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes)
					btn.setText(texto)
					btn.setIcon(self.iconaddtogroup)
					btn.setFlat(True)
					self.filaboton[fila] = btn
					filadict[fila] = fila
					self.SubVentanaGruposdeClientes.tableWidget_ListaGrupoClientes.setCellWidget(fila, columna, btn)
					columna = columna + 1
					self.filaboton[fila].clicked.connect(partial(self.AbrirCuentaGrupo,item))

				else:
					pass
			fila = fila + 1
	def AbrirCuentaGrupo(self,idasociado):

		self.emit(QtCore.SIGNAL("signalAbrirCuentasGrupo"),self,idasociado)
		
class DialogCuentasGrupo(QtGui.QDialog):
	def __init__(self,parent,idgrupo):
		super(DialogCuentasGrupo, self).__init__()
		self.parent = parent
		self.DialogCuentasGrupo = Ui_DialogCuentasGrupo()
		self.DialogCuentasGrupo.setupUi(self)
		self.idgrupo = idgrupo
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

		self.iconadd = QtGui.QIcon()
		self.iconadd.addPixmap(QtGui.QPixmap(":/iconos/ico/Glyph Add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

		self.iconremove = QtGui.QIcon()
		self.iconremove.addPixmap(QtGui.QPixmap(":/iconos/ico/Glyph Remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

		#Lista de Abonados a Guardar
		self.AbonadosAGuardarGrupo=[]

		#Acomodamos la Tabla de Los clientes
		self.DialogCuentasGrupo.tableWidget_ElegirAbonados.verticalHeader().setVisible(False)
		self.DialogCuentasGrupo.tableWidget_ElegirAbonados.setShowGrid(False)
		self.DialogCuentasGrupo.tableWidget_ElegirAbonados.setAlternatingRowColors(True)
		self.DialogCuentasGrupo.tableWidget_ElegirAbonados.resizeColumnsToContents()
		self.DialogCuentasGrupo.tableWidget_ElegirAbonados.verticalHeader().setDefaultSectionSize(26)
		self.DialogCuentasGrupo.tableWidget_ElegirAbonados.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

		self.header = self.DialogCuentasGrupo.tableWidget_ElegirAbonados.horizontalHeader()
		self.DialogCuentasGrupo.tableWidget_ElegirAbonados.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows);
		self.header.setResizeMode(QtGui.QHeaderView.Stretch)
		Resultado = globalvars.BD.Querys('AbonadosSinGrupo',self.idgrupo)
		lista = []
		for u in range(len(Resultado)):
			for i in Resultado[u]:
				lista.append(i)
		self.listadeclientes = [x.encode('latin-1') if isinstance(x, unicode) else x for x in lista]

		#Senales
		#Para Busqueda
		self.connect(self.DialogCuentasGrupo.pushButton_Buscar, QtCore.SIGNAL("clicked()"), self.BuscarClientes)

		#self.connect(self.DialogCuentasGrupo.lineEdit_Buscar, QtCore.SIGNAL("textEdited(const QString&)"), self.BuscarClientes)
		#Para Guardar
		self.connect(self.DialogCuentasGrupo.pushButton_Guardar, QtCore.SIGNAL("clicked()"), self.GuardarCambios)
		self.connect(self.DialogCuentasGrupo.pushButton_Cancelar, QtCore.SIGNAL("clicked()"), self.Cancelar)

		self.ListarClientesAsociados()
		self.ListarClientes(self.listadeclientes)



	def ListarClientes(self,datos=[]):

		rows = len(datos) / 3
		self.DialogCuentasGrupo.tableWidget_ElegirAbonados.setRowCount(rows)
		fila = 0
		columna = 0
		#Variable creada para concatenar Abonado y Nombre y pasarlo asi.
		filaboton = {}
		for item in datos:
			if item == None:
				item = ''
			texto = QtGui.QTableWidgetItem(str(item))
			self.DialogCuentasGrupo.tableWidget_ElegirAbonados.setItem(fila,columna,texto)
			#Para agregar el Boton en la tercera fila con el evento de que envie por parametros el abonado
			if columna == 0:
				btn = QtGui.QPushButton(self.DialogCuentasGrupo.tableWidget_ElegirAbonados)
				btn.setText("Agregar")
				btn.setIcon(self.iconadd)
				btn.setFlat(True)
				filaboton[fila] = btn
				self.DialogCuentasGrupo.tableWidget_ElegirAbonados.setCellWidget(fila, (columna+2), btn)
			if columna == 2:
				filaboton[fila].clicked.connect(partial(self.AgregarAbonado,item))
			columna = columna + 1
			if columna == 3:
				fila = fila + 1
				columna = 0
		#self.DialogCuentasGrupo.tableWidget_ElegirAbonados.resizeColumnsToContents()

	def ListarClientesAsociados(self):
		self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados.verticalHeader().setVisible(False)
		self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados.setShowGrid(False)
		self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados.setAlternatingRowColors(True)
		self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados.resizeColumnsToContents()
		self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados.verticalHeader().setDefaultSectionSize(26)
		self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados.setSortingEnabled(False)
		self.header = self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados.horizontalHeader()
		self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows);
		self.header.setResizeMode(QtGui.QHeaderView.Stretch)

		Resultado = globalvars.BD.Querys('AbonadosEnGrupo',self.idgrupo)
		lista = []
		for u in range(len(Resultado)):
			for i in Resultado[u]:
				lista.append(i)
		self.listadeclientesasociados = [x.encode('latin-1') if isinstance(x, unicode) else x for x in lista]
		rows = len(self.listadeclientesasociados) / 3
		self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados.setRowCount(rows)
		fila = 0
		columna = 0
		#Variable creada para concatenar Abonado y Nombre y pasarlo asi.
		filaboton = {}
		for index, item in enumerate(self.listadeclientesasociados):
			if item == None:
				item = ''
			texto = QtGui.QTableWidgetItem(str(item))
			self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados.setItem(fila,columna,texto)
			#Para agregar el Boton en la tercera fila con el evento de que envie por parametros el abonado
			if columna == 0:
				btn = QtGui.QPushButton(self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados)
				btn.setText("Quitar")
				btn.setIcon(self.iconremove)
				btn.setFlat(True)
				filaboton[fila] = btn
				self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados.setCellWidget(fila, (columna+2), btn)
			if columna == 2:
				self.AbonadosAGuardarGrupo.append(item)
				btn.clicked.connect(partial(self.QuitarAbonado,item))
			columna = columna + 1
			if columna == 3:	
				fila = fila + 1
				columna = 0

	def AgregarAbonado(self,abonado):
		abonado = str(abonado)
		self.AbonadosAGuardarGrupo.append(int(abonado))
		#Eliminamos el Abonado de la Lista General
		ResultadoBusqueda = self.DialogCuentasGrupo.tableWidget_ElegirAbonados.findItems(abonado,QtCore.Qt.MatchExactly)
		Fila = self.DialogCuentasGrupo.tableWidget_ElegirAbonados.row(ResultadoBusqueda[0])
		AbonadoNombre = []
		for i in range(2):
			items = self.DialogCuentasGrupo.tableWidget_ElegirAbonados.item(Fila,i)
			texto = items.text()
			AbonadoNombre.append(texto)
		self.DialogCuentasGrupo.tableWidget_ElegirAbonados.removeRow(Fila)
		#Lo agregamos a la Lista de Seleccionados
		fila = 0
		columna = 0
		self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados.insertRow(0)
		AbonadoNombreLatin1 = [x.encode('latin-1') if isinstance(x, unicode) else x for x in AbonadoNombre]
		filaboton = {}
		for item in AbonadoNombreLatin1:
			if item == None:
				item = ''
			texto = QtGui.QTableWidgetItem(item)
			self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados.setItem(fila,columna,texto)
			#Para agregar el Boton en la tercera fila con el evento de que envie por parametros el abonado
			if columna == 0:
				btn = QtGui.QPushButton(self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados)
				btn.setText("Quitar")
				filaboton[fila] = btn
				self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados.setCellWidget(fila, (columna+2), btn)
				filaboton[fila].clicked.connect(partial(self.QuitarAbonado,item))
			columna = columna + 1
			if columna == 2:
				fila = fila + 1
				columna = 0

	def QuitarAbonado(self,abonado):
		abonado = str(abonado)
		self.AbonadosAGuardarGrupo.remove(int(abonado))
		#Eliminamos el Abonado de la Lista General
		ResultadoBusqueda = self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados.findItems(abonado,QtCore.Qt.MatchExactly)
		Fila = self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados.row(ResultadoBusqueda[0])
		AbonadoNombre = []
		for i in range(2):
			items = self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados.item(Fila,i)
			texto = items.text()
			AbonadoNombre.append(texto)
		self.DialogCuentasGrupo.tableWidget_AbonadosSeleccionados.removeRow(Fila)
		#Lo agregamos a la Lista de Seleccionados
		fila = 0
		columna = 0
		self.DialogCuentasGrupo.tableWidget_ElegirAbonados.insertRow(0)
		AbonadoNombreLatin1 = [x.encode('latin-1') if isinstance(x, unicode) else x for x in AbonadoNombre]
		filaboton = {}
		for item in AbonadoNombreLatin1:
			if item == None:
				item = ''
			texto = QtGui.QTableWidgetItem(item)
			self.DialogCuentasGrupo.tableWidget_ElegirAbonados.setItem(fila,columna,texto)
			#Para agregar el Boton en la tercera fila con el evento de que envie por parametros el abonado
			if columna == 0:
				btn = QtGui.QPushButton(self.DialogCuentasGrupo.tableWidget_ElegirAbonados)
				btn.setText("Agregar")
				filaboton[fila] = btn
				self.DialogCuentasGrupo.tableWidget_ElegirAbonados.setCellWidget(fila, (columna+2), btn)
				filaboton[fila].clicked.connect(partial(self.AgregarAbonado,item))
			columna = columna + 1
			if columna == 2:
				fila = fila + 1
				columna = 0
	def BuscarClientes(self,busqueda=""):
		self.ListarClientes(self.listadeclientes)
		busqueda = self.DialogCuentasGrupo.lineEdit_Buscar.text()
		#print busqueda
		#for letra in busqueda:
		ResultadoBusqueda = self.DialogCuentasGrupo.tableWidget_ElegirAbonados.findItems(busqueda,QtCore.Qt.MatchContains)
		#print ResultadoBusqueda
		#for i in ResultadoBusqueda:
			#print i.text()
		listafilasresultado = []
		for r in ResultadoBusqueda:
			listafilasresultado.append(self.DialogCuentasGrupo.tableWidget_ElegirAbonados.row(r))
		#print listafilasresultado
		filasentotal = self.DialogCuentasGrupo.tableWidget_ElegirAbonados.rowCount()
		for eliminar in reversed(range(filasentotal)):
				if eliminar in listafilasresultado:
					pass
				else:
					self.DialogCuentasGrupo.tableWidget_ElegirAbonados.removeRow(eliminar)
	def GuardarCambios(self):
		#Borro Todos los Abonados Asociados
		globalvars.BD.Querys('BorrarAbonadosGrupo',self.idgrupo,globalvars.DatosUsuario['IDEmpresa'])
		#Agrego los Nuevos
		for abonado in self.AbonadosAGuardarGrupo:
			globalvars.BD.Querys('InsertarAbonadosGrupo',self.idgrupo,globalvars.DatosUsuario['IDEmpresa'],str(abonado))
		#Envio Senal para Cerrar
		self.parent.ListarGruposClientes()
		self.emit(QtCore.SIGNAL("signalCerrar"))

	def Cancelar(self):
		#Envio Senal para Cerrar
		self.emit(QtCore.SIGNAL("signalCerrar"))


class SubVentanaNuevoGrupoClientes(QtGui.QWidget):
	def __init__(self,parent):
		super(SubVentanaNuevoGrupoClientes, self).__init__()
		self.SubVentanaNuevoGrupoClientes = Ui_SubVentanaNuevoGrupoClientes()
		self.SubVentanaNuevoGrupoClientes.setupUi(self)
		self.connect(self.SubVentanaNuevoGrupoClientes.pushButton_Agregar, QtCore.SIGNAL("clicked()"), self.GuardarGrupo)
		self.parent = parent
	def GuardarGrupo(self):
		Nombre = str(self.SubVentanaNuevoGrupoClientes.lineEdit_Nombre.text())
		Direccion = str(self.SubVentanaNuevoGrupoClientes.textEdit_Direccion.toPlainText())
		Correo = str(self.SubVentanaNuevoGrupoClientes.lineEdit_Correo.text())
		Telefono = str(self.SubVentanaNuevoGrupoClientes.lineEdit_Telefono.text())
		Usuario = str(self.SubVentanaNuevoGrupoClientes.lineEdit_Usuario.text())
		Clave = str(self.SubVentanaNuevoGrupoClientes.lineEdit_Clave.text())
		Estatus = self.SubVentanaNuevoGrupoClientes.radioButton_Activado.isChecked()

		if Nombre.isalnum():
			if len(Direccion) > 5:
				if Telefono.isdigit() and len(Telefono) > 4:
					if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',Correo.lower()):
						if Usuario.isalnum():
							if Clave.isalnum():
								Resultado = globalvars.BD.Querys('VerificarUsuarioAsociado',Usuario)
								if not Resultado:
									globalvars.BD.Querys('InsertarGrupoClientes',globalvars.DatosUsuario['IDEmpresa'],Nombre,Direccion,Telefono,Correo,Usuario,Clave,Estatus)
									if self.parent:
										self.parent.ListarGruposClientes()
									self.emit(QtCore.SIGNAL("signalCerrar"))
								else:
									QtGui.QMessageBox.warning(self, 'Hay un problema!', "Nombre de Usuario ya existe!")
							else:
								QtGui.QMessageBox.warning(self, 'Hay un problema!', "La clave no debe estar vacia y no debe contener espacios")
						else:
							QtGui.QMessageBox.warning(self, 'Hay un problema!', "El usuario no debe estar vacio y no debe contener espacios")
					else:
						QtGui.QMessageBox.warning(self, 'Hay un problema!', "Correo Electronico no es valido")
				else:
					QtGui.QMessageBox.warning(self, 'Hay un problema!', "El telefono solo debe contener numeros")
			else:
				QtGui.QMessageBox.warning(self, 'Hay un problema!', "La direccion no debe estar vacia")
		else:
			QtGui.QMessageBox.warning(self, 'Hay un problema!', "El nombre no debe estar vacio y no debe contener espacios")


class SubVentanaEnvioSMS(QtGui.QWidget):
	def __init__(self):
		super(SubVentanaEnvioSMS, self).__init__()
		self.SubVentanaEnvioSMS = Ui_SubVentanaEnvioSMS()
		self.SubVentanaEnvioSMS.setupUi(self)


