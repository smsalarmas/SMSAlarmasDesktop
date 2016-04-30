# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaPlanesNotificaciones.ui'
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

class Ui_SubVentanaPlanesNotificaciones(object):
    def setupUi(self, SubVentanaPlanesNotificaciones):
        SubVentanaPlanesNotificaciones.setObjectName(_fromUtf8("SubVentanaPlanesNotificaciones"))
        SubVentanaPlanesNotificaciones.resize(745, 466)
        SubVentanaPlanesNotificaciones.setMinimumSize(QtCore.QSize(745, 466))
        SubVentanaPlanesNotificaciones.setMaximumSize(QtCore.QSize(745, 466))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Eventos_Planes.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubVentanaPlanesNotificaciones.setWindowIcon(icon)
        SubVentanaPlanesNotificaciones.setStyleSheet(_fromUtf8("QTableView {\n"
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
""))
        self.gridLayout_2 = QtGui.QGridLayout(SubVentanaPlanesNotificaciones)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(SubVentanaPlanesNotificaciones)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit_NombrePlan = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_NombrePlan.setObjectName(_fromUtf8("lineEdit_NombrePlan"))
        self.gridLayout_5.addWidget(self.lineEdit_NombrePlan, 1, 1, 1, 4)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_5.addWidget(self.label_2, 2, 0, 1, 1)
        self.comboBox_ProtocoloPlan = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_ProtocoloPlan.setObjectName(_fromUtf8("comboBox_ProtocoloPlan"))
        self.gridLayout_5.addWidget(self.comboBox_ProtocoloPlan, 2, 1, 1, 4)
        self.pushButton_GuardarPlan = QtGui.QPushButton(self.groupBox_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_GuardarPlan.setIcon(icon1)
        self.pushButton_GuardarPlan.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_GuardarPlan.setFlat(True)
        self.pushButton_GuardarPlan.setObjectName(_fromUtf8("pushButton_GuardarPlan"))
        self.gridLayout_5.addWidget(self.pushButton_GuardarPlan, 4, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(141, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 4, 0, 1, 1)
        self.pushButton_BorrarPlan = QtGui.QPushButton(self.groupBox_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/eraser-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_BorrarPlan.setIcon(icon2)
        self.pushButton_BorrarPlan.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_BorrarPlan.setFlat(True)
        self.pushButton_BorrarPlan.setObjectName(_fromUtf8("pushButton_BorrarPlan"))
        self.gridLayout_5.addWidget(self.pushButton_BorrarPlan, 4, 3, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget_EventosPlan = QtGui.QTableWidget(self.groupBox_3)
        self.tableWidget_EventosPlan.setObjectName(_fromUtf8("tableWidget_EventosPlan"))
        self.tableWidget_EventosPlan.setColumnCount(3)
        self.tableWidget_EventosPlan.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_EventosPlan.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_EventosPlan.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_EventosPlan.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.tableWidget_EventosPlan, 0, 0, 1, 1)
        self.textEdit_EventosPlan = QtGui.QTextEdit(self.groupBox_3)
        self.textEdit_EventosPlan.setMaximumSize(QtCore.QSize(16777215, 80))
        self.textEdit_EventosPlan.setReadOnly(True)
        self.textEdit_EventosPlan.setObjectName(_fromUtf8("textEdit_EventosPlan"))
        self.gridLayout.addWidget(self.textEdit_EventosPlan, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_3, 3, 0, 1, 5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(SubVentanaPlanesNotificaciones)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.tableWidget_ListadePlanes = QtGui.QTableWidget(self.groupBox)
        self.tableWidget_ListadePlanes.setObjectName(_fromUtf8("tableWidget_ListadePlanes"))
        self.tableWidget_ListadePlanes.setColumnCount(3)
        self.tableWidget_ListadePlanes.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_ListadePlanes.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_ListadePlanes.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_ListadePlanes.setHorizontalHeaderItem(2, item)
        self.gridLayout_6.addWidget(self.tableWidget_ListadePlanes, 4, 0, 1, 2)
        self.comboBox_Protocolos = QtGui.QComboBox(self.groupBox)
        self.comboBox_Protocolos.setObjectName(_fromUtf8("comboBox_Protocolos"))
        self.gridLayout_6.addWidget(self.comboBox_Protocolos, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_6.addWidget(self.label_3, 1, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit_NombreNuevoPlan = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_NombreNuevoPlan.setInputMask(_fromUtf8(""))
        self.lineEdit_NombreNuevoPlan.setObjectName(_fromUtf8("lineEdit_NombreNuevoPlan"))
        self.gridLayout_3.addWidget(self.lineEdit_NombreNuevoPlan, 0, 1, 1, 1)
        self.pushButton_AgregarPlan = QtGui.QPushButton(self.groupBox_4)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/4-Icone-plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AgregarPlan.setIcon(icon3)
        self.pushButton_AgregarPlan.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_AgregarPlan.setFlat(True)
        self.pushButton_AgregarPlan.setObjectName(_fromUtf8("pushButton_AgregarPlan"))
        self.gridLayout_3.addWidget(self.pushButton_AgregarPlan, 0, 2, 2, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.comboBox_ProtocoloNuevoPlan = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_ProtocoloNuevoPlan.setObjectName(_fromUtf8("comboBox_ProtocoloNuevoPlan"))
        self.gridLayout_3.addWidget(self.comboBox_ProtocoloNuevoPlan, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_4, 5, 0, 1, 2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_6.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(SubVentanaPlanesNotificaciones)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaPlanesNotificaciones)

    def retranslateUi(self, SubVentanaPlanesNotificaciones):
        SubVentanaPlanesNotificaciones.setWindowTitle(_translate("SubVentanaPlanesNotificaciones", "Planes Notificaciones", None))
        self.groupBox_2.setTitle(_translate("SubVentanaPlanesNotificaciones", "Datos del Plan", None))
        self.label.setText(_translate("SubVentanaPlanesNotificaciones", "Nombre del Plan", None))
        self.lineEdit_NombrePlan.setToolTip(_translate("SubVentanaPlanesNotificaciones", "Nombre Del  Plan de Notificacion   ", None))
        self.label_2.setText(_translate("SubVentanaPlanesNotificaciones", "Protocolo", None))
        self.comboBox_ProtocoloPlan.setToolTip(_translate("SubVentanaPlanesNotificaciones", "<html><head/><body><p>Protocolo del Plan del Usuario</p></body></html>", None))
        self.pushButton_GuardarPlan.setToolTip(_translate("SubVentanaPlanesNotificaciones", "Guardar Plan Del Usuario   ", None))
        self.pushButton_GuardarPlan.setText(_translate("SubVentanaPlanesNotificaciones", "Guardar", None))
        self.pushButton_BorrarPlan.setToolTip(_translate("SubVentanaPlanesNotificaciones", "Borrar Plan De Notificacion Del Usuario   ", None))
        self.pushButton_BorrarPlan.setText(_translate("SubVentanaPlanesNotificaciones", "Borrar", None))
        self.groupBox_3.setTitle(_translate("SubVentanaPlanesNotificaciones", "Eventos del Plan", None))
        item = self.tableWidget_EventosPlan.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaPlanesNotificaciones", "Seleccion", None))
        item = self.tableWidget_EventosPlan.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaPlanesNotificaciones", "Evento", None))
        item = self.tableWidget_EventosPlan.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaPlanesNotificaciones", "Descripcion", None))
        self.groupBox.setTitle(_translate("SubVentanaPlanesNotificaciones", "Lista de Planes", None))
        item = self.tableWidget_ListadePlanes.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaPlanesNotificaciones", "ID", None))
        item = self.tableWidget_ListadePlanes.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaPlanesNotificaciones", "Nombre", None))
        item = self.tableWidget_ListadePlanes.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaPlanesNotificaciones", "Protocolo", None))
        self.label_3.setText(_translate("SubVentanaPlanesNotificaciones", "Protocolo", None))
        self.groupBox_4.setTitle(_translate("SubVentanaPlanesNotificaciones", "Agregar Nuevo Plan", None))
        self.label_4.setText(_translate("SubVentanaPlanesNotificaciones", "Nuevo Plan:", None))
        self.lineEdit_NombreNuevoPlan.setToolTip(_translate("SubVentanaPlanesNotificaciones", "Agrege El Nuevo Nombre Del Plan de Notificaciones   ", None))
        self.lineEdit_NombreNuevoPlan.setPlaceholderText(_translate("SubVentanaPlanesNotificaciones", "Nombre del Nuevo Plan ", None))
        self.pushButton_AgregarPlan.setToolTip(_translate("SubVentanaPlanesNotificaciones", "Agregar Plan", None))
        self.pushButton_AgregarPlan.setText(_translate("SubVentanaPlanesNotificaciones", "Agregar", None))
        self.label_5.setText(_translate("SubVentanaPlanesNotificaciones", "Protocolo:", None))

import recursos_rc
