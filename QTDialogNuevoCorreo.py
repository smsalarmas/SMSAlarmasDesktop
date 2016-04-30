# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTDialogNuevoCorreo.ui'
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

class Ui_DialogNuevoCorreo(object):
    def setupUi(self, DialogNuevoCorreo):
        DialogNuevoCorreo.setObjectName(_fromUtf8("DialogNuevoCorreo"))
        DialogNuevoCorreo.resize(375, 280)
        DialogNuevoCorreo.setMinimumSize(QtCore.QSize(375, 280))
        DialogNuevoCorreo.setMaximumSize(QtCore.QSize(375, 290))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/mailbueno.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogNuevoCorreo.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(DialogNuevoCorreo)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_TextoMensaje = QtGui.QLabel(DialogNuevoCorreo)
        self.label_TextoMensaje.setObjectName(_fromUtf8("label_TextoMensaje"))
        self.gridLayout.addWidget(self.label_TextoMensaje, 1, 2, 1, 1)
        self.lineEdit_Correo = QtGui.QLineEdit(DialogNuevoCorreo)
        self.lineEdit_Correo.setMaxLength(50)
        self.lineEdit_Correo.setObjectName(_fromUtf8("lineEdit_Correo"))
        self.gridLayout.addWidget(self.lineEdit_Correo, 0, 1, 1, 2)
        self.plainTextEdit_Mensaje = QtGui.QPlainTextEdit(DialogNuevoCorreo)
        self.plainTextEdit_Mensaje.setObjectName(_fromUtf8("plainTextEdit_Mensaje"))
        self.gridLayout.addWidget(self.plainTextEdit_Mensaje, 2, 0, 1, 3)
        self.buttonBox = QtGui.QDialogButtonBox(DialogNuevoCorreo)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 2)
        self.labelTextoNumTelefonico = QtGui.QLabel(DialogNuevoCorreo)
        self.labelTextoNumTelefonico.setObjectName(_fromUtf8("labelTextoNumTelefonico"))
        self.gridLayout.addWidget(self.labelTextoNumTelefonico, 0, 0, 1, 1)

        self.retranslateUi(DialogNuevoCorreo)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogNuevoCorreo.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogNuevoCorreo.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogNuevoCorreo)
        DialogNuevoCorreo.setTabOrder(self.lineEdit_Correo, self.plainTextEdit_Mensaje)

    def retranslateUi(self, DialogNuevoCorreo):
        DialogNuevoCorreo.setWindowTitle(_translate("DialogNuevoCorreo", "Nuevo Correo", None))
        self.label_TextoMensaje.setText(_translate("DialogNuevoCorreo", "Texto del Correo", None))
        self.labelTextoNumTelefonico.setText(_translate("DialogNuevoCorreo", "Direccion de Correo", None))

import recursos_rc
