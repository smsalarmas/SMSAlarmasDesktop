# -*- coding: latin1 -*-

import xlsxwriter
import string
import datetime
def CrearXLS(reporte='Reporte',cliente='Cliente',direccion='Direccion',empresa='Empresa',logo='Logo.png',nombretitulos=['Sin Titulo','Sin Titulo','Sin Titulo','Sin Titulo'],datos=[['1','2','3','4'],['5','6','7','8']],color=False,nombrearchivo='Reporte'):
	# Create an new Excel file and add a worksheet.
	nombrearchivo =unicode(nombrearchivo.toLatin1(), encoding ="Latin-1")
	workbook = xlsxwriter.Workbook(nombrearchivo)
	worksheet = workbook.add_worksheet()

	#Fomarto del Merge
	merge_format = workbook.add_format({
		'bold': 1,
		'border': 0,
		'align': 'center',
		'valign': 'vcenter',
		'fg_color': 'white'})



	#Formato de las celdas de los Datos
	formatoceldasdatos = workbook.add_format({
		'border': 1,
		'align': 'center',
		'valign': 'vcenter',
		'fg_color': 'white',
		'font_color': 'white'})

	# Para darle tamano fijo a una columna
 

	#Para converger celdas entre si.
	worksheet.merge_range('A1:D2', str(empresa), merge_format)
	worksheet.merge_range('A6:D6', str(reporte), merge_format)

	# Add a bold format to use to highlight cells.
	bold = workbook.add_format({'bold': True,'font_size': 10})

	# Write some simple text.

	worksheet.write('A4', 'Cliente: '+cliente,bold)
	#worksheet.write('B4', cliente.decode('latin-1'),bold)


	# Text with formatting.
	worksheet.write('A5', 'Direccion: '+direccion, bold)
	#worksheet.write('B5', direccion.decode('latin-1'), bold)

	# Write some numbers, with row/column notation.
	#worksheet.write(2, 0, 123)
	#worksheet.write(3, 0, 123.456)



	#Formato del Titulo de la Tabla
	formatotitulostabla = workbook.add_format({
		'border': 1,
		'align': 'center',
		'valign': 'vcenter',
		'bg_color': '#005E8B',
		'font_color': 'white'})
	#Titulos de la Tabla
	abc = string.uppercase[:]
	pos = 0
	dictionanchos = {}
	for index,titulo in enumerate(nombretitulos):
		worksheet.write(str(abc[pos])+'8',titulo,formatotitulostabla)
		dictionanchos[index] = len(titulo)
		pos = pos + 1


	#Para desabilitar las columnas que no se van a usar
	columnastitulos = len(nombretitulos)
	worksheet.set_column(str(abc[columnastitulos])+':XFD', None, None, {'hidden': True})

	fila = 8
	columa = 0

	dictionstyles = {}

	for indexDict,listafila in enumerate(datos):
		columa = 0
		if color == True:
			ultimoelemento = len(listafila)-1
			if listafila[ultimoelemento] != None:
				dictionstyles[str(listafila[ultimoelemento])] = workbook.add_format({'font_color': str(listafila[ultimoelemento])})
				dictionstyles[str(listafila[ultimoelemento])].set_text_wrap()
				#dictionstyles[str(listafila[ultimoelemento])].set_align('fill')
				dictionstyles[str(listafila[ultimoelemento])].set_align('vcenter')
			else:
				dictionstyles[str(listafila[ultimoelemento])] = workbook.add_format({'font_color': 'black'})
				dictionstyles[str(listafila[ultimoelemento])].set_text_wrap()
				#dictionstyles[str(listafila[ultimoelemento])].set_align('fill')
				dictionstyles[str(listafila[ultimoelemento])].set_align('vcenter')
			print listafila[ultimoelemento]
		else:
			dictionstyles[indexDict] = workbook.add_format({'font_color': 'black'})
			dictionstyles[indexDict].set_text_wrap()
			#dictionstyles[indexDict].set_align('fill')
			dictionstyles[indexDict].set_align('vcenter')

		#Identificar el ancho que se le colocara a la columna.
		#Buscamos el texto mas largo por cada celda.
		for index, datocelda in enumerate(listafila):
			if datocelda == None:
				datocelda = '-----'
			if type(datocelda) == int or type(datocelda) == float or type(datocelda) == long:
				datocelda = str(datocelda)
			if isinstance(datocelda, datetime.datetime):
				datocelda = datocelda.strftime('%A, %d %b %Y %H:%M:%S')
			if type(datocelda) != unicode:
				datocelda = unicode(datocelda,'latin-1')
			if color == True:
				if index <= ultimoelemento-1:
					worksheet.write(fila, columa, datocelda, dictionstyles[str(listafila[ultimoelemento])])
					# Para manejar los anchos de las filas
					if index in dictionanchos:
						if len(datocelda) <= dictionanchos[index]:
							pass
						else:
							dictionanchos[index] = len(datocelda)
					else:
						dictionanchos[index] = len(datocelda)
			else:
				worksheet.write(fila, columa, datocelda, dictionstyles[indexDict])
				if index in dictionanchos:
					if len(datocelda) <= dictionanchos[index]:
						pass
					else:
						dictionanchos[index] = len(datocelda)
				else:
					dictionanchos[index] = len(datocelda)

			columa = columa + 1
		fila = fila + 1
	print dictionanchos

	#Ajusto los tamanos de las celdas al ancho mas largo de palabra
	for col,ancho in dictionanchos.iteritems():
		if ancho >= 50:
			ancho = 50
		worksheet.set_column(str(abc[col])+':'+str(abc[col]), ancho)
	# Insert an image.
	worksheet.insert_image('A1', logo)
	#worksheet.center_vertically()
	worksheet.center_horizontally()


	worksheet.set_footer('&CPage &P of &N')

	workbook.close()

