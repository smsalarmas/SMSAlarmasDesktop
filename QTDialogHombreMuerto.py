# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTDialogHombreMuerto.ui'
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

class Ui_Dialog_HombreMuerto(object):
    def setupUi(self, Dialog_HombreMuerto):
        Dialog_HombreMuerto.setObjectName(_fromUtf8("Dialog_HombreMuerto"))
        Dialog_HombreMuerto.resize(500, 350)
        Dialog_HombreMuerto.setMinimumSize(QtCore.QSize(500, 350))
        Dialog_HombreMuerto.setMaximumSize(QtCore.QSize(500, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/eye.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_HombreMuerto.setWindowIcon(icon)
        Dialog_HombreMuerto.setWindowOpacity(1.0)
        Dialog_HombreMuerto.setStyleSheet(_fromUtf8("font: bold 18pt \"Calibri\";"))
        self.label = QtGui.QLabel(Dialog_HombreMuerto)
        self.label.setGeometry(QtCore.QRect(90, 60, 341, 16))
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog_HombreMuerto)
        self.label_2.setGeometry(QtCore.QRect(96, 140, 251, 16))
        self.label_2.setStyleSheet(_fromUtf8("font: 12pt \"Calibri\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_Codigo = QtGui.QLabel(Dialog_HombreMuerto)
        self.label_Codigo.setGeometry(QtCore.QRect(348, 138, 61, 20))
        self.label_Codigo.setStyleSheet(_fromUtf8("font: bold 12pt \"Calibri\";"))
        self.label_Codigo.setObjectName(_fromUtf8("label_Codigo"))
        self.lineEdit_Codigo = QtGui.QLineEdit(Dialog_HombreMuerto)
        self.lineEdit_Codigo.setGeometry(QtCore.QRect(156, 180, 171, 31))
        self.lineEdit_Codigo.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.lineEdit_Codigo.setMaxLength(6)
        self.lineEdit_Codigo.setFrame(True)
        self.lineEdit_Codigo.setDragEnabled(False)
        self.lineEdit_Codigo.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_Codigo.setObjectName(_fromUtf8("lineEdit_Codigo"))
        self.label_4 = QtGui.QLabel(Dialog_HombreMuerto)
        self.label_4.setGeometry(QtCore.QRect(-4, 230, 511, 121))
        self.label_4.setStyleSheet(_fromUtf8("background-color: #38648B;\n"
"font: 10pt \"Calibri\";\n"
"color: rgb(255, 255, 255);"))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog_HombreMuerto)
        self.label_5.setGeometry(QtCore.QRect(-4, 0, 511, 121))
        self.label_5.setStyleSheet(_fromUtf8("background-color: #38648B;\n"
"font: 10pt \"Calibri\";\n"
"color: rgb(255, 255, 255);"))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog_HombreMuerto)
        self.label_6.setGeometry(QtCore.QRect(86, 270, 331, 41))
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 8pt \"Calibri\";"))
        self.label_6.setLineWidth(0)
        self.label_6.setMidLineWidth(1)
        self.label_6.setTextFormat(QtCore.Qt.PlainText)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_Aceptar = QtGui.QPushButton(Dialog_HombreMuerto)
        self.pushButton_Aceptar.setGeometry(QtCore.QRect(336, 180, 41, 31))
        self.pushButton_Aceptar.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Aceptar.setIcon(icon1)
        self.pushButton_Aceptar.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_Aceptar.setDefault(False)
        self.pushButton_Aceptar.setFlat(True)
        self.pushButton_Aceptar.setObjectName(_fromUtf8("pushButton_Aceptar"))
        self.label_7 = QtGui.QLabel(Dialog_HombreMuerto)
        self.label_7.setGeometry(QtCore.QRect(-4, 50, 91, 281))
        self.label_7.setStyleSheet(_fromUtf8("background-color: #38648B;\n"
"font: 10pt \"Calibri\";\n"
"color: rgb(255, 255, 255);"))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Dialog_HombreMuerto)
        self.label_8.setGeometry(QtCore.QRect(416, 40, 91, 281))
        self.label_8.setStyleSheet(_fromUtf8("background-color: #38648B;\n"
"font: 10pt \"Calibri\";\n"
"color: rgb(255, 255, 255);"))
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_12 = QtGui.QLabel(Dialog_HombreMuerto)
        self.label_12.setGeometry(QtCore.QRect(66, 120, 371, 111))
        self.label_12.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_12.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_Codigo.raise_()
        self.lineEdit_Codigo.raise_()
        self.label_6.raise_()
        self.pushButton_Aceptar.raise_()
        self.label_7.raise_()
        self.label_8.raise_()

        self.retranslateUi(Dialog_HombreMuerto)
        QtCore.QMetaObject.connectSlotsByName(Dialog_HombreMuerto)

    def retranslateUi(self, Dialog_HombreMuerto):
        Dialog_HombreMuerto.setWindowTitle(_translate("Dialog_HombreMuerto", "Captcha Hombre Muerto", None))
        self.label.setText(_translate("Dialog_HombreMuerto", "Notificacion de Hombre Muerto", None))
        self.label_2.setText(_translate("Dialog_HombreMuerto", "Por Favor ingrese el siguiente Codigo:", None))
        self.label_Codigo.setText(_translate("Dialog_HombreMuerto", "Codigo", None))
        self.lineEdit_Codigo.setPlaceholderText(_translate("Dialog_HombreMuerto", "Ingrese Codigo", None))
        self.label_6.setText(_translate("Dialog_HombreMuerto", "El uso de este codigo es por su seguridad. Recuerde que en caso de inactividad por el periodo establecido se le enviara una notificacion instantanea a su manager.", None))

import recursos_rc
