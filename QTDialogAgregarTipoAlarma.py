# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTDialogAgregarTipoAlarma.ui'
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

class Ui_Dialog_AgregarTipoAlarma(object):
    def setupUi(self, Dialog_AgregarTipoAlarma):
        Dialog_AgregarTipoAlarma.setObjectName(_fromUtf8("Dialog_AgregarTipoAlarma"))
        Dialog_AgregarTipoAlarma.resize(300, 300)
        Dialog_AgregarTipoAlarma.setMinimumSize(QtCore.QSize(300, 300))
        Dialog_AgregarTipoAlarma.setMaximumSize(QtCore.QSize(300, 303))
        Dialog_AgregarTipoAlarma.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout = QtGui.QGridLayout(Dialog_AgregarTipoAlarma)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog_AgregarTipoAlarma)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)
        self.pushButton_BuscarManualAyuda = QtGui.QPushButton(self.groupBox_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/search (2).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_BuscarManualAyuda.setIcon(icon)
        self.pushButton_BuscarManualAyuda.setObjectName(_fromUtf8("pushButton_BuscarManualAyuda"))
        self.gridLayout_2.addWidget(self.pushButton_BuscarManualAyuda, 0, 1, 1, 1)
        self.pushButton_BuscarManualUsuario = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_BuscarManualUsuario.setIcon(icon)
        self.pushButton_BuscarManualUsuario.setObjectName(_fromUtf8("pushButton_BuscarManualUsuario"))
        self.gridLayout_2.addWidget(self.pushButton_BuscarManualUsuario, 3, 1, 1, 1)
        self.pushButton_BuscarManualProgramacion = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_BuscarManualProgramacion.setIcon(icon)
        self.pushButton_BuscarManualProgramacion.setObjectName(_fromUtf8("pushButton_BuscarManualProgramacion"))
        self.gridLayout_2.addWidget(self.pushButton_BuscarManualProgramacion, 5, 1, 1, 1)
        self.label_NombreManualProgramacion = QtGui.QLabel(self.groupBox_2)
        self.label_NombreManualProgramacion.setText(_fromUtf8(""))
        self.label_NombreManualProgramacion.setObjectName(_fromUtf8("label_NombreManualProgramacion"))
        self.gridLayout_2.addWidget(self.label_NombreManualProgramacion, 6, 0, 1, 2)
        self.label_NombreManualUsuario = QtGui.QLabel(self.groupBox_2)
        self.label_NombreManualUsuario.setText(_fromUtf8(""))
        self.label_NombreManualUsuario.setObjectName(_fromUtf8("label_NombreManualUsuario"))
        self.gridLayout_2.addWidget(self.label_NombreManualUsuario, 4, 0, 1, 2)
        self.label_NombreManualAyuda = QtGui.QLabel(self.groupBox_2)
        self.label_NombreManualAyuda.setText(_fromUtf8(""))
        self.label_NombreManualAyuda.setObjectName(_fromUtf8("label_NombreManualAyuda"))
        self.gridLayout_2.addWidget(self.label_NombreManualAyuda, 1, 0, 1, 2)
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_NombreManualAyuda.raise_()
        self.label_NombreManualUsuario.raise_()
        self.label_NombreManualProgramacion.raise_()
        self.pushButton_BuscarManualAyuda.raise_()
        self.pushButton_BuscarManualUsuario.raise_()
        self.pushButton_BuscarManualProgramacion.raise_()
        self.gridLayout_3.addWidget(self.groupBox_2, 3, 0, 1, 2)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit_NombrePanel = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_NombrePanel.setObjectName(_fromUtf8("lineEdit_NombrePanel"))
        self.gridLayout_3.addWidget(self.lineEdit_NombrePanel, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 3)
        self.pushButton_Agregar = QtGui.QPushButton(Dialog_AgregarTipoAlarma)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Agregar.setIcon(icon1)
        self.pushButton_Agregar.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_Agregar.setFlat(True)
        self.pushButton_Agregar.setObjectName(_fromUtf8("pushButton_Agregar"))
        self.gridLayout.addWidget(self.pushButton_Agregar, 2, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(93, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(94, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 1, 1, 1, 1)

        self.retranslateUi(Dialog_AgregarTipoAlarma)
        QtCore.QMetaObject.connectSlotsByName(Dialog_AgregarTipoAlarma)

    def retranslateUi(self, Dialog_AgregarTipoAlarma):
        Dialog_AgregarTipoAlarma.setWindowTitle(_translate("Dialog_AgregarTipoAlarma", "Agregar Panel de Alarma", None))
        self.groupBox.setTitle(_translate("Dialog_AgregarTipoAlarma", "Agregar Nuevo Tipo de Alarma", None))
        self.groupBox_2.setTitle(_translate("Dialog_AgregarTipoAlarma", "Manuales", None))
        self.label_3.setText(_translate("Dialog_AgregarTipoAlarma", "Usuario", None))
        self.label_2.setText(_translate("Dialog_AgregarTipoAlarma", "Ayuda", None))
        self.label_4.setText(_translate("Dialog_AgregarTipoAlarma", "Programacion", None))
        self.pushButton_BuscarManualAyuda.setText(_translate("Dialog_AgregarTipoAlarma", "Buscar", None))
        self.pushButton_BuscarManualUsuario.setText(_translate("Dialog_AgregarTipoAlarma", "Buscar", None))
        self.pushButton_BuscarManualProgramacion.setText(_translate("Dialog_AgregarTipoAlarma", "Buscar", None))
        self.label.setText(_translate("Dialog_AgregarTipoAlarma", "Panel", None))
        self.pushButton_Agregar.setText(_translate("Dialog_AgregarTipoAlarma", "Agregar", None))

import recursos_rc
