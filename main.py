# -*- coding: utf-8 -*-



from PyQt4 import QtGui, QtCore
from QTMain import Ui_QMainWindow
from modules.login import Login
from monitoreogui import SubVentanaMonitoreo
from modules.listaclientes import SubVentanaListaClientes
from modules.nuevocliente import SubVentanaNuevoCliente
from modules.panelclientealarmas import SubVentanaPanelClienteAlarmas
from modules.panelclienterondas import SubVentanaPanelClienteRondas

from convertgui import SubVentanaVehiculos
from convertgui import SubVentanaNuevoGrupoClientes
from convertgui import SubVentanaGruposdeClientes
from modules.usuarios import SubVentanaUsuarios
from modules.tiposusuarios import SubVentanaTiposUsuarios
from modules.receptores import SubVentanaReceptores
from modules.empresas import SubVentanaEmpresas
from modules.parentesco import SubVentanaParentesco
from modules.resoluciones import SubVentanaResoluciones
from modules.eventos import SubVentanaEventos
from modules.codigosdealarma import SubVentanaCodigosAlarma
from modules.tiposclientes import SubVentanaTipoCliente
from modules.departamentos import SubVentanaDepartamentos
from modules.gruposcodigosalarma import SubVentanaGruposCodigosAlarma
from modules.motivossoporte import SubVentanaMotivosSoporte
from convertgui import SubVentanaDiasFeriados
from convertgui import DialogCuentasGrupo
from modules.clientessinimagen import SubVentanaClientesSinImagenes
from modules.reportecodigosalarma import SubVentanaReportesCodigoAlarma
from modules.mapaclientes import SubVentanaMapaClientes
from modules.planesnotificaciones import SubVentanaPlanesNotificaciones
from modules.monitoralertas import SubVentanaMonitorAlertas
from modules.monitoralertas import HiloMonitoreoAlertas
from modules.reporteactivaciones import SubVentanaReporteActivaciones
from modules.reportegrupossenales import SubVentanaGruposSenales
from modules.reporteeventonodefinido import SubVentanaReporteEventoNoDefinido
from modules.reportesmsentrada import SubVentanaReporteSMSEntrada
from modules.reportesmsclientes import SubVentanaReporteClientesSMS
from modules.reportesestatuspanel import SubVentanaReporteEstatusPanel
from modules.reporteclienteultimasenal import SubVentanaReporteClienteUltimaSenal
from modules.reporteclienteultimasenalac import SubVentanaReporteClientesUltimaAperturaCierre
from modules.reportefichacliente import SubVentanaReporteFichaCliente
from modules.reportetotalessms import SubVentanaReporteTotalesSMS
from modules.equipostipos import SubVentanaTiposEquipos
from modules.equipossubtipos import SubVentanaSubTiposEquipos
from modules.equiposmarcas import SubVentanaMarcasEquipos
from modules.equiposmodelos import SubVentanaModelosEquipos


from modules.calcurondas import HiloCalcRondas
from modules.calcuhorarios import HiloCalcHorarios
from modules.calcualertas import HiloCalcAlertas
import re
import globalvars
from manageerrors import SaveError
import sys
import traceback
import locale
locale.setlocale(locale.LC_ALL, '')



