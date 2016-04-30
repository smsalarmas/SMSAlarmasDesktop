# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaGrupoClientes.ui'
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

class Ui_SubVentanaGruposdeClientes(object):
    def setupUi(self, SubVentanaGruposdeClientes):
        SubVentanaGruposdeClientes.setObjectName(_fromUtf8("SubVentanaGruposdeClientes"))
        SubVentanaGruposdeClientes.resize(581, 427)
        SubVentanaGruposdeClientes.setMinimumSize(QtCore.QSize(550, 400))
        SubVentanaGruposdeClientes.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.horizontalLayout = QtGui.QHBoxLayout(SubVentanaGruposdeClientes)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_10 = QtGui.QFrame(SubVentanaGruposdeClientes)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_10.setStyleSheet(_fromUtf8("font: 75 12pt \"Calibri\";\n"
"\n"
"background-color: #38648B;\n"
"color: rgb(255, 255, 255);"))
        self.frame_10.setFrameShape(QtGui.QFrame.WinPanel)
        self.frame_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_10.setObjectName(_fromUtf8("frame_10"))
        self.gridLayout_37 = QtGui.QGridLayout(self.frame_10)
        self.gridLayout_37.setMargin(0)
        self.gridLayout_37.setSpacing(0)
        self.gridLayout_37.setObjectName(_fromUtf8("gridLayout_37"))
        self.label_32 = QtGui.QLabel(self.frame_10)
        self.label_32.setMinimumSize(QtCore.QSize(0, 0))
        self.label_32.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_32.setStyleSheet(_fromUtf8("font: 12pt \"Calibri\";"))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout_37.addWidget(self.label_32, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_10)
        self.groupBox_GrupoClientes = QtGui.QGroupBox(SubVentanaGruposdeClientes)
        self.groupBox_GrupoClientes.setMinimumSize(QtCore.QSize(550, 350))
        self.groupBox_GrupoClientes.setTitle(_fromUtf8(""))
        self.groupBox_GrupoClientes.setObjectName(_fromUtf8("groupBox_GrupoClientes"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_GrupoClientes)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 2, 1, 1)
        self.pushButton_AgregarGrupoCliente = QtGui.QPushButton(self.groupBox_GrupoClientes)
        self.pushButton_AgregarGrupoCliente.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/4-Icone-plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AgregarGrupoCliente.setIcon(icon)
        self.pushButton_AgregarGrupoCliente.setCheckable(False)
        self.pushButton_AgregarGrupoCliente.setAutoDefault(False)
        self.pushButton_AgregarGrupoCliente.setDefault(True)
        self.pushButton_AgregarGrupoCliente.setFlat(True)
        self.pushButton_AgregarGrupoCliente.setObjectName(_fromUtf8("pushButton_AgregarGrupoCliente"))
        self.gridLayout_2.addWidget(self.pushButton_AgregarGrupoCliente, 3, 3, 1, 1)
        self.tableWidget_ListaGrupoClientes = QtGui.QTableWidget(self.groupBox_GrupoClientes)
        self.tableWidget_ListaGrupoClientes.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget_ListaGrupoClientes.setObjectName(_fromUtf8("tableWidget_ListaGrupoClientes"))
        self.tableWidget_ListaGrupoClientes.setColumnCount(4)
        self.tableWidget_ListaGrupoClientes.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_ListaGrupoClientes.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_ListaGrupoClientes.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_ListaGrupoClientes.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_ListaGrupoClientes.setHorizontalHeaderItem(3, item)
        self.gridLayout_2.addWidget(self.tableWidget_ListaGrupoClientes, 4, 0, 1, 4)
        self.label = QtGui.QLabel(self.groupBox_GrupoClientes)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        self.lineEdit_Buscar = QtGui.QLineEdit(self.groupBox_GrupoClientes)
        self.lineEdit_Buscar.setObjectName(_fromUtf8("lineEdit_Buscar"))
        self.gridLayout_2.addWidget(self.lineEdit_Buscar, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_GrupoClientes)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem2 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)

        self.retranslateUi(SubVentanaGruposdeClientes)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaGruposdeClientes)

    def retranslateUi(self, SubVentanaGruposdeClientes):
        SubVentanaGruposdeClientes.setWindowTitle(_translate("SubVentanaGruposdeClientes", "Grupos de Clientes", None))
        self.label_32.setText(_translate("SubVentanaGruposdeClientes", "Administracion de Grupos de Clientes", None))
        item = self.tableWidget_ListaGrupoClientes.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaGruposdeClientes", "Nombre", None))
        item = self.tableWidget_ListaGrupoClientes.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaGruposdeClientes", "Correo", None))
        item = self.tableWidget_ListaGrupoClientes.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaGruposdeClientes", "Estatus", None))
        item = self.tableWidget_ListaGrupoClientes.horizontalHeaderItem(3)
        item.setText(_translate("SubVentanaGruposdeClientes", "Cuentas", None))
        self.label.setText(_translate("SubVentanaGruposdeClientes", " Buscar:", None))

import recursos_rc
