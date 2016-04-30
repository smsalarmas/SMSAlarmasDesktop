# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaTiposAlarmas.ui'
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

class Ui_SubVentanaTiposdeAlarmas(object):
    def setupUi(self, SubVentanaTiposdeAlarmas):
        SubVentanaTiposdeAlarmas.setObjectName(_fromUtf8("SubVentanaTiposdeAlarmas"))
        SubVentanaTiposdeAlarmas.resize(531, 424)
        SubVentanaTiposdeAlarmas.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout = QtGui.QGridLayout(SubVentanaTiposdeAlarmas)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_TiposdeAlarmas = QtGui.QGroupBox(SubVentanaTiposdeAlarmas)
        self.groupBox_TiposdeAlarmas.setObjectName(_fromUtf8("groupBox_TiposdeAlarmas"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_TiposdeAlarmas)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_Buscar = QtGui.QLabel(self.groupBox_TiposdeAlarmas)
        self.label_Buscar.setObjectName(_fromUtf8("label_Buscar"))
        self.gridLayout_2.addWidget(self.label_Buscar, 0, 0, 1, 1)
        self.lineEdit_BuscarTiposdeAlarmas = QtGui.QLineEdit(self.groupBox_TiposdeAlarmas)
        self.lineEdit_BuscarTiposdeAlarmas.setObjectName(_fromUtf8("lineEdit_BuscarTiposdeAlarmas"))
        self.gridLayout_2.addWidget(self.lineEdit_BuscarTiposdeAlarmas, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(262, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.pushButton_AgregarTiposdeAlarmas = QtGui.QPushButton(self.groupBox_TiposdeAlarmas)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/4-Icone-plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AgregarTiposdeAlarmas.setIcon(icon)
        self.pushButton_AgregarTiposdeAlarmas.setObjectName(_fromUtf8("pushButton_AgregarTiposdeAlarmas"))
        self.gridLayout_2.addWidget(self.pushButton_AgregarTiposdeAlarmas, 0, 3, 1, 1)
        self.tableWidget_TiposdeAlarmas = QtGui.QTableWidget(self.groupBox_TiposdeAlarmas)
        self.tableWidget_TiposdeAlarmas.setObjectName(_fromUtf8("tableWidget_TiposdeAlarmas"))
        self.tableWidget_TiposdeAlarmas.setColumnCount(2)
        self.tableWidget_TiposdeAlarmas.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_TiposdeAlarmas.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_TiposdeAlarmas.setHorizontalHeaderItem(1, item)
        self.gridLayout_2.addWidget(self.tableWidget_TiposdeAlarmas, 1, 0, 1, 4)
        self.gridLayout.addWidget(self.groupBox_TiposdeAlarmas, 0, 0, 1, 1)

        self.retranslateUi(SubVentanaTiposdeAlarmas)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaTiposdeAlarmas)

    def retranslateUi(self, SubVentanaTiposdeAlarmas):
        SubVentanaTiposdeAlarmas.setWindowTitle(_translate("SubVentanaTiposdeAlarmas", "Administrar Tipos de Alarmas", None))
        self.groupBox_TiposdeAlarmas.setTitle(_translate("SubVentanaTiposdeAlarmas", "Tipos de Alarmas", None))
        self.label_Buscar.setText(_translate("SubVentanaTiposdeAlarmas", "Buscar", None))
        self.pushButton_AgregarTiposdeAlarmas.setText(_translate("SubVentanaTiposdeAlarmas", "Agregar", None))
        item = self.tableWidget_TiposdeAlarmas.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaTiposdeAlarmas", "ID", None))
        item = self.tableWidget_TiposdeAlarmas.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaTiposdeAlarmas", "Nombre", None))

import recursos_rc
