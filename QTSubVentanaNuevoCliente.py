# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaNuevoCliente.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_VentanaNuevoCliente(object):
    def setupUi(self, VentanaNuevoCliente):
        VentanaNuevoCliente.setObjectName(_fromUtf8("VentanaNuevoCliente"))
        VentanaNuevoCliente.resize(881, 622)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/record-add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VentanaNuevoCliente.setWindowIcon(icon)
        VentanaNuevoCliente.setStyleSheet(_fromUtf8("QTableView {\n"
"    color: #4d4e51;\n"
"    border: 1px solid #6d6e71;\n"
"    gridline-color: #9a9b9e; /* Color Grilla Celdas Internas: */\n"
"    background-color: #ffffff; /* Color Fondo Celdas Internas: */\n"
"    selection-color: #4d4e51;\n"
"    selection-background-color: #adc5ed;\n"
"    border-radius: 3px;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QTableView::item:hover  {\n"
"    background: #1ba1e2;   /* Color Poner Raton Celdas Internas: */\n"
"}\n"
"\n"
"QTableView::item:disabled  {\n"
"    color: #85878a; /* Color  Celdas Internas Desabilitadas: */\n"
"}\n"
"\n"
"QTableView::item:selected  {\n"
"    color: #1b3774; /* Color  Letra Item Interno Seleccionado: */\n"
"    background-color: #7cabf9;  /* Color  Fondo Item o tabla Interno Seleccionado: */\n"
"}\n"
"\n"
"/* when editing a cell: */\n"
"QTableView QLineEdit {\n"
"    color: #4d4e51;  /* Color  Fondo Letra al dar doble click para editar: */\n"
"    background-color: #b3b8bf; /* Color  Fondo Item al dar doble click para editar: */\n"
"    border-radius: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QTreeView, QListView\n"
"{\n"
"    color: #4d4e51;\n"
"    border: 1px solid #6d6e71;\n"
"    gridline-color: #9a9b9e; /* Color Grilla Celdas Internas: */\n"
"    background-color: #ffffff; /* Color Fondo Celdas Internas: */\n"
"    selection-color: #4d4e51;\n"
"    selection-background-color: #adc5ed;\n"
"    border-radius: 3px;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QTreeView::item:hover  {\n"
"    background: #1ba1e2;   /* Color Poner Raton Celdas Internas: */\n"
"}\n"
"\n"
"QTreeView::item:disabled  {\n"
"    color: #85878a; /* Color  Celdas Internas Desabilitadas: */\n"
"}\n"
"\n"
"QTreeView::item:selected  {\n"
"    color: #1b3774; /* Color  Letra Item Interno Seleccionado: */\n"
"    background-color: #7cabf9;  /* Color  Fondo Item o tabla Interno Seleccionado: */\n"
"}\n"
"\n"
"/* when editing a cell: */\n"
"QTreeView QLineEdit {\n"
"    color: #4d4e51;  /* Color  Fondo Letra al dar doble click para editar: */\n"
"    background-color: #b3b8bf; /* Color  Fondo Item al dar doble click para editar: */\n"
"    border-radius: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    }    \n"
"\n"
"QHeaderView {\n"
"    border: none;\n"
"    background-color: #4276a4;    /* Color Celda Horizontal Item: */\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QHeaderView::section  {\n"
"    background-color: transparent;\n"
"    color: #fdfdfd;     /* Color Letra Celda Horizontal Item: */\n"
"    border: 4px solid transparent;   /* Ancho Celda Horizontal Item: */\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section::vertical  {\n"
"    padding: 0px 6px 0px 6px;\n"
"    border-bottom: 1px solid #6d6e71;\n"
"}\n"
"\n"
"QHeaderView::section::vertical:first {\n"
"    border-top: 1px solid  #6d6e71;\n"
"}\n"
"\n"
"QHeaderView::section::vertical:last {\n"
"    border-bottom: none;\n"
"}\n"
"\n"
"QHeaderView::section::vertical:only-one {\n"
"    border: none;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal  {\n"
"    padding: 0px 0px 0px 6px;\n"
"    border-right: 1px solid #6d6e71;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal:first {\n"
"    border-left: 1px solid #6d6e71;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal:last {\n"
"    border-left: none;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal:only-one {\n"
"    border: none;\n"
"}\n"
"\n"
"QTabBar::tab:top {\n"
"    color: #403f3f;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent black;\n"
"    background-color: #dfdfdf;\n"
"    padding: 4px;\n"
"    border-top-left-radius: 1px;\n"
"    border-top-right-radius: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    color: #fdfdfd;\n"
"    background-color: #2d5f8b;\n"
"    border: 1px transparent #4A4949;\n"
"    border-bottom: 1px transparent #4A4949;\n"
"    border-top-left-radius: 1px;\n"
"    border-top-right-radius: 1px;\n"
"    \n"
"}\n"
"\n"
"QTabWidget{\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #2d5f8b;\n"
"    border-radius: 1px;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border:1px solid #2d5f8b;\n"
"    border-radius: 1px;\n"
"    margin-top: 20px; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;    \n"
"    padding: 2px 3px;\n"
"    color: white;\n"
"   \n"
"    margin-top: 2px;\n"
"    background-color: #2d5f8b;\n"
"    border-radius: 1px;\n"
"    spacing: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"QMenuBar {\n"
"\n"
"background-color: #38648b;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item {\n"
"\n"
"color : white;\n"
"\n"
"margin-top:0px;\n"
"\n"
"spacing: 3px;\n"
"\n"
"padding: 6px 12px;\n"
"\n"
"background: #transparent;\n"
"\n"
"border-radius: 111px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"\n"
"background: #2d81cb;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed {\n"
"\n"
"background: #2d81cb;\n"
"\n"
"}\n"
"\n"
"\n"
"QDockWidget {\n"
"\n"
"background-color: #4276a4\n"
"\n"
"}\n"
"\n"
"\n"
"QDockWidget {\n"
"\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QDockWidget::title {\n"
"\n"
"text-align: left; /* align the text to the left */\n"
"\n"
"background: #4276a4;\n"
"\n"
"padding-left: 5px;\n"
"\n"
"}"))
        self.gridLayout_7 = QtGui.QGridLayout(VentanaNuevoCliente)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.frame = QtGui.QFrame(VentanaNuevoCliente)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame.setStyleSheet(_fromUtf8("background-color: #38648B;\n"
"font: 10pt \"Calibri\";\n"
"color: rgb(255, 255, 255);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_5 = QtGui.QGridLayout(self.frame)
        self.gridLayout_5.setContentsMargins(-1, -1, -1, 9)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_69 = QtGui.QLabel(self.frame)
        self.label_69.setStyleSheet(_fromUtf8("font: bold 12pt \"Calibri\";"))
        self.label_69.setObjectName(_fromUtf8("label_69"))
        self.gridLayout_5.addWidget(self.label_69, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame, 0, 0, 1, 3)
        self.groupBox_2 = QtGui.QGroupBox(VentanaNuevoCliente)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_58 = QtGui.QLabel(self.groupBox_2)
        self.label_58.setObjectName(_fromUtf8("label_58"))
        self.gridLayout_3.addWidget(self.label_58, 11, 0, 1, 1)
        self.pushButton_Imagen = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_Imagen.setObjectName(_fromUtf8("pushButton_Imagen"))
        self.gridLayout_3.addWidget(self.pushButton_Imagen, 11, 1, 1, 1)
        self.label_54 = QtGui.QLabel(self.groupBox_2)
        self.label_54.setObjectName(_fromUtf8("label_54"))
        self.gridLayout_3.addWidget(self.label_54, 0, 0, 1, 1)
        self.label_56 = QtGui.QLabel(self.groupBox_2)
        self.label_56.setObjectName(_fromUtf8("label_56"))
        self.gridLayout_3.addWidget(self.label_56, 2, 0, 1, 1)
        self.lineEdit_Ciudad = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_Ciudad.setMaxLength(80)
        self.lineEdit_Ciudad.setObjectName(_fromUtf8("lineEdit_Ciudad"))
        self.gridLayout_3.addWidget(self.lineEdit_Ciudad, 2, 1, 1, 1)
        self.lineEdit_Referencia = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_Referencia.setMaxLength(100)
        self.lineEdit_Referencia.setObjectName(_fromUtf8("lineEdit_Referencia"))
        self.gridLayout_3.addWidget(self.lineEdit_Referencia, 5, 1, 1, 1)
        self.lineEdit_Llave = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_Llave.setMaxLength(30)
        self.lineEdit_Llave.setObjectName(_fromUtf8("lineEdit_Llave"))
        self.gridLayout_3.addWidget(self.lineEdit_Llave, 9, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 9, 0, 1, 1)
        self.lineEdit_Latitud = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_Latitud.setMaxLength(20)
        self.lineEdit_Latitud.setObjectName(_fromUtf8("lineEdit_Latitud"))
        self.gridLayout_3.addWidget(self.lineEdit_Latitud, 6, 1, 1, 1)
        self.textEdit_Direccion = QtGui.QTextEdit(self.groupBox_2)
        self.textEdit_Direccion.setMaximumSize(QtCore.QSize(16777215, 50))
        self.textEdit_Direccion.setObjectName(_fromUtf8("textEdit_Direccion"))
        self.gridLayout_3.addWidget(self.textEdit_Direccion, 3, 1, 1, 1)
        self.label_52 = QtGui.QLabel(self.groupBox_2)
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.gridLayout_3.addWidget(self.label_52, 7, 0, 1, 1)
        self.label_55 = QtGui.QLabel(self.groupBox_2)
        self.label_55.setObjectName(_fromUtf8("label_55"))
        self.gridLayout_3.addWidget(self.label_55, 6, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 8, 0, 1, 1)
        self.comboBox_Estado = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_Estado.setObjectName(_fromUtf8("comboBox_Estado"))
        self.gridLayout_3.addWidget(self.comboBox_Estado, 1, 1, 1, 1)
        self.lineEdit_Punto = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_Punto.setObjectName(_fromUtf8("lineEdit_Punto"))
        self.gridLayout_3.addWidget(self.lineEdit_Punto, 8, 1, 1, 1)
        self.label_53 = QtGui.QLabel(self.groupBox_2)
        self.label_53.setObjectName(_fromUtf8("label_53"))
        self.gridLayout_3.addWidget(self.label_53, 1, 0, 1, 1)
        self.comboBox_Pais = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_Pais.setObjectName(_fromUtf8("comboBox_Pais"))
        self.gridLayout_3.addWidget(self.comboBox_Pais, 0, 1, 1, 1)
        self.label_57 = QtGui.QLabel(self.groupBox_2)
        self.label_57.setObjectName(_fromUtf8("label_57"))
        self.gridLayout_3.addWidget(self.label_57, 3, 0, 1, 1)
        self.lineEdit_Longitud = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_Longitud.setMaxLength(20)
        self.lineEdit_Longitud.setObjectName(_fromUtf8("lineEdit_Longitud"))
        self.gridLayout_3.addWidget(self.lineEdit_Longitud, 7, 1, 1, 1)
        self.label_51 = QtGui.QLabel(self.groupBox_2)
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.gridLayout_3.addWidget(self.label_51, 5, 0, 1, 1)
        self.verticalLayout_Imagen = QtGui.QVBoxLayout()
        self.verticalLayout_Imagen.setObjectName(_fromUtf8("verticalLayout_Imagen"))
        self.gridLayout_3.addLayout(self.verticalLayout_Imagen, 12, 0, 1, 2)
        self.gridLayout_7.addWidget(self.groupBox_2, 1, 1, 2, 1)
        self.groupBox = QtGui.QGroupBox(VentanaNuevoCliente)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_46 = QtGui.QLabel(self.groupBox)
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.gridLayout_2.addWidget(self.label_46, 0, 0, 1, 1)
        self.comboBox_Empresa = QtGui.QComboBox(self.groupBox)
        self.comboBox_Empresa.setObjectName(_fromUtf8("comboBox_Empresa"))
        self.gridLayout_2.addWidget(self.comboBox_Empresa, 0, 1, 1, 2)
        self.label_37 = QtGui.QLabel(self.groupBox)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.gridLayout_2.addWidget(self.label_37, 1, 0, 1, 1)
        self.comboBox_Prefijo = QtGui.QComboBox(self.groupBox)
        self.comboBox_Prefijo.setObjectName(_fromUtf8("comboBox_Prefijo"))
        self.gridLayout_2.addWidget(self.comboBox_Prefijo, 1, 1, 1, 1)
        self.label_44 = QtGui.QLabel(self.groupBox)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.gridLayout_2.addWidget(self.label_44, 2, 0, 1, 1)
        self.comboBox_TipoDispositivo = QtGui.QComboBox(self.groupBox)
        self.comboBox_TipoDispositivo.setObjectName(_fromUtf8("comboBox_TipoDispositivo"))
        self.gridLayout_2.addWidget(self.comboBox_TipoDispositivo, 4, 1, 1, 2)
        self.lineEdit_CodigoCliente = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_CodigoCliente.setMaxLength(10)
        self.lineEdit_CodigoCliente.setObjectName(_fromUtf8("lineEdit_CodigoCliente"))
        self.gridLayout_2.addWidget(self.lineEdit_CodigoCliente, 1, 2, 1, 1)
        self.lineEdit_NumeroFiscal = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_NumeroFiscal.setMaxLength(100)
        self.lineEdit_NumeroFiscal.setObjectName(_fromUtf8("lineEdit_NumeroFiscal"))
        self.gridLayout_2.addWidget(self.lineEdit_NumeroFiscal, 3, 1, 1, 2)
        self.comboBox_TipoCuenta = QtGui.QComboBox(self.groupBox)
        self.comboBox_TipoCuenta.setObjectName(_fromUtf8("comboBox_TipoCuenta"))
        self.gridLayout_2.addWidget(self.comboBox_TipoCuenta, 5, 1, 1, 2)
        self.label_41 = QtGui.QLabel(self.groupBox)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.gridLayout_2.addWidget(self.label_41, 5, 0, 1, 1)
        self.comboBox_Marca = QtGui.QComboBox(self.groupBox)
        self.comboBox_Marca.setObjectName(_fromUtf8("comboBox_Marca"))
        self.gridLayout_2.addWidget(self.comboBox_Marca, 6, 1, 1, 2)
        self.label_39 = QtGui.QLabel(self.groupBox)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.gridLayout_2.addWidget(self.label_39, 7, 0, 1, 1)
        self.label_38 = QtGui.QLabel(self.groupBox)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.gridLayout_2.addWidget(self.label_38, 3, 0, 1, 1)
        self.label_40 = QtGui.QLabel(self.groupBox)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.gridLayout_2.addWidget(self.label_40, 4, 0, 1, 1)
        self.label_43 = QtGui.QLabel(self.groupBox)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.gridLayout_2.addWidget(self.label_43, 6, 0, 1, 1)
        self.lineEdit_NombreCuenta = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_NombreCuenta.setMaxLength(100)
        self.lineEdit_NombreCuenta.setObjectName(_fromUtf8("lineEdit_NombreCuenta"))
        self.gridLayout_2.addWidget(self.lineEdit_NombreCuenta, 2, 1, 1, 2)
        self.comboBox_Modelo = QtGui.QComboBox(self.groupBox)
        self.comboBox_Modelo.setObjectName(_fromUtf8("comboBox_Modelo"))
        self.gridLayout_2.addWidget(self.comboBox_Modelo, 7, 1, 1, 2)
        self.label_48 = QtGui.QLabel(self.groupBox)
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.gridLayout_2.addWidget(self.label_48, 9, 0, 1, 1)
        self.label_49 = QtGui.QLabel(self.groupBox)
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.gridLayout_2.addWidget(self.label_49, 8, 0, 1, 1)
        self.lineEdit_ClaveMaster = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_ClaveMaster.setMaxLength(100)
        self.lineEdit_ClaveMaster.setObjectName(_fromUtf8("lineEdit_ClaveMaster"))
        self.gridLayout_2.addWidget(self.lineEdit_ClaveMaster, 9, 1, 1, 2)
        self.dateTimeEdit_FechaInicio = QtGui.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit_FechaInicio.setCalendarPopup(True)
        self.dateTimeEdit_FechaInicio.setObjectName(_fromUtf8("dateTimeEdit_FechaInicio"))
        self.gridLayout_2.addWidget(self.dateTimeEdit_FechaInicio, 10, 1, 1, 2)
        self.comboBox_Protocolo = QtGui.QComboBox(self.groupBox)
        self.comboBox_Protocolo.setObjectName(_fromUtf8("comboBox_Protocolo"))
        self.gridLayout_2.addWidget(self.comboBox_Protocolo, 8, 1, 1, 2)
        self.label_50 = QtGui.QLabel(self.groupBox)
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.gridLayout_2.addWidget(self.label_50, 10, 0, 1, 1)
        self.label_47 = QtGui.QLabel(self.groupBox)
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.gridLayout_2.addWidget(self.label_47, 11, 0, 1, 1)
        self.dateTimeEdit_FechaCorte = QtGui.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit_FechaCorte.setCalendarPopup(True)
        self.dateTimeEdit_FechaCorte.setObjectName(_fromUtf8("dateTimeEdit_FechaCorte"))
        self.gridLayout_2.addWidget(self.dateTimeEdit_FechaCorte, 11, 1, 1, 2)
        self.lineEdit_Usuario = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Usuario.setMaxLength(50)
        self.lineEdit_Usuario.setObjectName(_fromUtf8("lineEdit_Usuario"))
        self.gridLayout_2.addWidget(self.lineEdit_Usuario, 12, 1, 1, 2)
        self.label_45 = QtGui.QLabel(self.groupBox)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.gridLayout_2.addWidget(self.label_45, 13, 0, 1, 1)
        self.lineEdit_Clave = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Clave.setMaxLength(50)
        self.lineEdit_Clave.setObjectName(_fromUtf8("lineEdit_Clave"))
        self.gridLayout_2.addWidget(self.lineEdit_Clave, 13, 1, 1, 2)
        self.label_42 = QtGui.QLabel(self.groupBox)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.gridLayout_2.addWidget(self.label_42, 12, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 14, 0, 1, 1)
        self.comboBox_Instalador = QtGui.QComboBox(self.groupBox)
        self.comboBox_Instalador.setObjectName(_fromUtf8("comboBox_Instalador"))
        self.gridLayout_2.addWidget(self.comboBox_Instalador, 14, 1, 1, 2)
        self.gridLayout_7.addWidget(self.groupBox, 1, 0, 2, 1)
        self.groupBox_3 = QtGui.QGroupBox(VentanaNuevoCliente)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.lineEdit_Email = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_Email.setMaxLength(100)
        self.lineEdit_Email.setObjectName(_fromUtf8("lineEdit_Email"))
        self.gridLayout_4.addWidget(self.lineEdit_Email, 0, 1, 1, 1)
        self.lineEdit_PaginaWeb = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_PaginaWeb.setMaxLength(100)
        self.lineEdit_PaginaWeb.setObjectName(_fromUtf8("lineEdit_PaginaWeb"))
        self.gridLayout_4.addWidget(self.lineEdit_PaginaWeb, 1, 1, 1, 1)
        self.label_60 = QtGui.QLabel(self.groupBox_3)
        self.label_60.setObjectName(_fromUtf8("label_60"))
        self.gridLayout_4.addWidget(self.label_60, 0, 0, 1, 1)
        self.label_63 = QtGui.QLabel(self.groupBox_3)
        self.label_63.setObjectName(_fromUtf8("label_63"))
        self.gridLayout_4.addWidget(self.label_63, 1, 0, 1, 1)
        self.label_59 = QtGui.QLabel(self.groupBox_3)
        self.label_59.setObjectName(_fromUtf8("label_59"))
        self.gridLayout_4.addWidget(self.label_59, 3, 0, 1, 1)
        self.lineEdit_TelefonoLocal = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_TelefonoLocal.setMaxLength(50)
        self.lineEdit_TelefonoLocal.setObjectName(_fromUtf8("lineEdit_TelefonoLocal"))
        self.gridLayout_4.addWidget(self.lineEdit_TelefonoLocal, 2, 1, 1, 1)
        self.label_62 = QtGui.QLabel(self.groupBox_3)
        self.label_62.setObjectName(_fromUtf8("label_62"))
        self.gridLayout_4.addWidget(self.label_62, 2, 0, 1, 1)
        self.lineEdit_Fax = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_Fax.setMaxLength(50)
        self.lineEdit_Fax.setObjectName(_fromUtf8("lineEdit_Fax"))
        self.gridLayout_4.addWidget(self.lineEdit_Fax, 4, 1, 1, 1)
        self.lineEdit_Movil = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_Movil.setMaxLength(50)
        self.lineEdit_Movil.setObjectName(_fromUtf8("lineEdit_Movil"))
        self.gridLayout_4.addWidget(self.lineEdit_Movil, 3, 1, 1, 1)
        self.label_61 = QtGui.QLabel(self.groupBox_3)
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.gridLayout_4.addWidget(self.label_61, 4, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_3, 1, 2, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(VentanaNuevoCliente)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_66 = QtGui.QLabel(self.groupBox_4)
        self.label_66.setObjectName(_fromUtf8("label_66"))
        self.gridLayout_6.addWidget(self.label_66, 0, 0, 1, 1)
        self.comboBox_EstausGeneral = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_EstausGeneral.setObjectName(_fromUtf8("comboBox_EstausGeneral"))
        self.gridLayout_6.addWidget(self.comboBox_EstausGeneral, 0, 1, 1, 1)
        self.label_67 = QtGui.QLabel(self.groupBox_4)
        self.label_67.setObjectName(_fromUtf8("label_67"))
        self.gridLayout_6.addWidget(self.label_67, 1, 0, 1, 1)
        self.label_65 = QtGui.QLabel(self.groupBox_4)
        self.label_65.setObjectName(_fromUtf8("label_65"))
        self.gridLayout_6.addWidget(self.label_65, 2, 0, 1, 1)
        self.label_68 = QtGui.QLabel(self.groupBox_4)
        self.label_68.setObjectName(_fromUtf8("label_68"))
        self.gridLayout_6.addWidget(self.label_68, 3, 0, 1, 1)
        self.label_64 = QtGui.QLabel(self.groupBox_4)
        self.label_64.setObjectName(_fromUtf8("label_64"))
        self.gridLayout_6.addWidget(self.label_64, 4, 0, 1, 1)
        self.horizontalGroupBox_9 = QtGui.QGroupBox(self.groupBox_4)
        self.horizontalGroupBox_9.setObjectName(_fromUtf8("horizontalGroupBox_9"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.horizontalGroupBox_9)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.radioButton_ActivadoEmail = QtGui.QRadioButton(self.horizontalGroupBox_9)
        self.radioButton_ActivadoEmail.setStyleSheet(_fromUtf8("color: rgb(0, 85, 255);"))
        self.radioButton_ActivadoEmail.setObjectName(_fromUtf8("radioButton_ActivadoEmail"))
        self.horizontalLayout_11.addWidget(self.radioButton_ActivadoEmail)
        self.radioButton_DesactivadoEmail = QtGui.QRadioButton(self.horizontalGroupBox_9)
        self.radioButton_DesactivadoEmail.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.radioButton_DesactivadoEmail.setChecked(True)
        self.radioButton_DesactivadoEmail.setObjectName(_fromUtf8("radioButton_DesactivadoEmail"))
        self.horizontalLayout_11.addWidget(self.radioButton_DesactivadoEmail)
        self.gridLayout_6.addWidget(self.horizontalGroupBox_9, 2, 1, 1, 1)
        self.horizontalGroupBox_12 = QtGui.QGroupBox(self.groupBox_4)
        self.horizontalGroupBox_12.setObjectName(_fromUtf8("horizontalGroupBox_12"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.horizontalGroupBox_12)
        self.horizontalLayout_14.setMargin(9)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.radioButton_ActivadoWeb = QtGui.QRadioButton(self.horizontalGroupBox_12)
        self.radioButton_ActivadoWeb.setStyleSheet(_fromUtf8("color: rgb(85, 85, 255);"))
        self.radioButton_ActivadoWeb.setObjectName(_fromUtf8("radioButton_ActivadoWeb"))
        self.horizontalLayout_14.addWidget(self.radioButton_ActivadoWeb)
        self.radioButton_DesactivadoWeb = QtGui.QRadioButton(self.horizontalGroupBox_12)
        self.radioButton_DesactivadoWeb.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.radioButton_DesactivadoWeb.setChecked(True)
        self.radioButton_DesactivadoWeb.setObjectName(_fromUtf8("radioButton_DesactivadoWeb"))
        self.horizontalLayout_14.addWidget(self.radioButton_DesactivadoWeb)
        self.gridLayout_6.addWidget(self.horizontalGroupBox_12, 4, 1, 1, 1)
        self.horizontalGroupBox_10 = QtGui.QGroupBox(self.groupBox_4)
        self.horizontalGroupBox_10.setObjectName(_fromUtf8("horizontalGroupBox_10"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.horizontalGroupBox_10)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.radioButton_ActivadoMonitoreo = QtGui.QRadioButton(self.horizontalGroupBox_10)
        self.radioButton_ActivadoMonitoreo.setStyleSheet(_fromUtf8("color: rgb(85, 85, 255);"))
        self.radioButton_ActivadoMonitoreo.setObjectName(_fromUtf8("radioButton_ActivadoMonitoreo"))
        self.horizontalLayout_12.addWidget(self.radioButton_ActivadoMonitoreo)
        self.radioButton_DesactivadoMonitoreo = QtGui.QRadioButton(self.horizontalGroupBox_10)
        self.radioButton_DesactivadoMonitoreo.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.radioButton_DesactivadoMonitoreo.setChecked(True)
        self.radioButton_DesactivadoMonitoreo.setObjectName(_fromUtf8("radioButton_DesactivadoMonitoreo"))
        self.horizontalLayout_12.addWidget(self.radioButton_DesactivadoMonitoreo)
        self.gridLayout_6.addWidget(self.horizontalGroupBox_10, 3, 1, 1, 1)
        self.horizontalGroupBox_11 = QtGui.QGroupBox(self.groupBox_4)
        self.horizontalGroupBox_11.setObjectName(_fromUtf8("horizontalGroupBox_11"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.horizontalGroupBox_11)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.radioButton_ActivadoSMS = QtGui.QRadioButton(self.horizontalGroupBox_11)
        self.radioButton_ActivadoSMS.setStyleSheet(_fromUtf8("color: rgb(85, 85, 255);"))
        self.radioButton_ActivadoSMS.setObjectName(_fromUtf8("radioButton_ActivadoSMS"))
        self.horizontalLayout_13.addWidget(self.radioButton_ActivadoSMS)
        self.radioButton_DesactivadoSMS = QtGui.QRadioButton(self.horizontalGroupBox_11)
        self.radioButton_DesactivadoSMS.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);\n"
""))
        self.radioButton_DesactivadoSMS.setChecked(True)
        self.radioButton_DesactivadoSMS.setObjectName(_fromUtf8("radioButton_DesactivadoSMS"))
        self.horizontalLayout_13.addWidget(self.radioButton_DesactivadoSMS)
        self.gridLayout_6.addWidget(self.horizontalGroupBox_11, 1, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_4, 2, 2, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_Agregar = QtGui.QPushButton(VentanaNuevoCliente)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Agregar.setIcon(icon1)
        self.pushButton_Agregar.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_Agregar.setFlat(True)
        self.pushButton_Agregar.setObjectName(_fromUtf8("pushButton_Agregar"))
        self.horizontalLayout.addWidget(self.pushButton_Agregar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_7.addLayout(self.horizontalLayout, 3, 0, 1, 3)

        self.retranslateUi(VentanaNuevoCliente)
        QtCore.QMetaObject.connectSlotsByName(VentanaNuevoCliente)
        VentanaNuevoCliente.setTabOrder(self.comboBox_Empresa, self.comboBox_Prefijo)
        VentanaNuevoCliente.setTabOrder(self.comboBox_Prefijo, self.lineEdit_CodigoCliente)
        VentanaNuevoCliente.setTabOrder(self.lineEdit_CodigoCliente, self.lineEdit_NombreCuenta)
        VentanaNuevoCliente.setTabOrder(self.lineEdit_NombreCuenta, self.lineEdit_NumeroFiscal)
        VentanaNuevoCliente.setTabOrder(self.lineEdit_NumeroFiscal, self.comboBox_TipoDispositivo)
        VentanaNuevoCliente.setTabOrder(self.comboBox_TipoDispositivo, self.comboBox_TipoCuenta)
        VentanaNuevoCliente.setTabOrder(self.comboBox_TipoCuenta, self.comboBox_Marca)
        VentanaNuevoCliente.setTabOrder(self.comboBox_Marca, self.comboBox_Modelo)
        VentanaNuevoCliente.setTabOrder(self.comboBox_Modelo, self.comboBox_Protocolo)
        VentanaNuevoCliente.setTabOrder(self.comboBox_Protocolo, self.lineEdit_ClaveMaster)
        VentanaNuevoCliente.setTabOrder(self.lineEdit_ClaveMaster, self.dateTimeEdit_FechaInicio)
        VentanaNuevoCliente.setTabOrder(self.dateTimeEdit_FechaInicio, self.dateTimeEdit_FechaCorte)
        VentanaNuevoCliente.setTabOrder(self.dateTimeEdit_FechaCorte, self.lineEdit_Usuario)
        VentanaNuevoCliente.setTabOrder(self.lineEdit_Usuario, self.lineEdit_Clave)
        VentanaNuevoCliente.setTabOrder(self.lineEdit_Clave, self.comboBox_Instalador)
        VentanaNuevoCliente.setTabOrder(self.comboBox_Instalador, self.comboBox_Pais)
        VentanaNuevoCliente.setTabOrder(self.comboBox_Pais, self.comboBox_Estado)
        VentanaNuevoCliente.setTabOrder(self.comboBox_Estado, self.lineEdit_Ciudad)
        VentanaNuevoCliente.setTabOrder(self.lineEdit_Ciudad, self.textEdit_Direccion)
        VentanaNuevoCliente.setTabOrder(self.textEdit_Direccion, self.lineEdit_Referencia)
        VentanaNuevoCliente.setTabOrder(self.lineEdit_Referencia, self.lineEdit_Latitud)
        VentanaNuevoCliente.setTabOrder(self.lineEdit_Latitud, self.lineEdit_Longitud)
        VentanaNuevoCliente.setTabOrder(self.lineEdit_Longitud, self.lineEdit_Punto)
        VentanaNuevoCliente.setTabOrder(self.lineEdit_Punto, self.lineEdit_Llave)
        VentanaNuevoCliente.setTabOrder(self.lineEdit_Llave, self.pushButton_Imagen)
        VentanaNuevoCliente.setTabOrder(self.pushButton_Imagen, self.lineEdit_Email)
        VentanaNuevoCliente.setTabOrder(self.lineEdit_Email, self.lineEdit_PaginaWeb)
        VentanaNuevoCliente.setTabOrder(self.lineEdit_PaginaWeb, self.lineEdit_TelefonoLocal)
        VentanaNuevoCliente.setTabOrder(self.lineEdit_TelefonoLocal, self.lineEdit_Movil)
        VentanaNuevoCliente.setTabOrder(self.lineEdit_Movil, self.lineEdit_Fax)
        VentanaNuevoCliente.setTabOrder(self.lineEdit_Fax, self.comboBox_EstausGeneral)
        VentanaNuevoCliente.setTabOrder(self.comboBox_EstausGeneral, self.radioButton_ActivadoSMS)
        VentanaNuevoCliente.setTabOrder(self.radioButton_ActivadoSMS, self.radioButton_DesactivadoSMS)
        VentanaNuevoCliente.setTabOrder(self.radioButton_DesactivadoSMS, self.radioButton_ActivadoEmail)
        VentanaNuevoCliente.setTabOrder(self.radioButton_ActivadoEmail, self.radioButton_DesactivadoEmail)
        VentanaNuevoCliente.setTabOrder(self.radioButton_DesactivadoEmail, self.radioButton_ActivadoMonitoreo)
        VentanaNuevoCliente.setTabOrder(self.radioButton_ActivadoMonitoreo, self.radioButton_DesactivadoMonitoreo)
        VentanaNuevoCliente.setTabOrder(self.radioButton_DesactivadoMonitoreo, self.radioButton_ActivadoWeb)
        VentanaNuevoCliente.setTabOrder(self.radioButton_ActivadoWeb, self.radioButton_DesactivadoWeb)
        VentanaNuevoCliente.setTabOrder(self.radioButton_DesactivadoWeb, self.pushButton_Agregar)

    def retranslateUi(self, VentanaNuevoCliente):
        VentanaNuevoCliente.setWindowTitle(_translate("VentanaNuevoCliente", "Agregar Nuevo Cliente", None))
        self.label_69.setText(_translate("VentanaNuevoCliente", "Agregar Nuevo Cliente.", None))
        self.groupBox_2.setTitle(_translate("VentanaNuevoCliente", "Datos de Ubicacion", None))
        self.label_58.setText(_translate("VentanaNuevoCliente", "Imagen", None))
        self.pushButton_Imagen.setText(_translate("VentanaNuevoCliente", "Seleccionar", None))
        self.label_54.setText(_translate("VentanaNuevoCliente", "Pais", None))
        self.label_56.setText(_translate("VentanaNuevoCliente", "Ciudad", None))
        self.label_2.setText(_translate("VentanaNuevoCliente", "Llave", None))
        self.label_52.setText(_translate("VentanaNuevoCliente", "Longitud", None))
        self.label_55.setText(_translate("VentanaNuevoCliente", "Latitud", None))
        self.label.setText(_translate("VentanaNuevoCliente", "Punto / Tag", None))
        self.label_53.setText(_translate("VentanaNuevoCliente", "Estado", None))
        self.label_57.setText(_translate("VentanaNuevoCliente", "Direccion", None))
        self.label_51.setText(_translate("VentanaNuevoCliente", "Referencia", None))
        self.groupBox.setTitle(_translate("VentanaNuevoCliente", "Datos Principales", None))
        self.label_46.setText(_translate("VentanaNuevoCliente", "Empresa", None))
        self.label_37.setText(_translate("VentanaNuevoCliente", "Codigo Cliente", None))
        self.label_44.setText(_translate("VentanaNuevoCliente", "Nombre Cuenta", None))
        self.label_41.setText(_translate("VentanaNuevoCliente", "Tipo Cuenta:", None))
        self.label_39.setText(_translate("VentanaNuevoCliente", "Modelo", None))
        self.label_38.setText(_translate("VentanaNuevoCliente", "Numero Fiscal", None))
        self.label_40.setText(_translate("VentanaNuevoCliente", "Dispositivo:", None))
        self.label_43.setText(_translate("VentanaNuevoCliente", "Marca:", None))
        self.label_48.setText(_translate("VentanaNuevoCliente", "Clave Master", None))
        self.label_49.setText(_translate("VentanaNuevoCliente", "Protocolo", None))
        self.label_50.setText(_translate("VentanaNuevoCliente", "Fecha de Inicio", None))
        self.label_47.setText(_translate("VentanaNuevoCliente", "Fecha de Corte", None))
        self.label_45.setText(_translate("VentanaNuevoCliente", "Clave", None))
        self.label_42.setText(_translate("VentanaNuevoCliente", "Usuario", None))
        self.label_3.setText(_translate("VentanaNuevoCliente", "Instalador", None))
        self.groupBox_3.setTitle(_translate("VentanaNuevoCliente", "Datos de Contacto", None))
        self.label_60.setText(_translate("VentanaNuevoCliente", "Email", None))
        self.label_63.setText(_translate("VentanaNuevoCliente", "Pagina Web", None))
        self.label_59.setText(_translate("VentanaNuevoCliente", "Movil", None))
        self.label_62.setText(_translate("VentanaNuevoCliente", "Telefono Local", None))
        self.label_61.setText(_translate("VentanaNuevoCliente", "Fax", None))
        self.groupBox_4.setTitle(_translate("VentanaNuevoCliente", "Servicios", None))
        self.label_66.setText(_translate("VentanaNuevoCliente", "Estatus General", None))
        self.label_67.setText(_translate("VentanaNuevoCliente", "Estatus SMS", None))
        self.label_65.setText(_translate("VentanaNuevoCliente", "Estatus Email", None))
        self.label_68.setText(_translate("VentanaNuevoCliente", "Estatus Monitoreo", None))
        self.label_64.setText(_translate("VentanaNuevoCliente", "Estatus Web", None))
        self.radioButton_ActivadoEmail.setText(_translate("VentanaNuevoCliente", "Activado", None))
        self.radioButton_DesactivadoEmail.setText(_translate("VentanaNuevoCliente", "Desactivado", None))
        self.radioButton_ActivadoWeb.setText(_translate("VentanaNuevoCliente", "Activado", None))
        self.radioButton_DesactivadoWeb.setText(_translate("VentanaNuevoCliente", "Desactivado", None))
        self.radioButton_ActivadoMonitoreo.setText(_translate("VentanaNuevoCliente", "Activado", None))
        self.radioButton_DesactivadoMonitoreo.setText(_translate("VentanaNuevoCliente", "Desactivado", None))
        self.radioButton_ActivadoSMS.setText(_translate("VentanaNuevoCliente", "Activado", None))
        self.radioButton_DesactivadoSMS.setText(_translate("VentanaNuevoCliente", "Desactivado", None))
        self.pushButton_Agregar.setText(_translate("VentanaNuevoCliente", "Guardar", None))

import recursos_rc
