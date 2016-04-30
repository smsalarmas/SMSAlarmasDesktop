# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaModelosEquipos.ui'
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

class Ui_SubVentanaModelosEquipos(object):
    def setupUi(self, SubVentanaModelosEquipos):
        SubVentanaModelosEquipos.setObjectName(_fromUtf8("SubVentanaModelosEquipos"))
        SubVentanaModelosEquipos.resize(785, 560)
        SubVentanaModelosEquipos.setMinimumSize(QtCore.QSize(785, 560))
        SubVentanaModelosEquipos.setMaximumSize(QtCore.QSize(785, 564))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/codealarm.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubVentanaModelosEquipos.setWindowIcon(icon)
        SubVentanaModelosEquipos.setStyleSheet(_fromUtf8("QTableView {\n"
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
"}\n"
"\n"
""))
        self.gridLayout_2 = QtGui.QGridLayout(SubVentanaModelosEquipos)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_4 = QtGui.QGroupBox(SubVentanaModelosEquipos)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tableWidget_Lista = QtGui.QTableWidget(self.groupBox_4)
        self.tableWidget_Lista.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidget_Lista.setStyleSheet(_fromUtf8(""))
        self.tableWidget_Lista.setObjectName(_fromUtf8("tableWidget_Lista"))
        self.tableWidget_Lista.setColumnCount(3)
        self.tableWidget_Lista.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Lista.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Lista.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Lista.setHorizontalHeaderItem(2, item)
        self.gridLayout_3.addWidget(self.tableWidget_Lista, 1, 0, 1, 2)
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
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_Buscar = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_Buscar.setObjectName(_fromUtf8("lineEdit_Buscar"))
        self.gridLayout_3.addWidget(self.lineEdit_Buscar, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_4, 0, 0, 3, 1)
        self.groupBox_Datos = QtGui.QGroupBox(SubVentanaModelosEquipos)
        self.groupBox_Datos.setObjectName(_fromUtf8("groupBox_Datos"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_Datos)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self.groupBox_Datos)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_4.addWidget(self.line, 3, 0, 1, 2)
        self.NombreManualAyuda = QtGui.QLabel(self.groupBox)
        self.NombreManualAyuda.setObjectName(_fromUtf8("NombreManualAyuda"))
        self.gridLayout_4.addWidget(self.NombreManualAyuda, 2, 0, 1, 2)
        self.NombreManualUsuario = QtGui.QLabel(self.groupBox)
        self.NombreManualUsuario.setObjectName(_fromUtf8("NombreManualUsuario"))
        self.gridLayout_4.addWidget(self.NombreManualUsuario, 5, 0, 1, 2)
        self.NombreManualProgramacion = QtGui.QLabel(self.groupBox)
        self.NombreManualProgramacion.setObjectName(_fromUtf8("NombreManualProgramacion"))
        self.gridLayout_4.addWidget(self.NombreManualProgramacion, 8, 0, 1, 2)
        self.NombreManualConfiguracion = QtGui.QLabel(self.groupBox)
        self.NombreManualConfiguracion.setObjectName(_fromUtf8("NombreManualConfiguracion"))
        self.gridLayout_4.addWidget(self.NombreManualConfiguracion, 11, 0, 1, 2)
        self.line_2 = QtGui.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_4.addWidget(self.line_2, 6, 0, 1, 2)
        self.pushButton_BuscarManualUsuario = QtGui.QPushButton(self.groupBox)
        self.pushButton_BuscarManualUsuario.setObjectName(_fromUtf8("pushButton_BuscarManualUsuario"))
        self.gridLayout_4.addWidget(self.pushButton_BuscarManualUsuario, 4, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.pushButton_BuscarManualAyuda = QtGui.QPushButton(self.groupBox)
        self.pushButton_BuscarManualAyuda.setObjectName(_fromUtf8("pushButton_BuscarManualAyuda"))
        self.gridLayout_4.addWidget(self.pushButton_BuscarManualAyuda, 1, 1, 1, 1)
        self.pushButton_BuscarManualProgramacion = QtGui.QPushButton(self.groupBox)
        self.pushButton_BuscarManualProgramacion.setObjectName(_fromUtf8("pushButton_BuscarManualProgramacion"))
        self.gridLayout_4.addWidget(self.pushButton_BuscarManualProgramacion, 7, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_4.addWidget(self.label_8, 10, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_4.addWidget(self.label_7, 7, 0, 1, 1)
        self.pushButton_BuscarManualConfiguracion = QtGui.QPushButton(self.groupBox)
        self.pushButton_BuscarManualConfiguracion.setObjectName(_fromUtf8("pushButton_BuscarManualConfiguracion"))
        self.gridLayout_4.addWidget(self.pushButton_BuscarManualConfiguracion, 10, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_4.addWidget(self.label_6, 4, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.groupBox)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_4.addWidget(self.line_3, 9, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox, 12, 0, 1, 2)
        self.label_5 = QtGui.QLabel(self.groupBox_Datos)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_Descripcion = QtGui.QLabel(self.groupBox_Datos)
        self.label_Descripcion.setObjectName(_fromUtf8("label_Descripcion"))
        self.gridLayout.addWidget(self.label_Descripcion, 9, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_Datos)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEdit_NombreModelo = QtGui.QLineEdit(self.groupBox_Datos)
        self.lineEdit_NombreModelo.setMaxLength(100)
        self.lineEdit_NombreModelo.setObjectName(_fromUtf8("lineEdit_NombreModelo"))
        self.gridLayout.addWidget(self.lineEdit_NombreModelo, 0, 1, 1, 1)
        self.comboBox_SubTipoModelo = QtGui.QComboBox(self.groupBox_Datos)
        self.comboBox_SubTipoModelo.setObjectName(_fromUtf8("comboBox_SubTipoModelo"))
        self.gridLayout.addWidget(self.comboBox_SubTipoModelo, 9, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_Guardar = QtGui.QPushButton(self.groupBox_Datos)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Guardar.setIcon(icon2)
        self.pushButton_Guardar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Guardar.setFlat(True)
        self.pushButton_Guardar.setObjectName(_fromUtf8("pushButton_Guardar"))
        self.horizontalLayout.addWidget(self.pushButton_Guardar)
        self.pushButton_Borrar = QtGui.QPushButton(self.groupBox_Datos)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/eraser-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Borrar.setIcon(icon3)
        self.pushButton_Borrar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Borrar.setFlat(True)
        self.pushButton_Borrar.setObjectName(_fromUtf8("pushButton_Borrar"))
        self.horizontalLayout.addWidget(self.pushButton_Borrar)
        self.pushButton_Cancelar = QtGui.QPushButton(self.groupBox_Datos)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/uncheck.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Cancelar.setIcon(icon4)
        self.pushButton_Cancelar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Cancelar.setFlat(True)
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.horizontalLayout.addWidget(self.pushButton_Cancelar)
        self.gridLayout.addLayout(self.horizontalLayout, 13, 0, 1, 2)
        self.comboBox_MarcaModelo = QtGui.QComboBox(self.groupBox_Datos)
        self.comboBox_MarcaModelo.setObjectName(_fromUtf8("comboBox_MarcaModelo"))
        self.gridLayout.addWidget(self.comboBox_MarcaModelo, 3, 1, 1, 1)
        self.textEdit_String = QtGui.QTextEdit(self.groupBox_Datos)
        self.textEdit_String.setObjectName(_fromUtf8("textEdit_String"))
        self.gridLayout.addWidget(self.textEdit_String, 10, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_Datos)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 10, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.groupBox_Datos)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 4, 0, 1, 1)
        self.comboBox_TipoModelo = QtGui.QComboBox(self.groupBox_Datos)
        self.comboBox_TipoModelo.setObjectName(_fromUtf8("comboBox_TipoModelo"))
        self.gridLayout.addWidget(self.comboBox_TipoModelo, 4, 1, 1, 1)
        self.comboBox_VarString = QtGui.QComboBox(self.groupBox_Datos)
        self.comboBox_VarString.setObjectName(_fromUtf8("comboBox_VarString"))
        self.gridLayout.addWidget(self.comboBox_VarString, 11, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox_Datos)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 11, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_Datos, 0, 1, 3, 1)

        self.retranslateUi(SubVentanaModelosEquipos)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaModelosEquipos)
        SubVentanaModelosEquipos.setTabOrder(self.lineEdit_Buscar, self.tableWidget_Lista)
        SubVentanaModelosEquipos.setTabOrder(self.tableWidget_Lista, self.pushButton_Agregar)
        SubVentanaModelosEquipos.setTabOrder(self.pushButton_Agregar, self.lineEdit_NombreModelo)
        SubVentanaModelosEquipos.setTabOrder(self.lineEdit_NombreModelo, self.comboBox_MarcaModelo)
        SubVentanaModelosEquipos.setTabOrder(self.comboBox_MarcaModelo, self.comboBox_TipoModelo)
        SubVentanaModelosEquipos.setTabOrder(self.comboBox_TipoModelo, self.comboBox_SubTipoModelo)
        SubVentanaModelosEquipos.setTabOrder(self.comboBox_SubTipoModelo, self.textEdit_String)
        SubVentanaModelosEquipos.setTabOrder(self.textEdit_String, self.comboBox_VarString)
        SubVentanaModelosEquipos.setTabOrder(self.comboBox_VarString, self.pushButton_BuscarManualAyuda)
        SubVentanaModelosEquipos.setTabOrder(self.pushButton_BuscarManualAyuda, self.pushButton_BuscarManualUsuario)
        SubVentanaModelosEquipos.setTabOrder(self.pushButton_BuscarManualUsuario, self.pushButton_BuscarManualProgramacion)
        SubVentanaModelosEquipos.setTabOrder(self.pushButton_BuscarManualProgramacion, self.pushButton_BuscarManualConfiguracion)
        SubVentanaModelosEquipos.setTabOrder(self.pushButton_BuscarManualConfiguracion, self.pushButton_Guardar)
        SubVentanaModelosEquipos.setTabOrder(self.pushButton_Guardar, self.pushButton_Borrar)
        SubVentanaModelosEquipos.setTabOrder(self.pushButton_Borrar, self.pushButton_Cancelar)

    def retranslateUi(self, SubVentanaModelosEquipos):
        SubVentanaModelosEquipos.setWindowTitle(_translate("SubVentanaModelosEquipos", "Administracion de Modelos de Equipos", None))
        self.groupBox_4.setTitle(_translate("SubVentanaModelosEquipos", "Lista de Modelos de Equipos", None))
        item = self.tableWidget_Lista.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaModelosEquipos", "Nombre", None))
        item = self.tableWidget_Lista.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaModelosEquipos", "Marca", None))
        item = self.tableWidget_Lista.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaModelosEquipos", "SubTipo", None))
        self.pushButton_Agregar.setToolTip(_translate("SubVentanaModelosEquipos", "Agregar Nuevo Codigo", None))
        self.pushButton_Agregar.setText(_translate("SubVentanaModelosEquipos", "Agregar", None))
        self.label_3.setText(_translate("SubVentanaModelosEquipos", "Buscar:", None))
        self.groupBox_Datos.setTitle(_translate("SubVentanaModelosEquipos", "Datos del Modelo", None))
        self.groupBox.setTitle(_translate("SubVentanaModelosEquipos", "Manuales", None))
        self.NombreManualAyuda.setText(_translate("SubVentanaModelosEquipos", "No Seleccionado", None))
        self.NombreManualUsuario.setText(_translate("SubVentanaModelosEquipos", "No Seleccionado", None))
        self.NombreManualProgramacion.setText(_translate("SubVentanaModelosEquipos", "No Seleccionado", None))
        self.NombreManualConfiguracion.setText(_translate("SubVentanaModelosEquipos", "No Seleccionado", None))
        self.pushButton_BuscarManualUsuario.setText(_translate("SubVentanaModelosEquipos", "Buscar", None))
        self.label_4.setText(_translate("SubVentanaModelosEquipos", "Ayuda", None))
        self.pushButton_BuscarManualAyuda.setText(_translate("SubVentanaModelosEquipos", "Buscar", None))
        self.pushButton_BuscarManualProgramacion.setText(_translate("SubVentanaModelosEquipos", "Buscar", None))
        self.label_8.setText(_translate("SubVentanaModelosEquipos", "Configuracion", None))
        self.label_7.setText(_translate("SubVentanaModelosEquipos", "Programacion", None))
        self.pushButton_BuscarManualConfiguracion.setText(_translate("SubVentanaModelosEquipos", "Buscar", None))
        self.label_6.setText(_translate("SubVentanaModelosEquipos", "Usuario", None))
        self.label_5.setText(_translate("SubVentanaModelosEquipos", "Nombre:", None))
        self.label_Descripcion.setText(_translate("SubVentanaModelosEquipos", "SubTipo:", None))
        self.label_2.setText(_translate("SubVentanaModelosEquipos", "Marca:", None))
        self.pushButton_Guardar.setToolTip(_translate("SubVentanaModelosEquipos", "Guardar Codigo de Alarma", None))
        self.pushButton_Guardar.setText(_translate("SubVentanaModelosEquipos", "Guardar", None))
        self.pushButton_Borrar.setToolTip(_translate("SubVentanaModelosEquipos", "Borrar Codigo de Alarma", None))
        self.pushButton_Borrar.setText(_translate("SubVentanaModelosEquipos", "Borrar", None))
        self.pushButton_Cancelar.setToolTip(_translate("SubVentanaModelosEquipos", "Cancelar Edicion", None))
        self.pushButton_Cancelar.setText(_translate("SubVentanaModelosEquipos", "Cancelar", None))
        self.textEdit_String.setHtml(_translate("SubVentanaModelosEquipos", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">rtsp://</span></p></body></html>", None))
        self.label.setText(_translate("SubVentanaModelosEquipos", "String RTSP:", None))
        self.label_13.setText(_translate("SubVentanaModelosEquipos", "Tipo", None))
        self.label_14.setText(_translate("SubVentanaModelosEquipos", "Var String:", None))

import recursos_rc
