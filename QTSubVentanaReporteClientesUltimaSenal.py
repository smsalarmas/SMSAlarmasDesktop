# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaReporteClientesUltimaSenal.ui'
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

class Ui_SubVentanaReporteClientesUltimaSenal(object):
    def setupUi(self, SubVentanaReporteClientesUltimaSenal):
        SubVentanaReporteClientesUltimaSenal.setObjectName(_fromUtf8("SubVentanaReporteClientesUltimaSenal"))
        SubVentanaReporteClientesUltimaSenal.resize(860, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Cliente_ultima_senal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubVentanaReporteClientesUltimaSenal.setWindowIcon(icon)
        SubVentanaReporteClientesUltimaSenal.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout = QtGui.QGridLayout(SubVentanaReporteClientesUltimaSenal)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(SubVentanaReporteClientesUltimaSenal)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.comboBox_Grupo = QtGui.QComboBox(self.groupBox)
        self.comboBox_Grupo.setObjectName(_fromUtf8("comboBox_Grupo"))
        self.gridLayout_2.addWidget(self.comboBox_Grupo, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        self.comboBox_Tipo = QtGui.QComboBox(self.groupBox)
        self.comboBox_Tipo.setObjectName(_fromUtf8("comboBox_Tipo"))
        self.gridLayout_2.addWidget(self.comboBox_Tipo, 0, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 6, 1, 1)
        self.tableWidget_Reporte = QtGui.QTableWidget(self.groupBox)
        self.tableWidget_Reporte.setObjectName(_fromUtf8("tableWidget_Reporte"))
        self.tableWidget_Reporte.setColumnCount(4)
        self.tableWidget_Reporte.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Reporte.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Reporte.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Reporte.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Reporte.setHorizontalHeaderItem(3, item)
        self.gridLayout_2.addWidget(self.tableWidget_Reporte, 2, 0, 1, 7)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_Buscar = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Buscar.setObjectName(_fromUtf8("lineEdit_Buscar"))
        self.horizontalLayout.addWidget(self.lineEdit_Buscar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_PDF = QtGui.QPushButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/PDF.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_PDF.setIcon(icon1)
        self.pushButton_PDF.setFlat(True)
        self.pushButton_PDF.setObjectName(_fromUtf8("pushButton_PDF"))
        self.horizontalLayout.addWidget(self.pushButton_PDF)
        self.pushButton_XLS = QtGui.QPushButton(self.groupBox)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/XLS.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_XLS.setIcon(icon2)
        self.pushButton_XLS.setFlat(True)
        self.pushButton_XLS.setObjectName(_fromUtf8("pushButton_XLS"))
        self.horizontalLayout.addWidget(self.pushButton_XLS)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 7)
        self.pushButton_Generar = QtGui.QPushButton(self.groupBox)
        self.pushButton_Generar.setObjectName(_fromUtf8("pushButton_Generar"))
        self.gridLayout_2.addWidget(self.pushButton_Generar, 0, 4, 1, 1)
        self.pushButton_Reset = QtGui.QPushButton(self.groupBox)
        self.pushButton_Reset.setObjectName(_fromUtf8("pushButton_Reset"))
        self.gridLayout_2.addWidget(self.pushButton_Reset, 0, 5, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)
        self.frame = QtGui.QFrame(SubVentanaReporteClientesUltimaSenal)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame.setStyleSheet(_fromUtf8("background-color: #38648B;\n"
"font: 10pt \"Calibri\";\n"
"color: rgb(255, 255, 255);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_5 = QtGui.QGridLayout(self.frame)
        self.gridLayout_5.setContentsMargins(9, -1, 9, 9)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setStyleSheet(_fromUtf8("font: bold 12pt \"Calibri\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2)

        self.retranslateUi(SubVentanaReporteClientesUltimaSenal)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaReporteClientesUltimaSenal)

    def retranslateUi(self, SubVentanaReporteClientesUltimaSenal):
        SubVentanaReporteClientesUltimaSenal.setWindowTitle(_translate("SubVentanaReporteClientesUltimaSenal", "Reporte de Clientes Ultima Señal", None))
        self.groupBox.setTitle(_translate("SubVentanaReporteClientesUltimaSenal", "Reporte Detallado", None))
        self.label_3.setText(_translate("SubVentanaReporteClientesUltimaSenal", "Grupo:", None))
        self.label_4.setText(_translate("SubVentanaReporteClientesUltimaSenal", "Tipo:", None))
        item = self.tableWidget_Reporte.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaReporteClientesUltimaSenal", "Nombre del Cliente", None))
        item = self.tableWidget_Reporte.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaReporteClientesUltimaSenal", "Ultimo Evento", None))
        item = self.tableWidget_Reporte.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaReporteClientesUltimaSenal", "Fecha", None))
        item = self.tableWidget_Reporte.horizontalHeaderItem(3)
        item.setText(_translate("SubVentanaReporteClientesUltimaSenal", "Dias", None))
        self.label_2.setText(_translate("SubVentanaReporteClientesUltimaSenal", "Buscar:", None))
        self.pushButton_PDF.setText(_translate("SubVentanaReporteClientesUltimaSenal", "PDF", None))
        self.pushButton_XLS.setText(_translate("SubVentanaReporteClientesUltimaSenal", "XLS", None))
        self.pushButton_Generar.setText(_translate("SubVentanaReporteClientesUltimaSenal", "Generar", None))
        self.pushButton_Reset.setText(_translate("SubVentanaReporteClientesUltimaSenal", "Reset", None))
        self.label.setText(_translate("SubVentanaReporteClientesUltimaSenal", " Reporte Clientes Ultima Señal", None))

import recursos_rc
