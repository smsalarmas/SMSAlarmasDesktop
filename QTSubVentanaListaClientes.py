# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaListaClientes.ui'
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

class Ui_VentanaListaClientes(object):
    def setupUi(self, VentanaListaClientes):
        VentanaListaClientes.setObjectName(_fromUtf8("VentanaListaClientes"))
        VentanaListaClientes.resize(780, 580)
        VentanaListaClientes.setMinimumSize(QtCore.QSize(780, 580))
        VentanaListaClientes.setStyleSheet(_fromUtf8("font: bold 10pt \"Calibri\";"))
        self.gridLayout = QtGui.QGridLayout(VentanaListaClientes)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(VentanaListaClientes)
        self.groupBox.setStyleSheet(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setMaximumSize(QtCore.QSize(25, 25))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/search2.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.button_AgregarCliente = QtGui.QPushButton(self.groupBox)
        self.button_AgregarCliente.setStatusTip(_fromUtf8(""))
        self.button_AgregarCliente.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/CLIENTE.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_AgregarCliente.setIcon(icon)
        self.button_AgregarCliente.setIconSize(QtCore.QSize(25, 25))
        self.button_AgregarCliente.setFlat(True)
        self.button_AgregarCliente.setObjectName(_fromUtf8("button_AgregarCliente"))
        self.gridLayout_2.addWidget(self.button_AgregarCliente, 0, 3, 1, 1)
        self.lineEdit_BusquedaCliente = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_BusquedaCliente.setInputMask(_fromUtf8(""))
        self.lineEdit_BusquedaCliente.setText(_fromUtf8(""))
        self.lineEdit_BusquedaCliente.setFrame(True)
        self.lineEdit_BusquedaCliente.setObjectName(_fromUtf8("lineEdit_BusquedaCliente"))
        self.gridLayout_2.addWidget(self.lineEdit_BusquedaCliente, 0, 1, 1, 1)
        self.tableWidget_ListaClientes = QtGui.QTableWidget(self.groupBox)
        self.tableWidget_ListaClientes.setStyleSheet(_fromUtf8("f"))
        self.tableWidget_ListaClientes.setObjectName(_fromUtf8("tableWidget_ListaClientes"))
        self.tableWidget_ListaClientes.setColumnCount(5)
        self.tableWidget_ListaClientes.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/bubble.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.tableWidget_ListaClientes.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/direccionmap.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.tableWidget_ListaClientes.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/direccion.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.tableWidget_ListaClientes.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/mailbueno.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.tableWidget_ListaClientes.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/sms-search-icon (1).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon5)
        self.tableWidget_ListaClientes.setHorizontalHeaderItem(4, item)
        self.gridLayout_2.addWidget(self.tableWidget_ListaClientes, 1, 0, 1, 4)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(VentanaListaClientes)
        QtCore.QMetaObject.connectSlotsByName(VentanaListaClientes)

    def retranslateUi(self, VentanaListaClientes):
        VentanaListaClientes.setWindowTitle(_translate("VentanaListaClientes", "Lista de Clientes", None))
        self.groupBox.setTitle(_translate("VentanaListaClientes", "Lista de Clientes", None))
        self.button_AgregarCliente.setToolTip(_translate("VentanaListaClientes", "Agregar Nuevo Cliente", None))
        item = self.tableWidget_ListaClientes.horizontalHeaderItem(0)
        item.setText(_translate("VentanaListaClientes", "ID", None))
        item = self.tableWidget_ListaClientes.horizontalHeaderItem(1)
        item.setText(_translate("VentanaListaClientes", "Nombre", None))
        item = self.tableWidget_ListaClientes.horizontalHeaderItem(2)
        item.setText(_translate("VentanaListaClientes", "Direccion", None))
        item = self.tableWidget_ListaClientes.horizontalHeaderItem(3)
        item.setText(_translate("VentanaListaClientes", "Correo", None))
        item = self.tableWidget_ListaClientes.horizontalHeaderItem(4)
        item.setText(_translate("VentanaListaClientes", "Telefono", None))

import recursos_rc
