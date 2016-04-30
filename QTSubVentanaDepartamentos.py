# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaDepartamentos.ui'
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

class Ui_SubVentanaDepartamentos(object):
    def setupUi(self, SubVentanaDepartamentos):
        SubVentanaDepartamentos.setObjectName(_fromUtf8("SubVentanaDepartamentos"))
        SubVentanaDepartamentos.resize(338, 505)
        SubVentanaDepartamentos.setMinimumSize(QtCore.QSize(338, 505))
        SubVentanaDepartamentos.setMaximumSize(QtCore.QSize(338, 505))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Departamentos3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubVentanaDepartamentos.setWindowIcon(icon)
        SubVentanaDepartamentos.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout_2 = QtGui.QGridLayout(SubVentanaDepartamentos)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_4 = QtGui.QGroupBox(SubVentanaDepartamentos)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tableWidget_ListadeDepartamentos = QtGui.QTableWidget(self.groupBox_4)
        self.tableWidget_ListadeDepartamentos.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidget_ListadeDepartamentos.setStyleSheet(_fromUtf8(""))
        self.tableWidget_ListadeDepartamentos.setObjectName(_fromUtf8("tableWidget_ListadeDepartamentos"))
        self.tableWidget_ListadeDepartamentos.setColumnCount(1)
        self.tableWidget_ListadeDepartamentos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ListadeDepartamentos.setHorizontalHeaderItem(0, item)
        self.gridLayout_3.addWidget(self.tableWidget_ListadeDepartamentos, 1, 0, 1, 3)
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
        self.lineEdit_Buscar = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_Buscar.setObjectName(_fromUtf8("lineEdit_Buscar"))
        self.gridLayout_3.addWidget(self.lineEdit_Buscar, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_DatosDepartamento = QtGui.QGroupBox(SubVentanaDepartamentos)
        self.groupBox_DatosDepartamento.setObjectName(_fromUtf8("groupBox_DatosDepartamento"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_DatosDepartamento)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.groupBox_DatosDepartamento)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_Nombre = QtGui.QLineEdit(self.groupBox_DatosDepartamento)
        self.lineEdit_Nombre.setObjectName(_fromUtf8("lineEdit_Nombre"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_Nombre)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_Guardar = QtGui.QPushButton(self.groupBox_DatosDepartamento)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Guardar.setIcon(icon2)
        self.pushButton_Guardar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Guardar.setFlat(True)
        self.pushButton_Guardar.setObjectName(_fromUtf8("pushButton_Guardar"))
        self.horizontalLayout.addWidget(self.pushButton_Guardar)
        self.pushButton_Borrar = QtGui.QPushButton(self.groupBox_DatosDepartamento)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/eraser-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Borrar.setIcon(icon3)
        self.pushButton_Borrar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Borrar.setFlat(True)
        self.pushButton_Borrar.setObjectName(_fromUtf8("pushButton_Borrar"))
        self.horizontalLayout.addWidget(self.pushButton_Borrar)
        self.pushButton_Cancelar = QtGui.QPushButton(self.groupBox_DatosDepartamento)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/uncheck.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Cancelar.setIcon(icon4)
        self.pushButton_Cancelar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Cancelar.setFlat(True)
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.horizontalLayout.addWidget(self.pushButton_Cancelar)
        self.formLayout.setLayout(4, QtGui.QFormLayout.SpanningRole, self.horizontalLayout)
        self.lineEdit_Correo = QtGui.QLineEdit(self.groupBox_DatosDepartamento)
        self.lineEdit_Correo.setObjectName(_fromUtf8("lineEdit_Correo"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_Correo)
        self.label = QtGui.QLabel(self.groupBox_DatosDepartamento)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.label_4 = QtGui.QLabel(self.groupBox_DatosDepartamento)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_Encargado = QtGui.QLineEdit(self.groupBox_DatosDepartamento)
        self.lineEdit_Encargado.setMaxLength(100)
        self.lineEdit_Encargado.setObjectName(_fromUtf8("lineEdit_Encargado"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_Encargado)
        self.label_5 = QtGui.QLabel(self.groupBox_DatosDepartamento)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_Telefono = QtGui.QLineEdit(self.groupBox_DatosDepartamento)
        self.lineEdit_Telefono.setMaxLength(50)
        self.lineEdit_Telefono.setObjectName(_fromUtf8("lineEdit_Telefono"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_Telefono)
        self.gridLayout_2.addWidget(self.groupBox_DatosDepartamento, 1, 0, 1, 1)

        self.retranslateUi(SubVentanaDepartamentos)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaDepartamentos)
        SubVentanaDepartamentos.setTabOrder(self.lineEdit_Buscar, self.tableWidget_ListadeDepartamentos)
        SubVentanaDepartamentos.setTabOrder(self.tableWidget_ListadeDepartamentos, self.pushButton_Agregar)
        SubVentanaDepartamentos.setTabOrder(self.pushButton_Agregar, self.lineEdit_Nombre)
        SubVentanaDepartamentos.setTabOrder(self.lineEdit_Nombre, self.lineEdit_Correo)
        SubVentanaDepartamentos.setTabOrder(self.lineEdit_Correo, self.lineEdit_Encargado)
        SubVentanaDepartamentos.setTabOrder(self.lineEdit_Encargado, self.lineEdit_Telefono)
        SubVentanaDepartamentos.setTabOrder(self.lineEdit_Telefono, self.pushButton_Guardar)
        SubVentanaDepartamentos.setTabOrder(self.pushButton_Guardar, self.pushButton_Borrar)
        SubVentanaDepartamentos.setTabOrder(self.pushButton_Borrar, self.pushButton_Cancelar)

    def retranslateUi(self, SubVentanaDepartamentos):
        SubVentanaDepartamentos.setWindowTitle(_translate("SubVentanaDepartamentos", "Administrar Departamentos", None))
        self.groupBox_4.setTitle(_translate("SubVentanaDepartamentos", "Lista de Departamentos", None))
        item = self.tableWidget_ListadeDepartamentos.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaDepartamentos", "Descripcion", None))
        self.pushButton_Agregar.setToolTip(_translate("SubVentanaDepartamentos", "Nuevo Departamento", None))
        self.pushButton_Agregar.setText(_translate("SubVentanaDepartamentos", "Agregar", None))
        self.label_3.setText(_translate("SubVentanaDepartamentos", "Buscar:", None))
        self.groupBox_DatosDepartamento.setTitle(_translate("SubVentanaDepartamentos", "Datos del Departamento", None))
        self.label_2.setText(_translate("SubVentanaDepartamentos", "Nombre:", None))
        self.pushButton_Guardar.setToolTip(_translate("SubVentanaDepartamentos", "Guardar Departamento", None))
        self.pushButton_Guardar.setText(_translate("SubVentanaDepartamentos", "Guardar", None))
        self.pushButton_Borrar.setToolTip(_translate("SubVentanaDepartamentos", "Borrar Departamento ", None))
        self.pushButton_Borrar.setText(_translate("SubVentanaDepartamentos", "Borrar", None))
        self.pushButton_Cancelar.setToolTip(_translate("SubVentanaDepartamentos", "Cancelar Edicion", None))
        self.pushButton_Cancelar.setText(_translate("SubVentanaDepartamentos", "Cancelar", None))
        self.label.setText(_translate("SubVentanaDepartamentos", "Correo:", None))
        self.label_4.setText(_translate("SubVentanaDepartamentos", "Encargado:", None))
        self.label_5.setText(_translate("SubVentanaDepartamentos", "Telefono:", None))

import recursos_rc
