# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaNuevoGrupoClientes.ui'
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

class Ui_SubVentanaNuevoGrupoClientes(object):
    def setupUi(self, SubVentanaNuevoGrupoClientes):
        SubVentanaNuevoGrupoClientes.setObjectName(_fromUtf8("SubVentanaNuevoGrupoClientes"))
        SubVentanaNuevoGrupoClientes.resize(367, 320)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        SubVentanaNuevoGrupoClientes.setFont(font)
        SubVentanaNuevoGrupoClientes.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout_2 = QtGui.QGridLayout(SubVentanaNuevoGrupoClientes)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.groupBox_GrupoCliente = QtGui.QGroupBox(SubVentanaNuevoGrupoClientes)
        self.groupBox_GrupoCliente.setObjectName(_fromUtf8("groupBox_GrupoCliente"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_GrupoCliente)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_Direccion = QtGui.QLabel(self.groupBox_GrupoCliente)
        self.label_Direccion.setObjectName(_fromUtf8("label_Direccion"))
        self.gridLayout.addWidget(self.label_Direccion, 1, 0, 1, 1)
        self.lineEdit_Correo = QtGui.QLineEdit(self.groupBox_GrupoCliente)
        self.lineEdit_Correo.setMaxLength(100)
        self.lineEdit_Correo.setObjectName(_fromUtf8("lineEdit_Correo"))
        self.gridLayout.addWidget(self.lineEdit_Correo, 3, 1, 1, 2)
        self.label_Nombre = QtGui.QLabel(self.groupBox_GrupoCliente)
        self.label_Nombre.setObjectName(_fromUtf8("label_Nombre"))
        self.gridLayout.addWidget(self.label_Nombre, 0, 0, 1, 1)
        self.lineEdit_Nombre = QtGui.QLineEdit(self.groupBox_GrupoCliente)
        self.lineEdit_Nombre.setMaxLength(40)
        self.lineEdit_Nombre.setObjectName(_fromUtf8("lineEdit_Nombre"))
        self.gridLayout.addWidget(self.lineEdit_Nombre, 0, 1, 1, 2)
        self.label_Telefono = QtGui.QLabel(self.groupBox_GrupoCliente)
        self.label_Telefono.setObjectName(_fromUtf8("label_Telefono"))
        self.gridLayout.addWidget(self.label_Telefono, 2, 0, 1, 1)
        self.lineEdit_Telefono = QtGui.QLineEdit(self.groupBox_GrupoCliente)
        self.lineEdit_Telefono.setMaxLength(40)
        self.lineEdit_Telefono.setObjectName(_fromUtf8("lineEdit_Telefono"))
        self.gridLayout.addWidget(self.lineEdit_Telefono, 2, 1, 1, 2)
        self.label_Correo = QtGui.QLabel(self.groupBox_GrupoCliente)
        self.label_Correo.setObjectName(_fromUtf8("label_Correo"))
        self.gridLayout.addWidget(self.label_Correo, 3, 0, 1, 1)
        self.lineEdit_Usuario = QtGui.QLineEdit(self.groupBox_GrupoCliente)
        self.lineEdit_Usuario.setMaxLength(40)
        self.lineEdit_Usuario.setObjectName(_fromUtf8("lineEdit_Usuario"))
        self.gridLayout.addWidget(self.lineEdit_Usuario, 4, 1, 1, 2)
        self.label_Usuario = QtGui.QLabel(self.groupBox_GrupoCliente)
        self.label_Usuario.setObjectName(_fromUtf8("label_Usuario"))
        self.gridLayout.addWidget(self.label_Usuario, 4, 0, 1, 1)
        self.radioButton_Activado = QtGui.QRadioButton(self.groupBox_GrupoCliente)
        self.radioButton_Activado.setChecked(True)
        self.radioButton_Activado.setObjectName(_fromUtf8("radioButton_Activado"))
        self.gridLayout.addWidget(self.radioButton_Activado, 6, 1, 1, 1)
        self.radioButton_Desactivado = QtGui.QRadioButton(self.groupBox_GrupoCliente)
        self.radioButton_Desactivado.setObjectName(_fromUtf8("radioButton_Desactivado"))
        self.gridLayout.addWidget(self.radioButton_Desactivado, 6, 2, 1, 1)
        self.lineEdit_Clave = QtGui.QLineEdit(self.groupBox_GrupoCliente)
        self.lineEdit_Clave.setMaxLength(40)
        self.lineEdit_Clave.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_Clave.setObjectName(_fromUtf8("lineEdit_Clave"))
        self.gridLayout.addWidget(self.lineEdit_Clave, 5, 1, 1, 2)
        self.label_Clave = QtGui.QLabel(self.groupBox_GrupoCliente)
        self.label_Clave.setObjectName(_fromUtf8("label_Clave"))
        self.gridLayout.addWidget(self.label_Clave, 5, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_GrupoCliente)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_Agregar = QtGui.QPushButton(self.groupBox_GrupoCliente)
        self.pushButton_Agregar.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Agregar.setIcon(icon)
        self.pushButton_Agregar.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_Agregar.setFlat(True)
        self.pushButton_Agregar.setObjectName(_fromUtf8("pushButton_Agregar"))
        self.horizontalLayout.addWidget(self.pushButton_Agregar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 3)
        self.textEdit_Direccion = QtGui.QTextEdit(self.groupBox_GrupoCliente)
        self.textEdit_Direccion.setMaximumSize(QtCore.QSize(16777215, 50))
        self.textEdit_Direccion.setObjectName(_fromUtf8("textEdit_Direccion"))
        self.gridLayout.addWidget(self.textEdit_Direccion, 1, 1, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_GrupoCliente, 0, 2, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)

        self.retranslateUi(SubVentanaNuevoGrupoClientes)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaNuevoGrupoClientes)

    def retranslateUi(self, SubVentanaNuevoGrupoClientes):
        SubVentanaNuevoGrupoClientes.setWindowTitle(_translate("SubVentanaNuevoGrupoClientes", "Form", None))
        self.groupBox_GrupoCliente.setTitle(_translate("SubVentanaNuevoGrupoClientes", "Nuevo Grupo Clientes", None))
        self.label_Direccion.setText(_translate("SubVentanaNuevoGrupoClientes", "Direccion:", None))
        self.label_Nombre.setText(_translate("SubVentanaNuevoGrupoClientes", "Nombre:", None))
        self.label_Telefono.setText(_translate("SubVentanaNuevoGrupoClientes", "Telefono:", None))
        self.label_Correo.setText(_translate("SubVentanaNuevoGrupoClientes", "Correo:", None))
        self.label_Usuario.setText(_translate("SubVentanaNuevoGrupoClientes", "Usuario:", None))
        self.radioButton_Activado.setText(_translate("SubVentanaNuevoGrupoClientes", "Activado", None))
        self.radioButton_Desactivado.setText(_translate("SubVentanaNuevoGrupoClientes", "Desactivado", None))
        self.label_Clave.setText(_translate("SubVentanaNuevoGrupoClientes", "Clave:", None))
        self.label.setText(_translate("SubVentanaNuevoGrupoClientes", "Estatus:", None))

import recursos_rc