class VentanaMain(QtGui.QMainWindow):
	def __init__(self):
		super(VentanaMain, self).__init__()
		self.VentanaMain = Ui_QMainWindow()
		self.VentanaMain.setupUi(self)
		self.VentanaMain.dockWidget_ListaClientes.hide()
		self.Resize1 =  False
		self.Resize = False	
		self.LabelStatusBar = QtGui.QLabel()
		self.setWindowTitle('365Connect 4.15')
		self.LabelStatusBar.setText('365Connect - Todos los derechos reservados. 2016    ')
		self.VentanaMain.statusbar.addPermanentWidget(self.LabelStatusBar)
		#Conexiones
		self.connect(self.VentanaMain.actionIngresar_a_Monitoreo, QtCore.SIGNAL("triggered()"), self.AbrirMonitoreo)
		self.connect(self.VentanaMain.actionLista_de_Clientes, QtCore.SIGNAL("triggered()"), self.AbrirListaClientes)
		self.connect(self.VentanaMain.actionNuevo_Cliente, QtCore.SIGNAL("triggered()"), self.AbrirNuevoCliente)
		self.connect(self.VentanaMain.actionUsuarios, QtCore.SIGNAL("triggered()"), self.AbrirUsuarios)
		self.connect(self.VentanaMain.actionTipos_de_Usuarios, QtCore.SIGNAL("triggered()"), self.AbrirTiposUsuarios)
		self.connect(self.VentanaMain.actionConfiguracion_Vehiculos, QtCore.SIGNAL("triggered()"), self.AbrirVehiculos)
		self.connect(self.VentanaMain.actionGrupos_de_Clientes, QtCore.SIGNAL("triggered()"), self.AbrirGrupoClientes)
		self.connect(self.VentanaMain.actionNuevo_Grupo, QtCore.SIGNAL("triggered()"), self.AbrirNuevoGrupoClientes)
		self.connect(self.VentanaMain.actionVer_Mapa, QtCore.SIGNAL("triggered()"), self.AbrirMapaClientes)
		self.connect(self.VentanaMain.actionPlanes, QtCore.SIGNAL("triggered()"), self.AbrirPlanesNotificaciones)
		self.connect(self.VentanaMain.actionMonitor_de_Alertas, QtCore.SIGNAL("triggered()"), self.AbrirMonitoreoAlertas)
		self.connect(self.VentanaMain.actionLogin_Logout, QtCore.SIGNAL("triggered()"), self.LoginLogout)


		self.connect(self.VentanaMain.actionModoVentana, QtCore.SIGNAL("triggered()"), self.ModoVentana)
		self.connect(self.VentanaMain.actionLateralBar, QtCore.SIGNAL("triggered()"), self.HideShowBar)
		self.connect(self.VentanaMain.lineEdit_BuscarCliente, QtCore.SIGNAL("textEdited(const QString&)"), self.BuscarClientesHechapormi)
		self.connect(self.VentanaMain.tableWidget_ListaClientes, QtCore.SIGNAL("cellDoubleClicked(int,int)"),self.AbrirCliente)

################################  ABRIR CONFIGURACIONES ###################################
		
		self.connect(self.VentanaMain.actionReceptores, QtCore.SIGNAL("triggered()"), self.AbrirReceptores)
		self.connect(self.VentanaMain.actionEmpresas, QtCore.SIGNAL("triggered()"), self.AbrirEmpresas)
		self.connect(self.VentanaMain.actionParentesco, QtCore.SIGNAL("triggered()"), self.AbrirParentesco)
		self.connect(self.VentanaMain.actionResoluciones, QtCore.SIGNAL("triggered()"), self.AbrirResoluciones)
		self.connect(self.VentanaMain.actionEventos, QtCore.SIGNAL("triggered()"), self.AbrirEventos)
		self.connect(self.VentanaMain.actionCodigos_de_Alarma, QtCore.SIGNAL("triggered()"), self.AbrirCodigosAlarmas)
		self.connect(self.VentanaMain.actionTipo_de_Cliente, QtCore.SIGNAL("triggered()"), self.AbrirTipoCliente)
		self.connect(self.VentanaMain.actionDepartamentos, QtCore.SIGNAL("triggered()"), self.AbrirDepartamentos)
		self.connect(self.VentanaMain.actionGrupo_Codigos_de_Alarma, QtCore.SIGNAL("triggered()"), self.AbrirGruposCodigosAlarma)
		self.connect(self.VentanaMain.actionMotivos_Soporte, QtCore.SIGNAL("triggered()"), self.AbrirMotivosSoporte)
		self.connect(self.VentanaMain.actionDias_Feriados, QtCore.SIGNAL("triggered()"), self.AbrirDiasFeriados)
		self.connect(self.VentanaMain.actionTipos, QtCore.SIGNAL("triggered()"), self.AbrirTiposEquipos)
		self.connect(self.VentanaMain.actionSub_Tipos_de_Equipos, QtCore.SIGNAL("triggered()"), self.AbrirSubTiposEquipos)
		self.connect(self.VentanaMain.actionMarcas, QtCore.SIGNAL("triggered()"), self.AbrirMarcasEquipos)
		self.connect(self.VentanaMain.actionModelos_de_Equipos, QtCore.SIGNAL("triggered()"), self.AbrirModelosEquipos)


