# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaMonitoreoAlertas.ui'
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

class Ui_SubVentanaMonitorAlertas(object):
    def setupUi(self, SubVentanaMonitorAlertas):
        SubVentanaMonitorAlertas.setObjectName(_fromUtf8("SubVentanaMonitorAlertas"))
        SubVentanaMonitorAlertas.resize(724, 572)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Monitoreo_Alertas2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubVentanaMonitorAlertas.setWindowIcon(icon)
        SubVentanaMonitorAlertas.setStyleSheet(_fromUtf8("QTableView {\n"
"    color: #4d4e51;\n"
"    border: 1px solid #6d6e71;\n"
"    gridline-color: #9a9b9e; /* Color Grilla Celdas Internas: */\n"
"    background-color: #ffffff; /* Color Fondo Celdas Internas: */\n"
"    selection-color: #4d4e51;\n"
"    selection-background-color: #adc5ed;\n"
"    border-radius: 0px;\n"
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
"    border-radius: 0px;\n"
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
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
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
        self.gridLayout = QtGui.QGridLayout(SubVentanaMonitorAlertas)
        self.gridLayout.setMargin(6)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget_Cola = QtGui.QTableWidget(SubVentanaMonitorAlertas)
        self.tableWidget_Cola.setStyleSheet(_fromUtf8("font: bold 10pt \"Calibri\";"))
        self.tableWidget_Cola.setObjectName(_fromUtf8("tableWidget_Cola"))
        self.tableWidget_Cola.setColumnCount(4)
        self.tableWidget_Cola.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Cola.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Cola.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Cola.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Cola.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.tableWidget_Cola, 3, 0, 1, 1)
        self.tableWidget_Enviados = QtGui.QTableWidget(SubVentanaMonitorAlertas)
        self.tableWidget_Enviados.setStyleSheet(_fromUtf8("font: bold 10pt \"Calibri\";"))
        self.tableWidget_Enviados.setObjectName(_fromUtf8("tableWidget_Enviados"))
        self.tableWidget_Enviados.setColumnCount(4)
        self.tableWidget_Enviados.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Enviados.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Enviados.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Enviados.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Enviados.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.tableWidget_Enviados, 3, 1, 1, 1)
        self.tableWidget_Recibidos = QtGui.QTableWidget(SubVentanaMonitorAlertas)
        self.tableWidget_Recibidos.setStyleSheet(_fromUtf8("font: bold 10pt \"Calibri\";"))
        self.tableWidget_Recibidos.setObjectName(_fromUtf8("tableWidget_Recibidos"))
        self.tableWidget_Recibidos.setColumnCount(3)
        self.tableWidget_Recibidos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Recibidos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Recibidos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Recibidos.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.tableWidget_Recibidos, 3, 2, 1, 1)
        self.tableWidget_Log = QtGui.QTableWidget(SubVentanaMonitorAlertas)
        self.tableWidget_Log.setStyleSheet(_fromUtf8("font: bold 10pt \"Calibri\";"))
        self.tableWidget_Log.setObjectName(_fromUtf8("tableWidget_Log"))
        self.tableWidget_Log.setColumnCount(6)
        self.tableWidget_Log.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Log.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Log.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Log.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Log.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Log.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Log.setHorizontalHeaderItem(5, item)
        self.gridLayout.addWidget(self.tableWidget_Log, 1, 0, 1, 3)
        self.frame_2 = QtGui.QFrame(SubVentanaMonitorAlertas)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 52))
        self.frame_2.setStyleSheet(_fromUtf8("background-color: #38648B;\n"
"font: BOLD 10pt \"Calibri\";\n"
"color: rgb(255, 255, 255);"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_ColaMensajes = QtGui.QLabel(self.frame_2)
        self.label_ColaMensajes.setStyleSheet(_fromUtf8("font: bold 10pt \"Calibri\";"))
        self.label_ColaMensajes.setObjectName(_fromUtf8("label_ColaMensajes"))
        self.gridLayout_6.addWidget(self.label_ColaMensajes, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setStyleSheet(_fromUtf8("font: bold 10pt \"Calibri\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_6.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_MensajesRecibidos = QtGui.QLabel(self.frame_2)
        self.label_MensajesRecibidos.setStyleSheet(_fromUtf8("font: bold 10pt \"Calibri\";"))
        self.label_MensajesRecibidos.setObjectName(_fromUtf8("label_MensajesRecibidos"))
        self.gridLayout_6.addWidget(self.label_MensajesRecibidos, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 3)
        self.frame = QtGui.QFrame(SubVentanaMonitorAlertas)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 52))
        self.frame.setStyleSheet(_fromUtf8("background-color: #38648B;\n"
"font: BOLD 10pt \"Calibri\";\n"
"color: rgb(255, 255, 255);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_5 = QtGui.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setStyleSheet(_fromUtf8("font: bold 10pt \"Calibri\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_5.addWidget(self.label, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 3)

        self.retranslateUi(SubVentanaMonitorAlertas)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaMonitorAlertas)

    def retranslateUi(self, SubVentanaMonitorAlertas):
        SubVentanaMonitorAlertas.setWindowTitle(_translate("SubVentanaMonitorAlertas", "Monitor de Alertas", None))
        item = self.tableWidget_Cola.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaMonitorAlertas", "Cliente", None))
        item = self.tableWidget_Cola.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaMonitorAlertas", "Destino", None))
        item = self.tableWidget_Cola.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaMonitorAlertas", "Mensaje", None))
        item = self.tableWidget_Cola.horizontalHeaderItem(3)
        item.setText(_translate("SubVentanaMonitorAlertas", "Fecha", None))
        item = self.tableWidget_Enviados.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaMonitorAlertas", "Cliente", None))
        item = self.tableWidget_Enviados.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaMonitorAlertas", "Destino", None))
        item = self.tableWidget_Enviados.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaMonitorAlertas", "Mensaje", None))
        item = self.tableWidget_Enviados.horizontalHeaderItem(3)
        item.setText(_translate("SubVentanaMonitorAlertas", "Fecha", None))
        item = self.tableWidget_Recibidos.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaMonitorAlertas", "Desde", None))
        item = self.tableWidget_Recibidos.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaMonitorAlertas", "Mensaje", None))
        item = self.tableWidget_Recibidos.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaMonitorAlertas", "Fecha", None))
        item = self.tableWidget_Log.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaMonitorAlertas", "Protocolo", None))
        item = self.tableWidget_Log.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaMonitorAlertas", "Cliente", None))
        item = self.tableWidget_Log.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaMonitorAlertas", "Evento", None))
        item = self.tableWidget_Log.horizontalHeaderItem(3)
        item.setText(_translate("SubVentanaMonitorAlertas", "Zona/Usuario", None))
        item = self.tableWidget_Log.horizontalHeaderItem(4)
        item.setText(_translate("SubVentanaMonitorAlertas", "Linea", None))
        item = self.tableWidget_Log.horizontalHeaderItem(5)
        item.setText(_translate("SubVentanaMonitorAlertas", "Hora", None))
        self.label_ColaMensajes.setText(_translate("SubVentanaMonitorAlertas", "Cola de Mensajes", None))
        self.label_3.setText(_translate("SubVentanaMonitorAlertas", "Mensajes Enviados (Ultimos 100)", None))
        self.label_MensajesRecibidos.setText(_translate("SubVentanaMonitorAlertas", "Mensajes Recibidos", None))
        self.label.setText(_translate("SubVentanaMonitorAlertas", "Log de Señales Recibidas (Ultimas 100)", None))

import recursos_rc
