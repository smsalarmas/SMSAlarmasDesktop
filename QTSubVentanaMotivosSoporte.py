# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaMotivosSoporte.ui'
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

class Ui_SubVentanaMotivosSoporte(object):
    def setupUi(self, SubVentanaMotivosSoporte):
        SubVentanaMotivosSoporte.setObjectName(_fromUtf8("SubVentanaMotivosSoporte"))
        SubVentanaMotivosSoporte.resize(628, 463)
        SubVentanaMotivosSoporte.setMinimumSize(QtCore.QSize(628, 463))
        SubVentanaMotivosSoporte.setMaximumSize(QtCore.QSize(628, 463))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Motivo_Soporte.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubVentanaMotivosSoporte.setWindowIcon(icon)
        SubVentanaMotivosSoporte.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout_2 = QtGui.QGridLayout(SubVentanaMotivosSoporte)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_DatosMotivoSoporte = QtGui.QGroupBox(SubVentanaMotivosSoporte)
        self.groupBox_DatosMotivoSoporte.setObjectName(_fromUtf8("groupBox_DatosMotivoSoporte"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_DatosMotivoSoporte)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.groupBox_DatosMotivoSoporte)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_MotivoSoporte = QtGui.QLineEdit(self.groupBox_DatosMotivoSoporte)
        self.lineEdit_MotivoSoporte.setObjectName(_fromUtf8("lineEdit_MotivoSoporte"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_MotivoSoporte)
        self.label = QtGui.QLabel(self.groupBox_DatosMotivoSoporte)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_GuardarMotivoSoporte = QtGui.QPushButton(self.groupBox_DatosMotivoSoporte)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_GuardarMotivoSoporte.setIcon(icon1)
        self.pushButton_GuardarMotivoSoporte.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_GuardarMotivoSoporte.setFlat(True)
        self.pushButton_GuardarMotivoSoporte.setObjectName(_fromUtf8("pushButton_GuardarMotivoSoporte"))
        self.horizontalLayout.addWidget(self.pushButton_GuardarMotivoSoporte)
        self.pushButton_BorrarMotivoSoporte = QtGui.QPushButton(self.groupBox_DatosMotivoSoporte)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/eraser-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_BorrarMotivoSoporte.setIcon(icon2)
        self.pushButton_BorrarMotivoSoporte.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_BorrarMotivoSoporte.setFlat(True)
        self.pushButton_BorrarMotivoSoporte.setObjectName(_fromUtf8("pushButton_BorrarMotivoSoporte"))
        self.horizontalLayout.addWidget(self.pushButton_BorrarMotivoSoporte)
        self.pushButton_Cancelar = QtGui.QPushButton(self.groupBox_DatosMotivoSoporte)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/uncheck.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Cancelar.setIcon(icon3)
        self.pushButton_Cancelar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Cancelar.setFlat(True)
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.horizontalLayout.addWidget(self.pushButton_Cancelar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.formLayout.setLayout(2, QtGui.QFormLayout.SpanningRole, self.horizontalLayout)
        self.comboBox_Departamento = QtGui.QComboBox(self.groupBox_DatosMotivoSoporte)
        self.comboBox_Departamento.setObjectName(_fromUtf8("comboBox_Departamento"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox_Departamento)
        self.gridLayout_2.addWidget(self.groupBox_DatosMotivoSoporte, 1, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(SubVentanaMotivosSoporte)
        self.groupBox_4.setMinimumSize(QtCore.QSize(600, 0))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lineEdit_Buscar = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_Buscar.setObjectName(_fromUtf8("lineEdit_Buscar"))
        self.gridLayout_3.addWidget(self.lineEdit_Buscar, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.tableWidget_ListadeMotivosSoporte = QtGui.QTableWidget(self.groupBox_4)
        self.tableWidget_ListadeMotivosSoporte.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidget_ListadeMotivosSoporte.setStyleSheet(_fromUtf8(""))
        self.tableWidget_ListadeMotivosSoporte.setObjectName(_fromUtf8("tableWidget_ListadeMotivosSoporte"))
        self.tableWidget_ListadeMotivosSoporte.setColumnCount(2)
        self.tableWidget_ListadeMotivosSoporte.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ListadeMotivosSoporte.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ListadeMotivosSoporte.setHorizontalHeaderItem(1, item)
        self.gridLayout_3.addWidget(self.tableWidget_ListadeMotivosSoporte, 1, 0, 1, 3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton_AgregarMotivoSoporte = QtGui.QPushButton(self.groupBox_4)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/4-Icone-plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AgregarMotivoSoporte.setIcon(icon4)
        self.pushButton_AgregarMotivoSoporte.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_AgregarMotivoSoporte.setFlat(True)
        self.pushButton_AgregarMotivoSoporte.setObjectName(_fromUtf8("pushButton_AgregarMotivoSoporte"))
        self.horizontalLayout_2.addWidget(self.pushButton_AgregarMotivoSoporte)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 3)
        self.gridLayout_2.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.retranslateUi(SubVentanaMotivosSoporte)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaMotivosSoporte)
        SubVentanaMotivosSoporte.setTabOrder(self.lineEdit_Buscar, self.tableWidget_ListadeMotivosSoporte)
        SubVentanaMotivosSoporte.setTabOrder(self.tableWidget_ListadeMotivosSoporte, self.pushButton_AgregarMotivoSoporte)
        SubVentanaMotivosSoporte.setTabOrder(self.pushButton_AgregarMotivoSoporte, self.lineEdit_MotivoSoporte)
        SubVentanaMotivosSoporte.setTabOrder(self.lineEdit_MotivoSoporte, self.pushButton_GuardarMotivoSoporte)
        SubVentanaMotivosSoporte.setTabOrder(self.pushButton_GuardarMotivoSoporte, self.pushButton_BorrarMotivoSoporte)
        SubVentanaMotivosSoporte.setTabOrder(self.pushButton_BorrarMotivoSoporte, self.pushButton_Cancelar)

    def retranslateUi(self, SubVentanaMotivosSoporte):
        SubVentanaMotivosSoporte.setWindowTitle(_translate("SubVentanaMotivosSoporte", "Administracion de Motivos de Soporte", None))
        self.groupBox_DatosMotivoSoporte.setTitle(_translate("SubVentanaMotivosSoporte", "Datos del Motivo", None))
        self.label_2.setText(_translate("SubVentanaMotivosSoporte", "Nombre:", None))
        self.label.setText(_translate("SubVentanaMotivosSoporte", "Departamento:", None))
        self.pushButton_GuardarMotivoSoporte.setToolTip(_translate("SubVentanaMotivosSoporte", "Guardar Empresa", None))
        self.pushButton_GuardarMotivoSoporte.setText(_translate("SubVentanaMotivosSoporte", "Guardar", None))
        self.pushButton_BorrarMotivoSoporte.setToolTip(_translate("SubVentanaMotivosSoporte", "Borrar Empresa", None))
        self.pushButton_BorrarMotivoSoporte.setText(_translate("SubVentanaMotivosSoporte", "Borrar", None))
        self.pushButton_Cancelar.setToolTip(_translate("SubVentanaMotivosSoporte", "Cancelar Edicion", None))
        self.pushButton_Cancelar.setText(_translate("SubVentanaMotivosSoporte", "Cancelar", None))
        self.groupBox_4.setTitle(_translate("SubVentanaMotivosSoporte", "Lista de Motivos de Soporte", None))
        self.label_3.setText(_translate("SubVentanaMotivosSoporte", "Buscar:", None))
        item = self.tableWidget_ListadeMotivosSoporte.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaMotivosSoporte", "Descripcion", None))
        item = self.tableWidget_ListadeMotivosSoporte.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaMotivosSoporte", "Departamento", None))
        self.pushButton_AgregarMotivoSoporte.setToolTip(_translate("SubVentanaMotivosSoporte", "Nueva Empresa", None))
        self.pushButton_AgregarMotivoSoporte.setText(_translate("SubVentanaMotivosSoporte", "Agregar", None))

import recursos_rc
