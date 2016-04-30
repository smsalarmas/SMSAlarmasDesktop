# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaEmpresas.ui'
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

class Ui_SubVentanaEmpresas(object):
    def setupUi(self, SubVentanaEmpresas):
        SubVentanaEmpresas.setObjectName(_fromUtf8("SubVentanaEmpresas"))
        SubVentanaEmpresas.resize(700, 500)
        SubVentanaEmpresas.setMinimumSize(QtCore.QSize(700, 500))
        SubVentanaEmpresas.setMaximumSize(QtCore.QSize(700, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Empresas.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubVentanaEmpresas.setWindowIcon(icon)
        SubVentanaEmpresas.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout_5 = QtGui.QGridLayout(SubVentanaEmpresas)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.groupBox_4 = QtGui.QGroupBox(SubVentanaEmpresas)
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)
        self.lineEdit_Buscar = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_Buscar.setObjectName(_fromUtf8("lineEdit_Buscar"))
        self.gridLayout_3.addWidget(self.lineEdit_Buscar, 1, 1, 1, 1)
        self.tableWidget_ListadeEmpresas = QtGui.QTableWidget(self.groupBox_4)
        self.tableWidget_ListadeEmpresas.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidget_ListadeEmpresas.setStyleSheet(_fromUtf8(""))
        self.tableWidget_ListadeEmpresas.setObjectName(_fromUtf8("tableWidget_ListadeEmpresas"))
        self.tableWidget_ListadeEmpresas.setColumnCount(3)
        self.tableWidget_ListadeEmpresas.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ListadeEmpresas.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ListadeEmpresas.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ListadeEmpresas.setHorizontalHeaderItem(2, item)
        self.gridLayout_3.addWidget(self.tableWidget_ListadeEmpresas, 2, 0, 1, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_AgregarEmpresa = QtGui.QPushButton(self.groupBox_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/4-Icone-plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AgregarEmpresa.setIcon(icon1)
        self.pushButton_AgregarEmpresa.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_AgregarEmpresa.setFlat(True)
        self.pushButton_AgregarEmpresa.setObjectName(_fromUtf8("pushButton_AgregarEmpresa"))
        self.horizontalLayout_2.addWidget(self.pushButton_AgregarEmpresa)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 3, 0, 1, 2)
        self.gridLayout_5.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_DatosEmpresa = QtGui.QGroupBox(SubVentanaEmpresas)
        self.groupBox_DatosEmpresa.setObjectName(_fromUtf8("groupBox_DatosEmpresa"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_DatosEmpresa)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.comboBox_Prefijo = QtGui.QComboBox(self.groupBox_DatosEmpresa)
        self.comboBox_Prefijo.setObjectName(_fromUtf8("comboBox_Prefijo"))
        self.gridLayout_2.addWidget(self.comboBox_Prefijo, 4, 1, 1, 1)
        self.spinBox_RangoDesde = QtGui.QSpinBox(self.groupBox_DatosEmpresa)
        self.spinBox_RangoDesde.setMaximum(999999)
        self.spinBox_RangoDesde.setObjectName(_fromUtf8("spinBox_RangoDesde"))
        self.gridLayout_2.addWidget(self.spinBox_RangoDesde, 4, 2, 1, 1)
        self.spinBox_RangoHasta = QtGui.QSpinBox(self.groupBox_DatosEmpresa)
        self.spinBox_RangoHasta.setMaximum(999999)
        self.spinBox_RangoHasta.setObjectName(_fromUtf8("spinBox_RangoHasta"))
        self.gridLayout_2.addWidget(self.spinBox_RangoHasta, 4, 3, 1, 1)
        self.label_18 = QtGui.QLabel(self.groupBox_DatosEmpresa)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_2.addWidget(self.label_18, 4, 0, 1, 1)
        self.pushButton_AgregarPrefijo = QtGui.QPushButton(self.groupBox_DatosEmpresa)
        self.pushButton_AgregarPrefijo.setMinimumSize(QtCore.QSize(20, 0))
        self.pushButton_AgregarPrefijo.setMaximumSize(QtCore.QSize(20, 16777215))
        self.pushButton_AgregarPrefijo.setText(_fromUtf8(""))
        self.pushButton_AgregarPrefijo.setIcon(icon1)
        self.pushButton_AgregarPrefijo.setIconSize(QtCore.QSize(17, 17))
        self.pushButton_AgregarPrefijo.setFlat(True)
        self.pushButton_AgregarPrefijo.setObjectName(_fromUtf8("pushButton_AgregarPrefijo"))
        self.gridLayout_2.addWidget(self.pushButton_AgregarPrefijo, 4, 4, 1, 1)
        self.tableWidget_PrefijoRangos = QtGui.QTableWidget(self.groupBox_DatosEmpresa)
        self.tableWidget_PrefijoRangos.setObjectName(_fromUtf8("tableWidget_PrefijoRangos"))
        self.tableWidget_PrefijoRangos.setColumnCount(4)
        self.tableWidget_PrefijoRangos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_PrefijoRangos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_PrefijoRangos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_PrefijoRangos.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_PrefijoRangos.setHorizontalHeaderItem(3, item)
        self.gridLayout_2.addWidget(self.tableWidget_PrefijoRangos, 5, 0, 1, 5)
        self.scrollArea = QtGui.QScrollArea(self.groupBox_DatosEmpresa)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 285, 446))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_6 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.widget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_Longitud = QtGui.QLineEdit(self.widget)
        self.lineEdit_Longitud.setObjectName(_fromUtf8("lineEdit_Longitud"))
        self.gridLayout.addWidget(self.lineEdit_Longitud, 10, 1, 1, 4)
        self.comboBox_SonidoPendiente = QtGui.QComboBox(self.widget)
        self.comboBox_SonidoPendiente.setObjectName(_fromUtf8("comboBox_SonidoPendiente"))
        self.comboBox_SonidoPendiente.addItem(_fromUtf8(""))
        self.comboBox_SonidoPendiente.addItem(_fromUtf8(""))
        self.comboBox_SonidoPendiente.addItem(_fromUtf8(""))
        self.comboBox_SonidoPendiente.addItem(_fromUtf8(""))
        self.comboBox_SonidoPendiente.addItem(_fromUtf8(""))
        self.comboBox_SonidoPendiente.addItem(_fromUtf8(""))
        self.comboBox_SonidoPendiente.addItem(_fromUtf8(""))
        self.comboBox_SonidoPendiente.addItem(_fromUtf8(""))
        self.comboBox_SonidoPendiente.addItem(_fromUtf8(""))
        self.comboBox_SonidoPendiente.addItem(_fromUtf8(""))
        self.comboBox_SonidoPendiente.addItem(_fromUtf8(""))
        self.comboBox_SonidoPendiente.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_SonidoPendiente, 11, 1, 1, 4)
        self.lineEdit_RepClave = QtGui.QLineEdit(self.widget)
        self.lineEdit_RepClave.setObjectName(_fromUtf8("lineEdit_RepClave"))
        self.gridLayout.addWidget(self.lineEdit_RepClave, 8, 1, 1, 4)
        self.lineEdit_Latitud = QtGui.QLineEdit(self.widget)
        self.lineEdit_Latitud.setObjectName(_fromUtf8("lineEdit_Latitud"))
        self.gridLayout.addWidget(self.lineEdit_Latitud, 9, 1, 1, 4)
        self.lineEdit_Nombre = QtGui.QLineEdit(self.widget)
        self.lineEdit_Nombre.setObjectName(_fromUtf8("lineEdit_Nombre"))
        self.gridLayout.addWidget(self.lineEdit_Nombre, 1, 1, 1, 4)
        self.lineEdit_RIF = QtGui.QLineEdit(self.widget)
        self.lineEdit_RIF.setObjectName(_fromUtf8("lineEdit_RIF"))
        self.gridLayout.addWidget(self.lineEdit_RIF, 0, 1, 1, 4)
        self.lineEdit_Direccion = QtGui.QLineEdit(self.widget)
        self.lineEdit_Direccion.setMaxLength(100)
        self.lineEdit_Direccion.setObjectName(_fromUtf8("lineEdit_Direccion"))
        self.gridLayout.addWidget(self.lineEdit_Direccion, 2, 1, 1, 4)
        self.lineEdit_Telefono = QtGui.QLineEdit(self.widget)
        self.lineEdit_Telefono.setObjectName(_fromUtf8("lineEdit_Telefono"))
        self.gridLayout.addWidget(self.lineEdit_Telefono, 3, 1, 1, 4)
        self.lineEdit_Usuario = QtGui.QLineEdit(self.widget)
        self.lineEdit_Usuario.setObjectName(_fromUtf8("lineEdit_Usuario"))
        self.gridLayout.addWidget(self.lineEdit_Usuario, 6, 1, 1, 4)
        self.lineEdit_Clave = QtGui.QLineEdit(self.widget)
        self.lineEdit_Clave.setObjectName(_fromUtf8("lineEdit_Clave"))
        self.gridLayout.addWidget(self.lineEdit_Clave, 7, 1, 1, 4)
        self.lineEdit_Correo = QtGui.QLineEdit(self.widget)
        self.lineEdit_Correo.setObjectName(_fromUtf8("lineEdit_Correo"))
        self.gridLayout.addWidget(self.lineEdit_Correo, 4, 1, 1, 4)
        self.lineEdit_Web = QtGui.QLineEdit(self.widget)
        self.lineEdit_Web.setObjectName(_fromUtf8("lineEdit_Web"))
        self.gridLayout.addWidget(self.lineEdit_Web, 5, 1, 1, 4)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.widget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 5, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.widget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 7, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.widget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 10, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.widget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 11, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.widget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)
        self.label_17 = QtGui.QLabel(self.widget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout.addWidget(self.label_17, 14, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.widget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout.addWidget(self.label_15, 12, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.widget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout.addWidget(self.label_16, 13, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 15, 0, 1, 1)
        self.lineEdit_CorreosHM = QtGui.QLineEdit(self.widget)
        self.lineEdit_CorreosHM.setObjectName(_fromUtf8("lineEdit_CorreosHM"))
        self.gridLayout.addWidget(self.lineEdit_CorreosHM, 14, 1, 1, 4)
        self.comboBox_EmpresaMonitorea = QtGui.QComboBox(self.widget)
        self.comboBox_EmpresaMonitorea.setObjectName(_fromUtf8("comboBox_EmpresaMonitorea"))
        self.gridLayout.addWidget(self.comboBox_EmpresaMonitorea, 15, 1, 1, 4)
        self.comboBox_HombreMuerto = QtGui.QComboBox(self.widget)
        self.comboBox_HombreMuerto.setObjectName(_fromUtf8("comboBox_HombreMuerto"))
        self.comboBox_HombreMuerto.addItem(_fromUtf8(""))
        self.comboBox_HombreMuerto.addItem(_fromUtf8(""))
        self.comboBox_HombreMuerto.addItem(_fromUtf8(""))
        self.comboBox_HombreMuerto.addItem(_fromUtf8(""))
        self.comboBox_HombreMuerto.addItem(_fromUtf8(""))
        self.comboBox_HombreMuerto.addItem(_fromUtf8(""))
        self.comboBox_HombreMuerto.addItem(_fromUtf8(""))
        self.comboBox_HombreMuerto.addItem(_fromUtf8(""))
        self.comboBox_HombreMuerto.addItem(_fromUtf8(""))
        self.comboBox_HombreMuerto.addItem(_fromUtf8(""))
        self.comboBox_HombreMuerto.addItem(_fromUtf8(""))
        self.comboBox_HombreMuerto.addItem(_fromUtf8(""))
        self.comboBox_HombreMuerto.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_HombreMuerto, 12, 1, 1, 4)
        self.comboBox_NotificacionHM = QtGui.QComboBox(self.widget)
        self.comboBox_NotificacionHM.setObjectName(_fromUtf8("comboBox_NotificacionHM"))
        self.comboBox_NotificacionHM.addItem(_fromUtf8(""))
        self.comboBox_NotificacionHM.addItem(_fromUtf8(""))
        self.comboBox_NotificacionHM.addItem(_fromUtf8(""))
        self.comboBox_NotificacionHM.addItem(_fromUtf8(""))
        self.comboBox_NotificacionHM.addItem(_fromUtf8(""))
        self.comboBox_NotificacionHM.addItem(_fromUtf8(""))
        self.comboBox_NotificacionHM.addItem(_fromUtf8(""))
        self.comboBox_NotificacionHM.addItem(_fromUtf8(""))
        self.comboBox_NotificacionHM.addItem(_fromUtf8(""))
        self.comboBox_NotificacionHM.addItem(_fromUtf8(""))
        self.comboBox_NotificacionHM.addItem(_fromUtf8(""))
        self.comboBox_NotificacionHM.addItem(_fromUtf8(""))
        self.comboBox_NotificacionHM.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_NotificacionHM, 13, 1, 1, 4)
        self.gridLayout_6.addWidget(self.widget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 2, 0, 1, 5)
        self.groupBox = QtGui.QGroupBox(self.groupBox_DatosEmpresa)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setMargin(2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_GuardarEmpresas = QtGui.QPushButton(self.groupBox)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_GuardarEmpresas.setIcon(icon2)
        self.pushButton_GuardarEmpresas.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_GuardarEmpresas.setFlat(True)
        self.pushButton_GuardarEmpresas.setObjectName(_fromUtf8("pushButton_GuardarEmpresas"))
        self.horizontalLayout.addWidget(self.pushButton_GuardarEmpresas)
        self.pushButton_BorrarEmpresas = QtGui.QPushButton(self.groupBox)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/eraser-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_BorrarEmpresas.setIcon(icon3)
        self.pushButton_BorrarEmpresas.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_BorrarEmpresas.setFlat(True)
        self.pushButton_BorrarEmpresas.setObjectName(_fromUtf8("pushButton_BorrarEmpresas"))
        self.horizontalLayout.addWidget(self.pushButton_BorrarEmpresas)
        self.pushButton_Cancelar = QtGui.QPushButton(self.groupBox)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/uncheck.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Cancelar.setIcon(icon4)
        self.pushButton_Cancelar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Cancelar.setFlat(True)
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.horizontalLayout.addWidget(self.pushButton_Cancelar)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 1, 1, 4)
        self.gridLayout_2.addWidget(self.groupBox, 6, 0, 1, 5)
        self.gridLayout_5.addWidget(self.groupBox_DatosEmpresa, 0, 1, 1, 1)

        self.retranslateUi(SubVentanaEmpresas)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaEmpresas)
        SubVentanaEmpresas.setTabOrder(self.lineEdit_Buscar, self.tableWidget_ListadeEmpresas)
        SubVentanaEmpresas.setTabOrder(self.tableWidget_ListadeEmpresas, self.pushButton_AgregarEmpresa)
        SubVentanaEmpresas.setTabOrder(self.pushButton_AgregarEmpresa, self.lineEdit_RIF)
        SubVentanaEmpresas.setTabOrder(self.lineEdit_RIF, self.lineEdit_Nombre)
        SubVentanaEmpresas.setTabOrder(self.lineEdit_Nombre, self.lineEdit_Direccion)
        SubVentanaEmpresas.setTabOrder(self.lineEdit_Direccion, self.lineEdit_Telefono)
        SubVentanaEmpresas.setTabOrder(self.lineEdit_Telefono, self.lineEdit_Correo)
        SubVentanaEmpresas.setTabOrder(self.lineEdit_Correo, self.lineEdit_Web)
        SubVentanaEmpresas.setTabOrder(self.lineEdit_Web, self.lineEdit_Usuario)
        SubVentanaEmpresas.setTabOrder(self.lineEdit_Usuario, self.lineEdit_Clave)
        SubVentanaEmpresas.setTabOrder(self.lineEdit_Clave, self.lineEdit_RepClave)
        SubVentanaEmpresas.setTabOrder(self.lineEdit_RepClave, self.lineEdit_Latitud)
        SubVentanaEmpresas.setTabOrder(self.lineEdit_Latitud, self.lineEdit_Longitud)
        SubVentanaEmpresas.setTabOrder(self.lineEdit_Longitud, self.comboBox_SonidoPendiente)
        SubVentanaEmpresas.setTabOrder(self.comboBox_SonidoPendiente, self.comboBox_HombreMuerto)
        SubVentanaEmpresas.setTabOrder(self.comboBox_HombreMuerto, self.comboBox_NotificacionHM)
        SubVentanaEmpresas.setTabOrder(self.comboBox_NotificacionHM, self.pushButton_GuardarEmpresas)
        SubVentanaEmpresas.setTabOrder(self.pushButton_GuardarEmpresas, self.pushButton_BorrarEmpresas)
        SubVentanaEmpresas.setTabOrder(self.pushButton_BorrarEmpresas, self.pushButton_Cancelar)

    def retranslateUi(self, SubVentanaEmpresas):
        SubVentanaEmpresas.setWindowTitle(_translate("SubVentanaEmpresas", "Administracion de Empresas", None))
        self.groupBox_4.setTitle(_translate("SubVentanaEmpresas", "Lista de Empresas", None))
        self.label_3.setText(_translate("SubVentanaEmpresas", "Buscar:", None))
        self.lineEdit_Buscar.setToolTip(_translate("SubVentanaEmpresas", "Buscar Empresas", None))
        item = self.tableWidget_ListadeEmpresas.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaEmpresas", "Nombre", None))
        item = self.tableWidget_ListadeEmpresas.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaEmpresas", "Correo", None))
        item = self.tableWidget_ListadeEmpresas.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaEmpresas", "Telefonos", None))
        self.pushButton_AgregarEmpresa.setToolTip(_translate("SubVentanaEmpresas", "Nueva Empresa", None))
        self.pushButton_AgregarEmpresa.setText(_translate("SubVentanaEmpresas", "Agregar", None))
        self.groupBox_DatosEmpresa.setTitle(_translate("SubVentanaEmpresas", "Datos de la Empresa", None))
        self.comboBox_Prefijo.setToolTip(_translate("SubVentanaEmpresas", "Prefijo", None))
        self.spinBox_RangoDesde.setToolTip(_translate("SubVentanaEmpresas", "Desde la Cuenta", None))
        self.spinBox_RangoHasta.setToolTip(_translate("SubVentanaEmpresas", "Hasta la Cuenta", None))
        self.label_18.setText(_translate("SubVentanaEmpresas", "Prefijos - Rango", None))
        item = self.tableWidget_PrefijoRangos.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaEmpresas", "Prefijo", None))
        item = self.tableWidget_PrefijoRangos.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaEmpresas", "Desde", None))
        item = self.tableWidget_PrefijoRangos.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaEmpresas", "Hasta", None))
        item = self.tableWidget_PrefijoRangos.horizontalHeaderItem(3)
        item.setText(_translate("SubVentanaEmpresas", "Borrar", None))
        self.lineEdit_Longitud.setToolTip(_translate("SubVentanaEmpresas", "Coordenadas Para Mapa  ", None))
        self.comboBox_SonidoPendiente.setToolTip(_translate("SubVentanaEmpresas", "Tiempo Alerta Señales Pendientes  ", None))
        self.comboBox_SonidoPendiente.setItemText(0, _translate("SubVentanaEmpresas", "5 Minutos", None))
        self.comboBox_SonidoPendiente.setItemText(1, _translate("SubVentanaEmpresas", "10 Minutos", None))
        self.comboBox_SonidoPendiente.setItemText(2, _translate("SubVentanaEmpresas", "15 Minutos", None))
        self.comboBox_SonidoPendiente.setItemText(3, _translate("SubVentanaEmpresas", "20 Minutos", None))
        self.comboBox_SonidoPendiente.setItemText(4, _translate("SubVentanaEmpresas", "25 Minutos", None))
        self.comboBox_SonidoPendiente.setItemText(5, _translate("SubVentanaEmpresas", "30 Minutos", None))
        self.comboBox_SonidoPendiente.setItemText(6, _translate("SubVentanaEmpresas", "35 Minutos", None))
        self.comboBox_SonidoPendiente.setItemText(7, _translate("SubVentanaEmpresas", "40 Minutos", None))
        self.comboBox_SonidoPendiente.setItemText(8, _translate("SubVentanaEmpresas", "45 Minutos", None))
        self.comboBox_SonidoPendiente.setItemText(9, _translate("SubVentanaEmpresas", "50 Minutos", None))
        self.comboBox_SonidoPendiente.setItemText(10, _translate("SubVentanaEmpresas", "55 Minutos", None))
        self.comboBox_SonidoPendiente.setItemText(11, _translate("SubVentanaEmpresas", "60 Minutos", None))
        self.lineEdit_RepClave.setToolTip(_translate("SubVentanaEmpresas", "Repetir Password Modulo Web  ", None))
        self.lineEdit_Latitud.setToolTip(_translate("SubVentanaEmpresas", "Coordenadas Para Mapa  ", None))
        self.lineEdit_Nombre.setToolTip(_translate("SubVentanaEmpresas", "Nombre de Empresa  ", None))
        self.lineEdit_Direccion.setToolTip(_translate("SubVentanaEmpresas", "Direccion De la Empresa  ", None))
        self.lineEdit_Telefono.setToolTip(_translate("SubVentanaEmpresas", "Telefono de la Empresa  ", None))
        self.lineEdit_Usuario.setToolTip(_translate("SubVentanaEmpresas", "Usuario Modulo Web  ", None))
        self.lineEdit_Clave.setToolTip(_translate("SubVentanaEmpresas", "Password Modulo Web  ", None))
        self.lineEdit_Correo.setToolTip(_translate("SubVentanaEmpresas", "Correo de la Empresa  ", None))
        self.label_2.setText(_translate("SubVentanaEmpresas", "RIF / RUT", None))
        self.label_4.setText(_translate("SubVentanaEmpresas", "Nombre:", None))
        self.label_8.setText(_translate("SubVentanaEmpresas", "Direccion:", None))
        self.label_9.setText(_translate("SubVentanaEmpresas", "Telefono:", None))
        self.label_12.setText(_translate("SubVentanaEmpresas", "Pagina Web:", None))
        self.label_6.setText(_translate("SubVentanaEmpresas", "Email", None))
        self.label_10.setText(_translate("SubVentanaEmpresas", "Usuario:", None))
        self.label.setText(_translate("SubVentanaEmpresas", "Clave:", None))
        self.label_7.setText(_translate("SubVentanaEmpresas", "Repetir Clave:", None))
        self.label_13.setText(_translate("SubVentanaEmpresas", "Longitud:", None))
        self.label_14.setText(_translate("SubVentanaEmpresas", "Sonido Pendiente", None))
        self.label_11.setText(_translate("SubVentanaEmpresas", "Latitud:", None))
        self.label_17.setText(_translate("SubVentanaEmpresas", "Correos Hombre M", None))
        self.label_15.setText(_translate("SubVentanaEmpresas", "Hombre Muerto", None))
        self.label_16.setText(_translate("SubVentanaEmpresas", "Notificacion HM", None))
        self.label_5.setText(_translate("SubVentanaEmpresas", "¿Quien Monitorea?", None))
        self.lineEdit_CorreosHM.setToolTip(_translate("SubVentanaEmpresas", "Correos de la Empresa Separados por ( , )    ", None))
        self.lineEdit_CorreosHM.setPlaceholderText(_translate("SubVentanaEmpresas", "correo1@mail.com,correo2@mail.com", None))
        self.comboBox_HombreMuerto.setToolTip(_translate("SubVentanaEmpresas", "Tiempo en Minutos para señal de Hombre Muerto  ", None))
        self.comboBox_HombreMuerto.setItemText(0, _translate("SubVentanaEmpresas", "No Aplica", None))
        self.comboBox_HombreMuerto.setItemText(1, _translate("SubVentanaEmpresas", "5 Minutos", None))
        self.comboBox_HombreMuerto.setItemText(2, _translate("SubVentanaEmpresas", "10 Minutos", None))
        self.comboBox_HombreMuerto.setItemText(3, _translate("SubVentanaEmpresas", "15 Minutos", None))
        self.comboBox_HombreMuerto.setItemText(4, _translate("SubVentanaEmpresas", "20 Minutos", None))
        self.comboBox_HombreMuerto.setItemText(5, _translate("SubVentanaEmpresas", "25 Minutos", None))
        self.comboBox_HombreMuerto.setItemText(6, _translate("SubVentanaEmpresas", "30 Minutos", None))
        self.comboBox_HombreMuerto.setItemText(7, _translate("SubVentanaEmpresas", "35 Minutos", None))
        self.comboBox_HombreMuerto.setItemText(8, _translate("SubVentanaEmpresas", "40 Minutos", None))
        self.comboBox_HombreMuerto.setItemText(9, _translate("SubVentanaEmpresas", "45 Minutos", None))
        self.comboBox_HombreMuerto.setItemText(10, _translate("SubVentanaEmpresas", "50 Minutos", None))
        self.comboBox_HombreMuerto.setItemText(11, _translate("SubVentanaEmpresas", "55 Minutos", None))
        self.comboBox_HombreMuerto.setItemText(12, _translate("SubVentanaEmpresas", "60 Minutos", None))
        self.comboBox_NotificacionHM.setItemText(0, _translate("SubVentanaEmpresas", "No Aplica", None))
        self.comboBox_NotificacionHM.setItemText(1, _translate("SubVentanaEmpresas", "5 Minutos", None))
        self.comboBox_NotificacionHM.setItemText(2, _translate("SubVentanaEmpresas", "10 Minutos", None))
        self.comboBox_NotificacionHM.setItemText(3, _translate("SubVentanaEmpresas", "15 Minutos", None))
        self.comboBox_NotificacionHM.setItemText(4, _translate("SubVentanaEmpresas", "20 Minutos", None))
        self.comboBox_NotificacionHM.setItemText(5, _translate("SubVentanaEmpresas", "25 Minutos", None))
        self.comboBox_NotificacionHM.setItemText(6, _translate("SubVentanaEmpresas", "30 Minutos", None))
        self.comboBox_NotificacionHM.setItemText(7, _translate("SubVentanaEmpresas", "35 Minutos", None))
        self.comboBox_NotificacionHM.setItemText(8, _translate("SubVentanaEmpresas", "40 Minutos", None))
        self.comboBox_NotificacionHM.setItemText(9, _translate("SubVentanaEmpresas", "45 Minutos", None))
        self.comboBox_NotificacionHM.setItemText(10, _translate("SubVentanaEmpresas", "50 Minutos", None))
        self.comboBox_NotificacionHM.setItemText(11, _translate("SubVentanaEmpresas", "55 Minutos", None))
        self.comboBox_NotificacionHM.setItemText(12, _translate("SubVentanaEmpresas", "60 Minutos", None))
        self.pushButton_GuardarEmpresas.setToolTip(_translate("SubVentanaEmpresas", "Guardar Empresa", None))
        self.pushButton_GuardarEmpresas.setText(_translate("SubVentanaEmpresas", "Guardar", None))
        self.pushButton_BorrarEmpresas.setToolTip(_translate("SubVentanaEmpresas", "Borrar Empresa", None))
        self.pushButton_BorrarEmpresas.setText(_translate("SubVentanaEmpresas", "Borrar", None))
        self.pushButton_Cancelar.setToolTip(_translate("SubVentanaEmpresas", "Cancelar Edicion", None))
        self.pushButton_Cancelar.setText(_translate("SubVentanaEmpresas", "Cancelar", None))

import recursos_rc
