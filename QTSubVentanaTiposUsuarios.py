# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaTiposUsuarios.ui'
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

class Ui_SubVentanaTiposUsuarios(object):
    def setupUi(self, SubVentanaTiposUsuarios):
        SubVentanaTiposUsuarios.setObjectName(_fromUtf8("SubVentanaTiposUsuarios"))
        SubVentanaTiposUsuarios.resize(702, 536)
        SubVentanaTiposUsuarios.setMinimumSize(QtCore.QSize(702, 536))
        SubVentanaTiposUsuarios.setMaximumSize(QtCore.QSize(702, 536))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        SubVentanaTiposUsuarios.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/tipoUsuarios2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubVentanaTiposUsuarios.setWindowIcon(icon)
        SubVentanaTiposUsuarios.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.horizontalLayout = QtGui.QHBoxLayout(SubVentanaTiposUsuarios)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_Usuarios = QtGui.QGroupBox(SubVentanaTiposUsuarios)
        self.groupBox_Usuarios.setObjectName(_fromUtf8("groupBox_Usuarios"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_Usuarios)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_Edicion = QtGui.QGroupBox(self.groupBox_Usuarios)
        self.groupBox_Edicion.setObjectName(_fromUtf8("groupBox_Edicion"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_Edicion)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.groupBox_Edicion)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_GuardarTipoUsuario = QtGui.QPushButton(self.groupBox_Edicion)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_GuardarTipoUsuario.setIcon(icon1)
        self.pushButton_GuardarTipoUsuario.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_GuardarTipoUsuario.setFlat(True)
        self.pushButton_GuardarTipoUsuario.setObjectName(_fromUtf8("pushButton_GuardarTipoUsuario"))
        self.horizontalLayout_3.addWidget(self.pushButton_GuardarTipoUsuario)
        self.pushButton_BorrarTipoUsuario = QtGui.QPushButton(self.groupBox_Edicion)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/eraser-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_BorrarTipoUsuario.setIcon(icon2)
        self.pushButton_BorrarTipoUsuario.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_BorrarTipoUsuario.setFlat(True)
        self.pushButton_BorrarTipoUsuario.setObjectName(_fromUtf8("pushButton_BorrarTipoUsuario"))
        self.horizontalLayout_3.addWidget(self.pushButton_BorrarTipoUsuario)
        self.pushButton_Cancelar = QtGui.QPushButton(self.groupBox_Edicion)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/uncheck.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Cancelar.setIcon(icon3)
        self.pushButton_Cancelar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Cancelar.setFlat(True)
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.horizontalLayout_3.addWidget(self.pushButton_Cancelar)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_ColorEdicion = QtGui.QPushButton(self.groupBox_Edicion)
        self.pushButton_ColorEdicion.setStyleSheet(_fromUtf8(""))
        self.pushButton_ColorEdicion.setObjectName(_fromUtf8("pushButton_ColorEdicion"))
        self.horizontalLayout_2.addWidget(self.pushButton_ColorEdicion)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.comboBox_EmpresaEdicion = QtGui.QComboBox(self.groupBox_Edicion)
        self.comboBox_EmpresaEdicion.setObjectName(_fromUtf8("comboBox_EmpresaEdicion"))
        self.gridLayout.addWidget(self.comboBox_EmpresaEdicion, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_Edicion)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_Edicion)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_DescripcionEdicion = QtGui.QLineEdit(self.groupBox_Edicion)
        self.lineEdit_DescripcionEdicion.setObjectName(_fromUtf8("lineEdit_DescripcionEdicion"))
        self.gridLayout.addWidget(self.lineEdit_DescripcionEdicion, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_Edicion)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_TipoEdicion = QtGui.QComboBox(self.groupBox_Edicion)
        self.comboBox_TipoEdicion.setObjectName(_fromUtf8("comboBox_TipoEdicion"))
        self.gridLayout.addWidget(self.comboBox_TipoEdicion, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_Edicion, 5, 0, 1, 4)
        self.tableWidget_TiposUsuarios = QtGui.QTableWidget(self.groupBox_Usuarios)
        self.tableWidget_TiposUsuarios.setObjectName(_fromUtf8("tableWidget_TiposUsuarios"))
        self.tableWidget_TiposUsuarios.setColumnCount(3)
        self.tableWidget_TiposUsuarios.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_TiposUsuarios.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_TiposUsuarios.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_TiposUsuarios.setHorizontalHeaderItem(2, item)
        self.gridLayout_2.addWidget(self.tableWidget_TiposUsuarios, 3, 0, 1, 4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pushButton_AgregarTipoUsuario = QtGui.QPushButton(self.groupBox_Usuarios)
        self.pushButton_AgregarTipoUsuario.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/4-Icone-plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AgregarTipoUsuario.setIcon(icon4)
        self.pushButton_AgregarTipoUsuario.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_AgregarTipoUsuario.setFlat(True)
        self.pushButton_AgregarTipoUsuario.setObjectName(_fromUtf8("pushButton_AgregarTipoUsuario"))
        self.horizontalLayout_5.addWidget(self.pushButton_AgregarTipoUsuario)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 4, 0, 1, 4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 2, 1, 1)
        self.label_Empresa = QtGui.QLabel(self.groupBox_Usuarios)
        self.label_Empresa.setObjectName(_fromUtf8("label_Empresa"))
        self.gridLayout_2.addWidget(self.label_Empresa, 1, 0, 1, 1)
        self.comboBox_Empresa = QtGui.QComboBox(self.groupBox_Usuarios)
        self.comboBox_Empresa.setMinimumSize(QtCore.QSize(80, 0))
        self.comboBox_Empresa.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_Empresa.setObjectName(_fromUtf8("comboBox_Empresa"))
        self.comboBox_Empresa.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_Empresa, 1, 1, 1, 1)
        self.label_Busqueda = QtGui.QLabel(self.groupBox_Usuarios)
        self.label_Busqueda.setObjectName(_fromUtf8("label_Busqueda"))
        self.gridLayout_2.addWidget(self.label_Busqueda, 2, 0, 1, 1)
        self.lineEdit_BusquedaTiposUsuarios = QtGui.QLineEdit(self.groupBox_Usuarios)
        self.lineEdit_BusquedaTiposUsuarios.setObjectName(_fromUtf8("lineEdit_BusquedaTiposUsuarios"))
        self.gridLayout_2.addWidget(self.lineEdit_BusquedaTiposUsuarios, 2, 1, 1, 3)
        self.horizontalLayout.addWidget(self.groupBox_Usuarios)
        self.groupBox_Permisos = QtGui.QGroupBox(SubVentanaTiposUsuarios)
        self.groupBox_Permisos.setObjectName(_fromUtf8("groupBox_Permisos"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_Permisos)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tableWidget_Permisos = QtGui.QTableWidget(self.groupBox_Permisos)
        self.tableWidget_Permisos.setAlternatingRowColors(True)
        self.tableWidget_Permisos.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_Permisos.setObjectName(_fromUtf8("tableWidget_Permisos"))
        self.tableWidget_Permisos.setColumnCount(2)
        self.tableWidget_Permisos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Permisos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Permisos.setHorizontalHeaderItem(1, item)
        self.tableWidget_Permisos.horizontalHeader().setVisible(False)
        self.tableWidget_Permisos.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.tableWidget_Permisos, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_Permisos)

        self.retranslateUi(SubVentanaTiposUsuarios)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaTiposUsuarios)
        SubVentanaTiposUsuarios.setTabOrder(self.comboBox_Empresa, self.tableWidget_TiposUsuarios)
        SubVentanaTiposUsuarios.setTabOrder(self.tableWidget_TiposUsuarios, self.pushButton_AgregarTipoUsuario)
        SubVentanaTiposUsuarios.setTabOrder(self.pushButton_AgregarTipoUsuario, self.comboBox_EmpresaEdicion)
        SubVentanaTiposUsuarios.setTabOrder(self.comboBox_EmpresaEdicion, self.comboBox_TipoEdicion)
        SubVentanaTiposUsuarios.setTabOrder(self.comboBox_TipoEdicion, self.lineEdit_DescripcionEdicion)
        SubVentanaTiposUsuarios.setTabOrder(self.lineEdit_DescripcionEdicion, self.pushButton_GuardarTipoUsuario)
        SubVentanaTiposUsuarios.setTabOrder(self.pushButton_GuardarTipoUsuario, self.pushButton_BorrarTipoUsuario)
        SubVentanaTiposUsuarios.setTabOrder(self.pushButton_BorrarTipoUsuario, self.pushButton_Cancelar)
        SubVentanaTiposUsuarios.setTabOrder(self.pushButton_Cancelar, self.tableWidget_Permisos)

    def retranslateUi(self, SubVentanaTiposUsuarios):
        SubVentanaTiposUsuarios.setWindowTitle(_translate("SubVentanaTiposUsuarios", "Administracion de Tipos de Usuarios", None))
        self.groupBox_Usuarios.setTitle(_translate("SubVentanaTiposUsuarios", "Lista Tipos de Usuarios", None))
        self.groupBox_Edicion.setTitle(_translate("SubVentanaTiposUsuarios", "Datos del Tipo de Usuario", None))
        self.label_4.setText(_translate("SubVentanaTiposUsuarios", "Color", None))
        self.pushButton_GuardarTipoUsuario.setText(_translate("SubVentanaTiposUsuarios", "Guardar", None))
        self.pushButton_BorrarTipoUsuario.setToolTip(_translate("SubVentanaTiposUsuarios", "Borrar Codigo de Alarma", None))
        self.pushButton_BorrarTipoUsuario.setText(_translate("SubVentanaTiposUsuarios", "Borrar", None))
        self.pushButton_Cancelar.setToolTip(_translate("SubVentanaTiposUsuarios", "Cancelar Edicion", None))
        self.pushButton_Cancelar.setText(_translate("SubVentanaTiposUsuarios", "Cancelar ", None))
        self.pushButton_ColorEdicion.setText(_translate("SubVentanaTiposUsuarios", "...", None))
        self.label.setText(_translate("SubVentanaTiposUsuarios", "Empresa", None))
        self.label_3.setText(_translate("SubVentanaTiposUsuarios", "Descripcion", None))
        self.label_2.setText(_translate("SubVentanaTiposUsuarios", "Tipo Usuario", None))
        item = self.tableWidget_TiposUsuarios.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaTiposUsuarios", "ID", None))
        item = self.tableWidget_TiposUsuarios.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaTiposUsuarios", "Descripcion", None))
        item = self.tableWidget_TiposUsuarios.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaTiposUsuarios", "Empresa", None))
        self.pushButton_AgregarTipoUsuario.setToolTip(_translate("SubVentanaTiposUsuarios", "Agregar Nuevo Codigo", None))
        self.label_Empresa.setText(_translate("SubVentanaTiposUsuarios", "Empresa: ", None))
        self.comboBox_Empresa.setItemText(0, _translate("SubVentanaTiposUsuarios", "Todas", None))
        self.label_Busqueda.setText(_translate("SubVentanaTiposUsuarios", "Busqueda: ", None))
        self.groupBox_Permisos.setTitle(_translate("SubVentanaTiposUsuarios", "Permisos Tipos de Usuarios", None))
        item = self.tableWidget_Permisos.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaTiposUsuarios", "Nombre", None))
        item = self.tableWidget_Permisos.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaTiposUsuarios", "Check", None))

import recursos_rc
