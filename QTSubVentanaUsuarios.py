# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaUsuarios.ui'
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

class Ui_SubVentanaUsuarios(object):
    def setupUi(self, SubVentanaUsuarios):
        SubVentanaUsuarios.setObjectName(_fromUtf8("SubVentanaUsuarios"))
        SubVentanaUsuarios.resize(869, 580)
        SubVentanaUsuarios.setMinimumSize(QtCore.QSize(869, 450))
        SubVentanaUsuarios.setMaximumSize(QtCore.QSize(869, 580))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        SubVentanaUsuarios.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Usuarios_configuracion.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubVentanaUsuarios.setWindowIcon(icon)
        SubVentanaUsuarios.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.horizontalLayout = QtGui.QHBoxLayout(SubVentanaUsuarios)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_Usuarios = QtGui.QGroupBox(SubVentanaUsuarios)
        self.groupBox_Usuarios.setMinimumSize(QtCore.QSize(430, 0))
        self.groupBox_Usuarios.setObjectName(_fromUtf8("groupBox_Usuarios"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_Usuarios)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_Empresa = QtGui.QLabel(self.groupBox_Usuarios)
        self.label_Empresa.setObjectName(_fromUtf8("label_Empresa"))
        self.gridLayout_2.addWidget(self.label_Empresa, 0, 0, 1, 1)
        self.comboBox_Empresa = QtGui.QComboBox(self.groupBox_Usuarios)
        self.comboBox_Empresa.setObjectName(_fromUtf8("comboBox_Empresa"))
        self.comboBox_Empresa.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_Empresa, 0, 1, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pushButton_AgregarUsuario = QtGui.QPushButton(self.groupBox_Usuarios)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/4-Icone-plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AgregarUsuario.setIcon(icon1)
        self.pushButton_AgregarUsuario.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_AgregarUsuario.setFlat(True)
        self.pushButton_AgregarUsuario.setObjectName(_fromUtf8("pushButton_AgregarUsuario"))
        self.horizontalLayout_5.addWidget(self.pushButton_AgregarUsuario)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 3, 0, 1, 4)
        self.tableWidget_Usuarios = QtGui.QTableWidget(self.groupBox_Usuarios)
        self.tableWidget_Usuarios.setMinimumSize(QtCore.QSize(250, 0))
        self.tableWidget_Usuarios.setObjectName(_fromUtf8("tableWidget_Usuarios"))
        self.tableWidget_Usuarios.setColumnCount(5)
        self.tableWidget_Usuarios.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Usuarios.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Usuarios.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Usuarios.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Usuarios.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Usuarios.setHorizontalHeaderItem(4, item)
        self.gridLayout_2.addWidget(self.tableWidget_Usuarios, 2, 0, 1, 4)
        self.label_Busqueda = QtGui.QLabel(self.groupBox_Usuarios)
        self.label_Busqueda.setObjectName(_fromUtf8("label_Busqueda"))
        self.gridLayout_2.addWidget(self.label_Busqueda, 1, 0, 1, 1)
        self.lineEdit_BusquedaUsuario = QtGui.QLineEdit(self.groupBox_Usuarios)
        self.lineEdit_BusquedaUsuario.setObjectName(_fromUtf8("lineEdit_BusquedaUsuario"))
        self.gridLayout_2.addWidget(self.lineEdit_BusquedaUsuario, 1, 1, 1, 3)
        self.horizontalLayout.addWidget(self.groupBox_Usuarios)
        self.tabWidget = QtGui.QTabWidget(SubVentanaUsuarios)
        self.tabWidget.setMinimumSize(QtCore.QSize(410, 0))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.groupBox_Edicion = QtGui.QGroupBox(self.tab)
        self.groupBox_Edicion.setMinimumSize(QtCore.QSize(250, 0))
        self.groupBox_Edicion.setObjectName(_fromUtf8("groupBox_Edicion"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_Edicion)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(self.groupBox_Edicion)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_CorreoEdicion = QtGui.QLineEdit(self.groupBox_Edicion)
        self.lineEdit_CorreoEdicion.setObjectName(_fromUtf8("lineEdit_CorreoEdicion"))
        self.gridLayout.addWidget(self.lineEdit_CorreoEdicion, 5, 1, 1, 1)
        self.lineEdit_NombreEdicion = QtGui.QLineEdit(self.groupBox_Edicion)
        self.lineEdit_NombreEdicion.setObjectName(_fromUtf8("lineEdit_NombreEdicion"))
        self.gridLayout.addWidget(self.lineEdit_NombreEdicion, 3, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_Edicion)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_Edicion)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.lineEdit_TelefonoEdicion = QtGui.QLineEdit(self.groupBox_Edicion)
        self.lineEdit_TelefonoEdicion.setObjectName(_fromUtf8("lineEdit_TelefonoEdicion"))
        self.gridLayout.addWidget(self.lineEdit_TelefonoEdicion, 6, 1, 1, 1)
        self.lineEdit_DireccionEdicion = QtGui.QLineEdit(self.groupBox_Edicion)
        self.lineEdit_DireccionEdicion.setObjectName(_fromUtf8("lineEdit_DireccionEdicion"))
        self.gridLayout.addWidget(self.lineEdit_DireccionEdicion, 4, 1, 1, 1)
        self.lineEdit_ClaveEdicion = QtGui.QLineEdit(self.groupBox_Edicion)
        self.lineEdit_ClaveEdicion.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_ClaveEdicion.setObjectName(_fromUtf8("lineEdit_ClaveEdicion"))
        self.gridLayout.addWidget(self.lineEdit_ClaveEdicion, 9, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_Edicion)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 10, 0, 1, 1)
        self.lineEdit_UsuarioEdicion = QtGui.QLineEdit(self.groupBox_Edicion)
        self.lineEdit_UsuarioEdicion.setObjectName(_fromUtf8("lineEdit_UsuarioEdicion"))
        self.gridLayout.addWidget(self.lineEdit_UsuarioEdicion, 8, 1, 1, 1)
        self.lineEdit_RepetirClaveEdicion = QtGui.QLineEdit(self.groupBox_Edicion)
        self.lineEdit_RepetirClaveEdicion.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_RepetirClaveEdicion.setObjectName(_fromUtf8("lineEdit_RepetirClaveEdicion"))
        self.gridLayout.addWidget(self.lineEdit_RepetirClaveEdicion, 10, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_Edicion)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 9, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_Edicion)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)
        self.lineEdit_TelMovil = QtGui.QLineEdit(self.groupBox_Edicion)
        self.lineEdit_TelMovil.setObjectName(_fromUtf8("lineEdit_TelMovil"))
        self.gridLayout.addWidget(self.lineEdit_TelMovil, 7, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_Edicion)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 7, 0, 1, 1)
        self.comboBox_EmpresaEdicion = QtGui.QComboBox(self.groupBox_Edicion)
        self.comboBox_EmpresaEdicion.setObjectName(_fromUtf8("comboBox_EmpresaEdicion"))
        self.gridLayout.addWidget(self.comboBox_EmpresaEdicion, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_Edicion)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_TipoEdicion = QtGui.QComboBox(self.groupBox_Edicion)
        self.comboBox_TipoEdicion.setObjectName(_fromUtf8("comboBox_TipoEdicion"))
        self.gridLayout.addWidget(self.comboBox_TipoEdicion, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_Edicion)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_Edicion)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_DocumentoEdicion = QtGui.QLineEdit(self.groupBox_Edicion)
        self.lineEdit_DocumentoEdicion.setObjectName(_fromUtf8("lineEdit_DocumentoEdicion"))
        self.gridLayout.addWidget(self.lineEdit_DocumentoEdicion, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_Edicion)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_11 = QtGui.QLabel(self.groupBox_Edicion)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_2.addWidget(self.label_11)
        self.pushButton_Imagen = QtGui.QPushButton(self.groupBox_Edicion)
        self.pushButton_Imagen.setObjectName(_fromUtf8("pushButton_Imagen"))
        self.verticalLayout_2.addWidget(self.pushButton_Imagen)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout_2, 11, 0, 1, 1)
        self.horizontalLayout_Image = QtGui.QHBoxLayout()
        self.horizontalLayout_Image.setObjectName(_fromUtf8("horizontalLayout_Image"))
        self.gridLayout.addLayout(self.horizontalLayout_Image, 11, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_Edicion, 0, 0, 1, 1)
        self.frame = QtGui.QFrame(self.tab)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_GuardarUsuario = QtGui.QPushButton(self.frame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_GuardarUsuario.setIcon(icon2)
        self.pushButton_GuardarUsuario.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_GuardarUsuario.setFlat(True)
        self.pushButton_GuardarUsuario.setObjectName(_fromUtf8("pushButton_GuardarUsuario"))
        self.horizontalLayout_3.addWidget(self.pushButton_GuardarUsuario)
        self.pushButton_BorrarUsuario = QtGui.QPushButton(self.frame)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/eraser-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_BorrarUsuario.setIcon(icon3)
        self.pushButton_BorrarUsuario.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_BorrarUsuario.setFlat(True)
        self.pushButton_BorrarUsuario.setObjectName(_fromUtf8("pushButton_BorrarUsuario"))
        self.horizontalLayout_3.addWidget(self.pushButton_BorrarUsuario)
        self.pushButton_Cancelar = QtGui.QPushButton(self.frame)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/uncheck.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Cancelar.setIcon(icon4)
        self.pushButton_Cancelar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Cancelar.setFlat(True)
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.horizontalLayout_3.addWidget(self.pushButton_Cancelar)
        self.gridLayout_4.addWidget(self.frame, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.groupBox_Permisos = QtGui.QGroupBox(self.tab_2)
        self.groupBox_Permisos.setObjectName(_fromUtf8("groupBox_Permisos"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_Permisos)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tableWidget_Permisos = QtGui.QTableWidget(self.groupBox_Permisos)
        self.tableWidget_Permisos.setMinimumSize(QtCore.QSize(250, 0))
        self.tableWidget_Permisos.setAlternatingRowColors(True)
        self.tableWidget_Permisos.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_Permisos.setObjectName(_fromUtf8("tableWidget_Permisos"))
        self.tableWidget_Permisos.setColumnCount(2)
        self.tableWidget_Permisos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Permisos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Permisos.setHorizontalHeaderItem(1, item)
        self.tableWidget_Permisos.horizontalHeader().setVisible(False)
        self.tableWidget_Permisos.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.tableWidget_Permisos, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_Permisos, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(SubVentanaUsuarios)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaUsuarios)
        SubVentanaUsuarios.setTabOrder(self.comboBox_Empresa, self.tableWidget_Usuarios)
        SubVentanaUsuarios.setTabOrder(self.tableWidget_Usuarios, self.pushButton_AgregarUsuario)
        SubVentanaUsuarios.setTabOrder(self.pushButton_AgregarUsuario, self.comboBox_EmpresaEdicion)
        SubVentanaUsuarios.setTabOrder(self.comboBox_EmpresaEdicion, self.comboBox_TipoEdicion)
        SubVentanaUsuarios.setTabOrder(self.comboBox_TipoEdicion, self.lineEdit_DocumentoEdicion)
        SubVentanaUsuarios.setTabOrder(self.lineEdit_DocumentoEdicion, self.lineEdit_NombreEdicion)
        SubVentanaUsuarios.setTabOrder(self.lineEdit_NombreEdicion, self.lineEdit_DireccionEdicion)
        SubVentanaUsuarios.setTabOrder(self.lineEdit_DireccionEdicion, self.lineEdit_CorreoEdicion)
        SubVentanaUsuarios.setTabOrder(self.lineEdit_CorreoEdicion, self.lineEdit_TelefonoEdicion)
        SubVentanaUsuarios.setTabOrder(self.lineEdit_TelefonoEdicion, self.lineEdit_TelMovil)
        SubVentanaUsuarios.setTabOrder(self.lineEdit_TelMovil, self.lineEdit_UsuarioEdicion)
        SubVentanaUsuarios.setTabOrder(self.lineEdit_UsuarioEdicion, self.lineEdit_ClaveEdicion)
        SubVentanaUsuarios.setTabOrder(self.lineEdit_ClaveEdicion, self.lineEdit_RepetirClaveEdicion)
        SubVentanaUsuarios.setTabOrder(self.lineEdit_RepetirClaveEdicion, self.pushButton_GuardarUsuario)
        SubVentanaUsuarios.setTabOrder(self.pushButton_GuardarUsuario, self.pushButton_BorrarUsuario)
        SubVentanaUsuarios.setTabOrder(self.pushButton_BorrarUsuario, self.pushButton_Cancelar)
        SubVentanaUsuarios.setTabOrder(self.pushButton_Cancelar, self.tableWidget_Permisos)

    def retranslateUi(self, SubVentanaUsuarios):
        SubVentanaUsuarios.setWindowTitle(_translate("SubVentanaUsuarios", "Administracion de Usuarios", None))
        self.groupBox_Usuarios.setTitle(_translate("SubVentanaUsuarios", "Lista de Usuarios", None))
        self.label_Empresa.setText(_translate("SubVentanaUsuarios", "Empresa: ", None))
        self.comboBox_Empresa.setItemText(0, _translate("SubVentanaUsuarios", "Todas", None))
        self.pushButton_AgregarUsuario.setToolTip(_translate("SubVentanaUsuarios", "Agregar Nuevo Codigo", None))
        self.pushButton_AgregarUsuario.setText(_translate("SubVentanaUsuarios", "Agregar", None))
        item = self.tableWidget_Usuarios.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaUsuarios", "Nombre", None))
        item = self.tableWidget_Usuarios.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaUsuarios", "Login", None))
        item = self.tableWidget_Usuarios.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaUsuarios", "Tipo", None))
        item = self.tableWidget_Usuarios.horizontalHeaderItem(3)
        item.setText(_translate("SubVentanaUsuarios", "Empresa", None))
        item = self.tableWidget_Usuarios.horizontalHeaderItem(4)
        item.setText(_translate("SubVentanaUsuarios", "Estatus", None))
        self.label_Busqueda.setText(_translate("SubVentanaUsuarios", "Busqueda: ", None))
        self.groupBox_Edicion.setTitle(_translate("SubVentanaUsuarios", "Datos del Usuario", None))
        self.label_5.setText(_translate("SubVentanaUsuarios", "Direccion", None))
        self.label_7.setText(_translate("SubVentanaUsuarios", "Tel. Fijo", None))
        self.label_6.setText(_translate("SubVentanaUsuarios", "Correo", None))
        self.label_10.setText(_translate("SubVentanaUsuarios", "Rep. Clave", None))
        self.label_9.setText(_translate("SubVentanaUsuarios", "Clave", None))
        self.label_8.setText(_translate("SubVentanaUsuarios", "Usuario", None))
        self.label_12.setText(_translate("SubVentanaUsuarios", "Tel. Movil", None))
        self.label_2.setText(_translate("SubVentanaUsuarios", "Tipo", None))
        self.label_3.setText(_translate("SubVentanaUsuarios", "Documento", None))
        self.label.setText(_translate("SubVentanaUsuarios", "Empresa", None))
        self.label_4.setText(_translate("SubVentanaUsuarios", "Nombre", None))
        self.label_11.setText(_translate("SubVentanaUsuarios", "Imagen:", None))
        self.pushButton_Imagen.setText(_translate("SubVentanaUsuarios", "Seleccionar", None))
        self.pushButton_GuardarUsuario.setText(_translate("SubVentanaUsuarios", "Guardar", None))
        self.pushButton_BorrarUsuario.setToolTip(_translate("SubVentanaUsuarios", "Borrar Codigo de Alarma", None))
        self.pushButton_BorrarUsuario.setText(_translate("SubVentanaUsuarios", "Borrar", None))
        self.pushButton_Cancelar.setToolTip(_translate("SubVentanaUsuarios", "Cancelar Edicion", None))
        self.pushButton_Cancelar.setText(_translate("SubVentanaUsuarios", "Cancelar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SubVentanaUsuarios", "Informacion", None))
        self.groupBox_Permisos.setTitle(_translate("SubVentanaUsuarios", "Permisos del Usuario", None))
        item = self.tableWidget_Permisos.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaUsuarios", "Nombre", None))
        item = self.tableWidget_Permisos.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaUsuarios", "Check", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SubVentanaUsuarios", "Permisos", None))

import recursos_rc
