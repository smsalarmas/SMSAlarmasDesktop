# -*- coding: latin-1 -*-
import datetime
import os
#Librerias reportlab a usar:
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer,
Paragraph, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfgen.canvas import Canvas
def CrearReportePDF(logo='Logo.png',telefono=None,email=None,clavemaster=None,latitud=None,longitud=None,fechainicio=None,modelo=None,codigofiscal=None,nombrearchivo='Reporte.pdf',nombrecliente='Nombre Cliente',direccion='Direccion Cliente',nombrereporte='Reporte de Nombre de Reporte',zonas=False,achocolumnaszonas=None,tituloszonas=('titulo1','titulo2','titulo3'),datoszonas=(('1','2','3'),('4','5','6')),usuarios=False,achocolumnasusuarios=None,titulosusuarios=('titulo1','titulo2','titulo3'),datosusuarios=(('1','2','3'),('4','5','6')),contactos=False,achocolumnascontactos=None,tituloscontactos=('titulo1','titulo2','titulo3'),datoscontactos=(('1','2','3'),('4','5','6')),horarios=False,anchocolumnashorarios=None,tituloshorarios=('titulo1','titulo2','titulo3'),datoshorarios=(('1','2','3'),('4','5','6')),autoabrir=False):
		nombrearchivo =unicode(nombrearchivo.toLatin1(), encoding ="Latin-1")
		doc = SimpleDocTemplate(nombrearchivo, pagesize = A4,leftMargin=30,rightMargin=30,topMargin=15,bottomMargin=15)
		story=[]

		#Logo
		logo = logo
		im = Image(logo, 1.5*inch)
		story.append(im)

		#Espacio
		story.append(Spacer(1, 25))
		
		#Cargar Estilo Basico
		styles = getSampleStyleSheet()

		#Cliente
		cliente = '<font size=12><b>Cliente:</b> %s</font>' % nombrecliente
		Cliente = Paragraph(cliente,
							styles['Normal'])
		story.append(Cliente)

		#Espacio
		story.append(Spacer(1,5))

		#Rif
		codigofiscal = '<font size=12><b>Codigo Fiscal:</b> %s</font>' % codigofiscal
		CodigoFiscal = Paragraph(codigofiscal,
							styles['Normal'])
		story.append(CodigoFiscal)
		story.append(Spacer(1,5))

		#Direccio
		direccion = '<font size=12><b>Direccion:</b> %s</font>' % direccion
		Direccion = Paragraph(direccion,
							styles['Normal'])
		story.append(Direccion)
		story.append(Spacer(1,5))

		#Telefono
		telefono = '<font size=12><b>Telefono:</b> %s</font>' % telefono
		Telefono = Paragraph(telefono,
							styles['Normal'])
		story.append(Telefono)
		story.append(Spacer(1,5))

		#Correo
		correo = '<font size=12><b>Correo:</b> %s</font>' % email
		Correo = Paragraph(correo,
							styles['Normal'])
		story.append(Correo)
		story.append(Spacer(1,5))

		#ClaveMaster
		clavemaster = '<font size=12><b>Clave Master:</b> %s</font>' % clavemaster
		ClaveMaster = Paragraph(clavemaster,
							styles['Normal'])
		story.append(ClaveMaster)
		story.append(Spacer(1,5))

		#Modelo
		modelo = '<font size=12><b>Panel:</b> %s</font>' % modelo
		Modelo = Paragraph(modelo,
							styles['Normal'])
		story.append(Modelo)
		story.append(Spacer(1,5))

		#FechaInicio
		fechainicio = '<font size=12><b>Fecha Inicio:</b> %s</font>' % fechainicio.strftime("%d %b %Y %H:%M:%S")
		FechaInicio = Paragraph(fechainicio,
							styles['Normal'])
		story.append(FechaInicio)
		story.append(Spacer(1,5))

		#Coordenadas
		coordenadas = '<font size=12><b>Coordenadas:</b> '+str(latitud)+','+str(longitud)+'</font>'
		Coordenadas = Paragraph(coordenadas,
							styles['Normal'])
		story.append(Coordenadas)
		story.append(Spacer(1,5))

		#Fecha
		fecha = '<font size=12><b>Fecha Reporte:</b> %s</font>' % datetime.datetime.now().strftime("%d %b %Y %H:%M:%S")
		Fecha = Paragraph(fecha,
							styles['Normal'])
		story.append(Fecha)

		#Espacio
		story.append(Spacer(1,25))

		#Titulo Reporte
		styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
		titulo = '<font size=14><b>%s</b></font>' % nombrereporte
		Titulo = Paragraph(titulo,
							styles['Center'])
		story.append(Titulo)

		#Espacio
		story.append(Spacer(1, 25))

		if zonas == True:

			#Titulo Reporte
			titulo = '<font size=12><b>%s</b></font>' % 'Zonas'
			Titulo = Paragraph(titulo,
								styles['Center'])
			story.append(Titulo)

			#Espacio
			story.append(Spacer(1, 25))

			#Para agregar los titutlos
			datoszonas.insert(0,tituloszonas)


			#Para wordwrap en tablas
			nuevosDatos= []
			for number, fila in enumerate(datoszonas):
				listatemporal = []
				for texto in fila:
					if number == 0:
						text = texto
					else:
						if texto == None:
							texto = ''
						elif isinstance(texto, datetime.datetime):
							texto = texto.strftime("%d %b %Y %H:%M:%S")
						elif type(texto) == float or type(texto) == int or type(texto) == long:
							texto = str(texto)
						text = Paragraph(texto,styles['Normal'])
					listatemporal.append(text)
				nuevosDatos.append(listatemporal)

			color = HexColor('#2D5F8B')
			tabla = Table(data = nuevosDatos,colWidths=achocolumnaszonas,
										style = [
														 ('GRID',(0,0),(-1,-1),0.5,color),
														 ('BOX',(0,0),(-1,-1),0.5,colors.black),
														 ('BACKGROUND', (0, 0), (-1, 0), color),
														 ('TEXTCOLOR', (0, 0), (-1, 0), colors.white)
														 ]
										)
			story.append(tabla)
						#Espacio
			story.append(Spacer(1, 25))

		if usuarios == True:

			#Titulo Reporte
			titulo = '<font size=12><b>%s</b></font>' % 'Usuarios'
			Titulo = Paragraph(titulo,
								styles['Center'])
			story.append(Titulo)

			#Para agregar los titutlos
			datosusuarios.insert(0,titulosusuarios)

			#Espacio
			story.append(Spacer(1, 25))

			#Para wordwrap en tablas
			nuevosDatos= []
			for number, fila in enumerate(datosusuarios):
				listatemporal = []
				for texto in fila:
					if number == 0:
						text = texto
					else:
						if texto == None:
							texto = ''
						elif isinstance(texto, datetime.datetime):
							texto = texto.strftime("%d %b %Y %H:%M:%S")
						elif type(texto) == float or type(texto) == int or type(texto) == long:
							texto = str(texto)
						text = Paragraph(texto,styles['Normal'])
					listatemporal.append(text)
				nuevosDatos.append(listatemporal)

			color = HexColor('#2D5F8B')
			tabla = Table(data = nuevosDatos,colWidths=achocolumnasusuarios,
										style = [
														 ('GRID',(0,0),(-1,-1),0.5,color),
														 ('BOX',(0,0),(-1,-1),0.5,colors.black),
														 ('BACKGROUND', (0, 0), (-1, 0), color),
														 ('TEXTCOLOR', (0, 0), (-1, 0), colors.white)
														 ]
										)
			story.append(tabla)
						#Espacio
			story.append(Spacer(1, 25))

		if contactos == True:

			#Titulo Reporte
			titulo = '<font size=12><b>%s</b></font>' % 'Contactos'
			Titulo = Paragraph(titulo,
								styles['Center'])
			story.append(Titulo)

			#Espacio
			story.append(Spacer(1, 25))
			
			#Para agregar los titutlos
			datoscontactos.insert(0,tituloscontactos)


			#Para wordwrap en tablas
			nuevosDatos= []
			for number, fila in enumerate(datoscontactos):
				listatemporal = []
				for texto in fila:
					if number == 0:
						text = texto
					else:
						if texto == None:
							texto = ''
						elif isinstance(texto, datetime.datetime):
							texto = texto.strftime("%d %b %Y %H:%M:%S")
						elif type(texto) == float or type(texto) == int or type(texto) == long:
							texto = str(texto)
						text = Paragraph(texto,styles['Normal'])
					listatemporal.append(text)
				nuevosDatos.append(listatemporal)

			color = HexColor('#2D5F8B')
			tabla = Table(data = nuevosDatos,colWidths=achocolumnascontactos,
										style = [
														 ('GRID',(0,0),(-1,-1),0.5,color),
														 ('BOX',(0,0),(-1,-1),0.5,colors.black),
														 ('BACKGROUND', (0, 0), (-1, 0), color),
														 ('TEXTCOLOR', (0, 0), (-1, 0), colors.white)
														 ]
										)
			story.append(tabla)
						#Espacio
			story.append(Spacer(1, 25))

		if horarios == True:

			#Titulo Reporte
			titulo = '<font size=12><b>%s</b></font>' % 'Horarios'
			Titulo = Paragraph(titulo,
								styles['Center'])
			story.append(Titulo)

			#Espacio
			story.append(Spacer(1, 25))
			
			#Para agregar los titutlos
			datoshorarios.insert(0,tituloshorarios)


			#Para wordwrap en tablas
			nuevosDatos= []
			for number, fila in enumerate(datoshorarios):
				listatemporal = []
				for texto in fila:
					if number == 0:
						text = texto
					else:
						if texto == str(1):
							texto = 'Lunes'
						elif texto == str(2):
							texto = 'Martes'
						elif texto == str(3):
							texto = 'Miercoles'
						elif texto == str(4):
							texto = 'Jueves'
						elif texto == str(5):
							texto = 'Viernes'
						elif texto == str(6):
							texto = 'Sabado'
						elif texto == str(7):
							texto = 'Domingo'
						elif texto == str(8):
							texto = 'Feriados'
						elif texto == None:
							texto = ''
						elif isinstance(texto, datetime.datetime):
							texto = texto.strftime("%d %b %Y %H:%M:%S")
						elif isinstance(texto, datetime.time):

							texto = texto.strftime("%H:%M:%S")
						elif type(texto) == float or type(texto) == int or type(texto) == long:
							texto = str(texto)
						text = Paragraph(texto,styles['Normal'])
					listatemporal.append(text)
				nuevosDatos.append(listatemporal)
			color = HexColor('#2D5F8B')
			tabla = Table(data = nuevosDatos,colWidths=anchocolumnashorarios,
										style = [
														 ('GRID',(0,0),(-1,-1),0.5,color),
														 ('BOX',(0,0),(-1,-1),0.5,colors.black),
														 ('BACKGROUND', (0, 0), (-1, 0), color),
														 ('TEXTCOLOR', (0, 0), (2, 0), colors.white)
														 ]
										)
			story.append(tabla)
						#Espacio
			story.append(Spacer(1, 25))
		 
		doc.build(story)

		if autoabrir == True:
			os.system(str(nombrearchivo))

#CrearReportePDF()