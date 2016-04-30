# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaPanelClienteAlarmas.ui'
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

class Ui_SubVentanaPanelClienteAlarmas(object):
    def setupUi(self, SubVentanaPanelClienteAlarmas):
        SubVentanaPanelClienteAlarmas.setObjectName(_fromUtf8("SubVentanaPanelClienteAlarmas"))
        SubVentanaPanelClienteAlarmas.resize(920, 548)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Lista-Clientes.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubVentanaPanelClienteAlarmas.setWindowIcon(icon)
        SubVentanaPanelClienteAlarmas.setStyleSheet(_fromUtf8("QTableView {\n"
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
"QToolBox::tab {\n"
"    background: #4276a4;\n"
"                             \n"
"    border-radius: 1px;\n"
"    color: darkgray;\n"
"}\n"
"\n"
"QToolBox::tab:selected { /* italicize selected tabs */\n"
"    \n"
"    color: white;\n"
"}"))
        self.gridLayout_3 = QtGui.QGridLayout(SubVentanaPanelClienteAlarmas)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(SubVentanaPanelClienteAlarmas)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_Empresa = QtGui.QLabel(self.groupBox)
        self.label_Empresa.setObjectName(_fromUtf8("label_Empresa"))
        self.gridLayout.addWidget(self.label_Empresa, 0, 1, 1, 1)
        self.label_Email = QtGui.QLabel(self.groupBox)
        self.label_Email.setWordWrap(True)
        self.label_Email.setObjectName(_fromUtf8("label_Email"))
        self.gridLayout.addWidget(self.label_Email, 4, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_TipoCliente = QtGui.QLabel(self.groupBox)
        self.label_TipoCliente.setObjectName(_fromUtf8("label_TipoCliente"))
        self.gridLayout.addWidget(self.label_TipoCliente, 5, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_Protocolo = QtGui.QLabel(self.groupBox)
        self.label_Protocolo.setObjectName(_fromUtf8("label_Protocolo"))
        self.gridLayout.addWidget(self.label_Protocolo, 6, 1, 1, 1)
        self.label_ClaveMaster = QtGui.QLabel(self.groupBox)
        self.label_ClaveMaster.setObjectName(_fromUtf8("label_ClaveMaster"))
        self.gridLayout.addWidget(self.label_ClaveMaster, 3, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_CodigoFiscal = QtGui.QLabel(self.groupBox)
        self.label_CodigoFiscal.setWordWrap(True)
        self.label_CodigoFiscal.setObjectName(_fromUtf8("label_CodigoFiscal"))
        self.gridLayout.addWidget(self.label_CodigoFiscal, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_CodigoCliente = QtGui.QLabel(self.groupBox)
        self.label_CodigoCliente.setObjectName(_fromUtf8("label_CodigoCliente"))
        self.gridLayout.addWidget(self.label_CodigoCliente, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(SubVentanaPanelClienteAlarmas)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_Referencia = QtGui.QLabel(self.groupBox_2)
        self.label_Referencia.setWordWrap(True)
        self.label_Referencia.setObjectName(_fromUtf8("label_Referencia"))
        self.gridLayout_2.addWidget(self.label_Referencia, 2, 1, 1, 1)
        self.label_TelefonoLocal = QtGui.QLabel(self.groupBox_2)
        self.label_TelefonoLocal.setWordWrap(True)
        self.label_TelefonoLocal.setObjectName(_fromUtf8("label_TelefonoLocal"))
        self.gridLayout_2.addWidget(self.label_TelefonoLocal, 3, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.groupBox_2)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_2.addWidget(self.label_19, 4, 0, 1, 1)
        self.label_UltimoEvento = QtGui.QLabel(self.groupBox_2)
        self.label_UltimoEvento.setObjectName(_fromUtf8("label_UltimoEvento"))
        self.gridLayout_2.addWidget(self.label_UltimoEvento, 5, 1, 1, 1)
        self.label_18 = QtGui.QLabel(self.groupBox_2)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_2.addWidget(self.label_18, 3, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)
        self.label_Direccion = QtGui.QLabel(self.groupBox_2)
        self.label_Direccion.setWordWrap(True)
        self.label_Direccion.setObjectName(_fromUtf8("label_Direccion"))
        self.gridLayout_2.addWidget(self.label_Direccion, 1, 1, 1, 1)
        self.label_Ciudad = QtGui.QLabel(self.groupBox_2)
        self.label_Ciudad.setWordWrap(True)
        self.label_Ciudad.setObjectName(_fromUtf8("label_Ciudad"))
        self.gridLayout_2.addWidget(self.label_Ciudad, 0, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.groupBox_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_2.addWidget(self.label_16, 1, 0, 1, 1)
        self.label_17 = QtGui.QLabel(self.groupBox_2)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_2.addWidget(self.label_17, 2, 0, 1, 1)
        self.label_20 = QtGui.QLabel(self.groupBox_2)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_2.addWidget(self.label_20, 5, 0, 1, 1)
        self.label_FechaInicio = QtGui.QLabel(self.groupBox_2)
        self.label_FechaInicio.setObjectName(_fromUtf8("label_FechaInicio"))
        self.gridLayout_2.addWidget(self.label_FechaInicio, 4, 1, 1, 1)
        self.label_21 = QtGui.QLabel(self.groupBox_2)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_2.addWidget(self.label_21, 6, 0, 1, 1)
        self.label_UltimoReporte = QtGui.QLabel(self.groupBox_2)
        self.label_UltimoReporte.setObjectName(_fromUtf8("label_UltimoReporte"))
        self.gridLayout_2.addWidget(self.label_UltimoReporte, 6, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.widget_11 = QtGui.QWidget(SubVentanaPanelClienteAlarmas)
        self.widget_11.setEnabled(True)
        self.widget_11.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_11.setStyleSheet(_fromUtf8("font: 75 12pt \"Calibri\";\n"
"\n"
"background-color: #38648B;\n"
"color: rgb(255, 255, 255);"))
        self.widget_11.setObjectName(_fromUtf8("widget_11"))
        self.gridLayout_26 = QtGui.QGridLayout(self.widget_11)
        self.gridLayout_26.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_26.setMargin(0)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName(_fromUtf8("gridLayout_26"))
        self.pushButton_StatusAlarma = QtGui.QPushButton(self.widget_11)
        self.pushButton_StatusAlarma.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/get-info-7.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_StatusAlarma.setIcon(icon1)
        self.pushButton_StatusAlarma.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_StatusAlarma.setFlat(True)
        self.pushButton_StatusAlarma.setObjectName(_fromUtf8("pushButton_StatusAlarma"))
        self.gridLayout_26.addWidget(self.pushButton_StatusAlarma, 0, 0, 1, 1)
        self.label_NombreCuenta = QtGui.QLabel(self.widget_11)
        self.label_NombreCuenta.setMinimumSize(QtCore.QSize(0, 30))
        self.label_NombreCuenta.setStyleSheet(_fromUtf8("font: 75 12pt \"Calibri\";\n"
"\n"
"background-color: #38648B;\n"
"color: rgb(255, 255, 255);"))
        self.label_NombreCuenta.setTextFormat(QtCore.Qt.AutoText)
        self.label_NombreCuenta.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_NombreCuenta.setObjectName(_fromUtf8("label_NombreCuenta"))
        self.gridLayout_26.addWidget(self.label_NombreCuenta, 0, 3, 1, 1)
        self.label_StatusAlarma = QtGui.QLabel(self.widget_11)
        self.label_StatusAlarma.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);\n"
"font: bold 12pt \"Calibri\";"))
        self.label_StatusAlarma.setObjectName(_fromUtf8("label_StatusAlarma"))
        self.gridLayout_26.addWidget(self.label_StatusAlarma, 0, 1, 1, 1)
        self.pushButton_Editar = QtGui.QPushButton(self.widget_11)
        self.pushButton_Editar.setStyleSheet(_fromUtf8("font: bold 11pt \"Calibri\";"))
        self.pushButton_Editar.setIcon(icon)
        self.pushButton_Editar.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_Editar.setDefault(False)
        self.pushButton_Editar.setFlat(True)
        self.pushButton_Editar.setObjectName(_fromUtf8("pushButton_Editar"))
        self.gridLayout_26.addWidget(self.pushButton_Editar, 0, 9, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_26.addItem(spacerItem, 0, 6, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout_26.addItem(spacerItem1, 0, 4, 1, 1)
        self.label_MarcaModelo = QtGui.QLabel(self.widget_11)
        self.label_MarcaModelo.setStyleSheet(_fromUtf8("font: bold 11pt \"Calibri\";"))
        self.label_MarcaModelo.setObjectName(_fromUtf8("label_MarcaModelo"))
        self.gridLayout_26.addWidget(self.label_MarcaModelo, 0, 5, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout_26.addItem(spacerItem2, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.widget_11, 0, 0, 1, 2)
        self.tabWidget = QtGui.QTabWidget(SubVentanaPanelClienteAlarmas)
        self.tabWidget.setStyleSheet(_fromUtf8(""))
        self.tabWidget.setIconSize(QtCore.QSize(24, 24))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_Zonas = QtGui.QWidget()
        self.tab_Zonas.setObjectName(_fromUtf8("tab_Zonas"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_Zonas)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab_Zonas)
        self.groupBox_7.setStyleSheet(_fromUtf8(""))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.gridLayout_12 = QtGui.QGridLayout(self.groupBox_7)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.label_11 = QtGui.QLabel(self.groupBox_7)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_12.addWidget(self.label_11, 0, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(213, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem3, 0, 2, 1, 1)
        self.pushButton_AgregarZona = QtGui.QPushButton(self.groupBox_7)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/4-Icone-plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AgregarZona.setIcon(icon2)
        self.pushButton_AgregarZona.setDefault(False)
        self.pushButton_AgregarZona.setObjectName(_fromUtf8("pushButton_AgregarZona"))
        self.gridLayout_12.addWidget(self.pushButton_AgregarZona, 0, 3, 1, 1)
        self.lineEdit_BuscarZonas = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_BuscarZonas.setObjectName(_fromUtf8("lineEdit_BuscarZonas"))
        self.gridLayout_12.addWidget(self.lineEdit_BuscarZonas, 0, 1, 1, 1)
        self.tableWidget_Zonas = QtGui.QTableWidget(self.groupBox_7)
        self.tableWidget_Zonas.setObjectName(_fromUtf8("tableWidget_Zonas"))
        self.tableWidget_Zonas.setColumnCount(4)
        self.tableWidget_Zonas.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_Zonas.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Zonas.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Zonas.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Zonas.setHorizontalHeaderItem(3, item)
        self.gridLayout_12.addWidget(self.tableWidget_Zonas, 1, 0, 1, 4)
        self.gridLayout_5.addWidget(self.groupBox_7, 0, 0, 1, 2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/connections-512(1).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_Zonas, icon3, _fromUtf8(""))
        self.tab_Usuarios = QtGui.QWidget()
        self.tab_Usuarios.setObjectName(_fromUtf8("tab_Usuarios"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_Usuarios)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.groupBox_8 = QtGui.QGroupBox(self.tab_Usuarios)
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.gridLayout_13 = QtGui.QGridLayout(self.groupBox_8)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.label_BuscarUsuarios = QtGui.QLabel(self.groupBox_8)
        self.label_BuscarUsuarios.setObjectName(_fromUtf8("label_BuscarUsuarios"))
        self.gridLayout_13.addWidget(self.label_BuscarUsuarios, 0, 0, 1, 1)
        self.lineEdit_BuscarUsuarios = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_BuscarUsuarios.setObjectName(_fromUtf8("lineEdit_BuscarUsuarios"))
        self.gridLayout_13.addWidget(self.lineEdit_BuscarUsuarios, 0, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(210, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem4, 0, 2, 1, 1)
        self.pushButton_AgregarUsuario = QtGui.QPushButton(self.groupBox_8)
        self.pushButton_AgregarUsuario.setIcon(icon2)
        self.pushButton_AgregarUsuario.setAutoDefault(False)
        self.pushButton_AgregarUsuario.setDefault(False)
        self.pushButton_AgregarUsuario.setFlat(False)
        self.pushButton_AgregarUsuario.setObjectName(_fromUtf8("pushButton_AgregarUsuario"))
        self.gridLayout_13.addWidget(self.pushButton_AgregarUsuario, 0, 3, 1, 1)
        self.tableWidget_Usuarios = QtGui.QTableWidget(self.groupBox_8)
        self.tableWidget_Usuarios.setObjectName(_fromUtf8("tableWidget_Usuarios"))
        self.tableWidget_Usuarios.setColumnCount(5)
        self.tableWidget_Usuarios.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Usuarios.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Usuarios.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Usuarios.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Usuarios.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Usuarios.setHorizontalHeaderItem(4, item)
        self.gridLayout_13.addWidget(self.tableWidget_Usuarios, 1, 0, 1, 4)
        self.gridLayout_6.addWidget(self.groupBox_8, 0, 0, 1, 1)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Edit-Male-User-icon48x48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_Usuarios, icon4, _fromUtf8(""))
        self.tab_Notificaciones = QtGui.QWidget()
        self.tab_Notificaciones.setObjectName(_fromUtf8("tab_Notificaciones"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_Notificaciones)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_Notificaciones)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_27 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_27.setObjectName(_fromUtf8("gridLayout_27"))
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_27.addWidget(self.label_8, 0, 0, 1, 1)
        self.comboBox_UsuariosNotificacion = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_UsuariosNotificacion.setObjectName(_fromUtf8("comboBox_UsuariosNotificacion"))
        self.gridLayout_27.addWidget(self.comboBox_UsuariosNotificacion, 0, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_27.addWidget(self.label_9, 1, 0, 1, 1)
        self.comboBox_TipoNotificacion = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_TipoNotificacion.setObjectName(_fromUtf8("comboBox_TipoNotificacion"))
        self.comboBox_TipoNotificacion.addItem(_fromUtf8(""))
        self.comboBox_TipoNotificacion.addItem(_fromUtf8(""))
        self.gridLayout_27.addWidget(self.comboBox_TipoNotificacion, 1, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_27.addWidget(self.label_10, 2, 0, 1, 1)
        self.comboBox_Planes = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_Planes.setObjectName(_fromUtf8("comboBox_Planes"))
        self.gridLayout_27.addWidget(self.comboBox_Planes, 2, 1, 1, 1)
        self.tableWidget_EventosPlan = QtGui.QTableWidget(self.groupBox_3)
        self.tableWidget_EventosPlan.setObjectName(_fromUtf8("tableWidget_EventosPlan"))
        self.tableWidget_EventosPlan.setColumnCount(2)
        self.tableWidget_EventosPlan.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_EventosPlan.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_EventosPlan.setHorizontalHeaderItem(1, item)
        self.gridLayout_27.addWidget(self.tableWidget_EventosPlan, 3, 0, 1, 2)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem5, 0, 0, 1, 1)
        self.pushButton_AsignarPlan = QtGui.QPushButton(self.groupBox_3)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AsignarPlan.setIcon(icon5)
        self.pushButton_AsignarPlan.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_AsignarPlan.setFlat(True)
        self.pushButton_AsignarPlan.setObjectName(_fromUtf8("pushButton_AsignarPlan"))
        self.gridLayout_8.addWidget(self.pushButton_AsignarPlan, 0, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem6, 0, 2, 1, 1)
        self.gridLayout_27.addLayout(self.gridLayout_8, 4, 0, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_5 = QtGui.QGroupBox(self.tab_Notificaciones)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.scrollArea = QtGui.QScrollArea(self.groupBox_5)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 576, 224))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_7 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.toolBox_UsuariosEventos = QtGui.QToolBox(self.scrollAreaWidgetContents)
        self.toolBox_UsuariosEventos.setStyleSheet(_fromUtf8("QToolBox::tab {\n"
"    background: #4276a4;\n"
"                             \n"
"    border-radius: 1px;\n"
"    color: darkgray;\n"
"}\n"
"\n"
"QToolBox::tab:selected { /* italicize selected tabs */\n"
"    \n"
"    color: white;\n"
"}"))
        self.toolBox_UsuariosEventos.setObjectName(_fromUtf8("toolBox_UsuariosEventos"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 558, 179))
        self.page.setObjectName(_fromUtf8("page"))
        self.toolBox_UsuariosEventos.addItem(self.page, _fromUtf8(""))
        self.gridLayout_7.addWidget(self.toolBox_UsuariosEventos, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_9.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_5, 0, 1, 1, 1)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Codigos_Alarmas.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_Notificaciones, icon6, _fromUtf8(""))
        self.tab_SMS = QtGui.QWidget()
        self.tab_SMS.setObjectName(_fromUtf8("tab_SMS"))
        self.gridLayout_16 = QtGui.QGridLayout(self.tab_SMS)
        self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
        self.groupBox_9 = QtGui.QGroupBox(self.tab_SMS)
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.gridLayout_17 = QtGui.QGridLayout(self.groupBox_9)
        self.gridLayout_17.setObjectName(_fromUtf8("gridLayout_17"))
        self.pushButton_ExportarSMSXLS = QtGui.QPushButton(self.groupBox_9)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/XLS.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ExportarSMSXLS.setIcon(icon7)
        self.pushButton_ExportarSMSXLS.setFlat(True)
        self.pushButton_ExportarSMSXLS.setObjectName(_fromUtf8("pushButton_ExportarSMSXLS"))
        self.gridLayout_17.addWidget(self.pushButton_ExportarSMSXLS, 0, 4, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(276, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem7, 0, 0, 1, 1)
        self.tableWidget_SMS = QtGui.QTableWidget(self.groupBox_9)
        self.tableWidget_SMS.setObjectName(_fromUtf8("tableWidget_SMS"))
        self.tableWidget_SMS.setColumnCount(3)
        self.tableWidget_SMS.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SMS.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SMS.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SMS.setHorizontalHeaderItem(2, item)
        self.gridLayout_17.addWidget(self.tableWidget_SMS, 1, 0, 1, 5)
        self.pushButton_ExportarSMSPDF = QtGui.QPushButton(self.groupBox_9)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/PDF.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ExportarSMSPDF.setIcon(icon8)
        self.pushButton_ExportarSMSPDF.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_ExportarSMSPDF.setDefault(False)
        self.pushButton_ExportarSMSPDF.setFlat(True)
        self.pushButton_ExportarSMSPDF.setObjectName(_fromUtf8("pushButton_ExportarSMSPDF"))
        self.gridLayout_17.addWidget(self.pushButton_ExportarSMSPDF, 0, 3, 1, 1)
        self.label_FechaHistorialSMS = QtGui.QLabel(self.groupBox_9)
        self.label_FechaHistorialSMS.setObjectName(_fromUtf8("label_FechaHistorialSMS"))
        self.gridLayout_17.addWidget(self.label_FechaHistorialSMS, 0, 1, 1, 1)
        self.comboBox_FechaHistorialSMS = QtGui.QComboBox(self.groupBox_9)
        self.comboBox_FechaHistorialSMS.setObjectName(_fromUtf8("comboBox_FechaHistorialSMS"))
        self.gridLayout_17.addWidget(self.comboBox_FechaHistorialSMS, 0, 2, 1, 1)
        self.tableWidget_SMS.raise_()
        self.pushButton_ExportarSMSXLS.raise_()
        self.pushButton_ExportarSMSPDF.raise_()
        self.label_FechaHistorialSMS.raise_()
        self.comboBox_FechaHistorialSMS.raise_()
        self.gridLayout_16.addWidget(self.groupBox_9, 0, 0, 1, 1)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/sms-search-icon (1).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_SMS, icon9, _fromUtf8(""))
        self.tab_Contactos = QtGui.QWidget()
        self.tab_Contactos.setObjectName(_fromUtf8("tab_Contactos"))
        self.gridLayout_10 = QtGui.QGridLayout(self.tab_Contactos)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab_Contactos)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout_11 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.lineEdit_BuscarContactos = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_BuscarContactos.setObjectName(_fromUtf8("lineEdit_BuscarContactos"))
        self.gridLayout_11.addWidget(self.lineEdit_BuscarContactos, 1, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.groupBox_6)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_11.addWidget(self.label_13, 1, 0, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(241, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem8, 1, 2, 1, 1)
        self.pushButton_AgregarContacto = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_AgregarContacto.setIcon(icon2)
        self.pushButton_AgregarContacto.setDefault(False)
        self.pushButton_AgregarContacto.setObjectName(_fromUtf8("pushButton_AgregarContacto"))
        self.gridLayout_11.addWidget(self.pushButton_AgregarContacto, 1, 3, 1, 1)
        self.tableWidget_Contactos = QtGui.QTableWidget(self.groupBox_6)
        self.tableWidget_Contactos.setObjectName(_fromUtf8("tableWidget_Contactos"))
        self.tableWidget_Contactos.setColumnCount(4)
        self.tableWidget_Contactos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Contactos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Contactos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Contactos.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Contactos.setHorizontalHeaderItem(3, item)
        self.gridLayout_11.addWidget(self.tableWidget_Contactos, 5, 0, 1, 4)
        self.tableWidget_Contactos.raise_()
        self.lineEdit_BuscarContactos.raise_()
        self.label_13.raise_()
        self.pushButton_AgregarContacto.raise_()
        self.gridLayout_10.addWidget(self.groupBox_6, 0, 0, 1, 1)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Nuevo_Cliente6.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_Contactos, icon10, _fromUtf8(""))
        self.tab_Horarios = QtGui.QWidget()
        self.tab_Horarios.setObjectName(_fromUtf8("tab_Horarios"))
        self.gridLayout_14 = QtGui.QGridLayout(self.tab_Horarios)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.groupBox_Horarios = QtGui.QGroupBox(self.tab_Horarios)
        self.groupBox_Horarios.setObjectName(_fromUtf8("groupBox_Horarios"))
        self.gridLayout_15 = QtGui.QGridLayout(self.groupBox_Horarios)
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.label_DiaHorario = QtGui.QLabel(self.groupBox_Horarios)
        self.label_DiaHorario.setObjectName(_fromUtf8("label_DiaHorario"))
        self.gridLayout_15.addWidget(self.label_DiaHorario, 0, 0, 1, 1)
        self.comboBox_DiaHorario = QtGui.QComboBox(self.groupBox_Horarios)
        self.comboBox_DiaHorario.setObjectName(_fromUtf8("comboBox_DiaHorario"))
        self.comboBox_DiaHorario.addItem(_fromUtf8(""))
        self.comboBox_DiaHorario.addItem(_fromUtf8(""))
        self.comboBox_DiaHorario.addItem(_fromUtf8(""))
        self.comboBox_DiaHorario.addItem(_fromUtf8(""))
        self.comboBox_DiaHorario.addItem(_fromUtf8(""))
        self.comboBox_DiaHorario.addItem(_fromUtf8(""))
        self.comboBox_DiaHorario.addItem(_fromUtf8(""))
        self.comboBox_DiaHorario.addItem(_fromUtf8(""))
        self.comboBox_DiaHorario.addItem(_fromUtf8(""))
        self.gridLayout_15.addWidget(self.comboBox_DiaHorario, 0, 1, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(371, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem9, 0, 2, 1, 1)
        self.pushButton_AgregarHorario = QtGui.QPushButton(self.groupBox_Horarios)
        self.pushButton_AgregarHorario.setIcon(icon2)
        self.pushButton_AgregarHorario.setDefault(False)
        self.pushButton_AgregarHorario.setFlat(False)
        self.pushButton_AgregarHorario.setObjectName(_fromUtf8("pushButton_AgregarHorario"))
        self.gridLayout_15.addWidget(self.pushButton_AgregarHorario, 0, 3, 1, 1)
        self.tableWidget_Horarios = QtGui.QTableWidget(self.groupBox_Horarios)
        self.tableWidget_Horarios.setObjectName(_fromUtf8("tableWidget_Horarios"))
        self.tableWidget_Horarios.setColumnCount(5)
        self.tableWidget_Horarios.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Horarios.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Horarios.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Horarios.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Horarios.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Horarios.setHorizontalHeaderItem(4, item)
        self.gridLayout_15.addWidget(self.tableWidget_Horarios, 1, 0, 1, 4)
        self.tableWidget_Horarios.raise_()
        self.label_DiaHorario.raise_()
        self.comboBox_DiaHorario.raise_()
        self.pushButton_AgregarHorario.raise_()
        self.gridLayout_14.addWidget(self.groupBox_Horarios, 0, 0, 1, 1)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/calendar-add2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_Horarios, icon11, _fromUtf8(""))
        self.tab_Senales = QtGui.QWidget()
        self.tab_Senales.setObjectName(_fromUtf8("tab_Senales"))
        self.gridLayout_18 = QtGui.QGridLayout(self.tab_Senales)
        self.gridLayout_18.setObjectName(_fromUtf8("gridLayout_18"))
        self.groupBox_10 = QtGui.QGroupBox(self.tab_Senales)
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.gridLayout_19 = QtGui.QGridLayout(self.groupBox_10)
        self.gridLayout_19.setObjectName(_fromUtf8("gridLayout_19"))
        self.comboBox_FechaHistorialSenales = QtGui.QComboBox(self.groupBox_10)
        self.comboBox_FechaHistorialSenales.setObjectName(_fromUtf8("comboBox_FechaHistorialSenales"))
        self.gridLayout_19.addWidget(self.comboBox_FechaHistorialSenales, 0, 10, 1, 1)
        self.pushButton_BuscarAvanzado = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_BuscarAvanzado.setText(_fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/6-Loupe.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_BuscarAvanzado.setIcon(icon12)
        self.pushButton_BuscarAvanzado.setDefault(False)
        self.pushButton_BuscarAvanzado.setFlat(True)
        self.pushButton_BuscarAvanzado.setObjectName(_fromUtf8("pushButton_BuscarAvanzado"))
        self.gridLayout_19.addWidget(self.pushButton_BuscarAvanzado, 0, 8, 1, 1)
        self.dateEdit_FechaHasta = QtGui.QDateEdit(self.groupBox_10)
        self.dateEdit_FechaHasta.setEnabled(True)
        self.dateEdit_FechaHasta.setCalendarPopup(True)
        self.dateEdit_FechaHasta.setObjectName(_fromUtf8("dateEdit_FechaHasta"))
        self.gridLayout_19.addWidget(self.dateEdit_FechaHasta, 0, 5, 1, 1)
        self.pushButton_SenalesExportarPDF = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_SenalesExportarPDF.setIcon(icon8)
        self.pushButton_SenalesExportarPDF.setFlat(True)
        self.pushButton_SenalesExportarPDF.setObjectName(_fromUtf8("pushButton_SenalesExportarPDF"))
        self.gridLayout_19.addWidget(self.pushButton_SenalesExportarPDF, 0, 12, 1, 1)
        self.label_22 = QtGui.QLabel(self.groupBox_10)
        self.label_22.setEnabled(True)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_19.addWidget(self.label_22, 0, 6, 1, 1)
        self.label_FechaHistorialSenales = QtGui.QLabel(self.groupBox_10)
        self.label_FechaHistorialSenales.setObjectName(_fromUtf8("label_FechaHistorialSenales"))
        self.gridLayout_19.addWidget(self.label_FechaHistorialSenales, 0, 9, 1, 1)
        self.comboBox_Eventos = QtGui.QComboBox(self.groupBox_10)
        self.comboBox_Eventos.setEnabled(True)
        self.comboBox_Eventos.setObjectName(_fromUtf8("comboBox_Eventos"))
        self.gridLayout_19.addWidget(self.comboBox_Eventos, 0, 7, 1, 1)
        self.pushButton_SenalesExportarXLS = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_SenalesExportarXLS.setIcon(icon7)
        self.pushButton_SenalesExportarXLS.setFlat(True)
        self.pushButton_SenalesExportarXLS.setObjectName(_fromUtf8("pushButton_SenalesExportarXLS"))
        self.gridLayout_19.addWidget(self.pushButton_SenalesExportarXLS, 0, 13, 1, 1)
        self.tableWidget_Senales = QtGui.QTableWidget(self.groupBox_10)
        self.tableWidget_Senales.setObjectName(_fromUtf8("tableWidget_Senales"))
        self.tableWidget_Senales.setColumnCount(4)
        self.tableWidget_Senales.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Senales.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Senales.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Senales.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Senales.setHorizontalHeaderItem(3, item)
        self.gridLayout_19.addWidget(self.tableWidget_Senales, 2, 0, 1, 14)
        self.label_12 = QtGui.QLabel(self.groupBox_10)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_19.addWidget(self.label_12, 0, 2, 1, 1)
        self.pushButton_SelectorBusqueda = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_SelectorBusqueda.setObjectName(_fromUtf8("pushButton_SelectorBusqueda"))
        self.gridLayout_19.addWidget(self.pushButton_SelectorBusqueda, 0, 0, 1, 1)
        self.dateEdit_FechaDesde = QtGui.QDateEdit(self.groupBox_10)
        self.dateEdit_FechaDesde.setEnabled(True)
        self.dateEdit_FechaDesde.setCalendarPopup(True)
        self.dateEdit_FechaDesde.setObjectName(_fromUtf8("dateEdit_FechaDesde"))
        self.gridLayout_19.addWidget(self.dateEdit_FechaDesde, 0, 3, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox_10)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_19.addWidget(self.label_14, 0, 4, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem10, 0, 11, 1, 1)
        self.gridLayout_18.addWidget(self.groupBox_10, 0, 0, 1, 1)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Ven_Rep_avtivaciones.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_Senales, icon13, _fromUtf8(""))
        self.tab_Notas = QtGui.QWidget()
        self.tab_Notas.setObjectName(_fromUtf8("tab_Notas"))
        self.gridLayout_20 = QtGui.QGridLayout(self.tab_Notas)
        self.gridLayout_20.setObjectName(_fromUtf8("gridLayout_20"))
        self.groupBox_NotaFija = QtGui.QGroupBox(self.tab_Notas)
        self.groupBox_NotaFija.setObjectName(_fromUtf8("groupBox_NotaFija"))
        self.gridLayout_23 = QtGui.QGridLayout(self.groupBox_NotaFija)
        self.gridLayout_23.setObjectName(_fromUtf8("gridLayout_23"))
        self.pushButton_AsignarNotaFija = QtGui.QPushButton(self.groupBox_NotaFija)
        self.pushButton_AsignarNotaFija.setIcon(icon5)
        self.pushButton_AsignarNotaFija.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_AsignarNotaFija.setAutoDefault(False)
        self.pushButton_AsignarNotaFija.setDefault(False)
        self.pushButton_AsignarNotaFija.setFlat(True)
        self.pushButton_AsignarNotaFija.setObjectName(_fromUtf8("pushButton_AsignarNotaFija"))
        self.gridLayout_23.addWidget(self.pushButton_AsignarNotaFija, 1, 1, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_23.addItem(spacerItem11, 1, 0, 1, 1)
        self.textEdit_NotaFija = QtGui.QTextEdit(self.groupBox_NotaFija)
        self.textEdit_NotaFija.setObjectName(_fromUtf8("textEdit_NotaFija"))
        self.gridLayout_23.addWidget(self.textEdit_NotaFija, 0, 0, 1, 4)
        self.pushButton_BorrarNotaFija = QtGui.QPushButton(self.groupBox_NotaFija)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/uncheck.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_BorrarNotaFija.setIcon(icon14)
        self.pushButton_BorrarNotaFija.setIconSize(QtCore.QSize(23, 23))
        self.pushButton_BorrarNotaFija.setFlat(True)
        self.pushButton_BorrarNotaFija.setObjectName(_fromUtf8("pushButton_BorrarNotaFija"))
        self.gridLayout_23.addWidget(self.pushButton_BorrarNotaFija, 1, 2, 1, 1)
        self.gridLayout_20.addWidget(self.groupBox_NotaFija, 0, 0, 1, 1)
        self.groupBox_NotaTemporal = QtGui.QGroupBox(self.tab_Notas)
        self.groupBox_NotaTemporal.setObjectName(_fromUtf8("groupBox_NotaTemporal"))
        self.gridLayout_22 = QtGui.QGridLayout(self.groupBox_NotaTemporal)
        self.gridLayout_22.setObjectName(_fromUtf8("gridLayout_22"))
        self.label_Hasta = QtGui.QLabel(self.groupBox_NotaTemporal)
        self.label_Hasta.setObjectName(_fromUtf8("label_Hasta"))
        self.gridLayout_22.addWidget(self.label_Hasta, 0, 2, 1, 1)
        self.dateTimeEdit_FechaNotaTemporalDesde = QtGui.QDateTimeEdit(self.groupBox_NotaTemporal)
        self.dateTimeEdit_FechaNotaTemporalDesde.setCalendarPopup(True)
        self.dateTimeEdit_FechaNotaTemporalDesde.setObjectName(_fromUtf8("dateTimeEdit_FechaNotaTemporalDesde"))
        self.gridLayout_22.addWidget(self.dateTimeEdit_FechaNotaTemporalDesde, 1, 0, 1, 2)
        self.textEdit_NotaTemporal = QtGui.QTextEdit(self.groupBox_NotaTemporal)
        self.textEdit_NotaTemporal.setObjectName(_fromUtf8("textEdit_NotaTemporal"))
        self.gridLayout_22.addWidget(self.textEdit_NotaTemporal, 2, 0, 1, 5)
        self.label_Desde = QtGui.QLabel(self.groupBox_NotaTemporal)
        self.label_Desde.setObjectName(_fromUtf8("label_Desde"))
        self.gridLayout_22.addWidget(self.label_Desde, 0, 0, 1, 1)
        self.dateTimeEdit_FechaNotaTemporalHasta = QtGui.QDateTimeEdit(self.groupBox_NotaTemporal)
        self.dateTimeEdit_FechaNotaTemporalHasta.setCalendarPopup(True)
        self.dateTimeEdit_FechaNotaTemporalHasta.setObjectName(_fromUtf8("dateTimeEdit_FechaNotaTemporalHasta"))
        self.gridLayout_22.addWidget(self.dateTimeEdit_FechaNotaTemporalHasta, 1, 2, 1, 3)
        self.pushButton_BorrarNotaTemporal = QtGui.QPushButton(self.groupBox_NotaTemporal)
        self.pushButton_BorrarNotaTemporal.setIcon(icon14)
        self.pushButton_BorrarNotaTemporal.setIconSize(QtCore.QSize(23, 23))
        self.pushButton_BorrarNotaTemporal.setFlat(True)
        self.pushButton_BorrarNotaTemporal.setObjectName(_fromUtf8("pushButton_BorrarNotaTemporal"))
        self.gridLayout_22.addWidget(self.pushButton_BorrarNotaTemporal, 3, 4, 1, 1)
        self.pushButton_AsignarNotaTemporal = QtGui.QPushButton(self.groupBox_NotaTemporal)
        self.pushButton_AsignarNotaTemporal.setIcon(icon5)
        self.pushButton_AsignarNotaTemporal.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_AsignarNotaTemporal.setFlat(True)
        self.pushButton_AsignarNotaTemporal.setObjectName(_fromUtf8("pushButton_AsignarNotaTemporal"))
        self.gridLayout_22.addWidget(self.pushButton_AsignarNotaTemporal, 3, 3, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_22.addItem(spacerItem12, 3, 0, 1, 3)
        self.gridLayout_20.addWidget(self.groupBox_NotaTemporal, 0, 1, 1, 1)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/note_text-edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_Notas, icon15, _fromUtf8(""))
        self.tab_Mapa = QtGui.QWidget()
        self.tab_Mapa.setObjectName(_fromUtf8("tab_Mapa"))
        self.gridLayout_21 = QtGui.QGridLayout(self.tab_Mapa)
        self.gridLayout_21.setObjectName(_fromUtf8("gridLayout_21"))
        self.groupBox_Mapa = QtGui.QGroupBox(self.tab_Mapa)
        self.groupBox_Mapa.setObjectName(_fromUtf8("groupBox_Mapa"))
        self.gridLayout_25 = QtGui.QGridLayout(self.groupBox_Mapa)
        self.gridLayout_25.setObjectName(_fromUtf8("gridLayout_25"))
        self.webView_Mapa = QtWebKit.QWebView(self.groupBox_Mapa)
        self.webView_Mapa.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView_Mapa.setObjectName(_fromUtf8("webView_Mapa"))
        self.gridLayout_25.addWidget(self.webView_Mapa, 0, 0, 1, 2)
        self.gridLayout_21.addWidget(self.groupBox_Mapa, 0, 0, 1, 1)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Maps.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_Mapa, icon16, _fromUtf8(""))
        self.tab_Camaras = QtGui.QWidget()
        self.tab_Camaras.setObjectName(_fromUtf8("tab_Camaras"))
        self.gridLayout_24 = QtGui.QGridLayout(self.tab_Camaras)
        self.gridLayout_24.setObjectName(_fromUtf8("gridLayout_24"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_Camaras)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_38 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_38.setObjectName(_fromUtf8("gridLayout_38"))
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_38.addItem(spacerItem13, 0, 0, 1, 1)
        self.pushButton_AgregarCCTV = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_AgregarCCTV.setIcon(icon2)
        self.pushButton_AgregarCCTV.setDefault(False)
        self.pushButton_AgregarCCTV.setFlat(False)
        self.pushButton_AgregarCCTV.setObjectName(_fromUtf8("pushButton_AgregarCCTV"))
        self.gridLayout_38.addWidget(self.pushButton_AgregarCCTV, 0, 1, 1, 1)
        self.treeWidget_Camaras = QtGui.QTreeWidget(self.groupBox_4)
        self.treeWidget_Camaras.setObjectName(_fromUtf8("treeWidget_Camaras"))
        self.gridLayout_38.addWidget(self.treeWidget_Camaras, 1, 0, 1, 2)
        self.gridLayout_24.addWidget(self.groupBox_4, 1, 0, 1, 1)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/CCTVICON.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_Camaras, icon17, _fromUtf8(""))
        self.tab_Equipos = QtGui.QWidget()
        self.tab_Equipos.setObjectName(_fromUtf8("tab_Equipos"))
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Departamentos.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_Equipos, icon18, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 2, 0, 1, 2)

        self.retranslateUi(SubVentanaPanelClienteAlarmas)
        self.tabWidget.setCurrentIndex(0)
        self.comboBox_TipoNotificacion.setCurrentIndex(-1)
        self.toolBox_UsuariosEventos.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaPanelClienteAlarmas)

    def retranslateUi(self, SubVentanaPanelClienteAlarmas):
        SubVentanaPanelClienteAlarmas.setWindowTitle(_translate("SubVentanaPanelClienteAlarmas", "Panel del Cliente", None))
        self.groupBox.setTitle(_translate("SubVentanaPanelClienteAlarmas", "Datos del Cliente", None))
        self.label_Empresa.setText(_translate("SubVentanaPanelClienteAlarmas", "----------------------", None))
        self.label_Email.setText(_translate("SubVentanaPanelClienteAlarmas", "----------------------", None))
        self.label_6.setText(_translate("SubVentanaPanelClienteAlarmas", "Tipo de Cliente:", None))
        self.label_TipoCliente.setText(_translate("SubVentanaPanelClienteAlarmas", "----------------------", None))
        self.label_7.setText(_translate("SubVentanaPanelClienteAlarmas", "Protocolo:", None))
        self.label_Protocolo.setText(_translate("SubVentanaPanelClienteAlarmas", "----------------------", None))
        self.label_ClaveMaster.setText(_translate("SubVentanaPanelClienteAlarmas", "----------------------", None))
        self.label_3.setText(_translate("SubVentanaPanelClienteAlarmas", "Codigo Fiscal:", None))
        self.label_CodigoFiscal.setText(_translate("SubVentanaPanelClienteAlarmas", "----------------------", None))
        self.label_2.setText(_translate("SubVentanaPanelClienteAlarmas", "Codigo Cliente:", None))
        self.label_CodigoCliente.setText(_translate("SubVentanaPanelClienteAlarmas", "----------------------", None))
        self.label_5.setText(_translate("SubVentanaPanelClienteAlarmas", "Email:", None))
        self.label_4.setText(_translate("SubVentanaPanelClienteAlarmas", "Clave Master:", None))
        self.label.setText(_translate("SubVentanaPanelClienteAlarmas", "Empresa:", None))
        self.groupBox_2.setTitle(_translate("SubVentanaPanelClienteAlarmas", " Datos Adicionales", None))
        self.label_Referencia.setText(_translate("SubVentanaPanelClienteAlarmas", "----------------------", None))
        self.label_TelefonoLocal.setText(_translate("SubVentanaPanelClienteAlarmas", "----------------------", None))
        self.label_19.setText(_translate("SubVentanaPanelClienteAlarmas", "Fecha Inicio:", None))
        self.label_UltimoEvento.setText(_translate("SubVentanaPanelClienteAlarmas", "----------------------", None))
        self.label_18.setText(_translate("SubVentanaPanelClienteAlarmas", "Telefono Local:", None))
        self.label_15.setText(_translate("SubVentanaPanelClienteAlarmas", "Ciudad:", None))
        self.label_Direccion.setText(_translate("SubVentanaPanelClienteAlarmas", "----------------------", None))
        self.label_Ciudad.setText(_translate("SubVentanaPanelClienteAlarmas", "----------------------", None))
        self.label_16.setText(_translate("SubVentanaPanelClienteAlarmas", "Direccion:", None))
        self.label_17.setText(_translate("SubVentanaPanelClienteAlarmas", "Referencia:", None))
        self.label_20.setText(_translate("SubVentanaPanelClienteAlarmas", "Ultimo Evento:", None))
        self.label_FechaInicio.setText(_translate("SubVentanaPanelClienteAlarmas", "----------------------", None))
        self.label_21.setText(_translate("SubVentanaPanelClienteAlarmas", "Ultimo Reporte:", None))
        self.label_UltimoReporte.setText(_translate("SubVentanaPanelClienteAlarmas", "----------------------", None))
        self.label_NombreCuenta.setText(_translate("SubVentanaPanelClienteAlarmas", "-------------------------------------------------------", None))
        self.label_StatusAlarma.setText(_translate("SubVentanaPanelClienteAlarmas", "Armado", None))
        self.pushButton_Editar.setText(_translate("SubVentanaPanelClienteAlarmas", "Editar", None))
        self.label_MarcaModelo.setText(_translate("SubVentanaPanelClienteAlarmas", "Marca / Modelo", None))
        self.groupBox_7.setTitle(_translate("SubVentanaPanelClienteAlarmas", "Lista de Zonas", None))
        self.label_11.setText(_translate("SubVentanaPanelClienteAlarmas", "Buscar:", None))
        self.pushButton_AgregarZona.setText(_translate("SubVentanaPanelClienteAlarmas", "Agregar", None))
        item = self.tableWidget_Zonas.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "ID", None))
        item = self.tableWidget_Zonas.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Descripcion", None))
        item = self.tableWidget_Zonas.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Ubicacion", None))
        item = self.tableWidget_Zonas.horizontalHeaderItem(3)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Acciones", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Zonas), _translate("SubVentanaPanelClienteAlarmas", "Zonas", None))
        self.groupBox_8.setTitle(_translate("SubVentanaPanelClienteAlarmas", "Lista de Usuarios", None))
        self.label_BuscarUsuarios.setText(_translate("SubVentanaPanelClienteAlarmas", "Buscar: ", None))
        self.pushButton_AgregarUsuario.setText(_translate("SubVentanaPanelClienteAlarmas", "Agregar", None))
        item = self.tableWidget_Usuarios.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "ID", None))
        item = self.tableWidget_Usuarios.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Nombre", None))
        item = self.tableWidget_Usuarios.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Correo", None))
        item = self.tableWidget_Usuarios.horizontalHeaderItem(3)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Movil", None))
        item = self.tableWidget_Usuarios.horizontalHeaderItem(4)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Acciones", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Usuarios), _translate("SubVentanaPanelClienteAlarmas", "Usuarios", None))
        self.groupBox_3.setTitle(_translate("SubVentanaPanelClienteAlarmas", "Asignacion de Eventos", None))
        self.label_8.setText(_translate("SubVentanaPanelClienteAlarmas", "Usuarios", None))
        self.label_9.setText(_translate("SubVentanaPanelClienteAlarmas", "Tipo", None))
        self.comboBox_TipoNotificacion.setItemText(0, _translate("SubVentanaPanelClienteAlarmas", "SMS", None))
        self.comboBox_TipoNotificacion.setItemText(1, _translate("SubVentanaPanelClienteAlarmas", "Email", None))
        self.label_10.setText(_translate("SubVentanaPanelClienteAlarmas", "Planes", None))
        item = self.tableWidget_EventosPlan.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Codigo Evento", None))
        item = self.tableWidget_EventosPlan.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Descripcion", None))
        self.pushButton_AsignarPlan.setText(_translate("SubVentanaPanelClienteAlarmas", "Guardar", None))
        self.groupBox_5.setTitle(_translate("SubVentanaPanelClienteAlarmas", "Usuarios con Eventos", None))
        self.toolBox_UsuariosEventos.setItemText(self.toolBox_UsuariosEventos.indexOf(self.page), _translate("SubVentanaPanelClienteAlarmas", "Usuarios", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Notificaciones), _translate("SubVentanaPanelClienteAlarmas", "Notificaciones", None))
        self.groupBox_9.setTitle(_translate("SubVentanaPanelClienteAlarmas", "Lista de Notificaciones", None))
        self.pushButton_ExportarSMSXLS.setText(_translate("SubVentanaPanelClienteAlarmas", "EXCEL", None))
        item = self.tableWidget_SMS.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Movil", None))
        item = self.tableWidget_SMS.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Hora", None))
        item = self.tableWidget_SMS.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "SMS", None))
        self.pushButton_ExportarSMSPDF.setText(_translate("SubVentanaPanelClienteAlarmas", "PDF", None))
        self.label_FechaHistorialSMS.setText(_translate("SubVentanaPanelClienteAlarmas", "Fecha: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_SMS), _translate("SubVentanaPanelClienteAlarmas", "SMS", None))
        self.groupBox_6.setTitle(_translate("SubVentanaPanelClienteAlarmas", "Lista de Contactos de Emergencia", None))
        self.label_13.setText(_translate("SubVentanaPanelClienteAlarmas", "Buscar:", None))
        self.pushButton_AgregarContacto.setText(_translate("SubVentanaPanelClienteAlarmas", "Agregar", None))
        item = self.tableWidget_Contactos.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Numero", None))
        item = self.tableWidget_Contactos.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Descripcion", None))
        item = self.tableWidget_Contactos.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Observacion", None))
        item = self.tableWidget_Contactos.horizontalHeaderItem(3)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Acciones", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Contactos), _translate("SubVentanaPanelClienteAlarmas", "Contactos", None))
        self.groupBox_Horarios.setTitle(_translate("SubVentanaPanelClienteAlarmas", "Lista de Horarios", None))
        self.label_DiaHorario.setText(_translate("SubVentanaPanelClienteAlarmas", "Dia: ", None))
        self.comboBox_DiaHorario.setItemText(0, _translate("SubVentanaPanelClienteAlarmas", "Todos", None))
        self.comboBox_DiaHorario.setItemText(1, _translate("SubVentanaPanelClienteAlarmas", "Lunes", None))
        self.comboBox_DiaHorario.setItemText(2, _translate("SubVentanaPanelClienteAlarmas", "Martes", None))
        self.comboBox_DiaHorario.setItemText(3, _translate("SubVentanaPanelClienteAlarmas", "Miercoles", None))
        self.comboBox_DiaHorario.setItemText(4, _translate("SubVentanaPanelClienteAlarmas", "Jueves", None))
        self.comboBox_DiaHorario.setItemText(5, _translate("SubVentanaPanelClienteAlarmas", "Viernes", None))
        self.comboBox_DiaHorario.setItemText(6, _translate("SubVentanaPanelClienteAlarmas", "Sabado", None))
        self.comboBox_DiaHorario.setItemText(7, _translate("SubVentanaPanelClienteAlarmas", "Domingo", None))
        self.comboBox_DiaHorario.setItemText(8, _translate("SubVentanaPanelClienteAlarmas", "Feriados", None))
        self.pushButton_AgregarHorario.setText(_translate("SubVentanaPanelClienteAlarmas", "Agregar", None))
        item = self.tableWidget_Horarios.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "ID", None))
        item = self.tableWidget_Horarios.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Dia", None))
        item = self.tableWidget_Horarios.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Horario Apertura", None))
        item = self.tableWidget_Horarios.horizontalHeaderItem(3)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Horario Cierre", None))
        item = self.tableWidget_Horarios.horizontalHeaderItem(4)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Acciones", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Horarios), _translate("SubVentanaPanelClienteAlarmas", "Horarios", None))
        self.groupBox_10.setTitle(_translate("SubVentanaPanelClienteAlarmas", "Lista de Señales", None))
        self.pushButton_SenalesExportarPDF.setText(_translate("SubVentanaPanelClienteAlarmas", "PDF", None))
        self.label_22.setText(_translate("SubVentanaPanelClienteAlarmas", "Eventos", None))
        self.label_FechaHistorialSenales.setText(_translate("SubVentanaPanelClienteAlarmas", "Fecha: ", None))
        self.pushButton_SenalesExportarXLS.setText(_translate("SubVentanaPanelClienteAlarmas", "EXCEL", None))
        item = self.tableWidget_Senales.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Evento", None))
        item = self.tableWidget_Senales.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Usuario/Zonas", None))
        item = self.tableWidget_Senales.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Fecha Recepcion", None))
        item = self.tableWidget_Senales.horizontalHeaderItem(3)
        item.setText(_translate("SubVentanaPanelClienteAlarmas", "Fecha Procesada", None))
        self.label_12.setText(_translate("SubVentanaPanelClienteAlarmas", "Desde:", None))
        self.pushButton_SelectorBusqueda.setText(_translate("SubVentanaPanelClienteAlarmas", "Busqueda Avanzada", None))
        self.label_14.setText(_translate("SubVentanaPanelClienteAlarmas", "Hasta:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Senales), _translate("SubVentanaPanelClienteAlarmas", "Historial", None))
        self.groupBox_NotaFija.setTitle(_translate("SubVentanaPanelClienteAlarmas", "Nota Fija", None))
        self.pushButton_AsignarNotaFija.setText(_translate("SubVentanaPanelClienteAlarmas", "Guardar", None))
        self.pushButton_BorrarNotaFija.setText(_translate("SubVentanaPanelClienteAlarmas", "Borrar", None))
        self.groupBox_NotaTemporal.setTitle(_translate("SubVentanaPanelClienteAlarmas", "Notas Temporales", None))
        self.label_Hasta.setText(_translate("SubVentanaPanelClienteAlarmas", "Hasta", None))
        self.label_Desde.setText(_translate("SubVentanaPanelClienteAlarmas", "Desde", None))
        self.pushButton_BorrarNotaTemporal.setText(_translate("SubVentanaPanelClienteAlarmas", "Borrar", None))
        self.pushButton_AsignarNotaTemporal.setText(_translate("SubVentanaPanelClienteAlarmas", "Guardar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Notas), _translate("SubVentanaPanelClienteAlarmas", "Notas", None))
        self.groupBox_Mapa.setTitle(_translate("SubVentanaPanelClienteAlarmas", "Ubicacion del Cliente en el Mapa", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Mapa), _translate("SubVentanaPanelClienteAlarmas", "Mapa", None))
        self.groupBox_4.setTitle(_translate("SubVentanaPanelClienteAlarmas", "Lista de Dispositivos de CCTV", None))
        self.pushButton_AgregarCCTV.setText(_translate("SubVentanaPanelClienteAlarmas", "Agregar", None))
        self.treeWidget_Camaras.headerItem().setText(0, _translate("SubVentanaPanelClienteAlarmas", "Descripcion", None))
        self.treeWidget_Camaras.headerItem().setText(1, _translate("SubVentanaPanelClienteAlarmas", "Tipo", None))
        self.treeWidget_Camaras.headerItem().setText(2, _translate("SubVentanaPanelClienteAlarmas", "Modo", None))
        self.treeWidget_Camaras.headerItem().setText(3, _translate("SubVentanaPanelClienteAlarmas", "Acciones", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Camaras), _translate("SubVentanaPanelClienteAlarmas", "Camaras", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Equipos), _translate("SubVentanaPanelClienteAlarmas", "Equipos", None))

from PyQt4 import QtWebKit
import recursos_rc
