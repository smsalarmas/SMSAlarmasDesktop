# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTDialogAgregarZona.ui'
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

class Ui_Dialog_AgregarZona(object):
    def setupUi(self, Dialog_AgregarZona):
        Dialog_AgregarZona.setObjectName(_fromUtf8("Dialog_AgregarZona"))
        Dialog_AgregarZona.resize(300, 300)
        Dialog_AgregarZona.setMinimumSize(QtCore.QSize(300, 300))
        Dialog_AgregarZona.setMaximumSize(QtCore.QSize(300, 16777215))
        Dialog_AgregarZona.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout = QtGui.QGridLayout(Dialog_AgregarZona)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog_AgregarZona)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_Codigo = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Codigo.setMaxLength(50)
        self.lineEdit_Codigo.setObjectName(_fromUtf8("lineEdit_Codigo"))
        self.verticalLayout.addWidget(self.lineEdit_Codigo)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_Informacion = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Informacion.setMaxLength(100)
        self.lineEdit_Informacion.setObjectName(_fromUtf8("lineEdit_Informacion"))
        self.verticalLayout.addWidget(self.lineEdit_Informacion)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_Ubicacion = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Ubicacion.setMaxLength(50)
        self.lineEdit_Ubicacion.setObjectName(_fromUtf8("lineEdit_Ubicacion"))
        self.verticalLayout.addWidget(self.lineEdit_Ubicacion)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_AgregarFoto = QtGui.QPushButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/picture-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AgregarFoto.setIcon(icon)
        self.pushButton_AgregarFoto.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_AgregarFoto.setAutoDefault(False)
        self.pushButton_AgregarFoto.setFlat(False)
        self.pushButton_AgregarFoto.setObjectName(_fromUtf8("pushButton_AgregarFoto"))
        self.verticalLayout.addWidget(self.pushButton_AgregarFoto)
        self.label_Imagen = QtGui.QLabel(self.groupBox)
        self.label_Imagen.setText(_fromUtf8(""))
        self.label_Imagen.setObjectName(_fromUtf8("label_Imagen"))
        self.verticalLayout.addWidget(self.label_Imagen)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_GuardarZona = QtGui.QPushButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_GuardarZona.setIcon(icon1)
        self.pushButton_GuardarZona.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_GuardarZona.setFlat(True)
        self.pushButton_GuardarZona.setObjectName(_fromUtf8("pushButton_GuardarZona"))
        self.verticalLayout.addWidget(self.pushButton_GuardarZona)
        self.lineEdit_Ubicacion.raise_()
        self.lineEdit_Informacion.raise_()
        self.pushButton_AgregarFoto.raise_()
        self.pushButton_GuardarZona.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.lineEdit_Codigo.raise_()
        self.label_Imagen.raise_()
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Dialog_AgregarZona)
        QtCore.QMetaObject.connectSlotsByName(Dialog_AgregarZona)
        Dialog_AgregarZona.setTabOrder(self.lineEdit_Codigo, self.lineEdit_Informacion)
        Dialog_AgregarZona.setTabOrder(self.lineEdit_Informacion, self.lineEdit_Ubicacion)

    def retranslateUi(self, Dialog_AgregarZona):
        Dialog_AgregarZona.setWindowTitle(_translate("Dialog_AgregarZona", "Agregar Zona", None))
        self.groupBox.setTitle(_translate("Dialog_AgregarZona", "Agregue la Informacion de la Zona", None))
        self.label.setText(_translate("Dialog_AgregarZona", "Codigo:", None))
        self.lineEdit_Codigo.setPlaceholderText(_translate("Dialog_AgregarZona", "Numero de Zona", None))
        self.label_2.setText(_translate("Dialog_AgregarZona", "Descripcion:", None))
        self.lineEdit_Informacion.setPlaceholderText(_translate("Dialog_AgregarZona", "Informacion de la Zona", None))
        self.label_3.setText(_translate("Dialog_AgregarZona", "Ubicacion:", None))
        self.lineEdit_Ubicacion.setPlaceholderText(_translate("Dialog_AgregarZona", "Lugar de Ubicacion", None))
        self.pushButton_AgregarFoto.setText(_translate("Dialog_AgregarZona", "Agregar Foto", None))
        self.pushButton_GuardarZona.setText(_translate("Dialog_AgregarZona", "Guardar", None))

import recursos_rc
