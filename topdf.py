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
def CrearReportePDF(logo='Logo.png',nombrearchivo='Reporte.pdf',nombrecliente='Nombre Cliente',direccion='Direccion Cliente',nombrereporte='Reporte de Nombre de Reporte',achocolumnas=None,titulos=('titulo1','titulo2','titulo3'),datos=(('1','2','3'),('4','5','6')),autoabrir=False):
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
		cliente = '<font size=12>Cliente: %s</font>' % nombrecliente
		Cliente = Paragraph(cliente,
							styles['Normal'])
		story.append(Cliente)

		#Espacio
		story.append(Spacer(1,5))

		#Direccio
		direccion = '<font size=12>Direccion: %s</font>' % direccion
		Direccion = Paragraph(direccion,
							styles['Normal'])
		story.append(Direccion)
		story.append(Spacer(1,5))

		#Fecha
		fecha = '<font size=12>Fecha: %s</font>' % datetime.datetime.now().strftime("%d %b %Y %H:%M:%S")
		Fecha = Paragraph(fecha,
							styles['Normal'])
		story.append(Fecha)

		#Espacio
		story.append(Spacer(1,25))

		#Titulo Reporte
		styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
		titulo = '<font size=14>%s</font>' % nombrereporte
		Titulo = Paragraph(titulo,
							styles['Center'])
		story.append(Titulo)

		#Espacio
		story.append(Spacer(1, 25))

		#Para agregar los titutlos
		datos.insert(0,titulos)

		print datos
		#Para wordwrap en tablas
		nuevosDatos= []
		for number, fila in enumerate(datos):
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




 
		#Ejemplo02


		color = HexColor('#2D5F8B')
		tabla = Table(data = nuevosDatos,colWidths=achocolumnas,
									style = [
													 ('GRID',(0,0),(-1,-1),0.5,color),
													 ('BOX',(0,0),(-1,-1),0.5,colors.black),
													 ('BACKGROUND', (0, 0), (-1, 0), color),
													 ('TEXTCOLOR', (0, 0), (-1, 0), colors.white)
													 ]
									)
		story.append(tabla)
		 
		doc.build(story)

		if autoabrir == True:
			os.system(str(nombrearchivo))

#CrearReportePDF()