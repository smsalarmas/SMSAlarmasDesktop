# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaParentescos.ui'
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

class Ui_SubVentanaParentesco(object):
    def setupUi(self, SubVentanaParentesco):
        SubVentanaParentesco.setObjectName(_fromUtf8("SubVentanaParentesco"))
        SubVentanaParentesco.resize(338, 505)
        SubVentanaParentesco.setMinimumSize(QtCore.QSize(338, 505))
        SubVentanaParentesco.setMaximumSize(QtCore.QSize(338, 505))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/parentesco.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubVentanaParentesco.setWindowIcon(icon)
        SubVentanaParentesco.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout_2 = QtGui.QGridLayout(SubVentanaParentesco)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_4 = QtGui.QGroupBox(SubVentanaParentesco)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lineEdit_Buscar = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_Buscar.setObjectName(_fromUtf8("lineEdit_Buscar"))
        self.gridLayout_3.addWidget(self.lineEdit_Buscar, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.tableWidget_ListadeParentescos = QtGui.QTableWidget(self.groupBox_4)
        self.tableWidget_ListadeParentescos.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidget_ListadeParentescos.setStyleSheet(_fromUtf8(""))
        self.tableWidget_ListadeParentescos.setObjectName(_fromUtf8("tableWidget_ListadeParentescos"))
        self.tableWidget_ListadeParentescos.setColumnCount(1)
        self.tableWidget_ListadeParentescos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ListadeParentescos.setHorizontalHeaderItem(0, item)
        self.gridLayout_3.addWidget(self.tableWidget_ListadeParentescos, 1, 0, 1, 3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_AgregarParentesco = QtGui.QPushButton(self.groupBox_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/4-Icone-plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AgregarParentesco.setIcon(icon1)
        self.pushButton_AgregarParentesco.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_AgregarParentesco.setFlat(True)
        self.pushButton_AgregarParentesco.setObjectName(_fromUtf8("pushButton_AgregarParentesco"))
        self.horizontalLayout_2.addWidget(self.pushButton_AgregarParentesco)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 3)
        self.gridLayout_2.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_DatosParentesco = QtGui.QGroupBox(SubVentanaParentesco)
        self.groupBox_DatosParentesco.setObjectName(_fromUtf8("groupBox_DatosParentesco"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_DatosParentesco)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.groupBox_DatosParentesco)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_NombreParentesco = QtGui.QLineEdit(self.groupBox_DatosParentesco)
        self.lineEdit_NombreParentesco.setObjectName(_fromUtf8("lineEdit_NombreParentesco"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_NombreParentesco)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_GuardarParentesco = QtGui.QPushButton(self.groupBox_DatosParentesco)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_GuardarParentesco.setIcon(icon2)
        self.pushButton_GuardarParentesco.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_GuardarParentesco.setFlat(True)
        self.pushButton_GuardarParentesco.setObjectName(_fromUtf8("pushButton_GuardarParentesco"))
        self.horizontalLayout.addWidget(self.pushButton_GuardarParentesco)
        self.pushButton_BorrarParentesco = QtGui.QPushButton(self.groupBox_DatosParentesco)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/eraser-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_BorrarParentesco.setIcon(icon3)
        self.pushButton_BorrarParentesco.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_BorrarParentesco.setFlat(True)
        self.pushButton_BorrarParentesco.setObjectName(_fromUtf8("pushButton_BorrarParentesco"))
        self.horizontalLayout.addWidget(self.pushButton_BorrarParentesco)
        self.pushButton_Cancelar = QtGui.QPushButton(self.groupBox_DatosParentesco)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/uncheck.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Cancelar.setIcon(icon4)
        self.pushButton_Cancelar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Cancelar.setFlat(True)
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.horizontalLayout.addWidget(self.pushButton_Cancelar)
        self.formLayout.setLayout(1, QtGui.QFormLayout.SpanningRole, self.horizontalLayout)
        self.gridLayout_2.addWidget(self.groupBox_DatosParentesco, 1, 0, 1, 1)

        self.retranslateUi(SubVentanaParentesco)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaParentesco)
        SubVentanaParentesco.setTabOrder(self.lineEdit_Buscar, self.tableWidget_ListadeParentescos)
        SubVentanaParentesco.setTabOrder(self.tableWidget_ListadeParentescos, self.pushButton_AgregarParentesco)
        SubVentanaParentesco.setTabOrder(self.pushButton_AgregarParentesco, self.lineEdit_NombreParentesco)
        SubVentanaParentesco.setTabOrder(self.lineEdit_NombreParentesco, self.pushButton_GuardarParentesco)
        SubVentanaParentesco.setTabOrder(self.pushButton_GuardarParentesco, self.pushButton_BorrarParentesco)
        SubVentanaParentesco.setTabOrder(self.pushButton_BorrarParentesco, self.pushButton_Cancelar)

    def retranslateUi(self, SubVentanaParentesco):
        SubVentanaParentesco.setWindowTitle(_translate("SubVentanaParentesco", "Administracion de Parentescos", None))
        self.groupBox_4.setTitle(_translate("SubVentanaParentesco", "Lista de Parentescos", None))
        self.label_3.setText(_translate("SubVentanaParentesco", "Buscar:", None))
        item = self.tableWidget_ListadeParentescos.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaParentesco", "Nombre", None))
        self.pushButton_AgregarParentesco.setToolTip(_translate("SubVentanaParentesco", "Nueva Empresa", None))
        self.pushButton_AgregarParentesco.setText(_translate("SubVentanaParentesco", "Agregar", None))
        self.groupBox_DatosParentesco.setTitle(_translate("SubVentanaParentesco", "Datos del Parentesco", None))
        self.label_2.setText(_translate("SubVentanaParentesco", "Nombre:", None))
        self.pushButton_GuardarParentesco.setToolTip(_translate("SubVentanaParentesco", "Guardar Empresa", None))
        self.pushButton_GuardarParentesco.setText(_translate("SubVentanaParentesco", "Guardar", None))
        self.pushButton_BorrarParentesco.setToolTip(_translate("SubVentanaParentesco", "Borrar Empresa", None))
        self.pushButton_BorrarParentesco.setText(_translate("SubVentanaParentesco", "Borrar", None))
        self.pushButton_Cancelar.setToolTip(_translate("SubVentanaParentesco", "Cancelar Edicion", None))
        self.pushButton_Cancelar.setText(_translate("SubVentanaParentesco", "Cancelar", None))

import recursos_rc