################################## ABRIR REPORTES #############################################

		self.connect(self.VentanaMain.actionClientes_sin_Imagen, QtCore.SIGNAL("triggered()"), self.AbrirClientesSinImagenes)
		self.connect(self.VentanaMain.actionCodigo_ALarmas, QtCore.SIGNAL("triggered()"), self.AbrirReporteCodigosAlarmas)
		self.connect(self.VentanaMain.actionActivaciones, QtCore.SIGNAL("triggered()"), self.AbrirReporteActivaciones)
		self.connect(self.VentanaMain.actionGrupos_Alarmas, QtCore.SIGNAL("triggered()"), self.AbrirReporteGruposSenales)
		self.connect(self.VentanaMain.actionEventos_no_definidos, QtCore.SIGNAL("triggered()"), self.AbrirReporteEventoNoDefinido)
		self.connect(self.VentanaMain.actionSMS_Entrada, QtCore.SIGNAL("triggered()"), self.AbrirReporteSMSEntrada)
		self.connect(self.VentanaMain.actionSMS_Cliente, QtCore.SIGNAL("triggered()"), self.AbrirReporteClientesSMS)
		self.connect(self.VentanaMain.actionEstatus_Panel, QtCore.SIGNAL("triggered()"), self.AbrirReporteEstatusPanel)
		self.connect(self.VentanaMain.actionClientes_Ultima_Se_al, QtCore.SIGNAL("triggered()"), self.AbrirReporteClienteUltimaSenal)
		self.connect(self.VentanaMain.actionClientes_Ultima_A_C, QtCore.SIGNAL("triggered()"), self.AbrirReporteClienteUltimaAperturaCierre)
		self.connect(self.VentanaMain.actionSMS_Totales, QtCore.SIGNAL("triggered()"), self.AbrirReporteTotalesSMS)
		self.connect(self.VentanaMain.actionFicha_Cliente, QtCore.SIGNAL("triggered()"), self.AbrirReporteFichaClientes)



		#Para que las todas las subventanas del mdiarea no tomen el mismo estado cuando se maximiza una
		self.VentanaMain.mdiArea.setOption(QtGui.QMdiArea.DontMaximizeSubWindowOnActivation,False)

		self.ModoWindows = True	

