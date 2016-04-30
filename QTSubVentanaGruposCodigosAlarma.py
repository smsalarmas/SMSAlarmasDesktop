# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaGruposCodigosAlarma.ui'
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

class Ui_SubVentanaGruposCodigosAlarma(object):
    def setupUi(self, SubVentanaGruposCodigosAlarma):
        SubVentanaGruposCodigosAlarma.setObjectName(_fromUtf8("SubVentanaGruposCodigosAlarma"))
        SubVentanaGruposCodigosAlarma.resize(338, 505)
        SubVentanaGruposCodigosAlarma.setMinimumSize(QtCore.QSize(338, 505))
        SubVentanaGruposCodigosAlarma.setMaximumSize(QtCore.QSize(338, 505))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Grupo_Codigo_Alarmas.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubVentanaGruposCodigosAlarma.setWindowIcon(icon)
        SubVentanaGruposCodigosAlarma.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout_2 = QtGui.QGridLayout(SubVentanaGruposCodigosAlarma)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_4 = QtGui.QGroupBox(SubVentanaGruposCodigosAlarma)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lineEdit_Buscar = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_Buscar.setObjectName(_fromUtf8("lineEdit_Buscar"))
        self.gridLayout_3.addWidget(self.lineEdit_Buscar, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.tableWidget_ListadeGruposCodigoAlarma = QtGui.QTableWidget(self.groupBox_4)
        self.tableWidget_ListadeGruposCodigoAlarma.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidget_ListadeGruposCodigoAlarma.setStyleSheet(_fromUtf8(""))
        self.tableWidget_ListadeGruposCodigoAlarma.setObjectName(_fromUtf8("tableWidget_ListadeGruposCodigoAlarma"))
        self.tableWidget_ListadeGruposCodigoAlarma.setColumnCount(1)
        self.tableWidget_ListadeGruposCodigoAlarma.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ListadeGruposCodigoAlarma.setHorizontalHeaderItem(0, item)
        self.gridLayout_3.addWidget(self.tableWidget_ListadeGruposCodigoAlarma, 1, 0, 1, 3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_Agregar = QtGui.QPushButton(self.groupBox_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/4-Icone-plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Agregar.setIcon(icon1)
        self.pushButton_Agregar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Agregar.setFlat(True)
        self.pushButton_Agregar.setObjectName(_fromUtf8("pushButton_Agregar"))
        self.horizontalLayout_2.addWidget(self.pushButton_Agregar)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 3)
        self.gridLayout_2.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_DatosGrupoCA = QtGui.QGroupBox(SubVentanaGruposCodigosAlarma)
        self.groupBox_DatosGrupoCA.setObjectName(_fromUtf8("groupBox_DatosGrupoCA"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_DatosGrupoCA)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.groupBox_DatosGrupoCA)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_Nombre = QtGui.QLineEdit(self.groupBox_DatosGrupoCA)
        self.lineEdit_Nombre.setObjectName(_fromUtf8("lineEdit_Nombre"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_Nombre)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_Guardar = QtGui.QPushButton(self.groupBox_DatosGrupoCA)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Guardar.setIcon(icon2)
        self.pushButton_Guardar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Guardar.setFlat(True)
        self.pushButton_Guardar.setObjectName(_fromUtf8("pushButton_Guardar"))
        self.horizontalLayout.addWidget(self.pushButton_Guardar)
        self.pushButton_Borrar = QtGui.QPushButton(self.groupBox_DatosGrupoCA)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/eraser-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Borrar.setIcon(icon3)
        self.pushButton_Borrar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Borrar.setFlat(True)
        self.pushButton_Borrar.setObjectName(_fromUtf8("pushButton_Borrar"))
        self.horizontalLayout.addWidget(self.pushButton_Borrar)
        self.pushButton_Cancelar = QtGui.QPushButton(self.groupBox_DatosGrupoCA)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/uncheck.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Cancelar.setIcon(icon4)
        self.pushButton_Cancelar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Cancelar.setFlat(True)
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.horizontalLayout.addWidget(self.pushButton_Cancelar)
        self.formLayout.setLayout(1, QtGui.QFormLayout.SpanningRole, self.horizontalLayout)
        self.gridLayout_2.addWidget(self.groupBox_DatosGrupoCA, 1, 0, 1, 1)

        self.retranslateUi(SubVentanaGruposCodigosAlarma)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaGruposCodigosAlarma)
        SubVentanaGruposCodigosAlarma.setTabOrder(self.lineEdit_Buscar, self.tableWidget_ListadeGruposCodigoAlarma)
        SubVentanaGruposCodigosAlarma.setTabOrder(self.tableWidget_ListadeGruposCodigoAlarma, self.pushButton_Agregar)
        SubVentanaGruposCodigosAlarma.setTabOrder(self.pushButton_Agregar, self.lineEdit_Nombre)
        SubVentanaGruposCodigosAlarma.setTabOrder(self.lineEdit_Nombre, self.pushButton_Guardar)
        SubVentanaGruposCodigosAlarma.setTabOrder(self.pushButton_Guardar, self.pushButton_Borrar)
        SubVentanaGruposCodigosAlarma.setTabOrder(self.pushButton_Borrar, self.pushButton_Cancelar)

    def retranslateUi(self, SubVentanaGruposCodigosAlarma):
        SubVentanaGruposCodigosAlarma.setWindowTitle(_translate("SubVentanaGruposCodigosAlarma", "Administrar Grupos de Codigos de Alarma", None))
        self.groupBox_4.setTitle(_translate("SubVentanaGruposCodigosAlarma", "Lista de Codigos de Alarma", None))
        self.label_3.setText(_translate("SubVentanaGruposCodigosAlarma", "Buscar:", None))
        item = self.tableWidget_ListadeGruposCodigoAlarma.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaGruposCodigosAlarma", "Descripcion", None))
        self.pushButton_Agregar.setToolTip(_translate("SubVentanaGruposCodigosAlarma", "Nuevo Grupo ", None))
        self.pushButton_Agregar.setText(_translate("SubVentanaGruposCodigosAlarma", "Agregar", None))
        self.groupBox_DatosGrupoCA.setTitle(_translate("SubVentanaGruposCodigosAlarma", "Datos del Codigo de Alarma", None))
        self.label_2.setText(_translate("SubVentanaGruposCodigosAlarma", "Descripcion", None))
        self.pushButton_Guardar.setToolTip(_translate("SubVentanaGruposCodigosAlarma", "Guardar Grupo ", None))
        self.pushButton_Guardar.setText(_translate("SubVentanaGruposCodigosAlarma", "Guardar", None))
        self.pushButton_Borrar.setToolTip(_translate("SubVentanaGruposCodigosAlarma", "Borrar Grupo ", None))
        self.pushButton_Borrar.setText(_translate("SubVentanaGruposCodigosAlarma", "Borrar", None))
        self.pushButton_Cancelar.setToolTip(_translate("SubVentanaGruposCodigosAlarma", "Cancelar Edicion", None))
        self.pushButton_Cancelar.setText(_translate("SubVentanaGruposCodigosAlarma", "Cancelar", None))

import recursos_rc
