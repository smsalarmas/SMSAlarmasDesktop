# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTDialogNuevoSMS.ui'
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

class Ui_DialogNuevoSMS(object):
    def setupUi(self, DialogNuevoSMS):
        DialogNuevoSMS.setObjectName(_fromUtf8("DialogNuevoSMS"))
        DialogNuevoSMS.resize(375, 280)
        DialogNuevoSMS.setMinimumSize(QtCore.QSize(375, 280))
        DialogNuevoSMS.setMaximumSize(QtCore.QSize(375, 290))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/unnamed.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogNuevoSMS.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(DialogNuevoSMS)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelTextoNumTelefonico = QtGui.QLabel(DialogNuevoSMS)
        self.labelTextoNumTelefonico.setObjectName(_fromUtf8("labelTextoNumTelefonico"))
        self.gridLayout.addWidget(self.labelTextoNumTelefonico, 0, 0, 1, 1)
        self.lineEdit_NumeroTelefonico = QtGui.QLineEdit(DialogNuevoSMS)
        self.lineEdit_NumeroTelefonico.setMaxLength(50)
        self.lineEdit_NumeroTelefonico.setObjectName(_fromUtf8("lineEdit_NumeroTelefonico"))
        self.gridLayout.addWidget(self.lineEdit_NumeroTelefonico, 0, 1, 1, 2)
        self.label_TextoMensaje = QtGui.QLabel(DialogNuevoSMS)
        self.label_TextoMensaje.setObjectName(_fromUtf8("label_TextoMensaje"))
        self.gridLayout.addWidget(self.label_TextoMensaje, 1, 2, 1, 1)
        self.plainTextEdit_Mensaje = QtGui.QPlainTextEdit(DialogNuevoSMS)
        self.plainTextEdit_Mensaje.setObjectName(_fromUtf8("plainTextEdit_Mensaje"))
        self.gridLayout.addWidget(self.plainTextEdit_Mensaje, 2, 0, 1, 3)
        self.buttonBox = QtGui.QDialogButtonBox(DialogNuevoSMS)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 2)
        self.label_TextoCaracteres = QtGui.QLabel(DialogNuevoSMS)
        self.label_TextoCaracteres.setWordWrap(True)
        self.label_TextoCaracteres.setObjectName(_fromUtf8("label_TextoCaracteres"))
        self.gridLayout.addWidget(self.label_TextoCaracteres, 3, 0, 1, 3)

        self.retranslateUi(DialogNuevoSMS)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogNuevoSMS.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogNuevoSMS.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogNuevoSMS)
        DialogNuevoSMS.setTabOrder(self.lineEdit_NumeroTelefonico, self.plainTextEdit_Mensaje)

    def retranslateUi(self, DialogNuevoSMS):
        DialogNuevoSMS.setWindowTitle(_translate("DialogNuevoSMS", "Nuevo Mensaje", None))
        self.labelTextoNumTelefonico.setText(_translate("DialogNuevoSMS", "Numero Telefonico", None))
        self.label_TextoMensaje.setText(_translate("DialogNuevoSMS", "Texto del SMS", None))
        self.label_TextoCaracteres.setText(_translate("DialogNuevoSMS", "Si el mensaje sobrepasa los 160 caracteres se enviaran varios mensajes.", None))

import recursos_rc
