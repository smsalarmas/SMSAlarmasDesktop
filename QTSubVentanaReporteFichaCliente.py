# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaReporteFichaCliente.ui'
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

class Ui_SubVentanaReporteFichaCliente(object):
    def setupUi(self, SubVentanaReporteFichaCliente):
        SubVentanaReporteFichaCliente.setObjectName(_fromUtf8("SubVentanaReporteFichaCliente"))
        SubVentanaReporteFichaCliente.resize(344, 254)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/ficha_cliente.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubVentanaReporteFichaCliente.setWindowIcon(icon)
        SubVentanaReporteFichaCliente.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout = QtGui.QGridLayout(SubVentanaReporteFichaCliente)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(SubVentanaReporteFichaCliente)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame.setStyleSheet(_fromUtf8("background-color: #38648B;\n"
"font: 10pt \"Calibri\";\n"
"color: rgb(255, 255, 255);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_5 = QtGui.QGridLayout(self.frame)
        self.gridLayout_5.setContentsMargins(-1, -1, -1, 9)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setStyleSheet(_fromUtf8("font: bold 12pt \"Calibri\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2)
        self.groupBox = QtGui.QGroupBox(SubVentanaReporteFichaCliente)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.checkBox_Zonas = QtGui.QCheckBox(self.groupBox)
        self.checkBox_Zonas.setObjectName(_fromUtf8("checkBox_Zonas"))
        self.gridLayout_2.addWidget(self.checkBox_Zonas, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.checkBox_Usuarios = QtGui.QCheckBox(self.groupBox)
        self.checkBox_Usuarios.setObjectName(_fromUtf8("checkBox_Usuarios"))
        self.gridLayout_2.addWidget(self.checkBox_Usuarios, 2, 1, 1, 1)
        self.checkBox_Contactos = QtGui.QCheckBox(self.groupBox)
        self.checkBox_Contactos.setObjectName(_fromUtf8("checkBox_Contactos"))
        self.gridLayout_2.addWidget(self.checkBox_Contactos, 3, 1, 1, 1)
        self.comboBox_Clientes = QtGui.QComboBox(self.groupBox)
        self.comboBox_Clientes.setObjectName(_fromUtf8("comboBox_Clientes"))
        self.gridLayout_2.addWidget(self.comboBox_Clientes, 0, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_XLS = QtGui.QPushButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/XLS.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_XLS.setIcon(icon1)
        self.pushButton_XLS.setObjectName(_fromUtf8("pushButton_XLS"))
        self.horizontalLayout.addWidget(self.pushButton_XLS)
        self.pushButton_PDF = QtGui.QPushButton(self.groupBox)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/PDF.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_PDF.setIcon(icon2)
        self.pushButton_PDF.setObjectName(_fromUtf8("pushButton_PDF"))
        self.horizontalLayout.addWidget(self.pushButton_PDF)
        self.gridLayout_2.addLayout(self.horizontalLayout, 5, 0, 1, 2)
        self.checkBox_Horarios = QtGui.QCheckBox(self.groupBox)
        self.checkBox_Horarios.setObjectName(_fromUtf8("checkBox_Horarios"))
        self.gridLayout_2.addWidget(self.checkBox_Horarios, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)

        self.retranslateUi(SubVentanaReporteFichaCliente)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaReporteFichaCliente)

    def retranslateUi(self, SubVentanaReporteFichaCliente):
        SubVentanaReporteFichaCliente.setWindowTitle(_translate("SubVentanaReporteFichaCliente", "Reporte de Ficha del Cliente", None))
        self.label.setText(_translate("SubVentanaReporteFichaCliente", "Reporte de la Ficha del Cliente", None))
        self.groupBox.setTitle(_translate("SubVentanaReporteFichaCliente", "Generar Reporte", None))
        self.label_2.setText(_translate("SubVentanaReporteFichaCliente", "Cuenta", None))
        self.checkBox_Zonas.setText(_translate("SubVentanaReporteFichaCliente", "Zonas", None))
        self.label_3.setText(_translate("SubVentanaReporteFichaCliente", "Seleccione Datos", None))
        self.checkBox_Usuarios.setText(_translate("SubVentanaReporteFichaCliente", "Usuarios", None))
        self.checkBox_Contactos.setText(_translate("SubVentanaReporteFichaCliente", "Contactos", None))
        self.pushButton_XLS.setText(_translate("SubVentanaReporteFichaCliente", "Generar XLS", None))
        self.pushButton_PDF.setText(_translate("SubVentanaReporteFichaCliente", "Generar PDF", None))
        self.checkBox_Horarios.setText(_translate("SubVentanaReporteFichaCliente", "Horarios", None))

import recursos_rc
