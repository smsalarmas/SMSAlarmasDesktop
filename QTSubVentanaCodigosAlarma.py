# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaCodigosAlarma.ui'
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

class Ui_SubVentanaCodigosAlarma(object):
    def setupUi(self, SubVentanaCodigosAlarma):
        SubVentanaCodigosAlarma.setObjectName(_fromUtf8("SubVentanaCodigosAlarma"))
        SubVentanaCodigosAlarma.resize(645, 351)
        SubVentanaCodigosAlarma.setMinimumSize(QtCore.QSize(645, 351))
        SubVentanaCodigosAlarma.setMaximumSize(QtCore.QSize(645, 351))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Codigos_Alarmas.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubVentanaCodigosAlarma.setWindowIcon(icon)
        SubVentanaCodigosAlarma.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout_2 = QtGui.QGridLayout(SubVentanaCodigosAlarma)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_4 = QtGui.QGroupBox(SubVentanaCodigosAlarma)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tableWidget_ListadeCodigosAlarma = QtGui.QTableWidget(self.groupBox_4)
        self.tableWidget_ListadeCodigosAlarma.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidget_ListadeCodigosAlarma.setStyleSheet(_fromUtf8(""))
        self.tableWidget_ListadeCodigosAlarma.setObjectName(_fromUtf8("tableWidget_ListadeCodigosAlarma"))
        self.tableWidget_ListadeCodigosAlarma.setColumnCount(3)
        self.tableWidget_ListadeCodigosAlarma.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ListadeCodigosAlarma.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ListadeCodigosAlarma.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ListadeCodigosAlarma.setHorizontalHeaderItem(2, item)
        self.gridLayout_3.addWidget(self.tableWidget_ListadeCodigosAlarma, 1, 0, 1, 5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_AgregarCodigoAlarma = QtGui.QPushButton(self.groupBox_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/4-Icone-plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AgregarCodigoAlarma.setIcon(icon1)
        self.pushButton_AgregarCodigoAlarma.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_AgregarCodigoAlarma.setFlat(True)
        self.pushButton_AgregarCodigoAlarma.setObjectName(_fromUtf8("pushButton_AgregarCodigoAlarma"))
        self.horizontalLayout_2.addWidget(self.pushButton_AgregarCodigoAlarma)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 5)
        self.comboBox_Grupos = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_Grupos.setObjectName(_fromUtf8("comboBox_Grupos"))
        self.gridLayout_3.addWidget(self.comboBox_Grupos, 0, 4, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 0, 3, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_4, 0, 0, 3, 1)
        self.groupBox_DatosCodigoAlarma = QtGui.QGroupBox(SubVentanaCodigosAlarma)
        self.groupBox_DatosCodigoAlarma.setObjectName(_fromUtf8("groupBox_DatosCodigoAlarma"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_DatosCodigoAlarma)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_ColorCodigoAlarma = QtGui.QPushButton(self.groupBox_DatosCodigoAlarma)
        self.pushButton_ColorCodigoAlarma.setStyleSheet(_fromUtf8(""))
        self.pushButton_ColorCodigoAlarma.setObjectName(_fromUtf8("pushButton_ColorCodigoAlarma"))
        self.gridLayout.addWidget(self.pushButton_ColorCodigoAlarma, 7, 3, 1, 1)
        self.lineEdit_DescripcionCodigoAlarma = QtGui.QLineEdit(self.groupBox_DatosCodigoAlarma)
        self.lineEdit_DescripcionCodigoAlarma.setMaxLength(100)
        self.lineEdit_DescripcionCodigoAlarma.setObjectName(_fromUtf8("lineEdit_DescripcionCodigoAlarma"))
        self.gridLayout.addWidget(self.lineEdit_DescripcionCodigoAlarma, 5, 3, 1, 3)
        self.label = QtGui.QLabel(self.groupBox_DatosCodigoAlarma)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 7, 4, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 8, 3, 1, 1)
        self.comboBox_GrupoCodigoAlarma = QtGui.QComboBox(self.groupBox_DatosCodigoAlarma)
        self.comboBox_GrupoCodigoAlarma.setObjectName(_fromUtf8("comboBox_GrupoCodigoAlarma"))
        self.gridLayout.addWidget(self.comboBox_GrupoCodigoAlarma, 3, 3, 1, 3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_GuardarCodigoAlarma = QtGui.QPushButton(self.groupBox_DatosCodigoAlarma)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_GuardarCodigoAlarma.setIcon(icon2)
        self.pushButton_GuardarCodigoAlarma.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_GuardarCodigoAlarma.setFlat(True)
        self.pushButton_GuardarCodigoAlarma.setObjectName(_fromUtf8("pushButton_GuardarCodigoAlarma"))
        self.horizontalLayout.addWidget(self.pushButton_GuardarCodigoAlarma)
        self.pushButton_BorrarCodigoAlarma = QtGui.QPushButton(self.groupBox_DatosCodigoAlarma)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/eraser-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_BorrarCodigoAlarma.setIcon(icon3)
        self.pushButton_BorrarCodigoAlarma.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_BorrarCodigoAlarma.setFlat(True)
        self.pushButton_BorrarCodigoAlarma.setObjectName(_fromUtf8("pushButton_BorrarCodigoAlarma"))
        self.horizontalLayout.addWidget(self.pushButton_BorrarCodigoAlarma)
        self.pushButton_Cancelar = QtGui.QPushButton(self.groupBox_DatosCodigoAlarma)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/uncheck.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Cancelar.setIcon(icon4)
        self.pushButton_Cancelar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Cancelar.setFlat(True)
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.horizontalLayout.addWidget(self.pushButton_Cancelar)
        self.gridLayout.addLayout(self.horizontalLayout, 11, 0, 1, 6)
        self.label_Descripcion = QtGui.QLabel(self.groupBox_DatosCodigoAlarma)
        self.label_Descripcion.setObjectName(_fromUtf8("label_Descripcion"))
        self.gridLayout.addWidget(self.label_Descripcion, 5, 0, 1, 3)
        self.label_2 = QtGui.QLabel(self.groupBox_DatosCodigoAlarma)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 3)
        self.label_5 = QtGui.QLabel(self.groupBox_DatosCodigoAlarma)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 2)
        self.label_6 = QtGui.QLabel(self.groupBox_DatosCodigoAlarma)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.spinBox_Prioridad = QtGui.QSpinBox(self.groupBox_DatosCodigoAlarma)
        self.spinBox_Prioridad.setMinimum(1)
        self.spinBox_Prioridad.setMaximum(9)
        self.spinBox_Prioridad.setProperty("value", 9)
        self.spinBox_Prioridad.setObjectName(_fromUtf8("spinBox_Prioridad"))
        self.gridLayout.addWidget(self.spinBox_Prioridad, 7, 5, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 3, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 4, 3, 1, 1)
        self.lineEdit_CodigoAlarma = QtGui.QLineEdit(self.groupBox_DatosCodigoAlarma)
        self.lineEdit_CodigoAlarma.setMaxLength(3)
        self.lineEdit_CodigoAlarma.setObjectName(_fromUtf8("lineEdit_CodigoAlarma"))
        self.gridLayout.addWidget(self.lineEdit_CodigoAlarma, 1, 3, 1, 3)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 6, 3, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_DatosCodigoAlarma, 0, 1, 3, 1)

        self.retranslateUi(SubVentanaCodigosAlarma)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaCodigosAlarma)

    def retranslateUi(self, SubVentanaCodigosAlarma):
        SubVentanaCodigosAlarma.setWindowTitle(_translate("SubVentanaCodigosAlarma", "Administracion de Codigos de Alarma", None))
        self.groupBox_4.setTitle(_translate("SubVentanaCodigosAlarma", "Lista de Codigos de Alarma", None))
        item = self.tableWidget_ListadeCodigosAlarma.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaCodigosAlarma", "Cod Alarma", None))
        item = self.tableWidget_ListadeCodigosAlarma.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaCodigosAlarma", "Descripcion", None))
        item = self.tableWidget_ListadeCodigosAlarma.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaCodigosAlarma", "Grupo", None))
        self.pushButton_AgregarCodigoAlarma.setToolTip(_translate("SubVentanaCodigosAlarma", "Agregar Nuevo Codigo", None))
        self.pushButton_AgregarCodigoAlarma.setText(_translate("SubVentanaCodigosAlarma", "Agregar", None))
        self.comboBox_Grupos.setToolTip(_translate("SubVentanaCodigosAlarma", "Seleccionar Grupo", None))
        self.label_3.setText(_translate("SubVentanaCodigosAlarma", "Grupos", None))
        self.groupBox_DatosCodigoAlarma.setTitle(_translate("SubVentanaCodigosAlarma", "Datos del Codigo de Alarma", None))
        self.pushButton_ColorCodigoAlarma.setText(_translate("SubVentanaCodigosAlarma", "...", None))
        self.label.setText(_translate("SubVentanaCodigosAlarma", "Prioridad:", None))
        self.pushButton_GuardarCodigoAlarma.setToolTip(_translate("SubVentanaCodigosAlarma", "Guardar Codigo de Alarma", None))
        self.pushButton_GuardarCodigoAlarma.setText(_translate("SubVentanaCodigosAlarma", "Guardar", None))
        self.pushButton_BorrarCodigoAlarma.setToolTip(_translate("SubVentanaCodigosAlarma", "Borrar Codigo de Alarma", None))
        self.pushButton_BorrarCodigoAlarma.setText(_translate("SubVentanaCodigosAlarma", "Borrar", None))
        self.pushButton_Cancelar.setToolTip(_translate("SubVentanaCodigosAlarma", "Cancelar Edicion", None))
        self.pushButton_Cancelar.setText(_translate("SubVentanaCodigosAlarma", "Cancelar", None))
        self.label_Descripcion.setText(_translate("SubVentanaCodigosAlarma", "Descripcion:", None))
        self.label_2.setText(_translate("SubVentanaCodigosAlarma", "Grupo:", None))
        self.label_5.setText(_translate("SubVentanaCodigosAlarma", "Codigo:", None))
        self.label_6.setText(_translate("SubVentanaCodigosAlarma", "Color:", None))

import recursos_rc