########################## PARA LA BARRA LATERAL DE LISTA DE CLIENTE ###########################3

		#Invento mio para solucionar el Bug con que si esta activado el rezize de las tablas\
		#Con el resize de la ventana no se le puede colocar un tamano por defecto

		self.installEventFilter(self)
		self.HideBar = True
		self.BuscarClientesBD()
		self.ListarClientes()

		self.CargarTablasEstaticamente()

		if globalvars.Tipo ==  str(1):

			self.HiloRondas = HiloCalcRondas(self)
			self.HiloRondas.start()


			#self.HiloHorarios = HiloCalcHorarios(self)
			#self.HiloHorarios.start()

			self.HiloAlertas = HiloCalcAlertas(self)
			self.HiloAlertas.start()


	####################### ABRIR LOGIN ###########################
		self.TimerLogin = QtCore.QTimer()
		self.TimerLogin.setSingleShot(True)
		self.TimerLogin.start(100)
		self.connect(self.TimerLogin, QtCore.SIGNAL("timeout()"), self.AbrirLogin)



		##################FUNCIONES PARA EL SYSTEM TRAY ICON#######################
		self.exitOnClose = False
		exit = QtGui.QAction(QtGui.QIcon(":/iconos/ico/connections-512(1).png"), "Cerrar 365Connect", self)
		self.connect(exit, QtCore.SIGNAL("triggered()"), self.exitEvent)
		self.trayIcon = QtGui.QSystemTrayIcon(QtGui.QIcon(":/iconos/ico/connections-512(1).png"), self)
		menu = QtGui.QMenu(self)
		menu.addAction(exit)
		self.trayIcon.setContextMenu(menu)
		self.connect(self.trayIcon, \
			QtCore.SIGNAL("activated(QSystemTrayIcon::ActivationReason)"), \
			self.trayIconActivated)
		self.trayIcon.show()
		self.trayIcon.showMessage("365Connect Iniciando","Un momento...",QtGui.QSystemTrayIcon.Information,10000)
		self.trayIcon.setToolTip("365Connect")


		self.HayBD = True
	def trayIconActivated(self, reason):
		if reason == QtGui.QSystemTrayIcon.Context:
			self.trayIcon.contextMenu().show()
		elif reason == QtGui.QSystemTrayIcon.Trigger:
			self.show()
			self.raise_()
			if globalvars.Logueado == False:
				self.Login.show()


	def closeEvent(self,event):
		if self.exitOnClose:
			self.trayIcon.hide()


			if 'self.HiloMoniAlert' in locals():
				self.HiloMoniAlert.terminate()
				while True:
					if self.HiloMoniAlert.isTerminated():
						del self.HiloMoniAlert
						break
			if 'self.SubVentanaMonitoreoAlertas' in locals():
				del self.SubVentanaMonitoreoAlertas
			if 'self.SubVentanaEventos' in locals():
				del self.SubVentanaEventos
			if 'self.SubVentanaReporteTotalesSMS' in locals():
				del self.SubVentanaReporteTotalesSMS
			self.VentanaMain.mdiArea.closeAllSubWindows()
			event.accept()
		else:
			self.hide()
			event.setAccepted(True)
			event.ignore()



	def exitEvent(self):
		self.exitOnClose = True

		self.close()

		################################################################################

	def LoginLogout(self):
		if globalvars.Logueado == True:
			self.AbrirLogin()


	def AbrirLogin(self):
		self.Login = Login(self)
		self.Login.setWindowModality(QtCore.Qt.WindowModal)
		self.Login.exec_()

	def CargarTablasEstaticamente(self):

		self.VentanaMain.tableWidget_ListaClientes.setColumnWidth(0,40)
		self.VentanaMain.tableWidget_ListaClientes.setColumnWidth(1,195)

	def BuscarClientesHechapormi(self,busqueda):
		self.ListarClientes()
		#print busqueda
		#for letra in busqueda:
		ResultadoBusqueda = self.VentanaMain.tableWidget_ListaClientes.findItems(busqueda,QtCore.Qt.MatchContains)
		#print ResultadoBusqueda
		#for i in ResultadoBusqueda:
			#print i.text()
		listafilasresultado = []
		for r in ResultadoBusqueda:
			listafilasresultado.append(self.VentanaMain.tableWidget_ListaClientes.row(r))
		#print listafilasresultado
		filasentotal = self.VentanaMain.tableWidget_ListaClientes.rowCount()
		for eliminar in reversed(range(filasentotal)):
				if eliminar in listafilasresultado:
					pass
				else:
					self.VentanaMain.tableWidget_ListaClientes.removeRow(eliminar)

	def AbrirClienteDesdeExterno(self,idcliente):
		for nombretipo,listatipo in self.DictClientesPorTipo.iteritems():
			if int(idcliente) in listatipo:
				TipoCliente = nombretipo
				break
		if TipoCliente == 'Alarmas':
			self.AbrirPanelClienteAlarmas(idcliente)
		elif TipoCliente == 'GPS':
			pass
		elif TipoCliente ==  'Bastones':
			self.AbrirPanelClienteRondas(idcliente)		

	def AbrirCliente(self,*celda):
		ElementoTabla = self.VentanaMain.tableWidget_ListaClientes.item(celda[0],0)
		PrefijoCuenta = str(ElementoTabla.text())
		IDCliente = self.DictClientesIDCuenta[PrefijoCuenta]
		for nombretipo,listatipo in self.DictClientesPorTipo.iteritems():
			if int(IDCliente) in listatipo:
				TipoCliente = nombretipo
				break
		if TipoCliente == 'Alarmas':
			self.AbrirPanelClienteAlarmas(IDCliente)
		elif TipoCliente == 'GPS':
			pass
		elif TipoCliente ==  'Bastones':
			self.AbrirPanelClienteRondas(IDCliente)


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
			self.VentanaMain.tableWidget_ListaClientes.setColumnWidth(0,self.VentanaMain.tableWidget_ListaClientes.width()/5)
			self.VentanaMain.tableWidget_ListaClientes.setColumnWidth(1,self.VentanaMain.tableWidget_ListaClientes.width()/1.38)
		self.Resize = True

	def BuscarClientesBD(self):
		print 'CARGANDO'
		self.ResultadoListaClientes = globalvars.BD.Querys('ListarClientesIDNombre')
		self.ListarClientes()
	def ListarClientes(self):
		self.DictClientesIDCuenta = {}
		#Creo el diccionario donde estaran los clientes por tipo
		self.DictClientesPorTipo = {}
		#Agrego los Tipos
		self.DictClientesPorTipo['Alarmas'] = []
		self.DictClientesPorTipo['Bastones'] = []
		self.DictClientesPorTipo['GPS'] = []


		self.VentanaMain.tableWidget_ListaClientes.verticalHeader().setVisible(False)
		self.VentanaMain.tableWidget_ListaClientes.setShowGrid(False)
		self.VentanaMain.tableWidget_ListaClientes.setAlternatingRowColors(True)
		#self.VentanaMain.tableWidget_ListaClientes.resizeColumnsToContents()
		self.VentanaMain.tableWidget_ListaClientes.verticalHeader().setDefaultSectionSize(20)
		self.VentanaMain.tableWidget_ListaClientes.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.VentanaMain.tableWidget_ListaClientes.setSortingEnabled(False)
		self.VentanaMain.tableWidget_ListaClientes.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

		while self.VentanaMain.tableWidget_ListaClientes.rowCount() > 0:
			self.VentanaMain.tableWidget_ListaClientes.removeRow(0)

		fila = 0
		columna = 0

		for cliente in reversed(self.ResultadoListaClientes):
			self.VentanaMain.tableWidget_ListaClientes.insertRow(0)
			columna = 0
			#Columna 0
			texto = QtGui.QTableWidgetItem(str(cliente.prefijo)+'-'+str(cliente.cuenta))
			self.VentanaMain.tableWidget_ListaClientes.setItem(fila,columna,texto)
			#Columna 1
			columna = columna + 1
			texto = QtGui.QTableWidgetItem(cliente.nombre_cliente)
			self.VentanaMain.tableWidget_ListaClientes.setItem(fila,columna,texto)
			#Organizamos los Clientes segun su tipo de dispositivo (Alarma - GPS - Bastones) para al hacer click en Abrir abrir el panel que es
			if cliente.tipocuenta == None:
				ClienteTipo = 0
			else:
				ClienteTipo = cliente.tipocuenta
			if int(ClienteTipo) == 5:
				self.DictClientesPorTipo['Alarmas'].append(cliente.id_cliente)
			elif int(ClienteTipo) == 6:
				self.DictClientesPorTipo['GPS'].append(cliente.id_cliente)
			elif int(ClienteTipo) == 7:
				self.DictClientesPorTipo['Bastones'].append(cliente.id_cliente)
			#Agregamos al diccionario self.DictClientesIDCuenta clave prefijo-cuenta valor idcliente
			self.DictClientesIDCuenta[str(cliente.prefijo)+'-'+str(cliente.cuenta)] = str(cliente.id_cliente)

		self.ArreglarTamanoTablas()

	def ModoVentana(self):
		if self.ModoWindows == True:
			self.VentanaMain.mdiArea.setViewMode(1)
			self.ModoWindows = False
		else:
			self.VentanaMain.mdiArea.setViewMode(0)
			self.ModoWindows = True
		
	def HideShowBar(self):
		if self.HideBar == True:
			self.VentanaMain.dockWidget_ListaClientes.show()
			self.HideBar = False
		else:
			self.VentanaMain.dockWidget_ListaClientes.hide()
			self.HideBar = True
		self.ArreglarTamanoTablas()

