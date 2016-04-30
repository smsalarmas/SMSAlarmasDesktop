# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTDialogLogin.ui'
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

class Ui_Dialog_Login(object):
    def setupUi(self, Dialog_Login):
        Dialog_Login.setObjectName(_fromUtf8("Dialog_Login"))
        Dialog_Login.resize(342, 325)
        Dialog_Login.setMinimumSize(QtCore.QSize(342, 325))
        Dialog_Login.setMaximumSize(QtCore.QSize(342, 325))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/connections-512(1).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_Login.setWindowIcon(icon)
        Dialog_Login.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label = QtGui.QLabel(Dialog_Login)
        self.label.setGeometry(QtCore.QRect(78, 10, 181, 91))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/LogoLogin.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog_Login)
        self.label_2.setGeometry(QtCore.QRect(110, 300, 131, 16))
        self.label_2.setStyleSheet(_fromUtf8("\n"
"color: rgb(67, 67, 67);\n"
"font: 10pt \"Calibri\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_Ingresar = QtGui.QPushButton(Dialog_Login)
        self.pushButton_Ingresar.setGeometry(QtCore.QRect(110, 250, 81, 31))
        self.pushButton_Ingresar.setStyleSheet(_fromUtf8("background-color: #38648B;\n"
"font: 12pt \"Calibri\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButton_Ingresar.setObjectName(_fromUtf8("pushButton_Ingresar"))
        self.lineEdit_Contrasena = QtGui.QLineEdit(Dialog_Login)
        self.lineEdit_Contrasena.setGeometry(QtCore.QRect(90, 180, 160, 25))
        self.lineEdit_Contrasena.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";\n"
"color: rgb(63, 63, 63);"))
        self.lineEdit_Contrasena.setText(_fromUtf8(""))
        self.lineEdit_Contrasena.setMaxLength(20)
        self.lineEdit_Contrasena.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_Contrasena.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Contrasena.setObjectName(_fromUtf8("lineEdit_Contrasena"))
        self.lineEdit_Usuario = QtGui.QLineEdit(Dialog_Login)
        self.lineEdit_Usuario.setGeometry(QtCore.QRect(90, 140, 160, 25))
        self.lineEdit_Usuario.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";\n"
"color: rgb(72, 72, 72);"))
        self.lineEdit_Usuario.setText(_fromUtf8(""))
        self.lineEdit_Usuario.setMaxLength(50)
        self.lineEdit_Usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Usuario.setObjectName(_fromUtf8("lineEdit_Usuario"))
        self.label_3 = QtGui.QLabel(Dialog_Login)
        self.label_3.setGeometry(QtCore.QRect(-20, 110, 391, 121))
        self.label_3.setStyleSheet(_fromUtf8("background-color: #38648B;\n"
"font: 12pt \"Calibri\";\n"
"color: rgb(255, 255, 255);"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_Minimizar = QtGui.QPushButton(Dialog_Login)
        self.pushButton_Minimizar.setGeometry(QtCore.QRect(200, 250, 21, 31))
        self.pushButton_Minimizar.setStyleSheet(_fromUtf8("background-color: #38648B;\n"
"font: 12pt \"Calibri\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButton_Minimizar.setObjectName(_fromUtf8("pushButton_Minimizar"))
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton_Ingresar.raise_()
        self.lineEdit_Contrasena.raise_()
        self.lineEdit_Usuario.raise_()
        self.pushButton_Minimizar.raise_()

        self.retranslateUi(Dialog_Login)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Login)
        Dialog_Login.setTabOrder(self.lineEdit_Usuario, self.lineEdit_Contrasena)
        Dialog_Login.setTabOrder(self.lineEdit_Contrasena, self.pushButton_Ingresar)

    def retranslateUi(self, Dialog_Login):
        Dialog_Login.setWindowTitle(_translate("Dialog_Login", "Acceso 365Connect", None))
        self.label_2.setText(_translate("Dialog_Login", "2016 © 365Software", None))
        self.pushButton_Ingresar.setText(_translate("Dialog_Login", "Ingresar", None))
        self.lineEdit_Contrasena.setPlaceholderText(_translate("Dialog_Login", "Contraseña", None))
        self.lineEdit_Usuario.setPlaceholderText(_translate("Dialog_Login", "Usuario", None))
        self.pushButton_Minimizar.setToolTip(_translate("Dialog_Login", "Minimizar", None))
        self.pushButton_Minimizar.setText(_translate("Dialog_Login", "_", None))

import recursos_rc
