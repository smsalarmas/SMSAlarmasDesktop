# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTDialogCuentasGrupo.ui'
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

class Ui_DialogCuentasGrupo(object):
    def setupUi(self, DialogCuentasGrupo):
        DialogCuentasGrupo.setObjectName(_fromUtf8("DialogCuentasGrupo"))
        DialogCuentasGrupo.resize(370, 565)
        DialogCuentasGrupo.setMinimumSize(QtCore.QSize(370, 565))
        DialogCuentasGrupo.setMaximumSize(QtCore.QSize(370, 565))
        DialogCuentasGrupo.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout_3 = QtGui.QGridLayout(DialogCuentasGrupo)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox_ElegirAbonados = QtGui.QGroupBox(DialogCuentasGrupo)
        self.groupBox_ElegirAbonados.setObjectName(_fromUtf8("groupBox_ElegirAbonados"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_ElegirAbonados)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.groupBox_ElegirAbonados)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.tableWidget_ElegirAbonados = QtGui.QTableWidget(self.groupBox_ElegirAbonados)
        self.tableWidget_ElegirAbonados.setObjectName(_fromUtf8("tableWidget_ElegirAbonados"))
        self.tableWidget_ElegirAbonados.setColumnCount(3)
        self.tableWidget_ElegirAbonados.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_ElegirAbonados.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_ElegirAbonados.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_ElegirAbonados.setHorizontalHeaderItem(2, item)
        self.gridLayout_2.addWidget(self.tableWidget_ElegirAbonados, 1, 0, 1, 5)
        self.pushButton_Buscar = QtGui.QPushButton(self.groupBox_ElegirAbonados)
        self.pushButton_Buscar.setObjectName(_fromUtf8("pushButton_Buscar"))
        self.gridLayout_2.addWidget(self.pushButton_Buscar, 0, 3, 1, 1)
        self.lineEdit_Buscar = QtGui.QLineEdit(self.groupBox_ElegirAbonados)
        self.lineEdit_Buscar.setObjectName(_fromUtf8("lineEdit_Buscar"))
        self.gridLayout_2.addWidget(self.lineEdit_Buscar, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_ElegirAbonados, 1, 0, 1, 4)
        self.groupBox_AbonadosSeleccionados = QtGui.QGroupBox(DialogCuentasGrupo)
        self.groupBox_AbonadosSeleccionados.setObjectName(_fromUtf8("groupBox_AbonadosSeleccionados"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_AbonadosSeleccionados)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget_AbonadosSeleccionados = QtGui.QTableWidget(self.groupBox_AbonadosSeleccionados)
        self.tableWidget_AbonadosSeleccionados.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget_AbonadosSeleccionados.setObjectName(_fromUtf8("tableWidget_AbonadosSeleccionados"))
        self.tableWidget_AbonadosSeleccionados.setColumnCount(3)
        self.tableWidget_AbonadosSeleccionados.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_AbonadosSeleccionados.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_AbonadosSeleccionados.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_AbonadosSeleccionados.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.tableWidget_AbonadosSeleccionados, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_AbonadosSeleccionados, 0, 0, 1, 4)
        spacerItem1 = QtGui.QSpacerItem(112, 40, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 2, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(112, 40, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 2, 3, 1, 1)
        self.pushButton_Cancelar = QtGui.QPushButton(DialogCuentasGrupo)
        self.pushButton_Cancelar.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/uncheck.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Cancelar.setIcon(icon)
        self.pushButton_Cancelar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Cancelar.setFlat(True)
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.gridLayout_3.addWidget(self.pushButton_Cancelar, 2, 2, 1, 1)
        self.pushButton_Guardar = QtGui.QPushButton(DialogCuentasGrupo)
        self.pushButton_Guardar.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Guardar.setIcon(icon1)
        self.pushButton_Guardar.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_Guardar.setAutoDefault(False)
        self.pushButton_Guardar.setFlat(True)
        self.pushButton_Guardar.setObjectName(_fromUtf8("pushButton_Guardar"))
        self.gridLayout_3.addWidget(self.pushButton_Guardar, 2, 1, 1, 1)

        self.retranslateUi(DialogCuentasGrupo)
        QtCore.QMetaObject.connectSlotsByName(DialogCuentasGrupo)

    def retranslateUi(self, DialogCuentasGrupo):
        DialogCuentasGrupo.setWindowTitle(_translate("DialogCuentasGrupo", "Administracion del Grupo de Clientes", None))
        self.groupBox_ElegirAbonados.setTitle(_translate("DialogCuentasGrupo", "Elegir Abonados", None))
        self.label.setText(_translate("DialogCuentasGrupo", "Buscar: ", None))
        item = self.tableWidget_ElegirAbonados.horizontalHeaderItem(0)
        item.setText(_translate("DialogCuentasGrupo", "Abonado", None))
        item = self.tableWidget_ElegirAbonados.horizontalHeaderItem(1)
        item.setText(_translate("DialogCuentasGrupo", "Nombre", None))
        item = self.tableWidget_ElegirAbonados.horizontalHeaderItem(2)
        item.setText(_translate("DialogCuentasGrupo", "Accion", None))
        self.pushButton_Buscar.setText(_translate("DialogCuentasGrupo", "Buscar", None))
        self.groupBox_AbonadosSeleccionados.setTitle(_translate("DialogCuentasGrupo", "Abonados Seleccionados", None))
        item = self.tableWidget_AbonadosSeleccionados.horizontalHeaderItem(0)
        item.setText(_translate("DialogCuentasGrupo", "Abonado", None))
        item = self.tableWidget_AbonadosSeleccionados.horizontalHeaderItem(1)
        item.setText(_translate("DialogCuentasGrupo", "Nombre", None))
        item = self.tableWidget_AbonadosSeleccionados.horizontalHeaderItem(2)
        item.setText(_translate("DialogCuentasGrupo", "Accion", None))

import recursos_rc
