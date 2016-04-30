# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaReceptores.ui'
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

class Ui_SubVentanaReceptores(object):
    def setupUi(self, SubVentanaReceptores):
        SubVentanaReceptores.setObjectName(_fromUtf8("SubVentanaReceptores"))
        SubVentanaReceptores.resize(646, 572)
        SubVentanaReceptores.setMinimumSize(QtCore.QSize(646, 572))
        SubVentanaReceptores.setMaximumSize(QtCore.QSize(646, 572))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Receptores.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubVentanaReceptores.setWindowIcon(icon)
        SubVentanaReceptores.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout_4 = QtGui.QGridLayout(SubVentanaReceptores)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.groupBox_4 = QtGui.QGroupBox(SubVentanaReceptores)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tableWidget_ListadeReceptores = QtGui.QTableWidget(self.groupBox_4)
        self.tableWidget_ListadeReceptores.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidget_ListadeReceptores.setStyleSheet(_fromUtf8(""))
        self.tableWidget_ListadeReceptores.setObjectName(_fromUtf8("tableWidget_ListadeReceptores"))
        self.tableWidget_ListadeReceptores.setColumnCount(4)
        self.tableWidget_ListadeReceptores.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ListadeReceptores.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ListadeReceptores.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ListadeReceptores.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ListadeReceptores.setHorizontalHeaderItem(3, item)
        self.gridLayout_3.addWidget(self.tableWidget_ListadeReceptores, 1, 0, 1, 3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_AgregarReceptor = QtGui.QPushButton(self.groupBox_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/4-Icone-plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AgregarReceptor.setIcon(icon1)
        self.pushButton_AgregarReceptor.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_AgregarReceptor.setFlat(True)
        self.pushButton_AgregarReceptor.setObjectName(_fromUtf8("pushButton_AgregarReceptor"))
        self.horizontalLayout_2.addWidget(self.pushButton_AgregarReceptor)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 3)
        self.lineEdit_Buscar = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_Buscar.setObjectName(_fromUtf8("lineEdit_Buscar"))
        self.gridLayout_3.addWidget(self.lineEdit_Buscar, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_DatosReceptor = QtGui.QGroupBox(SubVentanaReceptores)
        self.groupBox_DatosReceptor.setObjectName(_fromUtf8("groupBox_DatosReceptor"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_DatosReceptor)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_11 = QtGui.QLabel(self.groupBox_DatosReceptor)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 10, 0, 1, 1)
        self.spinBox_Prefijo = QtGui.QSpinBox(self.groupBox_DatosReceptor)
        self.spinBox_Prefijo.setMinimum(0)
        self.spinBox_Prefijo.setMaximum(9000)
        self.spinBox_Prefijo.setSingleStep(1000)
        self.spinBox_Prefijo.setProperty("value", 0)
        self.spinBox_Prefijo.setObjectName(_fromUtf8("spinBox_Prefijo"))
        self.gridLayout_2.addWidget(self.spinBox_Prefijo, 10, 1, 1, 1)
        self.comboBox_Estatus = QtGui.QComboBox(self.groupBox_DatosReceptor)
        self.comboBox_Estatus.setToolTip(_fromUtf8(""))
        self.comboBox_Estatus.setStatusTip(_fromUtf8(""))
        self.comboBox_Estatus.setObjectName(_fromUtf8("comboBox_Estatus"))
        self.comboBox_Estatus.addItem(_fromUtf8(""))
        self.comboBox_Estatus.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_Estatus, 9, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_DatosReceptor)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 7, 0, 1, 1)
        self.comboBox_StopBits = QtGui.QComboBox(self.groupBox_DatosReceptor)
        self.comboBox_StopBits.setObjectName(_fromUtf8("comboBox_StopBits"))
        self.comboBox_StopBits.addItem(_fromUtf8(""))
        self.comboBox_StopBits.addItem(_fromUtf8(""))
        self.comboBox_StopBits.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_StopBits, 7, 1, 1, 1)
        self.comboBox_Bits = QtGui.QComboBox(self.groupBox_DatosReceptor)
        self.comboBox_Bits.setObjectName(_fromUtf8("comboBox_Bits"))
        self.comboBox_Bits.addItem(_fromUtf8(""))
        self.comboBox_Bits.addItem(_fromUtf8(""))
        self.comboBox_Bits.addItem(_fromUtf8(""))
        self.comboBox_Bits.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_Bits, 6, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_DatosReceptor)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 6, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_DatosReceptor)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 8, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_DatosReceptor)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 9, 0, 1, 1)
        self.comboBox_ACK = QtGui.QComboBox(self.groupBox_DatosReceptor)
        self.comboBox_ACK.setObjectName(_fromUtf8("comboBox_ACK"))
        self.comboBox_ACK.addItem(_fromUtf8(""))
        self.comboBox_ACK.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_ACK, 8, 1, 1, 1)
        self.comboBox_Paridad = QtGui.QComboBox(self.groupBox_DatosReceptor)
        self.comboBox_Paridad.setToolTip(_fromUtf8(""))
        self.comboBox_Paridad.setObjectName(_fromUtf8("comboBox_Paridad"))
        self.comboBox_Paridad.addItem(_fromUtf8(""))
        self.comboBox_Paridad.addItem(_fromUtf8(""))
        self.comboBox_Paridad.addItem(_fromUtf8(""))
        self.comboBox_Paridad.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_Paridad, 5, 1, 1, 1)
        self.lineEdit_Puerto = QtGui.QLineEdit(self.groupBox_DatosReceptor)
        self.lineEdit_Puerto.setMaxLength(6)
        self.lineEdit_Puerto.setObjectName(_fromUtf8("lineEdit_Puerto"))
        self.gridLayout_2.addWidget(self.lineEdit_Puerto, 2, 1, 1, 1)
        self.comboBox_TipoReceptor = QtGui.QComboBox(self.groupBox_DatosReceptor)
        self.comboBox_TipoReceptor.setObjectName(_fromUtf8("comboBox_TipoReceptor"))
        self.comboBox_TipoReceptor.addItem(_fromUtf8(""))
        self.comboBox_TipoReceptor.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_TipoReceptor, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_DatosReceptor)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_DatosReceptor)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_DatosReceptor)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_DatosReceptor)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.comboBox_Receptor = QtGui.QComboBox(self.groupBox_DatosReceptor)
        self.comboBox_Receptor.setObjectName(_fromUtf8("comboBox_Receptor"))
        self.gridLayout_2.addWidget(self.comboBox_Receptor, 3, 1, 1, 1)
        self.comboBox_Velocidad = QtGui.QComboBox(self.groupBox_DatosReceptor)
        self.comboBox_Velocidad.setObjectName(_fromUtf8("comboBox_Velocidad"))
        self.comboBox_Velocidad.addItem(_fromUtf8(""))
        self.comboBox_Velocidad.addItem(_fromUtf8(""))
        self.comboBox_Velocidad.addItem(_fromUtf8(""))
        self.comboBox_Velocidad.addItem(_fromUtf8(""))
        self.comboBox_Velocidad.addItem(_fromUtf8(""))
        self.comboBox_Velocidad.addItem(_fromUtf8(""))
        self.comboBox_Velocidad.addItem(_fromUtf8(""))
        self.comboBox_Velocidad.addItem(_fromUtf8(""))
        self.comboBox_Velocidad.addItem(_fromUtf8(""))
        self.comboBox_Velocidad.addItem(_fromUtf8(""))
        self.comboBox_Velocidad.addItem(_fromUtf8(""))
        self.comboBox_Velocidad.addItem(_fromUtf8(""))
        self.comboBox_Velocidad.addItem(_fromUtf8(""))
        self.comboBox_Velocidad.addItem(_fromUtf8(""))
        self.comboBox_Velocidad.addItem(_fromUtf8(""))
        self.comboBox_Velocidad.addItem(_fromUtf8(""))
        self.comboBox_Velocidad.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_Velocidad, 4, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_DatosReceptor)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 5, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.groupBox_DatosReceptor)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_Linea = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Linea.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lineEdit_Linea.setMaxLength(4)
        self.lineEdit_Linea.setObjectName(_fromUtf8("lineEdit_Linea"))
        self.gridLayout.addWidget(self.lineEdit_Linea, 0, 0, 1, 1)
        self.lineEdit_Prefijo = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Prefijo.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lineEdit_Prefijo.setMaxLength(3)
        self.lineEdit_Prefijo.setObjectName(_fromUtf8("lineEdit_Prefijo"))
        self.gridLayout.addWidget(self.lineEdit_Prefijo, 0, 1, 1, 1)
        self.lineEdit_DescripcionLinea = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_DescripcionLinea.setObjectName(_fromUtf8("lineEdit_DescripcionLinea"))
        self.gridLayout.addWidget(self.lineEdit_DescripcionLinea, 0, 2, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton_AgregarLinea = QtGui.QPushButton(self.groupBox)
        self.pushButton_AgregarLinea.setIcon(icon1)
        self.pushButton_AgregarLinea.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_AgregarLinea.setFlat(True)
        self.pushButton_AgregarLinea.setObjectName(_fromUtf8("pushButton_AgregarLinea"))
        self.horizontalLayout_4.addWidget(self.pushButton_AgregarLinea)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 3)
        self.gridLayout_2.addWidget(self.groupBox, 11, 0, 1, 2)
        self.tableWidget_LineasPrefijos = QtGui.QTableWidget(self.groupBox_DatosReceptor)
        self.tableWidget_LineasPrefijos.setObjectName(_fromUtf8("tableWidget_LineasPrefijos"))
        self.tableWidget_LineasPrefijos.setColumnCount(4)
        self.tableWidget_LineasPrefijos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_LineasPrefijos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_LineasPrefijos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_LineasPrefijos.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_LineasPrefijos.setHorizontalHeaderItem(3, item)
        self.gridLayout_2.addWidget(self.tableWidget_LineasPrefijos, 12, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_GuardarReceptor = QtGui.QPushButton(self.groupBox_DatosReceptor)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_GuardarReceptor.setIcon(icon2)
        self.pushButton_GuardarReceptor.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_GuardarReceptor.setFlat(True)
        self.pushButton_GuardarReceptor.setObjectName(_fromUtf8("pushButton_GuardarReceptor"))
        self.horizontalLayout.addWidget(self.pushButton_GuardarReceptor)
        self.pushButton_BorrarReceptor = QtGui.QPushButton(self.groupBox_DatosReceptor)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/eraser-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_BorrarReceptor.setIcon(icon3)
        self.pushButton_BorrarReceptor.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_BorrarReceptor.setFlat(True)
        self.pushButton_BorrarReceptor.setObjectName(_fromUtf8("pushButton_BorrarReceptor"))
        self.horizontalLayout.addWidget(self.pushButton_BorrarReceptor)
        self.pushButton_Cancelar = QtGui.QPushButton(self.groupBox_DatosReceptor)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/uncheck.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Cancelar.setIcon(icon4)
        self.pushButton_Cancelar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Cancelar.setFlat(True)
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.horizontalLayout.addWidget(self.pushButton_Cancelar)
        self.gridLayout_2.addLayout(self.horizontalLayout, 13, 0, 1, 2)
        self.label_12 = QtGui.QLabel(self.groupBox_DatosReceptor)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)
        self.lineEdit_Servidor = QtGui.QLineEdit(self.groupBox_DatosReceptor)
        self.lineEdit_Servidor.setObjectName(_fromUtf8("lineEdit_Servidor"))
        self.gridLayout_2.addWidget(self.lineEdit_Servidor, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_DatosReceptor, 0, 1, 1, 1)

        self.retranslateUi(SubVentanaReceptores)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaReceptores)
        SubVentanaReceptores.setTabOrder(self.lineEdit_Buscar, self.tableWidget_ListadeReceptores)
        SubVentanaReceptores.setTabOrder(self.tableWidget_ListadeReceptores, self.pushButton_AgregarReceptor)
        SubVentanaReceptores.setTabOrder(self.pushButton_AgregarReceptor, self.comboBox_TipoReceptor)
        SubVentanaReceptores.setTabOrder(self.comboBox_TipoReceptor, self.lineEdit_Servidor)
        SubVentanaReceptores.setTabOrder(self.lineEdit_Servidor, self.lineEdit_Puerto)
        SubVentanaReceptores.setTabOrder(self.lineEdit_Puerto, self.comboBox_Receptor)
        SubVentanaReceptores.setTabOrder(self.comboBox_Receptor, self.comboBox_Velocidad)
        SubVentanaReceptores.setTabOrder(self.comboBox_Velocidad, self.comboBox_Paridad)
        SubVentanaReceptores.setTabOrder(self.comboBox_Paridad, self.comboBox_Bits)
        SubVentanaReceptores.setTabOrder(self.comboBox_Bits, self.comboBox_StopBits)
        SubVentanaReceptores.setTabOrder(self.comboBox_StopBits, self.comboBox_ACK)
        SubVentanaReceptores.setTabOrder(self.comboBox_ACK, self.comboBox_Estatus)
        SubVentanaReceptores.setTabOrder(self.comboBox_Estatus, self.spinBox_Prefijo)
        SubVentanaReceptores.setTabOrder(self.spinBox_Prefijo, self.lineEdit_Linea)
        SubVentanaReceptores.setTabOrder(self.lineEdit_Linea, self.lineEdit_Prefijo)
        SubVentanaReceptores.setTabOrder(self.lineEdit_Prefijo, self.lineEdit_DescripcionLinea)
        SubVentanaReceptores.setTabOrder(self.lineEdit_DescripcionLinea, self.pushButton_AgregarLinea)
        SubVentanaReceptores.setTabOrder(self.pushButton_AgregarLinea, self.tableWidget_LineasPrefijos)
        SubVentanaReceptores.setTabOrder(self.tableWidget_LineasPrefijos, self.pushButton_GuardarReceptor)
        SubVentanaReceptores.setTabOrder(self.pushButton_GuardarReceptor, self.pushButton_BorrarReceptor)
        SubVentanaReceptores.setTabOrder(self.pushButton_BorrarReceptor, self.pushButton_Cancelar)

    def retranslateUi(self, SubVentanaReceptores):
        SubVentanaReceptores.setWindowTitle(_translate("SubVentanaReceptores", "Administracion de Receptores", None))
        self.groupBox_4.setTitle(_translate("SubVentanaReceptores", "Lista de Receptores", None))
        item = self.tableWidget_ListadeReceptores.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaReceptores", "Puerto", None))
        item = self.tableWidget_ListadeReceptores.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaReceptores", "Receptor", None))
        item = self.tableWidget_ListadeReceptores.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaReceptores", "Config", None))
        item = self.tableWidget_ListadeReceptores.horizontalHeaderItem(3)
        item.setText(_translate("SubVentanaReceptores", "Estatus", None))
        self.pushButton_AgregarReceptor.setToolTip(_translate("SubVentanaReceptores", "Agregar Receptor", None))
        self.pushButton_AgregarReceptor.setText(_translate("SubVentanaReceptores", "Agregar", None))
        self.label.setText(_translate("SubVentanaReceptores", "Buscar:", None))
        self.groupBox_DatosReceptor.setTitle(_translate("SubVentanaReceptores", "Datos del Receptor", None))
        self.label_11.setText(_translate("SubVentanaReceptores", "Prefijo:", None))
        self.comboBox_Estatus.setItemText(0, _translate("SubVentanaReceptores", "Activado", None))
        self.comboBox_Estatus.setItemText(1, _translate("SubVentanaReceptores", "Desactivado", None))
        self.label_6.setText(_translate("SubVentanaReceptores", "Stop Bits:", None))
        self.comboBox_StopBits.setItemText(0, _translate("SubVentanaReceptores", "1", None))
        self.comboBox_StopBits.setItemText(1, _translate("SubVentanaReceptores", "1.5", None))
        self.comboBox_StopBits.setItemText(2, _translate("SubVentanaReceptores", "2", None))
        self.comboBox_Bits.setItemText(0, _translate("SubVentanaReceptores", "5", None))
        self.comboBox_Bits.setItemText(1, _translate("SubVentanaReceptores", "6", None))
        self.comboBox_Bits.setItemText(2, _translate("SubVentanaReceptores", "7", None))
        self.comboBox_Bits.setItemText(3, _translate("SubVentanaReceptores", "8", None))
        self.label_3.setText(_translate("SubVentanaReceptores", "Bits:", None))
        self.label_7.setText(_translate("SubVentanaReceptores", "ACK:", None))
        self.label_10.setText(_translate("SubVentanaReceptores", "Estatus:", None))
        self.comboBox_ACK.setItemText(0, _translate("SubVentanaReceptores", "Si", None))
        self.comboBox_ACK.setItemText(1, _translate("SubVentanaReceptores", "No", None))
        self.comboBox_Paridad.setItemText(0, _translate("SubVentanaReceptores", "N", None))
        self.comboBox_Paridad.setItemText(1, _translate("SubVentanaReceptores", "E", None))
        self.comboBox_Paridad.setItemText(2, _translate("SubVentanaReceptores", "O", None))
        self.comboBox_Paridad.setItemText(3, _translate("SubVentanaReceptores", "M", None))
        self.comboBox_TipoReceptor.setItemText(0, _translate("SubVentanaReceptores", "Puerto Serial", None))
        self.comboBox_TipoReceptor.setItemText(1, _translate("SubVentanaReceptores", "TCP / IP", None))
        self.label_2.setText(_translate("SubVentanaReceptores", "Tipo:", None))
        self.label_5.setText(_translate("SubVentanaReceptores", "Puerto:", None))
        self.label_8.setText(_translate("SubVentanaReceptores", "Velocidad:", None))
        self.label_4.setText(_translate("SubVentanaReceptores", "Receptor:", None))
        self.comboBox_Velocidad.setItemText(0, _translate("SubVentanaReceptores", "50", None))
        self.comboBox_Velocidad.setItemText(1, _translate("SubVentanaReceptores", "75", None))
        self.comboBox_Velocidad.setItemText(2, _translate("SubVentanaReceptores", "110", None))
        self.comboBox_Velocidad.setItemText(3, _translate("SubVentanaReceptores", "134", None))
        self.comboBox_Velocidad.setItemText(4, _translate("SubVentanaReceptores", "150", None))
        self.comboBox_Velocidad.setItemText(5, _translate("SubVentanaReceptores", "200", None))
        self.comboBox_Velocidad.setItemText(6, _translate("SubVentanaReceptores", "300", None))
        self.comboBox_Velocidad.setItemText(7, _translate("SubVentanaReceptores", "600", None))
        self.comboBox_Velocidad.setItemText(8, _translate("SubVentanaReceptores", "1200", None))
        self.comboBox_Velocidad.setItemText(9, _translate("SubVentanaReceptores", "1800", None))
        self.comboBox_Velocidad.setItemText(10, _translate("SubVentanaReceptores", "2400", None))
        self.comboBox_Velocidad.setItemText(11, _translate("SubVentanaReceptores", "4800", None))
        self.comboBox_Velocidad.setItemText(12, _translate("SubVentanaReceptores", "9600", None))
        self.comboBox_Velocidad.setItemText(13, _translate("SubVentanaReceptores", "19200", None))
        self.comboBox_Velocidad.setItemText(14, _translate("SubVentanaReceptores", "38400", None))
        self.comboBox_Velocidad.setItemText(15, _translate("SubVentanaReceptores", "57600", None))
        self.comboBox_Velocidad.setItemText(16, _translate("SubVentanaReceptores", "115200", None))
        self.label_9.setText(_translate("SubVentanaReceptores", "Paridad:", None))
        self.groupBox.setTitle(_translate("SubVentanaReceptores", "Configurar Lineas", None))
        self.lineEdit_Linea.setPlaceholderText(_translate("SubVentanaReceptores", "Linea", None))
        self.lineEdit_Prefijo.setPlaceholderText(_translate("SubVentanaReceptores", "Prefijo", None))
        self.lineEdit_DescripcionLinea.setPlaceholderText(_translate("SubVentanaReceptores", "Descripcion", None))
        self.pushButton_AgregarLinea.setText(_translate("SubVentanaReceptores", "Agregar", None))
        item = self.tableWidget_LineasPrefijos.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaReceptores", "Linea", None))
        item = self.tableWidget_LineasPrefijos.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaReceptores", "Descripcion", None))
        item = self.tableWidget_LineasPrefijos.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaReceptores", "Prefijo", None))
        item = self.tableWidget_LineasPrefijos.horizontalHeaderItem(3)
        item.setText(_translate("SubVentanaReceptores", "Borrar", None))
        self.pushButton_GuardarReceptor.setToolTip(_translate("SubVentanaReceptores", "Guardar Receptor", None))
        self.pushButton_GuardarReceptor.setText(_translate("SubVentanaReceptores", "Guardar", None))
        self.pushButton_BorrarReceptor.setToolTip(_translate("SubVentanaReceptores", "Borrar Receptor", None))
        self.pushButton_BorrarReceptor.setText(_translate("SubVentanaReceptores", "Borrar", None))
        self.pushButton_Cancelar.setToolTip(_translate("SubVentanaReceptores", "Cancelar Edicion", None))
        self.pushButton_Cancelar.setText(_translate("SubVentanaReceptores", "Cancelar", None))
        self.label_12.setText(_translate("SubVentanaReceptores", "Servidor:", None))

import recursos_rc