##################################### SUB VENTANAS ##########################################################

	def AbrirReporteFichaClientes(self):
		self.SubVentanaReporteFichaCliente = SubVentanaReporteFichaCliente()
		self.SubVentanaReporteFichaCliente.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaReporteFichaCliente)
		self.SubVentanaReporteFichaCliente.show()

	def AbrirReporteTotalesSMS(self):
		self.SubVentanaReporteTotalesSMS = SubVentanaReporteTotalesSMS()
		self.SubVentanaReporteTotalesSMS.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaReporteTotalesSMS)
		self.SubVentanaReporteTotalesSMS.showMaximized()

	def AbrirReporteClienteUltimaAperturaCierre(self):
		self.SubVentanaReporteClienteUltimaAperturaCierre = SubVentanaReporteClientesUltimaAperturaCierre()
		self.SubVentanaReporteClienteUltimaAperturaCierre.setAttribute(QtCore.Qt.WA_DeleteOnClose,True);
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaReporteClienteUltimaAperturaCierre)
		self.SubVentanaReporteClienteUltimaAperturaCierre.showMaximized()

	def AbrirReporteClienteUltimaSenal(self):
		self.SubVentanaReporteUltimaSenal = SubVentanaReporteClienteUltimaSenal()
		self.SubVentanaReporteUltimaSenal.setAttribute(QtCore.Qt.WA_DeleteOnClose,True);
		#self.VentanaMain.mdiArea.addSubWindow(self.AbrirReporteGruposSenales)
		self.SubVentanaReporteUltimaSenal.showMaximized()

	def AbrirReporteEstatusPanel(self):
		self.SubVentanaReporteEstatusPanel = SubVentanaReporteEstatusPanel()
		self.SubVentanaReporteEstatusPanel.setAttribute(QtCore.Qt.WA_DeleteOnClose,True);
		#self.VentanaMain.mdiArea.addSubWindow(self.AbrirReporteGruposSenales)
		self.SubVentanaReporteEstatusPanel.showMaximized()

	def AbrirReporteClientesSMS(self):
		self.SubVentanaReporteClientesSMS = SubVentanaReporteClientesSMS()
		self.SubVentanaReporteClientesSMS.setAttribute(QtCore.Qt.WA_DeleteOnClose,True);
		#self.VentanaMain.mdiArea.addSubWindow(self.AbrirReporteGruposSenales)
		self.SubVentanaReporteClientesSMS.showMaximized()


	def AbrirReporteSMSEntrada(self):
		self.SubVentanaReporteSMSEntrada = SubVentanaReporteSMSEntrada()
		self.SubVentanaReporteSMSEntrada.setAttribute(QtCore.Qt.WA_DeleteOnClose,True);
		#self.VentanaMain.mdiArea.addSubWindow(self.AbrirReporteGruposSenales)
		self.SubVentanaReporteSMSEntrada.showMaximized()


	def AbrirReporteEventoNoDefinido(self):
		self.AbrirReporteEventoNoDefinido = SubVentanaReporteEventoNoDefinido()
		self.AbrirReporteEventoNoDefinido.setAttribute(QtCore.Qt.WA_DeleteOnClose,True);
		#self.VentanaMain.mdiArea.addSubWindow(self.AbrirReporteGruposSenales)
		self.AbrirReporteEventoNoDefinido.showMaximized()

	def AbrirReporteGruposSenales(self):
		self.AbrirReporteGruposSenales = SubVentanaGruposSenales()
		self.AbrirReporteGruposSenales.setAttribute(QtCore.Qt.WA_DeleteOnClose,True);
		#self.VentanaMain.mdiArea.addSubWindow(self.AbrirReporteGruposSenales)
		self.AbrirReporteGruposSenales.showMaximized()

	def AbrirReporteActivaciones(self):
		self.AbrirReporteActivaciones = SubVentanaReporteActivaciones()
		self.AbrirReporteActivaciones.setAttribute(QtCore.Qt.WA_DeleteOnClose,True);
		#self.VentanaMain.mdiArea.addSubWindow(self.AbrirReporteActivaciones)
		self.AbrirReporteActivaciones.showMaximized()	

	def AbrirMonitoreoAlertas(self):
		self.SubVentanaMonitoreoAlertas = SubVentanaMonitorAlertas()
		self.SubVentanaMonitoreoAlertas.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)
		self.SubVentanaMonitoreoAlertas.showMaximized()
		self.HiloMoniAlert = HiloMonitoreoAlertas(self,self.SubVentanaMonitoreoAlertas.SubVentanaMonitorAlertas.tableWidget_Log,self.SubVentanaMonitoreoAlertas.SubVentanaMonitorAlertas.tableWidget_Cola,self.SubVentanaMonitoreoAlertas.SubVentanaMonitorAlertas.tableWidget_Enviados,self.SubVentanaMonitoreoAlertas.SubVentanaMonitorAlertas.tableWidget_Recibidos,self.SubVentanaMonitoreoAlertas.SubVentanaMonitorAlertas.label_ColaMensajes)
		self.HiloMoniAlert.start()

	def AbrirModelosEquipos(self):
		self.SubVentanaModelosEquipos = SubVentanaModelosEquipos()
		self.SubVentanaModelosEquipos.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)
		self.SubVentanaModelosEquipos.show()

	def AbrirMarcasEquipos(self):
		self.SubVentanaMarcasEquipos = SubVentanaMarcasEquipos()
		self.SubVentanaMarcasEquipos.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)
		self.SubVentanaMarcasEquipos.show()

	def AbrirSubTiposEquipos(self):
		self.SubVentanaSubTiposEquipos = SubVentanaSubTiposEquipos()
		self.SubVentanaSubTiposEquipos.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)
		self.SubVentanaSubTiposEquipos.show()

	def AbrirTiposEquipos(self):
		self.SubVentanaTiposEquipos = SubVentanaTiposEquipos()
		self.SubVentanaTiposEquipos.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)
		self.SubVentanaTiposEquipos.show()

	def AbrirPlanesNotificaciones(self):
		self.AbrirPlanesNotificaciones = SubVentanaPlanesNotificaciones()
		self.AbrirPlanesNotificaciones.setAttribute(QtCore.Qt.WA_DeleteOnClose,True);
		#self.VentanaMain.mdiArea.addSubWindow(self.AbrirPlanesNotificaciones)
		self.AbrirPlanesNotificaciones.show()

	def AbrirMapaClientes(self):
		self.SubVentanaMapaClientes = SubVentanaMapaClientes()
		self.SubVentanaMapaClientes.setAttribute(QtCore.Qt.WA_DeleteOnClose,True);
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaMapaClientes)
		self.SubVentanaMapaClientes.show()

	def AbrirReceptores(self):
		self.SubVentanaReceptores = SubVentanaReceptores()
		self.SubVentanaReceptores.setAttribute(QtCore.Qt.WA_DeleteOnClose,True);

		
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaReceptores)
		self.SubVentanaReceptores.show()

	def AbrirEmpresas(self):
		self.SubVentanaEmpresas = SubVentanaEmpresas()
		self.SubVentanaEmpresas.setAttribute(QtCore.Qt.WA_DeleteOnClose,True);

		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaEmpresas)
		self.SubVentanaEmpresas.show()

	def AbrirParentesco(self):
		self.SubVentanaParentesco = SubVentanaParentesco()
		self.SubVentanaParentesco.setAttribute(QtCore.Qt.WA_DeleteOnClose,True);

		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaParentesco)
		self.SubVentanaParentesco.show()

	def AbrirResoluciones(self):
		self.SubVentanaResoluciones = SubVentanaResoluciones()
		self.SubVentanaResoluciones.setAttribute(QtCore.Qt.WA_DeleteOnClose,True);

		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaResoluciones)
		self.SubVentanaResoluciones.show()


	def AbrirEventos(self):
		self.SubVentanaEventos = SubVentanaEventos()
		self.SubVentanaEventos.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaEventos)
		self.SubVentanaEventos.show()


	def AbrirCodigosAlarmas(self):
		self.SubVentanaCodigosAlarma = SubVentanaCodigosAlarma()
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaCodigosAlarma)
		self.SubVentanaCodigosAlarma.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)

		self.SubVentanaCodigosAlarma.show()

	def AbrirTipoCliente(self):
		self.SubVentanaTipoCliente = SubVentanaTipoCliente()
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaTipoCliente)
		self.SubVentanaTipoCliente.show()

	def AbrirDepartamentos(self):
		self.SubVentanaDepartamentos = SubVentanaDepartamentos()
		
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaDepartamentos)
		self.SubVentanaDepartamentos.show()

	def AbrirCodigosAlarma(self):
		self.SubVentanaDepartamentos = SubVentanaDepartamentos()
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaDepartamentos)
		self.SubVentanaDepartamentos.show()

	def AbrirGruposCodigosAlarma(self):
		self.SubVentanaGruposCodigosAlarma = SubVentanaGruposCodigosAlarma()
		
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaGruposCodigosAlarma)
		self.SubVentanaGruposCodigosAlarma.show()

	def AbrirMotivosSoporte(self):
		self.SubVentanaMotivosSoporte = SubVentanaMotivosSoporte()
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaMotivosSoporte)
		self.SubVentanaMotivosSoporte.show()

	def AbrirDiasFeriados(self):
		self.SubVentanaDiasFeriados = SubVentanaDiasFeriados()
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaDiasFeriados)
		self.SubVentanaDiasFeriados.show()

	def AbrirGrupoClientes(self):
		self.SubVentanaGruposdeClientes = SubVentanaGruposdeClientes()
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaGruposdeClientes)
		self.SubVentanaGruposdeClientes.setWindowTitle("Grupos Clientes")
		self.SubVentanaGruposdeClientes.show()
		self.connect(self.SubVentanaGruposdeClientes, QtCore.SIGNAL("signalAbrirCuentasGrupo"), self.AbrirCuentasGrupo)
		self.connect(self.SubVentanaGruposdeClientes, QtCore.SIGNAL("signalAbrirAgregarGrupo"), self.AbrirNuevoGrupoClientes)

	def AbrirCuentasGrupo(self,parent,idgrupo):
		self.DialogCuentasGrupo = DialogCuentasGrupo(parent,idgrupo)
		#self.VentanaMain.mdiArea.addSubWindow(self.DialogCuentasGrupo)
		self.DialogCuentasGrupo.show()
		self.connect(self.DialogCuentasGrupo, QtCore.SIGNAL("signalCerrar"), self.CerrarVentanaActiva)

	def CerrarVentanaActiva(self):
		self.VentanaMain.mdiArea.closeActiveSubWindow()


	def AbrirNuevoGrupoClientes(self,parent=None):
		self.SubVentanaNuevoGrupoClientes = SubVentanaNuevoGrupoClientes(parent)
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaNuevoGrupoClientes)
		self.SubVentanaNuevoGrupoClientes.setWindowTitle("Nuevo Grupo Clientes")
		self.SubVentanaNuevoGrupoClientes.show()
		self.connect(self.SubVentanaNuevoGrupoClientes, QtCore.SIGNAL("signalCerrar"), self.CerrarVentanaActiva)


	def AbrirVehiculos(self):
		self.SubVentanaVehiculos = SubVentanaVehiculos()
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaVehiculos)
		self.SubVentanaVehiculos.setWindowTitle("Vehiculos")
		self.SubVentanaVehiculos.show()

	def AbrirUsuarios(self):
		self.SubVentanaUsuarios = SubVentanaUsuarios()
		self.SubVentanaUsuarios.setAttribute(QtCore.Qt.WA_DeleteOnClose,True);

		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaUsuarios)
		self.SubVentanaUsuarios.show()


	def AbrirTiposUsuarios(self):
		self.SubVentanaTiposUsuarios = SubVentanaTiposUsuarios()
		self.SubVentanaTiposUsuarios.setAttribute(QtCore.Qt.WA_DeleteOnClose,True);

		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaTiposUsuarios)
		self.SubVentanaTiposUsuarios.show()

	def AbrirMonitoreo(self):
		self.SubVentanaMonitoreo = SubVentanaMonitoreo(self)
		self.SubVentanaMonitoreo.setAttribute(QtCore.Qt.WA_DeleteOnClose,True);
		self.SubVentanaMonitoreo.setWindowTitle("Monitoreo")
		self.SubVentanaMonitoreo.showMaximized()		



	def AbrirListaClientes(self):
		self.SubVentanaListaClientes = SubVentanaListaClientes()
		#self.SubVentanaListaClientes.setWindowIcon(QtGui.QIcon(":/iconos/ico/Feedbin-Icon-check.svg.png"))
		self.SW = self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaListaClientes)
		self.SW.setWindowIcon(QtGui.QIcon(":/iconos/ico/Feedbin-Icon-check.svg.png"))
		self.SW.show()

		self.connect(self.SubVentanaListaClientes, QtCore.SIGNAL("signalAbrirPanelCliente"),self.AbrirClienteDesdeExterno)

	def AbrirNuevoCliente(self):
		self.SubVentanaNuevoCliente = SubVentanaNuevoCliente()
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaNuevoCliente)
		self.SubVentanaNuevoCliente.setWindowTitle("Agregar Cliente")
		self.SubVentanaNuevoCliente.show()
		self.connect(self.SubVentanaNuevoCliente, QtCore.SIGNAL("signalCargarClientesNuevamente"),self.BuscarClientesBD)
		self.connect(self.SubVentanaNuevoCliente, QtCore.SIGNAL("signalAbrirPanelClienteAlarmas"),self.AbrirPanelClienteAlarmas)
		self.connect(self.SubVentanaNuevoCliente, QtCore.SIGNAL("signalAbrirPanelClienteRondas"),self.AbrirPanelClienteRondas)


	def AbrirPanelClienteAlarmas(self,abonado):
		self.SubVentanaPanelClienteAlarmas = SubVentanaPanelClienteAlarmas(abonado)
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaPanelCliente)
		self.SubVentanaPanelClienteAlarmas.setStyleSheet(self.styleSheet())
		self.SubVentanaPanelClienteAlarmas.show()
		self.connect(self.SubVentanaPanelClienteAlarmas, QtCore.SIGNAL("signalCargarClientesNuevamente"),self.BuscarClientesBD)
		self.connect(self.SubVentanaPanelClienteAlarmas, QtCore.SIGNAL("signalAbrirPanelClienteAlarmas"),self.AbrirPanelClienteAlarmas)
		self.connect(self.SubVentanaPanelClienteAlarmas, QtCore.SIGNAL("signalAbrirPanelClienteRondas"),self.AbrirPanelClienteRondas)


	def AbrirPanelClienteRondas(self,abonado):
		self.SubVentanaPanelClienteRondas = SubVentanaPanelClienteRondas(abonado)
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaPanelCliente)
		self.SubVentanaPanelClienteRondas.setStyleSheet(self.styleSheet())
		self.SubVentanaPanelClienteRondas.show()
		self.connect(self.SubVentanaPanelClienteRondas, QtCore.SIGNAL("signalCargarClientesNuevamente"),self.BuscarClientesBD)
		self.connect(self.SubVentanaPanelClienteRondas, QtCore.SIGNAL("signalAbrirPanelClienteRondas"),self.AbrirPanelClienteRondas)
		self.connect(self.SubVentanaPanelClienteRondas, QtCore.SIGNAL("signalAbrirPanelClienteAlarmas"),self.AbrirPanelClienteAlarmas)


	def AbrirClientesSinImagenes(self):
		self.SubVentanaClientesSinImagenes = SubVentanaClientesSinImagenes()
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaClientesSinImagenes)
		self.SubVentanaClientesSinImagenes.show()

	def AbrirReporteCodigosAlarmas(self):
		self.SubVentanaReportesCodigoAlarma = SubVentanaReportesCodigoAlarma()
		#self.VentanaMain.mdiArea.addSubWindow(self.SubVentanaReportesCodigoAlarma)
		self.SubVentanaReportesCodigoAlarma.showMaximized()




if __name__ == "__main__":
	import sys
	from tendo import singleton
	me = singleton.SingleInstance()
	print me
	app = QtGui.QApplication(sys.argv)
	import pyqt_style_rc
	#app.setStyle(QtGui.QStyleFactory.create("plastique"))
	globalvars.initvars()
	window = VentanaMain()
	sshFile='Estilo1.0.qss'
	with open(sshFile,"r") as fh:
	    window.setStyleSheet(fh.read())
	window.showMaximized()
	app.exec_()
	del window


