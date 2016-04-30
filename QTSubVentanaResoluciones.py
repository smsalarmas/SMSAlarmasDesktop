# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaResoluciones.ui'
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

class Ui_SubVentanaResoluciones(object):
    def setupUi(self, SubVentanaResoluciones):
        SubVentanaResoluciones.setObjectName(_fromUtf8("SubVentanaResoluciones"))
        SubVentanaResoluciones.resize(530, 483)
        SubVentanaResoluciones.setMinimumSize(QtCore.QSize(530, 483))
        SubVentanaResoluciones.setMaximumSize(QtCore.QSize(530, 483))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Resoluciones.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubVentanaResoluciones.setWindowIcon(icon)
        SubVentanaResoluciones.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout_3 = QtGui.QGridLayout(SubVentanaResoluciones)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox_4 = QtGui.QGroupBox(SubVentanaResoluciones)
        self.groupBox_4.setMinimumSize(QtCore.QSize(500, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_Buscar = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_Buscar.setObjectName(_fromUtf8("lineEdit_Buscar"))
        self.gridLayout.addWidget(self.lineEdit_Buscar, 0, 1, 1, 1)
        self.tableWidget_ListadeResoluciones = QtGui.QTableWidget(self.groupBox_4)
        self.tableWidget_ListadeResoluciones.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget_ListadeResoluciones.setStyleSheet(_fromUtf8(""))
        self.tableWidget_ListadeResoluciones.setObjectName(_fromUtf8("tableWidget_ListadeResoluciones"))
        self.tableWidget_ListadeResoluciones.setColumnCount(1)
        self.tableWidget_ListadeResoluciones.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget_ListadeResoluciones.setHorizontalHeaderItem(0, item)
        self.gridLayout.addWidget(self.tableWidget_ListadeResoluciones, 1, 0, 1, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_AgregarResolucion = QtGui.QPushButton(self.groupBox_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/4-Icone-plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AgregarResolucion.setIcon(icon1)
        self.pushButton_AgregarResolucion.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_AgregarResolucion.setFlat(True)
        self.pushButton_AgregarResolucion.setObjectName(_fromUtf8("pushButton_AgregarResolucion"))
        self.horizontalLayout_2.addWidget(self.pushButton_AgregarResolucion)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        self.gridLayout_3.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.groupBox_DatosResolucion = QtGui.QGroupBox(SubVentanaResoluciones)
        self.groupBox_DatosResolucion.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_DatosResolucion.setObjectName(_fromUtf8("groupBox_DatosResolucion"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_DatosResolucion)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_GuardarResolucion = QtGui.QPushButton(self.groupBox_DatosResolucion)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_GuardarResolucion.setIcon(icon2)
        self.pushButton_GuardarResolucion.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_GuardarResolucion.setFlat(True)
        self.pushButton_GuardarResolucion.setObjectName(_fromUtf8("pushButton_GuardarResolucion"))
        self.horizontalLayout.addWidget(self.pushButton_GuardarResolucion)
        self.pushButton_BorrarResolucion = QtGui.QPushButton(self.groupBox_DatosResolucion)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/eraser-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_BorrarResolucion.setIcon(icon3)
        self.pushButton_BorrarResolucion.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_BorrarResolucion.setFlat(True)
        self.pushButton_BorrarResolucion.setObjectName(_fromUtf8("pushButton_BorrarResolucion"))
        self.horizontalLayout.addWidget(self.pushButton_BorrarResolucion)
        self.pushButton_Cancelar = QtGui.QPushButton(self.groupBox_DatosResolucion)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/uncheck.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Cancelar.setIcon(icon4)
        self.pushButton_Cancelar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Cancelar.setFlat(True)
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.horizontalLayout.addWidget(self.pushButton_Cancelar)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.textEdit_Resolucion = QtGui.QTextEdit(self.groupBox_DatosResolucion)
        self.textEdit_Resolucion.setMaximumSize(QtCore.QSize(16777215, 50))
        self.textEdit_Resolucion.setObjectName(_fromUtf8("textEdit_Resolucion"))
        self.gridLayout_2.addWidget(self.textEdit_Resolucion, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_DatosResolucion)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_DatosResolucion, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 0, 1, 1)

        self.retranslateUi(SubVentanaResoluciones)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaResoluciones)
        SubVentanaResoluciones.setTabOrder(self.lineEdit_Buscar, self.tableWidget_ListadeResoluciones)
        SubVentanaResoluciones.setTabOrder(self.tableWidget_ListadeResoluciones, self.pushButton_AgregarResolucion)
        SubVentanaResoluciones.setTabOrder(self.pushButton_AgregarResolucion, self.pushButton_GuardarResolucion)
        SubVentanaResoluciones.setTabOrder(self.pushButton_GuardarResolucion, self.pushButton_BorrarResolucion)
        SubVentanaResoluciones.setTabOrder(self.pushButton_BorrarResolucion, self.pushButton_Cancelar)

    def retranslateUi(self, SubVentanaResoluciones):
        SubVentanaResoluciones.setWindowTitle(_translate("SubVentanaResoluciones", "Administracion de Resoluciones", None))
        self.groupBox_4.setTitle(_translate("SubVentanaResoluciones", "Lista de Resoluciones", None))
        self.label_3.setText(_translate("SubVentanaResoluciones", "Busqueda:", None))
        item = self.tableWidget_ListadeResoluciones.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaResoluciones", "Resolucion", None))
        self.pushButton_AgregarResolucion.setToolTip(_translate("SubVentanaResoluciones", "Nueva Empresa", None))
        self.pushButton_AgregarResolucion.setText(_translate("SubVentanaResoluciones", "Agregar", None))
        self.groupBox_DatosResolucion.setTitle(_translate("SubVentanaResoluciones", "Datos de la Resolucion", None))
        self.pushButton_GuardarResolucion.setToolTip(_translate("SubVentanaResoluciones", "Guardar Empresa", None))
        self.pushButton_GuardarResolucion.setText(_translate("SubVentanaResoluciones", "Guardar", None))
        self.pushButton_BorrarResolucion.setToolTip(_translate("SubVentanaResoluciones", "Borrar Empresa", None))
        self.pushButton_BorrarResolucion.setText(_translate("SubVentanaResoluciones", "Borrar", None))
        self.pushButton_Cancelar.setToolTip(_translate("SubVentanaResoluciones", "Cancelar Edicion", None))
        self.pushButton_Cancelar.setText(_translate("SubVentanaResoluciones", "Cancelar", None))
        self.label_2.setText(_translate("SubVentanaResoluciones", "Resolucion:", None))

import recursos_rc
