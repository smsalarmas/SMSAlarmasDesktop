#Importamos el Modulo Pyodbc para conexion con la base de datos
import pyodbc
from PyQt4 import QtCore
from PyQt4 import QtGui
#Importamos el modulo para archivos INI
from ConfigParser import ConfigParser
#Importamos Desencriptador XOR Pycrypto
from Crypto.Cipher import XOR
import base64
import time, datetime
import threading
import globalvars


class BasedeDatosThread(QtCore.QThread):
	def __init__(self,nombrequery,tipoquery,*datos):
		QtCore.QThread.__init__(self)
		self.resultado = None
		#Buscando el archivo INI para saber el String de Conexion
		config = ConfigParser()
		config.read("conf/config.ini")
		self.conexioncifrada = config.get('BASE DE DATOS', 'conexion')
		PASSWORD = XOR.new(base64.b64decode('MjAxMDE3MzMtOTYwOTkyNg=='))
		self.conexion = PASSWORD.decrypt(base64.b64decode(str(self.conexioncifrada)))
		self.cantidad = 0
		self.nombrequery = nombrequery
		self.datos = datos
		self.tipoquery = tipoquery
	def Conectar(self):
		try:
			self.cnxn = pyodbc.connect(self.conexion)
			self.cursor = self.cnxn.cursor()
		except:
			print 'No se pudo conectar a BD'
		
	def Desconectar(self):
		try:
			self.cursor.close()
			del self.cursor
			self.cnxn.close()
		except:
			pass

	def run(self):
		#globalvars.Aplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
		self.Conectar()
		if self.tipoquery == "SEL":
			self.CrearCodigoDatos()
			self.QuerysSelect()
		elif self.tipoquery == "INS":
			self.QueryInsert()
		elif self.tipoquery == "DELUPD":
			self.QuerysUpdateDelete()
		self.Desconectar()

		#globalvars.Aplication.restoreOverrideCursor()

	def QueryInsert(self):
		######################################## INSERT ###############################################
		try:
			if self.nombrequery == 'InsertarZonaPuntoCliente':
				self.cursor.execute("INSERT INTO t365_ClienteZonas (id_zona, descrip, ubicacion, id_cliente) VALUES (?,?,?,?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarNotaFijaCliente':
				self.cursor.execute("INSERT INTO t365_NotasClientes (IdCliente, NotaFija)   VALUES(?,?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarNotaTemporalCliente':
				self.cursor.execute("INSERT INTO t365_NotasClientes (IdCliente, NotaTemp, FechaIni, FechaFin)   VALUES(?,?,?,?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarGrupoClientes': #### INSERTAR ASOCIADO ####
				self.cursor.execute("INSERT INTO t365_asociados (id_empresa, nombre, direccion, telef_contacto, email, usuario, clave, status) VALUES (?,?,?,?,?,?,?,?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarAbonadosGrupo':  ##### INSERTAR ABONADOS A ASOCIADOS ####
				self.cursor.execute("INSERT INTO t365_asociados_abonados (id_asociado, id_empresa, id_cliente) VALUES (?,?,?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarAbonado':  ##### INSERTAR ABONADOS ####
				self.cursor.execute("INSERT INTO t365_Clientes (nombre_cliente, ciudad, direccion, referencia, telf_local, web_site, email, telf_movil, id_type_cliente, id_status, status_web, status, id_protocolo, id_empresa,cuenta, telf_fax,clavemaster,rif,fechinicio,latitud,longitud,id_estado,status_monitoreo,status_mail,prefijo,login,clave,tipocuenta,modelo) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarUsuario': 
				self.cursor.execute("INSERT INTO t365_Usuarios (id_user, id_cliente, cod_user, id_type_user, nombre , apellido, movil, email, FechaAniversario, status, send_mail, frecuencia_mail, bbpin,clavevoz,active_email,id_plan,id_plan_email,maximosms) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarContactoEmergencia':  
				self.cursor.execute("INSERT INTO t365_NumEmergencia (numero, descript,observacion,id_cliente)   VALUES(?,?,?,?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarEventosUsuario':  
				self.cursor.execute("INSERT INTO t365_ClienteEventos (id_cliente, cod_evento, id_user, status, variante, type)   SELECT  id_cliente=?, cod_evento, id_user=?, 1, variante, type=?  FROM t365_EventosPlanes where id_plan = ?",self.datos)
				self.cnxn.commit()
			
			elif self.nombrequery == 'InsertarHorarioCliente':  
				self.cursor.execute("INSERT INTO t365_HorariosOC (id_cliente,diaapertura,horaapertura,toleranciaapertura,diacierre,horacierre,toleranciacierre,tomada,borrar) VALUES (?,?,?,?,?,?,?,0,0)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarTipoCliente':  
				self.cursor.execute("INSERT INTO  t365_TypeCliente  (descrip,img,id_dispositivo,id_empresa) VALUES (?,?,?,?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarDepartamento':  
				self.cursor.execute("INSERT INTO t365_DepartamentosEmpresa (idEmpresa, nombre, correo) VALUES (?,?,?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarTipoAlarma':  
				self.cursor.execute("INSERT INTO  t365_TypeAlarma (Descrip) VALUES (?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarOperadorSession':  
				self.cursor.execute("INSERT INTO t365_OperadorSession (IdSession, IdOperador, FechaPIN, Ip, StatusLogin, StatusMonitoreo, FechaDesocupado) Values (?,?,GETDATE(),?,?,?,GETDATE())",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarObservacionTrama':  
				self.cursor.execute("INSERT INTO t365_TramasObservaciones (idtrama, fecha, observacion, idoperador) values (?,GETDATE(),?,?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarTramaProcesada':  
				self.cursor.execute("INSERT INTO t365_TramasProcesadas (id_trama,descrip, cliente, status, evento, protocolo, user_zone, fecha, Variante, Linea,observacion,IdOperador,EmpresaMonitorea) SELECT id_trama,descrip, cliente,status, evento,  protocolo, user_zone, fecha, Variante, Linea,?, ?,EmpresaMonitorea FROM t365_Tramas WHERE  id_trama = ?",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarPlanNotificaciones':  
				self.cursor.execute("INSERT INTO t365_Planes (descrip,id_protocolo) VALUES(?, ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarEventosPlan':  
				self.cursor.execute("INSERT INTO t365_EventosPlanes (cod_evento,id_plan,id_protocolo) VALUES(?,?,?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarEvento':  
				self.cursor.execute("INSERT INTO t365_Eventos (cod_event,id_protocolo,descript,mensaje,type_evento,monitorea,cod_alarm,prioridad,web_color) VALUES(?,?,?,?,?,?,?,?,?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarCodigoAlarma':  
				self.cursor.execute("INSERT INTO t365_CodigosAlarma (codigo,descript,prioridad,grupo,idGrupo,web_color,color) VALUES(?,?,?,?,?,?,'1')",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarUsuarioPersonal':  
				self.cursor.execute("INSERT INTO t365_Personal (id_empresa, idTipoUsuario, cedula, nombre, telefono, correo, Dirreccion, Telf_Habitacion, usuario, clave,eliminado,estatus,id_perfil) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarPermisosPersonal':
				parentesis = len(self.datos)-2 
				Query = "INSERT INTO t365_PermisosAdmin SELECT p.idPagina, a.idAccion,?  FROM t365_PaginasAdmin p INNER JOIN  t365_PaginasAcciones a ON p.idPagina = a.idPagina WHERE  (a.idAccion IN ("
				par = '?'
				for i in range(parentesis):
					par = par + ',?'
				Query = Query + par + '))'
				self.cursor.execute(Query,self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarPermisosTipoUsuario':
				parentesis = len(self.datos)-2 
				Query = "INSERT INTO t365_PermisosTipoUsuario SELECT p.idPagina, a.idAccion, ?    FROM t365_PaginasAdmin p INNER JOIN  t365_PaginasAcciones a ON p.idPagina = a.idPagina WHERE   (a.idAccion IN ("
				par = '?'
				for i in range(parentesis):
					par = par + ',?'
				Query = Query + par + '))'
				self.cursor.execute(Query,self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarTipoUsuario':
				self.cursor.execute("INSERT INTO t365_TiposUsuarios (idEmpresa, color, descripcion, eliminado,id_perfilUsuario) VALUES (?,?,?,?,?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarEmpresa':
				self.cursor.execute("INSERT INTO t365_Empresas (id_pais, nombre, direccion, telefonos, email, web, login, clave, status, rif, ip, puerto, master,latitud, longuitud,timeAlertPen, timeHombreM, timeNotifiHombre, correosHombre)VALUES (1,?,?,?,?,?,?,?,?,?,0,0,0,?,?,?,?,?,?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarParentesco':
				self.cursor.execute("INSERT INTO t365_TypeUser (descrip) VALUES (?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarMensajePredefinido':
				self.cursor.execute("INSERT INTO t365_MensajesCierre (Mensaje) VALUES (?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarReceptorConfigPort':
				self.cursor.execute("INSERT INTO t365_ConfigPortII (PortID, Descrip, Config, type, Server, Port, idReceptor, Heartbeat, Status, geta,idReceiver,orden, fechaCreator,prefijo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 1,?,1, GETDATE(),?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarSoporteMotivos':
				self.cursor.execute("INSERT INTO  t365_SoporteMotivos ( idEmpresa, descripcion, idDepartCorreo) VALUES (?,?,?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarCCTVCliente':
				self.cursor.execute("""INSERT INTO  t365_ClientesCCTV ([id_cliente],[id_modo],[id_tipo],[id_marca],[id_modelo],[descripcion],[ip],[puerto],[usuario],[clave]) VALUES (?,?,?,?,?,?,?,?,?,?)""",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarChannelCCTVCliente':
				self.cursor.execute("""INSERT INTO  t365_ClientesCCTV_Channel ([id_cctv],[channel],[descripcion]) VALUES (?,?,?)""",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarPrefijosRangosEmpresa':
				self.cursor.execute("""INSERT INTO  t365_EmpresasRangoClientes ([prefijo],[IniRango],[FinRango],[id_empresa]) VALUES (?,?,?,?)""",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarPrefijosLineas':
				self.cursor.execute("""INSERT INTO  t365_ConfigPort_Lineas (linea,PortID,descripcion,prefijo) VALUES (?,?,?,?)""",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarRonda':
				self.cursor.execute("""INSERT INTO t365_Rondas (id_Cliente,Nombre,Tolerancia,Hora_Inicio,Hora_Fin,id_Calendario,id_Tipo,id_padre,Intervalo,Hora_Fin_Total,Tomada,Borrar) VALUES (?,?,?,?,?,?,?,?,?,?,?,0)""",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarPuntosRonda':
				self.cursor.execute("""INSERT INTO  t365_RondasPuntos (id_ronda,id_punto,orden) VALUES (?,?,?)""",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarAlertBSalidaSpeed':
				self.cursor.execute("""INSERT INTO t365_BsalidaSpeed (id_cliente,movil,sms,server,status) VALUES (?,?,?,'1','0')""",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarAlertBSalidaMail':
				self.cursor.execute("""INSERT INTO t365_BsalidaMail (id_cliente,email,mensaje,server,status) VALUES (?,?,?,'1','0')""",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarTramasEventoSistema':
				self.cursor.execute(" exec jssp_InsertarTramaSistema ?,?,?,?,?,?,?,?,? ",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarGrupoCodigoAlarma':
				self.cursor.execute("""INSERT INTO t365_GrupoCodigosAlarma (Descript) VALUES (?)""",self.datos)
				self.cnxn.commit()
			
			elif self.nombrequery == 'InsertarTipoEquipo':
				self.cursor.execute("""INSERT INTO t365_EquiposTipos (id_empresa,descripcion,eliminado) VALUES (1,?,0)""",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarSubTipoEquipo':
				self.cursor.execute("""INSERT INTO t365_EquiposSubTipos (descripcion,id_tipo,monitoreoequipo,eliminado) VALUES (?,?,0,0)""",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarMarcaEquipos':
				self.cursor.execute("""INSERT INTO t365_EquiposMarcas (descripcion,eliminado) VALUES (?,0)""",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarModeloEquipos':
				self.cursor.execute("""INSERT INTO t365_EquiposModelos (id_subtipo_marca,descripcion,string_acceso,id_manual_help,id_manual_user,id_manual_prog,id_manual_insta,eliminado) VALUES (?,?,?,Null,Null,Null,Null,0)""",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarIDSubTipoMarca':
				self.cursor.execute("""INSERT INTO t365_EquiposSubTipos_Marcas (id_marca,id_subtipo) VALUES (?,?)""",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarPuntoTagCliente':
				self.cursor.execute("""INSERT INTO t365_ClientesPuntos (id_cliente,id_punto) VALUES (?,?)""",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'InsertarRelacionZonaCCTV':
				self.cursor.execute("""INSERT INTO t365_ClienteZonasCCTV (id_zona,id_channel) VALUES (?,?)""",self.datos)
				self.cnxn.commit()

		except:
			pass
	def QuerysSelect(self):
		try:
			if self.nombrequery == 'SenalesUltimas20Cliete':
				self.cursor.execute("SELECT TOP 20 CASE WHEN evento +' - ' + descript IS NULL THEN evento ELSE evento +' - ' + descript END  as descript, UserZona, fecha, Fecha_proc, web_color,id_trama FROM v365_HistorialSenales WHERE (cliente = ?) ORDER BY fecha DESC",self.datos)
				self.resultado = self.cursor.fetchall()
				
			elif self.nombrequery == 'UsuariosClienteProcesarSenal':
				self.cursor.execute("""SELECT id_user,nombre + ' ' + apellido AS nombre , email , movil, clavevoz FROM t365_Usuarios WHERE id_cliente = ? AND id_user < 500 ORDER BY CASE WHEN ISNUMERIC(id_user) = 1 THEN 0 ELSE 1 END,
		CASE WHEN ISNUMERIC(id_user) = 1 THEN CAST(id_user AS INT) ELSE 0 END""",self.datos)
				self.resultado = self.cursor.fetchall()


			elif self.nombrequery == 'SeleccionarNombreRondaAlerta':
				self.cursor.execute("""SELECT Nombre FROM [t365_Rondas] WHERE id_ronda = ? and id_cliente = ?""",self.datos)
				self.resultado = self.cursor.fetchall()
	
			elif self.nombrequery == 'SeleccionarNombreCuentaAlerta':
				self.cursor.execute("""SELECT [nombre_cliente] FROM [t365_Clientes] WHERE id_cliente = ?""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarCamarasClienteZona':
				self.cursor.execute("""SELECT t365_ClientesCCTV.descripcion, t365_ClientesCCTV.id_tipo, t365_ClientesCCTV.ip, t365_ClientesCCTV.puerto, t365_ClientesCCTV.usuario, t365_ClientesCCTV.clave, t365_ClientesCCTV.id_modo, t365_ClientesCCTV.id_cctv, t365_ClientesCCTV.id_marca, t365_ClientesCCTV.id_modelo FROM t365_ClientesCCTV INNER JOIN t365_ClientesCCTV_Channel ON t365_ClientesCCTV.id_cctv = t365_ClientesCCTV_Channel.id_cctv INNER JOIN t365_ClienteZonasCCTV ON t365_ClientesCCTV_Channel.id_channel = t365_ClienteZonasCCTV.id_channel WHERE (t365_ClientesCCTV.id_cliente = ?) group by t365_ClientesCCTV.descripcion, t365_ClientesCCTV.id_tipo, t365_ClientesCCTV.ip, t365_ClientesCCTV.puerto, t365_ClientesCCTV.usuario, t365_ClientesCCTV.clave, t365_ClientesCCTV.id_modo, t365_ClientesCCTV.id_cctv, t365_ClientesCCTV.id_marca, t365_ClientesCCTV.id_modelo""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'ZonasPuntosClienteReporteFicha':
				self.cursor.execute("SELECT id_zona, descrip as str_zona,ubicacion FROM t365_ClienteZonas where id_cliente = ? ORDER BY CASE WHEN ISNUMERIC(id_zona) = 1 THEN 0 ELSE 1 END, CASE WHEN ISNUMERIC(id_zona) = 1 THEN CAST(id_zona AS INT) ELSE 0 END",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarCanalesIDCCTVZona':
				self.cursor.execute("""SELECT        t365_ClientesCCTV_Channel.id_channel, t365_ClientesCCTV_Channel.id_cctv, t365_ClientesCCTV_Channel.channel, t365_ClientesCCTV_Channel.descripcion FROM            t365_ClientesCCTV_Channel INNER JOIN
						 t365_ClienteZonasCCTV ON t365_ClientesCCTV_Channel.id_channel = t365_ClienteZonasCCTV.id_channel WHERE        (t365_ClientesCCTV_Channel.id_cctv = ?)""",self.datos)
				self.resultado = self.cursor.fetchall()


			elif self.nombrequery == 'UltimoPK':
				self.cursor.execute('SELECT @@identity')
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'LoginPersonal':
				self.cursor.execute('SELECT        o.idPersonal, o.nombre, o.id_empresa, o.correo, e.id_pais, e.nombre AS NameEmpresa, e.web, o.estatus, e.master, e.logo, e.direccion, o.imagen, e.webTheme, o.webTheme AS themePer, e.webThemeSoport,  o.WebThemeSoport AS themeSoportPer, o.id_perfil, e.correlativo_ordenes_cont, e.correlativo_ordenes_ini, e.correosHombre, e.timeNotifiHombre, e.timeHombreM, e.timeAlertPen, e.monitorea, e.longuitud,  e.latitud, e.puerto, e.ip, e.rif, e.status, e.clave, e.login, e.email, e.telefonos FROM  t365_Personal AS o INNER JOIN t365_Empresas AS e ON o.id_empresa = e.id_empresa WHERE (o.usuario COLLATE Latin1_General_CS_AS = ?) AND (o.clave COLLATE Latin1_General_CS_AS = ?) AND (o.eliminado=0)',self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'ListarClientesIDNombre':
				self.cursor.execute('SELECT  id_cliente, nombre_cliente,cuenta,prefijo,tipocuenta FROM t365_Clientes ORDER BY CASE WHEN ISNUMERIC(cuenta) = 1 THEN 0 ELSE 1 END, CASE WHEN ISNUMERIC(cuenta) = 1 THEN CAST(cuenta AS INT) ELSE 0 END')
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'ListarClientesTodos':
				self.cursor.execute("SELECT prefijo,cuenta, nombre_cliente, direccion, email,telf_local,id_cliente FROM t365_Clientes ORDER BY CASE WHEN ISNUMERIC(cuenta) = 1 THEN 0 ELSE 1 END, CASE WHEN ISNUMERIC(cuenta) = 1 THEN CAST(cuenta AS INT) ELSE 0 END")
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'ListarClientesTodosLike':
				self.cursor.execute("SELECT  prefijo,cuenta, nombre_cliente, direccion, email,telf_local FROM t365_Clientes where nombre_cliente like ? or cuenta like ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'self.datosPanelCliente':
				self.cursor.execute("""SELECT        E.latitud AS LatiEmpresa, E.longuitud AS LongiEmpresa, E.nombre AS Empresa, C.cuenta, C.prefijo, C.id_cliente, C.latitud, C.longitud, C.rif, C.clave, C.fechinicio, t365_StatusCliente.Descrip AS StatusC, 
							 TC.descrip AS TipoC, P.descrip AS Protocolo, TA.descripcion AS Modelo, C.nombre_cliente, C.ciudad, C.direccion, C.referencia, C.telf_local, C.imagen AS pic, C.telf_fax, C.telf_movil, C.email, C.web_site, 
							 CASE WHEN CAST(C.fecha_corte AS varchar(20)) IS NULL THEN 'Sin fecha de corte' ELSE CAST(C.fecha_corte AS varchar(20)) END AS fecha_corte,
								 (SELECT        manual_file
								   FROM            t365_EquiposManuales AS m
								   WHERE        (id_tipo_manual = 1) AND (id_manual = TA.id_manual_help)) AS manu_help, C.login, C.clave AS Expr1, C.status_web, TC.img AS icon, pa.descripcion AS pais, es.descripcion AS estado, 
							 C.clavemaster, t365_EquiposMarcas.descripcion AS Marca, t365_EquiposSubTipos_Marcas.id_marca
	FROM            t365_EquiposMarcas INNER JOIN
							 t365_EquiposSubTipos_Marcas ON t365_EquiposMarcas.id_marca = t365_EquiposSubTipos_Marcas.id_marca INNER JOIN
							 t365_EquiposModelos AS TA ON t365_EquiposSubTipos_Marcas.id_subtipo_marca = TA.id_subtipo_marca RIGHT OUTER JOIN
							 t365_Paises AS pa INNER JOIN
							 t365_PaisEstados AS es ON pa.id_pais = es.id_pais RIGHT OUTER JOIN
							 t365_Clientes AS C INNER JOIN
							 t365_Protocolos AS P ON C.id_protocolo = P.id_protocolo ON es.id_estado = C.id_estado LEFT OUTER JOIN
							 t365_Empresas AS E ON C.id_empresa = E.id_empresa LEFT OUTER JOIN
							 t365_StatusCliente ON C.id_status = t365_StatusCliente.id_Status LEFT OUTER JOIN
							 t365_TypeCliente AS TC ON C.id_type_cliente = TC.id_type_empresa ON TA.id_modelo = C.modelo
	WHERE        (C.id_cliente = ?)""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'ZonasPuntosCliente':
				self.cursor.execute("SELECT id_zona, descrip as str_zona,ubicacion,id FROM t365_ClienteZonas where id_cliente = ? ORDER BY CASE WHEN ISNUMERIC(id_zona) = 1 THEN 0 ELSE 1 END, CASE WHEN ISNUMERIC(id_zona) = 1 THEN CAST(id_zona AS INT) ELSE 0 END",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'UsuariosCliente':
				self.cursor.execute("""SELECT id_user,nombre + ' ' + apellido AS nombre , email , movil FROM t365_Usuarios WHERE id_cliente = ? AND id_user < 500 ORDER BY CASE WHEN ISNUMERIC(id_user) = 1 THEN 0 ELSE 1 END,
		CASE WHEN ISNUMERIC(id_user) = 1 THEN CAST(id_user AS INT) ELSE 0 END""",self.datos)
				self.resultado = self.cursor.fetchall()
			
			elif self.nombrequery == 'self.datosUsuarioCliente':
				self.cursor.execute("SELECT * FROM t365_Usuarios u WHERE (id_user = ?) AND (id_cliente = ?)",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'ContactosEmergenciaCliente':
				self.cursor.execute("SELECT numero, descript, observacion, id_numero from t365_NumEmergencia  WHERE (id_cliente = ?)",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'ContactosEmergenciaClienteFichaCliente':
				self.cursor.execute("SELECT numero, descript, observacion from t365_NumEmergencia  WHERE (id_cliente = ?)",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'ContactoEmergenciaself.datos':
				self.cursor.execute("SELECT * FROM t365_NumEmergencia  WHERE id_cliente = ? AND numero = ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'VerificarContactoEmergencia':
				self.cursor.execute("SELECT descript,numero FROM t365_NumEmergencia where id_cliente = ? and numero = ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'DiasSMSCliente':
				self.cursor.execute("SELECT DISTINCT TOP 31 CAST(CAST(send_date AS varchar(11)) AS smalldatetime) AS fech FROM t365_MensajesSend WHERE id_cliente = ? ORDER BY fech DESC",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'MensajesEnviandosClienteFecha':
				self.cursor.execute("SELECT  movil, send_date, sms FROM t365_MensajesSend WHERE CAST(send_date AS DATE ) = ? AND status = 1 AND id_cliente = ? ORDER BY send_date DESC ",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'DiasSenalesCliente':
				self.cursor.execute("SELECT DISTINCT TOP 20 CAST(LEFT(fecha, 12)  AS SMALLDATETIME) AS fechaSalida FROM t365_Tramas WHERE (cliente = ?) ORDER BY fechaSalida DESC",self.datos)
				self.resultado = self.cursor.fetchall()
			
			elif self.nombrequery == 'SenalesClienteFecha':
				self.cursor.execute("SELECT CASE WHEN evento +' - ' + descript IS NULL THEN evento ELSE evento +' - ' + descript END  as descript, UserZona, fecha, Fecha_proc, web_color, id_trama FROM v365_HistorialSenales WHERE cliente = ? AND CAST(fecha AS DATE ) = ? ORDER BY fecha DESC ",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SenalesUltimas100Cliete':
				self.cursor.execute("SELECT TOP 100 CASE WHEN evento +' - ' + descript IS NULL THEN evento ELSE evento +' - ' + descript END  as descript, UserZona, fecha, Fecha_proc, web_color,id_trama FROM v365_HistorialSenales WHERE (cliente = ?) ORDER BY fecha DESC",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'NotasCliente':
				self.cursor.execute("SELECT top 1 IdNota,NotaFija,NotaTemp, CAST(CONVERT(NVARCHAR, FechaIni, 112) AS DATETIME)  AS FechaIni, CAST(CONVERT(NVARCHAR, FechaFin, 112) AS DATETIME) AS FechaFin FROM t365_NotasClientes WHERE (IdCliente = ?) ORDER BY IdNota DESC",self.datos)
				self.resultado = self.cursor.fetchall()
			
			elif self.nombrequery == 'HorariosClienteTodos':
				#Ojo la interfaz no concuerda con la base de self.datos, hice una copia del Web pero en la BD
				#Puede ser distinto el dia de apertura que el de cierre pero aqui no lo permite porque en el web tampoco
				self.cursor.execute("SELECT Id, diaapertura, horaapertura, horacierre FROM t365_HorariosOC WHERE (id_cliente = ?) and borrar = 0 ",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'HorariosClienteTodosFichaCliente':
				#Ojo la interfaz no concuerda con la base de self.datos, hice una copia del Web pero en la BD
				#Puede ser distinto el dia de apertura que el de cierre pero aqui no lo permite porque en el web tampoco
				self.cursor.execute("SELECT diaapertura, horaapertura, horacierre FROM t365_HorariosOC WHERE (id_cliente = ?) and borrar = 0 ",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'HorariosClienteDia':
				#Ojo la interfaz no concuerda con la base de self.datos, hice una copia del Web pero en la BD
				#Puede ser distinto el dia de apertura que el de cierre pero aqui no lo permite porque en el web tampoco
				self.cursor.execute("SELECT Id, diaapertura, horaapertura, horacierre FROM t365_HorariosOC WHERE id_cliente = ? AND diaapertura = ? AND Borrar = 0 ",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'PlanesProtocoloCliente':
				self.cursor.execute(" SELECT p.* FROM t365_Clientes c INNER JOIN t365_Planes p ON c.id_protocolo = p.id_protocolo WHERE c.id_cliente = ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'EventosDetalleCliente':
				self.cursor.execute(" SELECT EP.cod_evento, E.descript FROM t365_Clientes C INNER JOIN t365_Planes P ON C.id_protocolo = P.id_protocolo   INNER JOIN t365_EventosPlanes EP ON P.id_plan = EP.id_plan AND P.id_protocolo = EP.id_protocolo INNER JOIN t365_Eventos E ON EP.cod_evento = E.cod_event AND EP.id_protocolo = E.id_protocolo WHERE (C.id_cliente = ?) AND (P.id_plan = ?)",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'TodosUsuariosEventosCliente':
				self.cursor.execute("SELECT DISTINCT t365_Usuarios.nombre + ' ' + t365_Usuarios.apellido AS nombrecompleto, t365_Usuarios.* FROM  t365_Usuarios INNER JOIN t365_ClienteEventos ON t365_Usuarios.id_cliente =   t365_ClienteEventos.id_cliente AND t365_Usuarios.id_user = t365_ClienteEventos.id_user   WHERE (t365_Usuarios.id_cliente = ?) AND (t365_Usuarios.id_user < 500) order by t365_Usuarios.id_user",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'EventosUsuarioCliente':
				self.cursor.execute("SELECT E.cod_event, E.descript, CE.type FROM t365_ClienteEventos CE INNER JOIN t365_Eventos E ON CE.cod_evento = E.cod_event INNER JOIN t365_Clientes C ON CE.id_cliente = C.id_cliente AND  E.id_protocolo = C.id_protocolo WHERE     (CE.id_user = ?) AND (CE.id_cliente = ?) ORDER BY CE.type DESC",self.datos)
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'PlanesUsuariosCliente':
				self.cursor.execute("SELECT EP.*, E.descript FROM t365_Clientes C INNER JOIN t365_Planes P ON C.id_protocolo = P.id_protocolo   INNER JOIN t365_EventosPlanes EP ON P.id_plan = EP.id_plan AND P.id_protocolo = EP.id_protocolo INNER JOIN t365_Eventos E ON EP.cod_evento = E.cod_event AND EP.id_protocolo = E.id_protocolo WHERE (C.id_cliente =?) AND (P.id_plan =?)",self.datos)
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'NombrePlan':
				self.cursor.execute("SELECT descrip FROM t365_Planes where id_plan = ?",self.datos)
				self.resultado = self.cursor.fetchall()	
		
			elif self.nombrequery == 'self.datosReceptores':
				self.cursor.execute("SELECT descrip FROM t365_Planes where id_plan = ?",self.datos)
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'self.datosAsociados':
				self.cursor.execute("SELECT nombre, email, status, id_asociado, direccion, telef_contacto, id_empresa,usuario, clave  FROM t365_asociados where id_empresa = ?",self.datos)
				self.resultado = self.cursor.fetchall()	
			
			elif self.nombrequery == 'CantidadAsociadosAbonados':
				self.cursor.execute("SELECT COUNT(*) AS Total FROM   t365_asociados_abonados  WHERE (id_asociado = ?) AND (id_empresa = ?)",self.datos)
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'AbonadosEnGrupo':
				self.cursor.execute("SELECT CONVERT(varchar(10),t365_Clientes.prefijo)+'-'+CONVERT(varchar(10),t365_Clientes.cuenta) as cuent,t365_Clientes.nombre_cliente, t365_Clientes.id_cliente as nombre FROM  t365_asociados_abonados ASO INNER JOIN  t365_Clientes ON ASO.id_cliente = t365_Clientes.id_cliente  WHERE  ASO.id_asociado = ?",self.datos)
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'AbonadosSinGrupo':
				self.cursor.execute("SELECT  CONVERT(varchar(10),t365_Clientes.prefijo)+'-'+CONVERT(varchar(10),t365_Clientes.cuenta)as cuent,  nombre_cliente, id_cliente FROM t365_Clientes WHERE (id_cliente NOT IN (SELECT  id_cliente FROM  t365_asociados_abonados   WHERE id_asociado =  ?)) order by id_cliente asc",self.datos)
				self.resultado = self.cursor.fetchall()	
			
			elif self.nombrequery == 'VerificarUsuarioAsociado':
				self.cursor.execute("SELECT * FROM t365_asociados WHERE (usuario = ? ) ",self.datos)
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'Paises':
				self.cursor.execute("SELECT * FROM t365_Paises  order by descripcion asc")
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'EstadosPaises':
				self.cursor.execute(" SELECT * FROM t365_PaisEstados where id_pais=?  order by descripcion asc",self.datos)
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'Protocolos':
				self.cursor.execute("SELECT descrip, id_protocolo FROM t365_Protocolos")
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'TiposClientes':
				self.cursor.execute("SELECT id_type_empresa, descrip FROM t365_TypeCliente")
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'TiposClientesPorDispositivo':
				self.cursor.execute("SELECT id_type_empresa, descrip FROM t365_TypeCliente WHERE id_dispositivo = ?",self.datos)
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'Empresas':
				self.cursor.execute("SELECT id_empresa, nombre FROM t365_Empresas")
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'VistaValidarLoginGeneral':
				self.cursor.execute("SELECT login FROM v365_ValidarLogins where login = ?",self.datos)
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'VerificarAbonado':
				self.cursor.execute("SELECT id_cliente,prefijo,cuenta FROM t365_Clientes WHERE (prefijo = ? and cuenta = ? ) ",self.datos)
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'EstatusGenerales':
				self.cursor.execute("SELECT * FROM t365_StatusGeneral ")
				self.resultado = self.cursor.fetchall()
			
			elif self.nombrequery == 'VerificarZona':
				self.cursor.execute("SELECT cast(id_zona as int) as id_zona, descrip  FROM  t365_ClienteZonas where (id_zona=?) AND (id_cliente =?)",self.datos)
				self.resultado = self.cursor.fetchall()	
			
			elif self.nombrequery == 'VerificarPunto':
				self.cursor.execute("SELECT id_zona, descrip  FROM  t365_ClienteZonas where (id_zona=?) AND (id_cliente =?)",self.datos)
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'VerificarUsuario':
				self.cursor.execute("SELECT cast(id_user as int) as id_user, nombre + ' ' + apellido AS nombre  FROM  t365_Usuarios where (id_user=?) AND (id_cliente =?)",self.datos)
				self.resultado = self.cursor.fetchall()			

			elif self.nombrequery == 'TiposUsuarioClientes': 
				self.cursor.execute("SELECT id_type_user, descrip FROM t365_TypeUser t order by id_type_user asc")
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'FrecuenciaEmail': 
				self.cursor.execute("SELECT id_frecuencia, descripcion FROM t365_FrecuenciaEmail order by descripcion")
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'SeleccionarUnHorario': 
				self.cursor.execute("SELECT * FROM   t365_HorariosOC WHERE  id_cliente = ?  and Id = ?",self.datos)
				self.resultado = self.cursor.fetchall()		

			elif self.nombrequery == 'ClientesSinImagen': 
				self.cursor.execute("SELECT  CONVERT(varchar(10),c.prefijo)+'-'+CONVERT(varchar(10),c.cuenta)as cuent, nombre_cliente, id_cliente FROM t365_Clientes c WHERE (id_cliente > 0) AND  (imagen IS NULL OR imagen = '')")
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'ListaTiposCliente': 
				self.cursor.execute("SELECT id_type_empresa, descrip, img, id_dispositivo, id_empresa FROM t365_TypeCliente Where id_empresa = ? or id_empresa = 0",self.datos)
				self.resultado = self.cursor.fetchall()
			
			elif self.nombrequery == 'VerificarIDTipoCliente': 
				self.cursor.execute("SELECT  descrip, id_type_empresa FROM t365_TypeCliente WHERE  id_type_empresa = ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'UnTipoCliente': 
				self.cursor.execute("SELECT TOP 1 id_type_empresa, descrip, img FROM t365_TypeCliente WHERE id_type_empresa = ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'DepartamentosEmpresa': 
				self.cursor.execute("SELECT idDepartamento, nombre, correo FROM t365_DepartamentosEmpresa WHERE idEmpresa = ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'UnDepartamentosEmpresa': 
				self.cursor.execute("SELECT idDepartamento, nombre, correo FROM t365_DepartamentosEmpresa WHERE idDepartamento = ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'UnDepartamentosNombreEmpresa': 
				self.cursor.execute("SELECT idDepartamento, nombre, correo FROM t365_DepartamentosEmpresa WHERE nombre = ? and idEmpresa = ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'GruposdeAlarmas': 
				self.cursor.execute("SELECT * FROM t365_GrupoCodigosAlarma",self.datos)
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'GruposCodigodeAlarmasUno': 
				self.cursor.execute("SELECT * FROM t365_GrupoCodigosAlarma WHERE Descript = ?",self.datos)
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'SenalesBusquedaAvanzada':
				self.cursor.execute("SELECT CASE WHEN evento +' - ' + descript IS NULL THEN evento ELSE evento +' - ' + descript END  as descript, UserZona, fecha, Fecha_proc, web_color, id_trama FROM v365_HistorialSenales WHERE cliente = ? AND CAST(fecha AS DATE ) >= ? AND CAST(fecha AS DATE ) <= ? AND idGrupo = ?  ORDER BY fecha DESC ",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'TiposAlarmas':
				self.cursor.execute("SELECT id_Alarma,Descrip FROM t365_TypeAlarma order by Descrip")
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'UnTipoAlarma':
				self.cursor.execute("SELECT id_Alarma, Descrip, id_manual_help, id_manual_user, id_manual_prog FROM t365_TypeAlarma  where id_Alarma = ?",self.datos)
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'StatusPanel':
				self.cursor.execute("SELECT * FROM t365_StatusPanelCliente where idCliente = ?",self.datos)
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'self.datosClienteParaMapa':
				self.cursor.execute("SELECT latitud,longitud FROM t365_Clientes where id_cliente= ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'TramasPorProcesarOperador':
				self.cursor.execute('''SELECT TOP 1000 [cuen],[NameCliente],[StrEvento],[UserZona],[fecha],[web_color],[id_trama],[web_colorBg],[protocolo],[Linea],[descrip],[type_evento],[evento],[cliente],[Variante],[color],[colorBg],[Obser],[idGrupo],[status],[id_empresa],[direccion],[referencia],[latitud],[longitud],[clavemaster],[id_type_cliente],[img],[telf_local],[pic],[codAlrm],[codDesc],[staPanel],[fechaStatusp],[nombreempresa],[movil],[id_cliente],[IdOperador]
	  FROM v365_TramasPorProcesar WHERE  IdOperador = ? order by id_trama desc
	''',self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'TramasPendientesOperador':
				self.cursor.execute('''SELECT  [cuen]
			,[NameCliente],[StrEvento],[UserZona],[fecha],[web_color],[id_trama],[web_colorBg],[protocolo],[Linea],[descrip],[type_evento],[evento],[cliente],[Variante],[color],[colorBg],[Obser],[idGrupo],[status],[id_empresa],[direccion],[referencia],[latitud],[longitud],[clavemaster],[id_type_cliente],[img],[telf_local],[pic],[codAlrm],[codDesc],[staPanel],[fechaStatusp],[nombreempresa],[movil],[id_cliente],[IdOperador]
	  FROM v365_TramasPendientes WHERE  (IdOperador = ?) ORDER BY id_trama DESC''',self.datos)
				self.resultado = self.cursor.fetchall()


			elif self.nombrequery == 'MonitoreoEstatico':  #Log Senales
				self.cursor.execute('''SELECT TOP 100 [cuen],[NameCliente],[StrEvento],[UserZona],[fecha],[color] as web_color,[colorBg] as web_colorBg,[id_trama],[codEvento],[pic],[CodProtocolo],[EmpresaMonitorea],[cliente]
	  FROM [v365_MonitoreoEstatico] WHERE (EmpresaMonitorea = ?) ORDER BY id_trama DESC''',self.datos)
				self.resultado = self.cursor.fetchall()



			elif self.nombrequery == 'TramasProcesadas':  
				self.cursor.execute('''SELECT TOP 100 [cuen],[NameCliente],[StrEvento],[UserZona],[Obser],[fecha],[Fecha_proc],[color],[id_trama],[colorBg],[pic],[TipoEvento],[CodProtocolo],[IdOperador],[operador],[EmpresaMonitorea]
	  FROM v365_TramasProcesadas WHERE (EmpresaMonitorea = ?) ORDER BY Fecha_proc DESC, id_trama DESC''',self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'ComprobarExisteOperadorSession': #Saber si existo en la Tabla de OperadorSession
				self.cursor.execute("SELECT TOP 1 [IdOperador] FROM [t365_OperadorSession] where IdOperador = ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'self.datosClienteSenalMonitoreo':
				self.cursor.execute("""SELECT t365_Clientes.id_cliente,t365_Clientes.nombre_cliente, t365_TramasPorProcesar.fecha, t365_Clientes.direccion, t365_Clientes.referencia, 
							 t365_StatusPanelCliente.cod_alarm AS StatusPanel, t365_StatusPanelCliente.Fecha AS fechastatuspanel, t365_TramasPorProcesar.user_zone, 
							 t365_TramasPorProcesar.evento, t365_Empresas.nombre AS nameempresa, t365_Clientes.telf_local, t365_Clientes.telf_movil, t365_Clientes.clavemaster, 
							 t365_Eventos.descript
	FROM            t365_Clientes INNER JOIN
							 t365_TramasPorProcesar ON t365_Clientes.id_cliente = t365_TramasPorProcesar.cliente INNER JOIN
							 t365_StatusPanelCliente ON t365_Clientes.id_cliente = t365_StatusPanelCliente.idCliente INNER JOIN
							 t365_Empresas ON t365_Clientes.id_empresa = t365_Empresas.id_empresa INNER JOIN
							 t365_Eventos ON t365_TramasPorProcesar.evento = t365_Eventos.cod_event
	WHERE        (t365_TramasPorProcesar.id_trama =?)""",self.datos)
				self.resultado = self.cursor.fetchall()


			elif self.nombrequery == 'MensajesPredefinidosMonitoreo':
				self.cursor.execute("""SELECT mensaje FROM t365_MensajesCierre""")
				self.resultado = self.cursor.fetchall()
		
			elif self.nombrequery == 'MapaClienteMonitoreo':
				self.cursor.execute("""SELECT     c.nombre_cliente, c.latitud AS latclie, c.longitud AS logclie, em.latitud AS latemp , em.longuitud AS logemp, c.direccion AS dirclie, c.referencia AS refclie, e.nombre AS nomemp, c.id_type_cliente, t.img AS icon FROM t365_Clientes c INNER JOIN  t365_Empresas em ON c.id_empresa = em.id_empresa INNER JOIN  t365_Empresas e ON em.id_empresa = e.id_empresa INNER JOIN t365_TypeCliente t ON c.id_type_cliente = t.id_type_empresa WHERE (c.id_cliente = ?)""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'NumerosEmergenciaMonitoreo':
				self.cursor.execute("""SELECT numero, descript, observacion FROM t365_NumEmergencia WHERE (id_cliente = ?)""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'TimeLineSenal':
				self.cursor.execute("""SELECT t365_TramasObservaciones.fecha, t365_TramasObservaciones.observacion , (CAST(t365_TramasObservaciones.idoperador as varchar(10))) +' - ' + (t365_Personal.nombre ) FROM t365_TramasObservaciones INNER JOIN t365_Personal ON t365_TramasObservaciones.idoperador = t365_Personal.idPersonal WHERE (t365_TramasObservaciones.idtrama = ?) ORDER BY t365_TramasObservaciones.fecha DESC""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'OperadoresActivosWeb':   #Para verificar los operadores que estan activos en el web por Base de self.datos
				self.cursor.execute("SELECT IdOperador, Ip, StatusMonitoreo FROM t365_OperadorSession where statuslogin = 1")
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'CierreSenalPorCliente':   #Para verificar los operadores que estan activos en el web por Base de self.datos
				self.cursor.execute("""SELECT        t365_TramasPorProcesar.cliente, t365_Clientes.nombre_cliente
	FROM            t365_TramasPorProcesar INNER JOIN
							 t365_Clientes ON t365_TramasPorProcesar.cliente = t365_Clientes.id_cliente INNER JOIN
							 t365_Eventos ON t365_TramasPorProcesar.evento = t365_Eventos.cod_event
	WHERE        (t365_TramasPorProcesar.IdOperador = ?) group by t365_TramasPorProcesar.cliente,  t365_Clientes.nombre_cliente""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'MapaMonitoreo':   
				self.cursor.execute("""SELECT  [id_cliente],[cuen],[nombre_cliente],[direccion],[referencia],[telf_local],[latitud],[longitud],[imagencliente],[id_type_cliente],[icono],[CodigoEstatusPanel],[FechaEstatusPanel],[cod_event],[DescripcionEvento],[UserZona],[FechaUltimaSenal]
	  FROM v365_MapaUbicacionClientes""")
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarPlanesNotificaciones':
				self.cursor.execute("""SELECT t365_Planes.id_plan, t365_Planes.descrip, t365_Planes.id_protocolo, t365_Protocolos.descrip AS nombreprotocolo
	FROM  t365_Planes INNER JOIN t365_Protocolos ON t365_Planes.id_protocolo = t365_Protocolos.id_protocolo""")
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'EventosPorProtocolo':
				self.cursor.execute("SELECT cod_event, descript, web_color FROM t365_Eventos WHERE id_protocolo = ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'EventosPorPlan':
				self.cursor.execute("SELECT cod_evento FROM t365_EventosPlanes WHERE id_plan = ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarEventos':
				self.cursor.execute("""SELECT t365_Eventos.cod_event, t365_Eventos.id_protocolo, t365_Eventos.descript, t365_Eventos.mensaje, t365_Eventos.type_evento, t365_Eventos.monitorea, 
	 t365_Eventos.cod_alarm, t365_Eventos.orden, t365_Eventos.sonido, t365_Eventos.prioridad, t365_Eventos.web_color, t365_Eventos.web_colorBg, t365_Protocolos.descrip AS nombreprotocolo
	FROM  t365_Eventos INNER JOIN t365_Protocolos ON t365_Eventos.id_protocolo = t365_Protocolos.id_protocolo""")
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'CodigosAlarma':
				self.cursor.execute("""SELECT codigo,descript,web_color,web_colorBg,grupo,idgrupo,prioridad FROM t365_CodigosAlarma""")
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'CodigosAlarmaPorIDGrupo':
				self.cursor.execute("""SELECT codigo,descript,web_color,web_colorBg,grupo,idgrupo,prioridad FROM t365_CodigosAlarma WHERE idgrupo = ?""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarVariables':
				self.cursor.execute("""SELECT descrip FROM t365_Variables""")
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarEvento':
				self.cursor.execute("SELECT cod_event, id_protocolo FROM t365_Eventos WHERE cod_event = ? and id_protocolo = ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'GruposCodigosAlarma':
				self.cursor.execute("SELECT [idGrupo],[Descript],[webColor] FROM t365_GrupoCodigosAlarma")
				self.resultado = self.cursor.fetchall()			

			elif self.nombrequery == 'SeleccionarCodigoAlarma':
				self.cursor.execute("SELECT codigo  FROM t365_CodigosAlarma WHERE codigo = ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarPermisologias':
				self.cursor.execute(" SELECT p.*, a.idAccion, a.descripcion FROM t365_PaginasAdmin p INNER   JOIN t365_PaginasAcciones a ON p.idPagina = a.idPagina  ORDER BY p.orden,p.idPagina,a.orden, p.nombre ",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarPersonal':
				self.cursor.execute("SELECT p.idPersonal, e.nombre as Empresa, t.color, t.descripcion, p.id_empresa, p.idTipoUsuario,p.imagen,p.id_perfil,p.cedula, p.nombre , p.telefono, p.correo, p.Dirreccion, p.Telf_Habitacion, p.usuario, p.clave,p.estatus FROM t365_TiposUsuarios t INNER JOIN  t365_Personal p ON t.idtipoUsuario = p.idTipoUsuario INNER JOIN  t365_Empresas e ON p.id_empresa = e.id_empresa WHERE (p.eliminado = 0)",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarTiposUsuarios':
				self.cursor.execute("SELECT t.*, e.nombre  FROM t365_TiposUsuarios t INNER JOIN t365_Empresas e ON t.idEmpresa = e.id_empresa  WHERE (t.eliminado = 0) ")
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarPermisosUsuario':
				self.cursor.execute("SELECT idPagina,idAccion,idUsuario FROM t365_PermisosAdmin where idUsuario = ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarPersonalUno':
				self.cursor.execute("SELECT  [idPersonal] FROM t365_Personal WHERE usuario = ? AND id_empresa = ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarPerfilesUsuario':
				self.cursor.execute("SELECT * FROM t365_UsuariosPerfil where   (id_perfil NOT IN (3, 5))",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarPermisosTipoUsuario':
				self.cursor.execute("SELECT * FROM t365_PermisosTipoUsuario where (idTipoUsuario=?)",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarTipoUsuarioUno':
				self.cursor.execute("SELECT idtipoUsuario FROM t365_TiposUsuarios WHERE idEmpresa = ? AND id_perfilUsuario = ? AND color = ? AND descripcion = ? ",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarPermisosPorTipoUsuario':
				self.cursor.execute("SELECT [idAccion] FROM t365_PermisosTipoUsuario WHERE idTipoUsuario = ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarEmpresas':
				self.cursor.execute("SELECT * FROM t365_Empresas where id_empresa>0",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarEmpresaUna':
				self.cursor.execute("SELECT  [id_empresa]  FROM [t365_Empresas] WHERE nombre = ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarParentesco':
				self.cursor.execute("SELECT id_type_user, descrip FROM t365_TypeUser t order by id_type_user asc",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarParentescoUno':
				self.cursor.execute("SELECT id_type_user, descrip FROM t365_TypeUser WHERE descrip = ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarMensajesPredefinidos':  #Resoluciones
				self.cursor.execute("SELECT * FROM  t365_MensajesCierre",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarResolucionUna':  #Resoluciones
				self.cursor.execute("SELECT * FROM  t365_MensajesCierre WHERE Mensaje = ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarReceptoresConfigPort':  
				self.cursor.execute("SELECT [PortID],[Descrip],[Config],[type],[Server],[Port],[idReceptor],[Heartbeat],[orden],[Status],[geta],[fechaCreator],[idReceiver],[prefijo] FROM [t365_ConfigPortII]",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarReceptores':  
				self.cursor.execute("SELECT idReceptor,str_receptor,serial,tcpip FROM t365_Receptores",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarReceptoresConfigPortUno':  
				self.cursor.execute("SELECT PortID FROM t365_ConfigPortII where PortID = ?",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarMotivosSoporte':  
				self.cursor.execute("SELECT s.*, d.nombre  FROM t365_SoporteMotivos s INNER JOIN t365_DepartamentosEmpresa d ON s.idDepartCorreo = d.idDepartamento where s.idEmpresa = ? ",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarMotivosSoportePorDepartamento':  
				self.cursor.execute("SELECT *  FROM t365_SoporteMotivos where idDepartCorreo = ? ",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarMotivosSoporteUno':  
				self.cursor.execute("SELECT s.*, d.nombre  FROM t365_SoporteMotivos s INNER JOIN t365_DepartamentosEmpresa d ON s.idDepartCorreo = d.idDepartamento where s.idEmpresa = ? and s.descripcion = ? ",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'LogSenalesMonitoreoAlertas':  
				self.cursor.execute("""SELECT  TOP (100) t365_Protocolos.descrip AS protocolo, CONVERT(varchar(10),T.cliente) +'-'+ C.nombre_cliente AS nombrecliente, E.cod_event +'-'+ E.descript AS StrEvento, CASE WHEN E.type_evento = 0 THEN CASE WHEN
								 (SELECT        U.nombre + ' ' + U.apellido
								   FROM            t365_Usuarios AS U
								   WHERE        T .cliente = U.id_cliente AND T .user_zone = U.cod_user) IS NULL THEN 'Usuario ' + CAST(T .user_zone AS varchar(10)) ELSE
								 (SELECT        T .user_zone + ' - ' + U.nombre + ' ' + U.apellido
								   FROM            t365_Usuarios AS U
								   WHERE        T .cliente = U.id_cliente AND T .user_zone = U.cod_user) END 

	WHEN E.type_evento = 5 THEN CASE WHEN
								 (SELECT prefijo+cuenta+' - '+nombre_cliente FROM t365_Clientes where id_cliente = T.user_zone) IS NULL THEN 'ID ' + CAST(T .user_zone AS varchar(10)) ELSE
								 (SELECT prefijo+cuenta+' - '+nombre_cliente FROM t365_Clientes where id_cliente = T.user_zone) END



								   WHEN E.type_evento = 1 THEN CASE WHEN
								 (SELECT        Z.descrip
								   FROM            t365_ClienteZonas AS Z
								   WHERE        T .cliente = Z.id_cliente AND T .user_zone = Z.id_zona) IS NULL THEN 'Zona ' + CAST(T .user_zone AS varchar(10)) ELSE
								 (SELECT        T .user_zone + ' - ' + Z.descrip
								   FROM            t365_ClienteZonas AS Z
								   WHERE        T .cliente = Z.id_cliente AND T .user_zone = Z.id_zona) END WHEN E.type_evento = 3 THEN CASE WHEN
								 (SELECT        R.nombre
								   FROM            t365_Rondas AS R
								   WHERE        T .cliente = R.id_cliente AND T .user_zone = R.id_ronda) IS NULL THEN 'Ronda ' + CAST(T .user_zone AS varchar(3)) ELSE
								 (SELECT        R.nombre
								   FROM            t365_Rondas AS R
								   WHERE        T .cliente = R.id_cliente AND T .user_zone = R.id_ronda) END WHEN E.type_evento = 2 THEN '' WHEN E.type_evento = 4 THEN T .user_zone END AS UserZona, T.Linea, T.fecha, E.web_color
	FROM            t365_Personal AS p RIGHT OUTER JOIN
							 t365_Eventos AS E INNER JOIN
							 t365_Tramas AS T ON E.cod_event = T.evento AND E.id_protocolo = T.protocolo INNER JOIN
							 t365_Protocolos ON T.protocolo = t365_Protocolos.id_protocolo ON p.idPersonal = T.IdOperador LEFT OUTER JOIN
							 t365_Usuarios AS U ON T.cliente = U.id_cliente AND T.user_zone = U.cod_user LEFT OUTER JOIN
							 t365_ClienteZonas AS Z ON T.cliente = Z.id_cliente AND T.user_zone = Z.id_zona LEFT OUTER JOIN
							 t365_Clientes AS C ON T.cliente = C.id_cliente
	ORDER BY T.id_trama DESC """,self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarMensajesCola':
				self.cursor.execute("""SELECT TOP 200 CONVERT(varchar(10), t365_Clientes.id_cliente)+'-'+ t365_Clientes.nombre_cliente AS nombrecliente, t365_BsalidaSpeed.movil, t365_BsalidaSpeed.sms AS mensaje , t365_BsalidaSpeed.fecha_creada AS fecha
	FROM t365_BsalidaSpeed LEFT OUTER JOIN t365_Clientes ON t365_BsalidaSpeed.id_cliente = t365_Clientes.id_cliente WHERE t365_BsalidaSpeed.status = 0 order by t365_BsalidaSpeed.id_salida desc""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarMensajesEnviado':
				self.cursor.execute("""SELECT TOP 20 CONVERT(varchar(10), t365_Clientes.id_cliente)+'-'+ t365_Clientes.nombre_cliente AS nombrecliente, t365_BsalidaSpeed.movil, t365_BsalidaSpeed.sms AS mensaje , t365_BsalidaSpeed.fecha_creada AS fecha
	FROM t365_BsalidaSpeed LEFT OUTER JOIN t365_Clientes ON t365_BsalidaSpeed.id_cliente = t365_Clientes.id_cliente WHERE t365_BsalidaSpeed.status = 1 order by t365_BsalidaSpeed.id_salida desc""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarMensajesRecibidos':
				self.cursor.execute("""SELECT TOP 50  movil,sms,fecha  FROM t365_Bentrada ORDER BY fecha desc""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarCamarasCliente':
				self.cursor.execute("""SELECT [descripcion] , [id_tipo],[ip],[puerto],[usuario],[clave],[id_modo] ,[id_cctv],[id_marca],[id_modelo]
	  FROM [t365_ClientesCCTV] WHERE [id_cliente] = ?""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarMarcasPorIDSubTipo':
				self.cursor.execute("""SELECT t365_EquiposMarcas.descripcion, t365_EquiposMarcas.id_marca, t365_EquiposSubTipos.id_subtipo
	FROM            t365_EquiposMarcas INNER JOIN
							 t365_EquiposSubTipos_Marcas ON t365_EquiposMarcas.id_marca = t365_EquiposSubTipos_Marcas.id_marca INNER JOIN
							 t365_EquiposSubTipos ON t365_EquiposSubTipos_Marcas.id_subtipo = t365_EquiposSubTipos.id_subtipo
	WHERE        (t365_EquiposSubTipos.id_subtipo = ?)""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarMarcasEquipos':
				self.cursor.execute("""SELECT id_marca,descripcion FROM t365_EquiposMarcas where eliminado = 0""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarMarcasEquiposPorNombre':
				self.cursor.execute("""SELECT id_marca,descripcion FROM t365_EquiposMarcas where descripcion = ?""",self.datos)
				self.resultado = self.cursor.fetchall()


			elif self.nombrequery == 'SeleccionarModelosCCTV':
				self.cursor.execute("""SELECT        t365_EquiposModelos.id_modelo, t365_EquiposModelos.descripcion, t365_EquiposModelos.string_acceso, t365_EquiposSubTipos_Marcas.id_marca
	FROM            t365_EquiposModelos INNER JOIN
							 t365_EquiposSubTipos_Marcas ON t365_EquiposModelos.id_subtipo_marca = t365_EquiposSubTipos_Marcas.id_subtipo_marca""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarModelosPorMarca':
				self.cursor.execute("""SELECT        t365_EquiposModelos.id_modelo, t365_EquiposModelos.descripcion
	FROM            t365_EquiposModelos INNER JOIN
							 t365_EquiposSubTipos_Marcas ON t365_EquiposModelos.id_subtipo_marca = t365_EquiposSubTipos_Marcas.id_subtipo_marca INNER JOIN
							 t365_EquiposSubTipos ON t365_EquiposSubTipos_Marcas.id_subtipo = t365_EquiposSubTipos.id_subtipo
	WHERE        (t365_EquiposSubTipos_Marcas.id_marca = ?) AND (t365_EquiposSubTipos.id_subtipo = ?)""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarSubTiposCCTV':
				self.cursor.execute("""SELECT [id_subtipo],[descripcion] FROM [t365_EquiposSubTipos] where id_subtipo = 1 OR id_subtipo = 2 OR id_subtipo = 3""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarModoCCTV':
				self.cursor.execute("""SELECT [id_modo],[descripcion] FROM [t365_CCTVModoRegistro]""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarCanalesIDCCTV':
				self.cursor.execute("""SELECT id_channel,id_cctv,channel,descripcion FROM t365_ClientesCCTV_Channel where id_cctv = ?""",self.datos)
				self.resultado = self.cursor.fetchall()
			
			elif self.nombrequery == 'SeleccionarStringPorModelo':
				self.cursor.execute("""SELECT string_acceso FROM t365_EquiposModelos WHERE id_modelo = ?""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarCCTVClienteUno':
				self.cursor.execute("""SELECT [id_cctv],[descripcion] FROM [t365_ClientesCCTV] WHERE [descripcion] = ? and [id_cliente] = ?""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarCamarasPorID':
				self.cursor.execute("""SELECT [id_cliente],[descripcion] , [id_tipo],[ip],[puerto],[usuario],[clave],[id_modo],[id_marca],[id_modelo]
	  FROM [t365_ClientesCCTV] WHERE[id_cctv]  = ?""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarPrefijosNoRepetidos':
				self.cursor.execute("""SELECT DISTINCT prefijo FROM t365_ConfigPort_Lineas""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarPrefijosRangosEmpresa':
				self.cursor.execute("""SELECT idRango,prefijo,IniRango,FinRango FROM t365_EmpresasRangoClientes WHERE id_empresa = ?""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarPrefijosLineas':
				self.cursor.execute("""SELECT id_linea,linea,PortID,descripcion,prefijo FROM t365_ConfigPort_Lineas""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarSubTiposDispositivosCuentas':
				self.cursor.execute("""SELECT [id_subtipo],[descripcion] FROM t365_EquiposSubTipos WHERE monitoreoequipo = 1""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarClientesUltimaAperturaCierreGeneral':
				self.cursor.execute("""SELECT c.id_cliente, c.nombre_cliente,c.prefijo,c.cuenta, c.direccion, c.telf_local, sp.cod_alarm,  
		CONVERT(DATETIME, sp.Fecha, 100) AS fecha, DATEDIFF(day, sp.Fecha, GETDATE()) AS Dif,case when sp.cod_alarm='CIE' then 'Cierre' when 
		sp.cod_alarm='APE' then 'Apertura' when sp.cod_alarm is null then'Sin transmision'end as status   FROM t365_Clientes AS c LEFT OUTER JOIN t365_StatusPanelCliente 
		AS sp ON c.id_cliente=sp.idCliente ORDER BY DATEDIFF(day, sp.Fecha, GETDATE()) desc""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarClientesUltimaAperturaCierreGeneralLike':
				self.cursor.execute("""SELECT c.id_cliente, c.nombre_cliente,c.prefijo,c.cuenta, c.direccion, c.telf_local, sp.cod_alarm,  
		CONVERT(DATETIME, sp.Fecha, 100) AS fecha, DATEDIFF(day, sp.Fecha, GETDATE()) AS Dif,case when sp.cod_alarm='CIE' then 'Cierre' when 
		sp.cod_alarm='APE' then 'Apertura' when sp.cod_alarm is null then'Sin transmision'end as status   FROM t365_Clientes AS c LEFT OUTER JOIN t365_StatusPanelCliente 
		AS sp ON c.id_cliente=sp.idCliente WHERE (id_cliente like ? or nombre_cliente like ?) ORDER BY DATEDIFF(day, sp.Fecha, GETDATE()) desc  """,self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarClientesUltimaAperturaCierreParam':
				self.cursor.execute("""SELECT c.id_cliente, c.nombre_cliente,c.prefijo,c.cuenta, c.direccion, c.telf_local, sp.cod_alarm,  
		CONVERT(DATETIME, sp.Fecha, 100) AS fecha, DATEDIFF(day, sp.Fecha, GETDATE()) AS Dif,case when sp.cod_alarm='CIE' then 'Cierre' when 
		sp.cod_alarm='APE' then 'Apertura' when sp.cod_alarm is null then'Sin transmision'end as status   FROM t365_Clientes AS c LEFT OUTER JOIN t365_StatusPanelCliente 
		AS sp ON c.id_cliente=sp.idCliente WHERE cod_alarm %s ORDER BY DATEDIFF(day, sp.Fecha, GETDATE()) desc """%self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarClientesUltimaAperturaCierreParamLike':
				self.cursor.execute("""SELECT c.id_cliente, c.nombre_cliente,c.prefijo,c.cuenta, c.direccion, c.telf_local, sp.cod_alarm,  
		CONVERT(DATETIME, sp.Fecha, 100) AS fecha, DATEDIFF(day, sp.Fecha, GETDATE()) AS Dif,case when sp.cod_alarm='CIE' then 'Cierre' when 
		sp.cod_alarm='APE' then 'Apertura' when sp.cod_alarm is null then'Sin transmision'end as status   FROM t365_Clientes AS c LEFT OUTER JOIN t365_StatusPanelCliente 
		AS sp ON c.id_cliente=sp.idCliente WHERE  cod_alarm %s and (id_cliente like %s or nombre_cliente like %s) ORDER BY DATEDIFF(day, sp.Fecha, GETDATE()) desc """% (self.datos[0],self.datos[1],self.datos[2]))
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarReporteEstatusPanel':
				self.cursor.execute("""SELECT COUNT(*) AS cont, s.cod_alarm FROM t365_StatusPanelCliente s INNER JOIN  t365_Clientes c ON s.idCliente = c.id_cliente where (s.Fecha >= ?) AND (s.Fecha <= ?) GROUP BY s.cod_alarm""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarReporteGruposSenales':
				self.cursor.execute("""SELECT g.idGrupo, g.Descript, COUNT(t.id_trama) AS cont FROM t365_Tramas t INNER JOIN   t365_Clientes c ON t.cliente = c.id_cliente INNER JOIN t365_Eventos e ON t.evento = e.cod_event AND t.protocolo = e.id_protocolo  INNER JOIN t365_CodigosAlarma a ON e.cod_alarm = a.codigo INNER JOIN  t365_GrupoCodigosAlarma g ON a.idGrupo = g.idGrupo    where (t.fecha >= ?) AND (t.fecha <= ?) GROUP BY g.idGrupo, g.Descript ORDER BY cont DESC""",self.datos)
				self.resultado = self.cursor.fetchall()		

			elif self.nombrequery == 'SeleccionarReporteActivaciones':
				self.cursor.execute(""" SELECT t.cliente, COUNT(t.id_trama) AS cont, c.nombre_cliente,c.prefijo,c.cuenta,ROW_NUMBER() OVER(ORDER BY COUNT(t.id_trama) DESC) AS RowID  FROM t365_Clientes c INNER JOIN t365_Tramas t ON c.id_cliente = t.cliente INNER JOIN  t365_Eventos e ON t.evento = e.cod_event  AND t.protocolo = e.id_protocolo  INNER JOIN t365_CodigosAlarma alarm ON   e.cod_alarm = alarm.codigo INNER JOIN t365_GrupoCodigosAlarma g ON alarm.idGrupo = g.idGrupo WHERE (g.idGrupo = 1)  AND (t.fecha >=  ?) AND (t.fecha <=?)  %s GROUP BY cliente, nombre_cliente,c.prefijo,c.cuenta 
	"""% self.datos[2],self.datos[0],self.datos[1])
				self.resultado = self.cursor.fetchall()		

			elif self.nombrequery == 'SeleccionarReporteActivacionesDetalleCliente':
				self.cursor.execute(""" SELECT cod_alarm,descript,evento,UserZona, fecha FROM v365_HistorialSenales  WHERE (idGrupo = 1)  AND (cliente = ?) AND (fecha >= ?) AND (fecha <= ?) ORDER BY fecha""",self.datos)
				self.resultado = self.cursor.fetchall()		

			elif self.nombrequery == 'SeleccionarDireccionyNombreEmpresaCliente':
				self.cursor.execute(""" SELECT        t365_Empresas.nombre, t365_Clientes.direccion,t365_Clientes.cuenta,t365_Clientes.prefijo
	FROM            t365_Clientes INNER JOIN
							 t365_Empresas ON t365_Clientes.id_empresa = t365_Empresas.id_empresa
	WHERE        (t365_Clientes.id_cliente = ?)""",self.datos)
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'SeleccionarDireccionyNombreEmpresaClienteFichaCliente':
				self.cursor.execute("""SELECT        t365_Empresas.nombre, t365_Clientes.direccion, t365_Clientes.cuenta, t365_Clientes.prefijo, t365_Clientes.telf_local, t365_Clientes.email, t365_Clientes.ciudad, t365_Paises.descripcion AS pais, 
							 t365_EquiposModelos.descripcion AS modeloalarma, t365_Clientes.fechinicio AS fechainicio, t365_Clientes.latitud, t365_Clientes.longitud, t365_Clientes.rif, t365_Clientes.clavemaster
	FROM            t365_Clientes LEFT OUTER JOIN
							 t365_Empresas ON t365_Clientes.id_empresa = t365_Empresas.id_empresa LEFT OUTER JOIN
							 t365_PaisEstados ON t365_Clientes.id_estado = t365_PaisEstados.id_estado LEFT OUTER JOIN
							 t365_Paises ON t365_PaisEstados.id_pais = t365_Paises.id_pais LEFT OUTER JOIN
							 t365_EquiposModelos ON t365_Clientes.modelo = t365_EquiposModelos.id_modelo
	WHERE        (t365_Clientes.id_cliente = ?)""",self.datos)
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'SeleccionarReporteCodigoAlarma':
				self.cursor.execute("""SELECT t.cliente, c.nombre_cliente AS nombreCliente,c.prefijo,c.cuenta, COUNT(*) AS cont,ROW_NUMBER() OVER(ORDER BY COUNT(*) DESC) AS RowID FROM v365_HistorialSenales t INNER JOIN t365_Clientes c ON t.cliente = c.id_cliente  WHERE (c.id_cliente > 0) AND (t.fecha >= ?) AND (t.fecha <= ?)  %s   %s GROUP BY t.cliente, c.nombre_cliente,c.prefijo,c.cuenta """% (self.datos[2],self.datos[3]),self.datos[0],self.datos[1])
				self.resultado = self.cursor.fetchall()		

			elif self.nombrequery == 'SeleccionarReporteCodigoAlarmaCliente':
				self.cursor.execute("""SELECT t.cod_alarm, t.descript, t.evento,t.UserZona, t.fecha FROM v365_HistorialSenales t INNER JOIN t365_Clientes c ON t.cliente = c.id_cliente WHERE (t.fecha >= ?) AND (t.fecha <= ?) %s  %s  %s  ORDER BY t.fecha DESC"""%(self.datos[2],self.datos[3],self.datos[4]) ,self.datos[0],self.datos[1])
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'Seleccionarself.datosClienteEditar':
				self.cursor.execute("""SELECT        c.id_cliente, c.cuenta, c.prefijo, c.id_empresa, c.id_protocolo, c.nombre_cliente, c.ciudad, c.direccion, c.referencia, c.telf_local, c.telf_fax, c.telf_movil, c.email, c.web_site, c.id_type_cliente, c.id_status, 
							 c.fecha_corte, c.login, c.clave, c.status, c.status_web, c.latitud, c.longitud, c.clavemaster, c.fechinicio, c.rif, c.imagen, c.id_estado, c.status_mail, c.status_monitoreo, c.tipocuenta, c.modelo, e.id_pais, 
							 m.id_subtipo_marca, ma.id_marca, t365_ClientesPuntos.id_punto
	FROM            t365_PaisEstados AS e RIGHT OUTER JOIN
							 t365_Clientes AS c LEFT OUTER JOIN
							 t365_ClientesPuntos ON c.id_cliente = t365_ClientesPuntos.id_cliente ON e.id_estado = c.id_estado LEFT OUTER JOIN
							 t365_EquiposSubTipos_Marcas AS ma INNER JOIN
							 t365_EquiposModelos AS m ON ma.id_subtipo_marca = m.id_subtipo_marca ON c.modelo = m.id_modelo
	WHERE        (c.id_cliente = ?)""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarRondasCliente':
				self.cursor.execute("""SELECT t365_Rondas.id_ronda, t365_Rondas.Nombre,t365_Rondas.Tolerancia, t365_Rondas.Hora_Inicio, t365_Rondas.Hora_Fin, t365_RondasTipo.Descripcion AS Tipo, t365_RondasCalendario.Descripcion AS Calendario, t365_Rondas.Hora_Fin_Total FROM  t365_Rondas LEFT OUTER JOIN t365_RondasCalendario ON t365_Rondas.id_Calendario = t365_RondasCalendario.id_rondacalendario LEFT OUTER JOIN
							 t365_RondasTipo ON t365_Rondas.id_Tipo = t365_RondasTipo.id_Tipo
	WHERE        (t365_Rondas.id_Cliente = ?) and (t365_Rondas.id_padre = 0) and (t365_Rondas.Borrar = 0)""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'Seleccionarself.datosRonda':
				self.cursor.execute("""SELECT  t365_Rondas.id_Cliente, t365_Rondas.Nombre, t365_Rondas.Tolerancia, t365_Rondas.Hora_Inicio, t365_Rondas.Hora_Fin, 
							 t365_RondasTipo.Descripcion AS Tipo, t365_RondasCalendario.Descripcion AS Calendario,t365_Rondas.Intervalo, t365_Rondas.Hora_Fin_Total FROM t365_Rondas LEFT OUTER JOIN
							 t365_RondasCalendario ON t365_Rondas.id_Calendario = t365_RondasCalendario.id_rondacalendario LEFT OUTER JOIN
							 t365_RondasTipo ON t365_Rondas.id_Tipo = t365_RondasTipo.id_Tipo WHERE (t365_Rondas.id_ronda = ?)""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'Seleccionarself.datosRondasHijas':
				self.cursor.execute("""SELECT  t365_Rondas.Hora_Inicio, t365_Rondas.Hora_Fin, t365_Rondas.id_ronda
							FROM t365_Rondas  WHERE (t365_Rondas.id_padre = ?)""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarPuntosCliente':
				self.cursor.execute("""SELECT  [id],[id_zona] as id_punto ,[id_cliente],[descrip],[ubicacion] FROM [t365_ClienteZonas] where id_cliente = ? order by id""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionaridZonaporIDPuntos':
				self.cursor.execute("""SELECT TOP 1 id_zona as id_punto FROM [t365_ClienteZonas] where id = ?""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarPuntosRonda':
				self.cursor.execute("""SELECT t365_ClienteZonas.id, t365_ClienteZonas.id_zona AS id_punto, t365_ClienteZonas.descrip
	FROM  t365_Rondas INNER JOIN t365_RondasPuntos ON t365_Rondas.id_ronda = t365_RondasPuntos.id_ronda INNER JOIN  t365_ClienteZonas ON t365_RondasPuntos.id_punto = t365_ClienteZonas.id
	WHERE  (t365_Rondas.id_ronda = ?) ORDER BY t365_ClienteZonas.id""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarRondasCalendario':
				self.cursor.execute("""SELECT [id_rondacalendario] ,[Descripcion] FROM [t365_RondasCalendario]""",self.datos)
				self.resultado = self.cursor.fetchall()
				
			elif self.nombrequery == 'SeleccionarRondasTipo':
				self.cursor.execute("""SELECT [id_Tipo],[Descripcion] FROM [t365_RondasTipo]""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarRondasPorPadre':
				self.cursor.execute("""SELECT id_ronda FROM t365_Rondas WHERE id_padre = ?""",self.datos)
				self.resultado = self.cursor.fetchall()

	#		elif self.nombrequery == 'SeleccionarRondasActuales':
	#			self.cursor.execute("""SELECT  id_ronda, id_Cliente, Nombre, Tolerancia, id_Tipo, DATEADD(mi, - Tolerancia, Hora_Inicio) AS Inicio, DATEADD(mi, Tolerancia, Hora_Fin) AS Fin
	#FROM    t365_Rondas
	#WHERE (DATEADD(mi, Tolerancia, Hora_Fin) >= CAST(GETDATE() AS time)) AND (id_Calendario = 1)  %s  ORDER BY Fin desc  """%self.datos[0])
	#			self.resultado = self.cursor.fetchall()

	#		elif self.nombrequery == 'SeleccionarRondasActuales':           VERSION VIEJA 
	#			self.cursor.execute("""SELECT  id_ronda, id_Cliente, Nombre, Tolerancia, id_Tipo, DATEADD(mi, - Tolerancia, Hora_Inicio) AS Inicio, DATEADD(mi, Tolerancia, Hora_Fin) AS Fin
	#FROM    t365_Rondas
	#WHERE   (DATEADD(mi, - Tolerancia, Hora_Inicio) <= CAST(GETDATE() AS time)) AND (DATEADD(mi, Tolerancia, Hora_Fin) >= CAST(GETDATE() AS time)) AND (id_Calendario = 1)  %s  ORDER BY Fin desc  """%self.datos[0])
	#			self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarPuntosRondaCalcuRondas':
				self.cursor.execute("""SELECT id_punto FROM t365_RondasPuntos WHERE id_ronda = ? ORDER BY ORDEN ASC""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarPuntosUltimaSenal':
				self.cursor.execute("""SELECT id_punto, fecha FROM t365_RondasPuntosUltSenal WHERE Tomada = ? or Tomada = ? ORDER BY fecha ASC""",self.datos)
				self.resultado = self.cursor.fetchall()

			#elif self.nombrequery == 'SeleccionarPuntosUltimaSenal':
			#	self.cursor.execute("""UPDATE t365_RondasPuntosUltSenal SET Tomada = ? OUTPUT DELETED.id_punto, DELETED.fecha WHERE Tomada = ? or  Tomada = ? ORDER BY fecha ASC """,self.datos)
			#	self.resultado = self.cursor.fetchall()
				#self.cnxn.commit()

			elif self.nombrequery == 'SeleccionarRondasActuales':
				self.cursor.execute("""SELECT  id_ronda, id_Cliente, Nombre, Tolerancia, id_Tipo, DATEADD(mi, - Tolerancia, Hora_Inicio) AS Inicio, DATEADD(mi, Tolerancia, Hora_Fin) AS Fin FROM    t365_Rondas WHERE ( DATEADD(mi, Tolerancia, Hora_Fin) >= CAST(GETDATE() AS time) OR DATEADD(mi, Tolerancia, Hora_Inicio) >= CAST(GETDATE() AS time) OR ( DATEADD(mi, Tolerancia, Hora_Inicio) < CAST(GETDATE() AS time) and DATEADD(mi, Tolerancia, Hora_Fin) < DATEADD(mi, Tolerancia, Hora_Inicio)) )   and ( (id_Calendario = 1)  %s  )  %s  %s  ORDER BY Fin desc  """%(self.datos[0],self.datos[1],self.datos[2]))
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarRondasPorBorrar':
				self.cursor.execute("""SELECT id_ronda FROM t365_Rondas WHERE Borrar = 1""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarPuntosOrdenados':
				self.cursor.execute("""SELECT id_punto FROM t365_RondasPuntos WHERE (id_ronda = ?) ORDER BY orden ASC""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarReporteTotalesSMS':
				self.cursor.execute("""SELECT  m.id_cliente, COUNT(m.id_mensajes) AS cont, c.nombre_cliente ,c.prefijo,c.cuenta FROM t365_MensajesSend m INNER JOIN t365_Clientes c ON m.id_cliente = c.id_cliente where m.send_date >= ? AND m.send_date <= ?  %s  GROUP BY m.id_cliente, c.nombre_cliente,c.prefijo,c.cuenta ORDER BY cont DESC"""% self.datos[2],self.datos[0],self.datos[1])
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarReporteTotalesSMSDetalleCliente':
				self.cursor.execute("""SELECT m.movil, m.sms, m.send_date FROM t365_MensajesSend m INNER JOIN 
	t365_Clientes c ON m.id_cliente = c.id_cliente  WHERE c.id_cliente =? and  m.send_date >= ? AND m.send_date <= ? """,self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarHorarios':
				self.cursor.execute("""SELECT        t365_HorariosOC.Id, t365_HorariosOC.id_cliente, DATEADD(mi, - t365_HorariosOC.toleranciaapertura, t365_HorariosOC.horaapertura) AS MinApertura, DATEADD(mi, t365_HorariosOC.toleranciaapertura, 
							 t365_HorariosOC.horaapertura) AS MaxApertura, DATEADD(mi, - t365_HorariosOC.toleranciacierre, t365_HorariosOC.horacierre) AS MinCierre, DATEADD(mi, t365_HorariosOC.toleranciacierre, 
							 t365_HorariosOC.horacierre) AS MaxCierre, t365_HorariosOC.fecha, t365_Clientes.id_protocolo
	FROM            t365_HorariosOC INNER JOIN
							 t365_Clientes ON t365_HorariosOC.id_cliente = t365_Clientes.id_cliente
	WHERE        (DATEADD(mi, t365_HorariosOC.toleranciacierre, t365_HorariosOC.horacierre) >= CAST(GETDATE() AS time) OR
							 DATEADD(mi, - t365_HorariosOC.toleranciaapertura, t365_HorariosOC.horaapertura) >= CAST(GETDATE() AS time) OR
							 DATEADD(mi, - t365_HorariosOC.toleranciaapertura, t365_HorariosOC.horaapertura) < CAST(GETDATE() AS time) AND DATEADD(mi, t365_HorariosOC.toleranciacierre, t365_HorariosOC.horacierre) 
							 < DATEADD(mi, - t365_HorariosOC.toleranciaapertura, t365_HorariosOC.horaapertura)) AND (t365_HorariosOC.diaapertura = ?) AND (t365_HorariosOC.Tomada = ? OR
							 t365_HorariosOC.Tomada = ?) """,self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarAperturasCierresHorariosControl':
				self.cursor.execute("""SELECT idControl,id_cliente,cod_alarm,fecha,id_protocolo FROM t365_HorarioControl WHERE status = ? or status = ?""",self.datos)
				self.resultado = self.cursor.fetchall()
			
			elif self.nombrequery == 'SeleccionarTramasAlertas':
				self.cursor.execute("""SELECT id_trama,cliente,evento,user_zone,protocolo,fecha,tipo_alerta,status FROM t365_TramasAlertas WHERE status = 0""",self.datos)
				self.resultado = self.cursor.fetchall()	

			elif self.nombrequery == 'SeleccionarUsuariosSMSAlertas':
				self.cursor.execute("""SELECT  t365_Usuarios.movil, t365_ClienteEventos.id_user AS usuario FROM t365_ClienteEventos INNER JOIN t365_Usuarios ON t365_ClienteEventos.id_cliente = t365_Usuarios.id_cliente AND t365_ClienteEventos.id_user = t365_Usuarios.id_user WHERE (t365_ClienteEventos.id_cliente = ?) AND (t365_ClienteEventos.cod_evento = ?) AND (t365_ClienteEventos.type = ?) AND (t365_Usuarios.status = 1)""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarUsuariosEmailAlertas':
				self.cursor.execute("""SELECT  t365_Usuarios.email, t365_ClienteEventos.id_user AS usuario FROM t365_ClienteEventos INNER JOIN t365_Usuarios ON t365_ClienteEventos.id_cliente = t365_Usuarios.id_cliente AND t365_ClienteEventos.id_user = t365_Usuarios.id_user WHERE (t365_ClienteEventos.id_cliente = ?) AND (t365_ClienteEventos.cod_evento = ?) AND (t365_ClienteEventos.type = ?) AND (t365_Usuarios.status = 1)""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarNombreClienteyEmpresaPorID':
				self.cursor.execute("""SELECT t365_Empresas.nombre, t365_Clientes.nombre_cliente FROM t365_Empresas INNER JOIN t365_Clientes ON t365_Empresas.id_empresa = t365_Clientes.id_empresa WHERE (t365_Clientes.id_cliente = ?)""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarTipoDescripMensajeAlerta':
				self.cursor.execute("""SELECT type_evento , descript , mensaje  from t365_Eventos where cod_event =? and id_protocolo = ?""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarNombreUsuarioAlerta':
				self.cursor.execute("""SELECT nombre +' '+ apellido as name FROM t365_Usuarios WHERE id_user = ? and id_cliente = ?""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarNombreZonaAlerta':
				self.cursor.execute("""SELECT descrip FROM t365_ClienteZonas WHERE id_zona = ? and id_cliente = ?""",self.datos)
				self.resultado = self.cursor.fetchall()		

			elif self.nombrequery == 'SeleccionarHorariosPorBorrar':
				self.cursor.execute("""SELECT id FROM t365_HorariosOC WHERE Borrar = 1""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarTiposDispositivosCuentas':
				self.cursor.execute("""SELECT  [id_subtipo],[descripcion],[id_tipo],[monitoreoequipo]
	  FROM t365_EquiposSubTipos WHERE monitoreoequipo = 1""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarObservacionesTramasProcesadas':
				self.cursor.execute("""SELECT        t365_TramasProcesadasObservaciones.fecha, t365_TramasProcesadasObservaciones.observacion, t365_Personal.nombre
	FROM            t365_TramasProcesadasObservaciones INNER JOIN
							 t365_Personal ON t365_TramasProcesadasObservaciones.idoperador = t365_Personal.idPersonal
	WHERE        (t365_TramasProcesadasObservaciones.idtrama = ?)
	ORDER BY t365_TramasProcesadasObservaciones.fecha DESC""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarTiposEquipos':
				self.cursor.execute("""SELECT [id_tipo_equipo],[descripcion]  FROM [t365_EquiposTipos] WHERE eliminado = 0""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarTiposEquiposUnoNombre':
				self.cursor.execute("""SELECT [id_tipo_equipo],[descripcion]  FROM [t365_EquiposTipos] WHERE eliminado = 0 and descripcion = ?""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarSubTiposEquipos':
				self.cursor.execute("""SELECT [id_subtipo],[descripcion],[id_tipo] FROM t365_EquiposSubTipos WHERE eliminado = 0""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarSubTiposEquiposUnoNombre':
				self.cursor.execute("""SELECT [id_subtipo],[descripcion],[id_tipo] FROM t365_EquiposSubTipos WHERE eliminado = 0 and descripcion = ?""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarModelosEquipos':
				self.cursor.execute("""SELECT        t365_EquiposModelos.id_modelo, t365_EquiposModelos.id_subtipo_marca, t365_EquiposModelos.descripcion, t365_EquiposModelos.string_acceso, 
							 t365_EquiposModelos.id_manual_help, t365_EquiposModelos.id_manual_user, t365_EquiposModelos.id_manual_prog, t365_EquiposModelos.id_manual_insta, t365_EquiposSubTipos.id_tipo, t365_EquiposSubTipos_Marcas.id_subtipo, 
							 t365_EquiposSubTipos_Marcas.id_marca
	FROM            t365_EquiposModelos INNER JOIN
							 t365_EquiposSubTipos_Marcas ON t365_EquiposModelos.id_subtipo_marca = t365_EquiposSubTipos_Marcas.id_subtipo_marca INNER JOIN
							 t365_EquiposSubTipos ON t365_EquiposSubTipos_Marcas.id_subtipo = t365_EquiposSubTipos.id_subtipo WHERE t365_EquiposModelos.eliminado = 0""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarVariablesCCTV':
				self.cursor.execute("""SELECT [descrip] FROM [t365_VariablesCCTV]""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarModeloPorNombre':
				self.cursor.execute("""SELECT [id_modelo] FROM [t365_EquiposModelos] WHERE [descripcion] = ?""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarIDSubTipoMarca':
				self.cursor.execute("""SELECT [id_subtipo_marca] FROM [t365_EquiposSubTipos_Marcas] WHERE [id_subtipo] = ? AND  [id_marca] = ?""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarEventosNoDefinidos':
				self.cursor.execute("""SELECT t.evento, t.fecha, t.id_trama, c.prefijo, c.cuenta, c.nombre_cliente,t.descrip , c.id_cliente FROM t365_Tramas t  LEFT OUTER JOIN t365_Clientes c ON t.cliente = c.id_cliente WHERE (t.evento NOT IN (SELECT cod_event FROM t365_Eventos)) ORDER BY t.fecha """,self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarSMSEntrada':
				self.cursor.execute("""SELECT e.movil , u.id_user, u.nombre + ' ' + u.apellido AS usuario, c.nombre_cliente, c.id_cliente,c.prefijo,c.cuenta,  e.sms, e.recib_date as fecha FROM t365_MensajesRecib e INNER JOIN t365_Usuarios u ON e.movil = u.movil INNER JOIN  t365_Clientes c ON u.id_cliente = c.id_cliente WHERE e.recib_date >= ? and e.recib_date <= ?""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarReporteClientesUltimaSenal':
				self.cursor.execute("""SELECT DISTINCT s.id_trama, s.descrip, s.status, s.cliente, s.evento, s.user_zone, CONVERT(DATETIME, s.fecha, 100) AS fecha, DATEDIFF(day, s.fecha, GETDATE()) AS Dif, s.protocolo, s.Variante, s.Linea, c.id_cliente, c.nombre_cliente,c.prefijo,c.cuenta, CASE WHEN s.evento is null and e.descript is null THEN 'Sin transmision' WHEN s.evento is not null and e.descript is null THEN 'Evento '+s.evento+' no definido' ELSE s.evento+' - '+e.descript end as descript, DATEDIFF(hour, s.fecha, GETDATE()) AS horas, gc.idGrupo ,ROW_NUMBER() OVER(ORDER BY s.fecha asc) AS RowID FROM t365_GrupoCodigosAlarma AS gc INNER JOIN t365_CodigosAlarma AS ca ON gc.idGrupo = ca.idGrupo RIGHT OUTER JOIN t365_Eventos AS e ON ca.codigo = e.cod_alarm RIGHT OUTER JOIN t365_TramasUltimaSignal AS s ON e.cod_event = s.evento AND e.id_protocolo = s.protocolo RIGHT OUTER JOIN t365_Clientes AS c ON s.cliente = c.id_cliente WHERE c.id_cliente > 0  %s  %s  ORDER BY horas desc"""%(self.datos[0],self.datos[1]))
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarTiposEventos':
				self.cursor.execute("""SELECT [id_tipoevento],[descripcion] FROM t365_TypeEvento order by [id_tipoevento] ASC""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'Seleccionar10UltSenalesCliente':
				self.cursor.execute(""" SELECT TOP 10 * FROM v365_HistorialSenales WHERE (cliente = ?) ORDER BY fecha DESC""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'NombresTablas':
				self.cursor.execute("""SELECT CAST(table_name as varchar(100))  FROM INFORMATION_SCHEMA.TABLES""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarPuntoTagCliente':
				self.cursor.execute("""SELECT id_cliente,id_punto FROM  t365_ClientesPuntos WHERE id_cliente = ?""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarPuntoTagPorTag':
				self.cursor.execute("""SELECT t365_ClientesPuntos.id_cliente, t365_ClientesPuntos.id_punto, t365_Clientes.prefijo, t365_Clientes.cuenta
	FROM  t365_ClientesPuntos INNER JOIN t365_Clientes ON t365_ClientesPuntos.id_cliente = t365_Clientes.id_cliente WHERE (t365_ClientesPuntos.id_punto = ?)""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarEstatusPanelHorarios':
				self.cursor.execute("""SELECT TOP 1 [cod_alarm] FROM t365_StatusPanelCliente where  CAST(fecha AS DATE) = CAST( getdate() AS DATE) and idCliente = ?""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarCamarasRTSPCliente':
				self.cursor.execute("""SELECT t365_ClientesCCTV_Channel.descripcion AS nombrecanal, t365_ClientesCCTV_Channel.channel, t365_ClientesCCTV_Channel.id_channel, t365_ClientesCCTV.descripcion AS nombredvr
FROM t365_ClientesCCTV INNER JOIN t365_ClientesCCTV_Channel ON t365_ClientesCCTV.id_cctv = t365_ClientesCCTV_Channel.id_cctv WHERE (t365_ClientesCCTV.id_cliente = ?) AND (t365_ClientesCCTV.id_modo = 2)
ORDER BY t365_ClientesCCTV.id_cctv, t365_ClientesCCTV_Channel.channel""",self.datos)
				self.resultado = self.cursor.fetchall()

			elif self.nombrequery == 'SeleccionarCanalesAsignadosZona':
				self.cursor.execute("""SELECT id_channel, id from t365_ClienteZonasCCTV where id_zona = ?""",self.datos)
				self.resultado = self.cursor.fetchall()


			globalvars.DictColaResultados[self.nombrecodigo] = self.resultado
		except:
			self.Desconectar()
			self.Conectar()

	def QuerysUpdateDelete(self):

		try:

			




			#################################################### UPDATE ############################################################

			if self.nombrequery == 'ActualizarNotaFijaCliente':
				self.cursor.execute("UPDATE t365_NotasClientes SET NotaFija =? where IdCliente = ?",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarNotaTemporalCliente':
				self.cursor.execute("UPDATE t365_NotasClientes SET NotaTemp =?, FechaIni = ?, FechaFin= ? where IdCliente = ?",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarZonaCliente':
				self.cursor.execute("UPDATE t365_ClienteZonas SET descrip =? , ubicacion =?, id_zona=? WHERE id_zona =? and id_cliente =? ",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarPuntoCliente':
				self.cursor.execute("UPDATE t365_ClienteZonas SET descrip =? , ubicacion =?, id_zona=? WHERE id_zona =? and id_cliente =? ",self.datos)
				self.cnxn.commit()
			
			elif self.nombrequery == 'ActualizarUsuariosCliente':
				self.cursor.execute("UPDATE t365_Usuarios SET id_user=?, cod_user=?, id_type_user =?, nombre =?, apellido =?, movil =?, email =?, FechaAniversario =?, status =?, send_mail =?, frecuencia_mail =?, bbpin =?, clavevoz =? , active_email=? ,maximosms= ? WHERE (id_user =?) AND (id_cliente =?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarContactoCliente':
				self.cursor.execute("UPDATE t365_NumEmergencia SET descript =? ,numero =?, observacion=? where (numero=?) AND (id_cliente =?) ",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarPlanSMS':
				self.cursor.execute("UPDATE t365_Usuarios SET id_plan = ?  where id_user=? AND id_cliente=?",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarPlanEmail':
				self.cursor.execute("UPDATE t365_Usuarios SET id_plan_email = ?  where id_user=? AND id_cliente=?",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarHorario':
				self.cursor.execute("UPDATE t365_HorariosOC SET diaapertura =?, horaapertura =?,toleranciaapertura =?,diacierre =?, horacierre =?, toleranciacierre =?, tomada = 0, borrar = 0 WHERE (Id = ?) ",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarTipoCliente':
				self.cursor.execute("UPDATE  t365_TypeCliente SET descrip=?,img=?,id_dispositivo=?,id_empresa=? WHERE id_type_empresa = ?",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarDepartamento':
				self.cursor.execute("UPDATE t365_DepartamentosEmpresa SET nombre =?, correo =? WHERE (idDepartamento =?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarTipoEquipo':
				self.cursor.execute("UPDATE t365_EquiposTipos SET descripcion =?, eliminado =? WHERE (id_tipo_equipo =?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarSubTipoEquipo':
				self.cursor.execute("UPDATE t365_EquiposSubTipos SET descripcion =?, id_tipo=?, eliminado =? WHERE (id_subtipo=?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarLatitudLongitud':
				self.cursor.execute("UPDATE t365_Clientes SET latitud =?, longitud =? WHERE (id_cliente =?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarHeartBeatOperador':
				self.cursor.execute(" UPDATE t365_OperadorSession SET FechaPIN=GETDATE(), Ip=?, StatusLogin=1, StatusMonitoreo = ? WHERE IdOperador = ?",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarFechaDesocupado':
				self.cursor.execute(" UPDATE t365_OperadorSession SET FechaPIN = GETDATE(), StatusLogin=1, StatusMonitoreo = 1, FechaDesocupado = GETDATE() WHERE IdOperador = ?",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarTramaPendiente':
				self.cursor.execute("UPDATE t365_TramasPorProcesar SET status =4 where id_trama = ?",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarPlanNotificaciones':
				self.cursor.execute("UPDATE t365_Planes SET descrip =?, id_protocolo =? where id_plan = ?",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarEvento':
				self.cursor.execute("UPDATE t365_Eventos SET cod_event =?, id_protocolo =?, descript = ?, mensaje = ?, type_evento = ?, monitorea = ?, cod_alarm = ?, prioridad = ?, web_color = ? where cod_event =? and id_protocolo =?",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarCodigoAlarma':
				self.cursor.execute("UPDATE t365_CodigosAlarma SET codigo =?, descript =?, prioridad = ?, grupo = ?, idGrupo = ?, web_color = ? where codigo =?",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'EliminarUsuarioPersonal':
				self.cursor.execute("UPDATE t365_Personal SET eliminado =1 where (idPersonal=?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarUsuarioPersonal':
				self.cursor.execute("UPDATE t365_Personal SET id_empresa =?,idTipoUsuario =?,cedula =?, nombre =?, telefono =?, correo =?, Dirreccion =?, Telf_Habitacion =? ,id_perfil=? where idPersonal=?",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarClaveUsuarioPersonal':
				self.cursor.execute("UPDATE t365_Personal SET clave =? where idPersonal=?",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarTipoUsuario':
				self.cursor.execute("UPDATE t365_TiposUsuarios SET color =?, descripcion =?, id_perfilUsuario =?, idEmpresa = ? where idtipoUsuario=?",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarEmpresa':
				self.cursor.execute(" UPDATE t365_Empresas SET nombre =?, direccion =?, telefonos =?, email =?, web =?,  rif =? , latitud =?, longuitud =?,timeAlertPen =?, timeHombreM =?, timeNotifiHombre =?, correosHombre =?, monitorea =  ?  WHERE (id_empresa =?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarEmpresaEmpresaMonitorea':
				self.cursor.execute(" UPDATE t365_Empresas SET monitorea = ?  WHERE (id_empresa =?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarClaveEmpresa':
				self.cursor.execute(" UPDATE t365_Empresas SET clave = ? WHERE (id_empresa =?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarParentesco':
				self.cursor.execute("UPDATE t365_TypeUser SET descrip =? WHERE (id_type_user = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarGrupoCodigodeAlarma':
				self.cursor.execute("UPDATE t365_GrupoCodigosAlarma SET Descript =? WHERE (idGrupo = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarMensajesPredefinidos': #Resoluciones
				self.cursor.execute("UPDATE  t365_MensajesCierre SET Mensaje =? WHERE (id = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarReceptorConfigPort': 
				self.cursor.execute("UPDATE t365_ConfigPortII SET Descrip =?, Config =?, type =?, Server =?, Port =?, idReceptor =?, Heartbeat =?, geta =?, Status =?, idReceiver =?, prefijo = ?,PortID = ? WHERE (PortID = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarMotivoSoporte': 
				self.cursor.execute("UPDATE t365_SoporteMotivos SET idEmpresa = ? descripcion = ?, idDepartCorreo= ? WHERE (id_motivo = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarMotivoSoporte': 
				self.cursor.execute("UPDATE t365_SoporteMotivos SET idEmpresa = ? descripcion = ?, idDepartCorreo= ? WHERE (id_motivo = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarCCTVCliente': 
				self.cursor.execute("UPDATE t365_ClientesCCTV SET id_cliente = ?, id_modo = ?, id_tipo= ?, id_marca = ?, id_modelo = ?, descripcion = ?, ip = ?, puerto = ?, usuario = ?, clave = ? WHERE (id_cctv = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarCuentaCliente': 
				self.cursor.execute("UPDATE t365_Clientes SET nombre_cliente=?,ciudad=?,direccion=?,referencia=?,telf_local=?,web_site=?,email=?,telf_movil=?,id_type_cliente=?,id_status=?,status_web=?,status=?,id_protocolo=?,id_empresa=?,cuenta=?,telf_fax=?,clavemaster=?,rif=?,latitud=?,longitud=?,id_estado=?,status_monitoreo=?,status_mail=?,prefijo=?,login=?,tipocuenta=?,modelo=? WHERE (id_cliente = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarClaveCliente': 
				self.cursor.execute("UPDATE t365_Clientes SET clave=? WHERE (id_cliente = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarRonda': 
				self.cursor.execute("UPDATE t365_Rondas SET Nombre=?,Tolerancia=?,Hora_Inicio=?,Hora_Fin=?,id_Calendario=?,id_Tipo=?,Intervalo=?,Hora_Fin_Total=?,Tomada=0,Borrar=0 WHERE (id_ronda = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarStatusRondasCalcuRonda': 
				self.cursor.execute("UPDATE t365_Rondas SET Tomada=? WHERE (id_ronda = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarTomadaPuntoUltimaSenal': 
				self.cursor.execute("UPDATE t365_RondasPuntosUltSenal SET Tomada=? WHERE (id_punto = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarRondaActualizandoStatus': 
				self.cursor.execute("UPDATE t365_Rondas SET Borrar=1 WHERE (id_ronda = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarStatusHorarioCalcuHorarios': 
				self.cursor.execute("UPDATE t365_HorariosOC SET Tomada=? WHERE (Id = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarStatusHorarioControl':
				self.cursor.execute("UPDATE t365_HorarioControl SET Status=? WHERE (idControl = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarStatusTramasparaAlertas':
				self.cursor.execute("UPDATE t365_TramasAlertas SET Status='1' WHERE Status = '0'",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarStatusTramasparaAlertasIDTrama':
				self.cursor.execute("UPDATE t365_TramasAlertas SET Status=1 WHERE id_trama = ?",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarHorarioActualizarStatus': 
				self.cursor.execute("UPDATE t365_HorariosOC SET Borrar=1 WHERE (id = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarEquiposMarcas': 
				self.cursor.execute("UPDATE t365_EquiposMarcas SET descripcion = ?, eliminado=? WHERE (id_marca = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'ActualizarEquiposModelos': 
				self.cursor.execute("UPDATE t365_EquiposModelos SET id_subtipo_marca=?,descripcion=?,eliminado=?,string_acceso=? WHERE (id_modelo = ?)",self.datos)
				self.cnxn.commit()


			elif self.nombrequery == 'ActualizarPuntoTagCliente':
				self.cursor.execute("""UPDATE t365_ClientesPuntos SET id_punto = ? WHERE id_cliente = ?""",self.datos)
				self.cnxn.commit()


			################################################### DELETE #########################################################
		
			elif self.nombrequery == 'BorrarAbonadosGrupo':
				self.cursor.execute("DELETE FROM t365_asociados_abonados WHERE (id_asociado = ?) AND (id_empresa = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarEventosUsuario':
				self.cursor.execute("DELETE FROM t365_ClienteEventos WHERE (id_cliente=?) and (id_user=?) and (type=?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarZonaPunto':
				self.cursor.execute(" DELETE FROM t365_ClienteZonas WHERE (id_zona = ?) AND (id_cliente = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarUsuario':
				self.cursor.execute("DELETE FROM t365_Usuarios WHERE (id_user = ?) AND (id_cliente = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarHorario':
				self.cursor.execute("DELETE FROM t365_HorariosOC WHERE   (Id = ?) ",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarContacto':
				self.cursor.execute("DELETE FROM t365_NumEmergencia WHERE ( id_numero = ?) AND (id_cliente = ?) ",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarPlanNotificaciones':
				self.cursor.execute("DELETE FROM t365_Planes WHERE (id_plan = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarEventosPlanesNotificaciones':
				self.cursor.execute("DELETE FROM t365_EventosPlanes WHERE (id_plan = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarEvento':
				self.cursor.execute("DELETE FROM t365_Eventos WHERE (cod_event = ?) AND (id_protocolo = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarCodigoAlarma':
				self.cursor.execute("DELETE FROM [t365_CodigosAlarma] WHERE (codigo = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarPermisosUsuarioPersonal':
				self.cursor.execute("DELETE FROM t365_PermisosAdmin WHERE (idUsuario =?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarTipoUsuario':
				self.cursor.execute("UPDATE t365_TiposUsuarios SET eliminado =1 WHERE (idtipoUsuario = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarPermisosTipoUsuario':
				self.cursor.execute(" DELETE FROM t365_PermisosTipoUsuario WHERE (idTipoUsuario = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarEmpresa':
				self.cursor.execute("DELETE FROM t365_Empresas WHERE (id_empresa = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarParentesco':
				self.cursor.execute("DELETE FROM  t365_TypeUser WHERE (id_type_user = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarMensajePredefinido': #Resoluciones
				self.cursor.execute(" DELETE FROM t365_MensajesCierre WHERE (id = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarReceptor': 
				self.cursor.execute("DELETE FROM t365_ConfigPortII WHERE PortID = ?",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarMotivoSoporte': 
				self.cursor.execute("DELETE FROM t365_SoporteMotivos WHERE (id_motivo = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarChannelsCCTVCliente': 
				self.cursor.execute("DELETE FROM t365_ClientesCCTV_Channel WHERE (id_cctv = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarTodosPrefijosRangoCliente': 
				self.cursor.execute("DELETE FROM t365_EmpresasRangoClientes WHERE (id_empresa = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarTodosPrefijosLineas': 
				self.cursor.execute("DELETE FROM t365_ConfigPort_Lineas WHERE (id_linea = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarTipoCliente': 
				self.cursor.execute("DELETE FROM t365_TypeCliente WHERE (id_type_empresa = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarRonda': 
				self.cursor.execute("DELETE FROM t365_Rondas WHERE (id_ronda = ?) OR (id_padre =?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarRondaPorID': 
				self.cursor.execute("DELETE FROM t365_Rondas WHERE (id_ronda = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarRondaPorPadre': 
				self.cursor.execute("DELETE FROM t365_Rondas WHERE (id_padre = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarPuntosRonda': 
				self.cursor.execute("DELETE FROM t365_RondasPuntos WHERE (id_ronda = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarPuntosRondaPorPadre': 
				self.cursor.execute("DELETE t365_RondasPuntos FROM  t365_RondasPuntos INNER JOIN t365_Rondas ON t365_RondasPuntos.id_ronda = t365_Rondas.id_ronda WHERE (t365_Rondas.id_Padre = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarGrupoCodigoAlarma': 
				self.cursor.execute("DELETE t365_GrupoCodigosAlarma WHERE (idGrupo = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarDepartamento': 
				self.cursor.execute("DELETE t365_DepartamentosEmpresa WHERE (idDepartamento = ?)",self.datos)
				self.cnxn.commit()


			elif self.nombrequery == 'BorrarPuntoTagCliente': 
				self.cursor.execute("DELETE t365_ClientesPuntos WHERE (id_cliente = ?)",self.datos)
				self.cnxn.commit()

			elif self.nombrequery == 'BorrarCliente': 
				self.cursor.execute("exec websp_DeleteCuentaCliente ?",self.datos)
				self.cnxn.commit()


			elif self.nombrequery == 'BorrarRelacionZonaCCTV': 
				self.cursor.execute("DELETE t365_ClienteZonasCCTV WHERE (id_zona = ?)",self.datos)
				self.cnxn.commit()





		except:
			self.Desconectar()
			self.Conectar()

	def CrearCodigoDatos(self):
		self.nombrecodigo = self.nombrequery
		for i in self.datos:
			self.nombrecodigo = self.nombrecodigo+str(i)






