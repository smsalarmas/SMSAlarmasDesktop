# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaTiposClientes.ui'
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

class Ui_SubVentanaTipoClientes(object):
    def setupUi(self, SubVentanaTipoClientes):
        SubVentanaTipoClientes.setObjectName(_fromUtf8("SubVentanaTipoClientes"))
        SubVentanaTipoClientes.resize(350, 560)
        SubVentanaTipoClientes.setMinimumSize(QtCore.QSize(350, 560))
        SubVentanaTipoClientes.setMaximumSize(QtCore.QSize(350, 560))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/company-employee.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubVentanaTipoClientes.setWindowIcon(icon)
        SubVentanaTipoClientes.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout_2 = QtGui.QGridLayout(SubVentanaTipoClientes)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(SubVentanaTipoClientes)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_AgregarTipodeCliente = QtGui.QPushButton(self.groupBox_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/4-Icone-plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AgregarTipodeCliente.setIcon(icon1)
        self.pushButton_AgregarTipodeCliente.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_AgregarTipodeCliente.setFlat(True)
        self.pushButton_AgregarTipodeCliente.setObjectName(_fromUtf8("pushButton_AgregarTipodeCliente"))
        self.horizontalLayout_2.addWidget(self.pushButton_AgregarTipodeCliente)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
        self.tableWidget_ListadeTiposdeClientes = QtGui.QTableWidget(self.groupBox_4)
        self.tableWidget_ListadeTiposdeClientes.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidget_ListadeTiposdeClientes.setStyleSheet(_fromUtf8(""))
        self.tableWidget_ListadeTiposdeClientes.setObjectName(_fromUtf8("tableWidget_ListadeTiposdeClientes"))
        self.tableWidget_ListadeTiposdeClientes.setColumnCount(2)
        self.tableWidget_ListadeTiposdeClientes.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ListadeTiposdeClientes.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ListadeTiposdeClientes.setHorizontalHeaderItem(1, item)
        self.gridLayout_3.addWidget(self.tableWidget_ListadeTiposdeClientes, 0, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.groupBox_DatosParentesco = QtGui.QGroupBox(SubVentanaTipoClientes)
        self.groupBox_DatosParentesco.setObjectName(_fromUtf8("groupBox_DatosParentesco"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_DatosParentesco)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_Descripcion = QtGui.QLineEdit(self.groupBox_DatosParentesco)
        self.lineEdit_Descripcion.setObjectName(_fromUtf8("lineEdit_Descripcion"))
        self.gridLayout.addWidget(self.lineEdit_Descripcion, 0, 1, 1, 1)
        self.label_IconoSeleccionado = QtGui.QLabel(self.groupBox_DatosParentesco)
        self.label_IconoSeleccionado.setText(_fromUtf8(""))
        self.label_IconoSeleccionado.setScaledContents(False)
        self.label_IconoSeleccionado.setAlignment(QtCore.Qt.AlignCenter)
        self.label_IconoSeleccionado.setObjectName(_fromUtf8("label_IconoSeleccionado"))
        self.gridLayout.addWidget(self.label_IconoSeleccionado, 5, 1, 1, 1)
        self.comboBox_Icono = QtGui.QComboBox(self.groupBox_DatosParentesco)
        self.comboBox_Icono.setObjectName(_fromUtf8("comboBox_Icono"))
        self.gridLayout.addWidget(self.comboBox_Icono, 3, 1, 1, 1)
        self.label_Descripcion = QtGui.QLabel(self.groupBox_DatosParentesco)
        self.label_Descripcion.setObjectName(_fromUtf8("label_Descripcion"))
        self.gridLayout.addWidget(self.label_Descripcion, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_DatosParentesco)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_DatosParentesco)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.comboBox_Dispositivo = QtGui.QComboBox(self.groupBox_DatosParentesco)
        self.comboBox_Dispositivo.setObjectName(_fromUtf8("comboBox_Dispositivo"))
        self.gridLayout.addWidget(self.comboBox_Dispositivo, 2, 1, 1, 1)
        self.comboBox_Empresa = QtGui.QComboBox(self.groupBox_DatosParentesco)
        self.comboBox_Empresa.setObjectName(_fromUtf8("comboBox_Empresa"))
        self.gridLayout.addWidget(self.comboBox_Empresa, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_DatosParentesco)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_DatosParentesco, 1, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_GuardarTipoCliente = QtGui.QPushButton(SubVentanaTipoClientes)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_GuardarTipoCliente.setIcon(icon2)
        self.pushButton_GuardarTipoCliente.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_GuardarTipoCliente.setFlat(True)
        self.pushButton_GuardarTipoCliente.setObjectName(_fromUtf8("pushButton_GuardarTipoCliente"))
        self.horizontalLayout.addWidget(self.pushButton_GuardarTipoCliente)
        self.pushButton_BorrarTipoCliente = QtGui.QPushButton(SubVentanaTipoClientes)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/eraser-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_BorrarTipoCliente.setIcon(icon3)
        self.pushButton_BorrarTipoCliente.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_BorrarTipoCliente.setFlat(True)
        self.pushButton_BorrarTipoCliente.setObjectName(_fromUtf8("pushButton_BorrarTipoCliente"))
        self.horizontalLayout.addWidget(self.pushButton_BorrarTipoCliente)
        self.pushButton_Cancelar = QtGui.QPushButton(SubVentanaTipoClientes)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/uncheck.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Cancelar.setIcon(icon4)
        self.pushButton_Cancelar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Cancelar.setFlat(True)
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.horizontalLayout.addWidget(self.pushButton_Cancelar)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 1, 1, 1)

        self.retranslateUi(SubVentanaTipoClientes)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaTipoClientes)
        SubVentanaTipoClientes.setTabOrder(self.tableWidget_ListadeTiposdeClientes, self.pushButton_AgregarTipodeCliente)
        SubVentanaTipoClientes.setTabOrder(self.pushButton_AgregarTipodeCliente, self.lineEdit_Descripcion)
        SubVentanaTipoClientes.setTabOrder(self.lineEdit_Descripcion, self.pushButton_GuardarTipoCliente)
        SubVentanaTipoClientes.setTabOrder(self.pushButton_GuardarTipoCliente, self.pushButton_BorrarTipoCliente)
        SubVentanaTipoClientes.setTabOrder(self.pushButton_BorrarTipoCliente, self.pushButton_Cancelar)

    def retranslateUi(self, SubVentanaTipoClientes):
        SubVentanaTipoClientes.setWindowTitle(_translate("SubVentanaTipoClientes", "Administracion de Tipos de Clientes", None))
        self.groupBox_4.setTitle(_translate("SubVentanaTipoClientes", "Lista de Tipos de Clientes", None))
        self.pushButton_AgregarTipodeCliente.setToolTip(_translate("SubVentanaTipoClientes", "Nueva Tipo de Cliente", None))
        self.pushButton_AgregarTipodeCliente.setText(_translate("SubVentanaTipoClientes", "Agregar", None))
        item = self.tableWidget_ListadeTiposdeClientes.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaTipoClientes", "Descripcion", None))
        item = self.tableWidget_ListadeTiposdeClientes.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaTipoClientes", "Dispositivo", None))
        self.groupBox_DatosParentesco.setTitle(_translate("SubVentanaTipoClientes", "Datos del Tipo de Cliente", None))
        self.label_Descripcion.setText(_translate("SubVentanaTipoClientes", "Nombre:", None))
        self.label_2.setText(_translate("SubVentanaTipoClientes", "Dispositivo:", None))
        self.label.setText(_translate("SubVentanaTipoClientes", "Icono:", None))
        self.label_3.setText(_translate("SubVentanaTipoClientes", "Empresa:", None))
        self.pushButton_GuardarTipoCliente.setToolTip(_translate("SubVentanaTipoClientes", "Guardar Empresa", None))
        self.pushButton_GuardarTipoCliente.setText(_translate("SubVentanaTipoClientes", "Guardar", None))
        self.pushButton_BorrarTipoCliente.setToolTip(_translate("SubVentanaTipoClientes", "Borrar Empresa", None))
        self.pushButton_BorrarTipoCliente.setText(_translate("SubVentanaTipoClientes", "Borrar", None))
        self.pushButton_Cancelar.setToolTip(_translate("SubVentanaTipoClientes", "Cancelar Edicion", None))
        self.pushButton_Cancelar.setText(_translate("SubVentanaTipoClientes", "Cancelar", None))

import recursos_rc
