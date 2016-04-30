# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaMapaClientes.ui'
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

class Ui_VentanaMapaClientes(object):
    def setupUi(self, VentanaMapaClientes):
        VentanaMapaClientes.setObjectName(_fromUtf8("VentanaMapaClientes"))
        VentanaMapaClientes.resize(753, 644)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/map.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VentanaMapaClientes.setWindowIcon(icon)
        VentanaMapaClientes.setStyleSheet(_fromUtf8("font: bold 10pt \"Calibri\";"))
        self.gridLayout = QtGui.QGridLayout(VentanaMapaClientes)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(VentanaMapaClientes)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 52))
        self.frame.setStyleSheet(_fromUtf8("background-color: #38648B;\n"
"font: BOLD 10pt \"Calibri\";\n"
"color: rgb(255, 255, 255);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_5 = QtGui.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.pushButton_kmz = QtGui.QPushButton(self.frame)
        self.pushButton_kmz.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_kmz.setObjectName(_fromUtf8("pushButton_kmz"))
        self.gridLayout_5.addWidget(self.pushButton_kmz, 0, 3, 1, 1)
        self.pushButton_kml = QtGui.QPushButton(self.frame)
        self.pushButton_kml.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_kml.setObjectName(_fromUtf8("pushButton_kml"))
        self.gridLayout_5.addWidget(self.pushButton_kml, 0, 4, 1, 1)
        self.comboBox_SeleccionCliente = QtGui.QComboBox(self.frame)
        self.comboBox_SeleccionCliente.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.comboBox_SeleccionCliente.setObjectName(_fromUtf8("comboBox_SeleccionCliente"))
        self.gridLayout_5.addWidget(self.comboBox_SeleccionCliente, 0, 6, 1, 1)
        self.label_LogoMonitoreo = QtGui.QLabel(self.frame)
        self.label_LogoMonitoreo.setText(_fromUtf8(""))
        self.label_LogoMonitoreo.setPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/logomonitoreo.png")))
        self.label_LogoMonitoreo.setObjectName(_fromUtf8("label_LogoMonitoreo"))
        self.gridLayout_5.addWidget(self.label_LogoMonitoreo, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(389, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_5.addWidget(self.label, 0, 5, 1, 1)
        self.pushButton_gpx = QtGui.QPushButton(self.frame)
        self.pushButton_gpx.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_gpx.setObjectName(_fromUtf8("pushButton_gpx"))
        self.gridLayout_5.addWidget(self.pushButton_gpx, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(VentanaMapaClientes)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.label_FooterMonitoreo = QtGui.QLabel(VentanaMapaClientes)
        self.label_FooterMonitoreo.setMinimumSize(QtCore.QSize(0, 30))
        self.label_FooterMonitoreo.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_FooterMonitoreo.setStyleSheet(_fromUtf8("font: BOLD 10pt  \"Calibri\";\n"
"background-color: #38648B;\n"
"color: rgb(255, 255, 255);"))
        self.label_FooterMonitoreo.setLineWidth(1)
        self.label_FooterMonitoreo.setObjectName(_fromUtf8("label_FooterMonitoreo"))
        self.gridLayout.addWidget(self.label_FooterMonitoreo, 2, 0, 1, 1)

        self.retranslateUi(VentanaMapaClientes)
        QtCore.QMetaObject.connectSlotsByName(VentanaMapaClientes)

    def retranslateUi(self, VentanaMapaClientes):
        VentanaMapaClientes.setWindowTitle(_translate("VentanaMapaClientes", "Mapa Posicion de Clientes", None))
        self.pushButton_kmz.setText(_translate("VentanaMapaClientes", "KMZ", None))
        self.pushButton_kml.setText(_translate("VentanaMapaClientes", "KML", None))
        self.label.setText(_translate("VentanaMapaClientes", "Seleccione un Cliente", None))
        self.pushButton_gpx.setText(_translate("VentanaMapaClientes", "GPX", None))
        self.groupBox.setTitle(_translate("VentanaMapaClientes", "Posicion de Clientes", None))
        self.label_FooterMonitoreo.setText(_translate("VentanaMapaClientes", " Desarrollado por 365 Monitoreo C.A. - Copyright © 2015 ", None))

import recursos_rc
