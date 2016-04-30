# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaMonitoreo.ui'
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

class Ui_SubVentanaMonitoreo(object):
    def setupUi(self, SubVentanaMonitoreo):
        SubVentanaMonitoreo.setObjectName(_fromUtf8("SubVentanaMonitoreo"))
        SubVentanaMonitoreo.resize(838, 595)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Monitoreo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubVentanaMonitoreo.setWindowIcon(icon)
        SubVentanaMonitoreo.setStyleSheet(_fromUtf8("QTableView {\n"
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
""))
        self.gridLayout_6 = QtGui.QGridLayout(SubVentanaMonitoreo)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.frame = QtGui.QFrame(SubVentanaMonitoreo)
        self.frame.setStyleSheet(_fromUtf8("background-color: #38648B;\n"
"font: 10pt \"Calibri\";\n"
"color: rgb(255, 255, 255);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_5 = QtGui.QGridLayout(self.frame)
        self.gridLayout_5.setContentsMargins(-1, -1, -1, 9)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.pushButton_Mapa = QtGui.QPushButton(self.frame)
        self.pushButton_Mapa.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/world91.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Mapa.setIcon(icon1)
        self.pushButton_Mapa.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_Mapa.setFlat(True)
        self.pushButton_Mapa.setObjectName(_fromUtf8("pushButton_Mapa"))
        self.gridLayout_5.addWidget(self.pushButton_Mapa, 0, 2, 1, 1)
        self.label_LogoMonitoreo = QtGui.QLabel(self.frame)
        self.label_LogoMonitoreo.setText(_fromUtf8(""))
        self.label_LogoMonitoreo.setPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/logomonitoreo.png")))
        self.label_LogoMonitoreo.setObjectName(_fromUtf8("label_LogoMonitoreo"))
        self.gridLayout_5.addWidget(self.label_LogoMonitoreo, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(389, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButton_CierreRapido = QtGui.QPushButton(self.frame)
        self.pushButton_CierreRapido.setStyleSheet(_fromUtf8("font: 75 10pt \"Calibri\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: #38648B;"))
        self.pushButton_CierreRapido.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/fast19.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_CierreRapido.setIcon(icon2)
        self.pushButton_CierreRapido.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_CierreRapido.setFlat(True)
        self.pushButton_CierreRapido.setObjectName(_fromUtf8("pushButton_CierreRapido"))
        self.gridLayout_5.addWidget(self.pushButton_CierreRapido, 0, 3, 1, 1)
        self.pushButton_Silenciar = QtGui.QPushButton(self.frame)
        self.pushButton_Silenciar.setStyleSheet(_fromUtf8("font: 75 10pt \"Calibri\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: #38648B;"))
        self.pushButton_Silenciar.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/speaker113.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Silenciar.setIcon(icon3)
        self.pushButton_Silenciar.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_Silenciar.setFlat(True)
        self.pushButton_Silenciar.setObjectName(_fromUtf8("pushButton_Silenciar"))
        self.gridLayout_5.addWidget(self.pushButton_Silenciar, 0, 4, 1, 1)
        self.pushButton_Pause = QtGui.QPushButton(self.frame)
        self.pushButton_Pause.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/pause41.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Pause.setIcon(icon4)
        self.pushButton_Pause.setFlat(True)
        self.pushButton_Pause.setObjectName(_fromUtf8("pushButton_Pause"))
        self.gridLayout_5.addWidget(self.pushButton_Pause, 0, 5, 1, 1)
        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 1)
        self.tabWidget_Monitoreo = QtGui.QTabWidget(SubVentanaMonitoreo)
        self.tabWidget_Monitoreo.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget_Monitoreo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget_Monitoreo.setStyleSheet(_fromUtf8("font: 75 BOLD 10pt \"Calibri\";"))
        self.tabWidget_Monitoreo.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_Monitoreo.setObjectName(_fromUtf8("tabWidget_Monitoreo"))
        self.tab_SenalesPorProcesar = QtGui.QWidget()
        self.tab_SenalesPorProcesar.setObjectName(_fromUtf8("tab_SenalesPorProcesar"))
        self.gridLayout = QtGui.QGridLayout(self.tab_SenalesPorProcesar)
        self.gridLayout.setMargin(9)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget_SenalesPorProcesar = QtGui.QTableWidget(self.tab_SenalesPorProcesar)
        self.tableWidget_SenalesPorProcesar.setStyleSheet(_fromUtf8(""))
        self.tableWidget_SenalesPorProcesar.setObjectName(_fromUtf8("tableWidget_SenalesPorProcesar"))
        self.tableWidget_SenalesPorProcesar.setColumnCount(6)
        self.tableWidget_SenalesPorProcesar.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SenalesPorProcesar.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SenalesPorProcesar.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SenalesPorProcesar.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SenalesPorProcesar.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SenalesPorProcesar.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SenalesPorProcesar.setHorizontalHeaderItem(5, item)
        self.gridLayout.addWidget(self.tableWidget_SenalesPorProcesar, 0, 0, 1, 1)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/85-Volume-son.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_Monitoreo.addTab(self.tab_SenalesPorProcesar, icon5, _fromUtf8(""))
        self.tab_SenalesPendientes = QtGui.QWidget()
        self.tab_SenalesPendientes.setObjectName(_fromUtf8("tab_SenalesPendientes"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_SenalesPendientes)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tableWidget_SenalesPendientes = QtGui.QTableWidget(self.tab_SenalesPendientes)
        self.tableWidget_SenalesPendientes.setObjectName(_fromUtf8("tableWidget_SenalesPendientes"))
        self.tableWidget_SenalesPendientes.setColumnCount(6)
        self.tableWidget_SenalesPendientes.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SenalesPendientes.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SenalesPendientes.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SenalesPendientes.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SenalesPendientes.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SenalesPendientes.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SenalesPendientes.setHorizontalHeaderItem(5, item)
        self.gridLayout_2.addWidget(self.tableWidget_SenalesPendientes, 0, 0, 1, 1)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/55-Trombone.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_Monitoreo.addTab(self.tab_SenalesPendientes, icon6, _fromUtf8(""))
        self.tab_TodasLasSenales = QtGui.QWidget()
        self.tab_TodasLasSenales.setObjectName(_fromUtf8("tab_TodasLasSenales"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_TodasLasSenales)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.tableWidget_TodasLasSenales = QtGui.QTableWidget(self.tab_TodasLasSenales)
        self.tableWidget_TodasLasSenales.setObjectName(_fromUtf8("tableWidget_TodasLasSenales"))
        self.tableWidget_TodasLasSenales.setColumnCount(6)
        self.tableWidget_TodasLasSenales.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_TodasLasSenales.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_TodasLasSenales.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_TodasLasSenales.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_TodasLasSenales.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_TodasLasSenales.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_TodasLasSenales.setHorizontalHeaderItem(5, item)
        self.gridLayout_4.addWidget(self.tableWidget_TodasLasSenales, 0, 0, 1, 1)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/20-Liste1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_Monitoreo.addTab(self.tab_TodasLasSenales, icon7, _fromUtf8(""))
        self.tab_SenalesProcesadas = QtGui.QWidget()
        self.tab_SenalesProcesadas.setObjectName(_fromUtf8("tab_SenalesProcesadas"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_SenalesProcesadas)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tableWidget_SenalesProcesadas = QtGui.QTableWidget(self.tab_SenalesProcesadas)
        self.tableWidget_SenalesProcesadas.setFrameShadow(QtGui.QFrame.Sunken)
        self.tableWidget_SenalesProcesadas.setShowGrid(False)
        self.tableWidget_SenalesProcesadas.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_SenalesProcesadas.setCornerButtonEnabled(True)
        self.tableWidget_SenalesProcesadas.setObjectName(_fromUtf8("tableWidget_SenalesProcesadas"))
        self.tableWidget_SenalesProcesadas.setColumnCount(7)
        self.tableWidget_SenalesProcesadas.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SenalesProcesadas.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SenalesProcesadas.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SenalesProcesadas.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SenalesProcesadas.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SenalesProcesadas.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SenalesProcesadas.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SenalesProcesadas.setHorizontalHeaderItem(6, item)
        self.gridLayout_3.addWidget(self.tableWidget_SenalesProcesadas, 0, 0, 1, 1)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Feedbin-Icon-check.svg.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_Monitoreo.addTab(self.tab_SenalesProcesadas, icon8, _fromUtf8(""))
        self.gridLayout_6.addWidget(self.tabWidget_Monitoreo, 2, 0, 1, 1)
        self.frame_ModoPause = QtGui.QFrame(SubVentanaMonitoreo)
        self.frame_ModoPause.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_ModoPause.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_ModoPause.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.frame_ModoPause.setFrameShape(QtGui.QFrame.Panel)
        self.frame_ModoPause.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_ModoPause.setLineWidth(1)
        self.frame_ModoPause.setObjectName(_fromUtf8("frame_ModoPause"))
        self.gridLayout_7 = QtGui.QGridLayout(self.frame_ModoPause)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame_ModoPause)
        self.label_3.setStyleSheet(_fromUtf8("font: bold 14pt \"MS Shell Dlg 2\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_7.addWidget(self.label_3, 0, 4, 1, 1)
        self.label = QtGui.QLabel(self.frame_ModoPause)
        self.label.setStyleSheet(_fromUtf8("\n"
"font: bold 14pt \"MS Shell Dlg 2\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_7.addWidget(self.label, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame_ModoPause)
        self.label_2.setMaximumSize(QtCore.QSize(45, 45))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/get-info-7.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_7.addWidget(self.label_2, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 0, 5, 1, 1)
        self.pushButton_aqui = QtGui.QPushButton(self.frame_ModoPause)
        self.pushButton_aqui.setMaximumSize(QtCore.QSize(47, 16777215))
        self.pushButton_aqui.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_aqui.setStyleSheet(_fromUtf8("font: bold 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color: rgb(0, 85, 255);"))
        self.pushButton_aqui.setCheckable(False)
        self.pushButton_aqui.setAutoRepeatInterval(1)
        self.pushButton_aqui.setDefault(False)
        self.pushButton_aqui.setFlat(True)
        self.pushButton_aqui.setObjectName(_fromUtf8("pushButton_aqui"))
        self.gridLayout_7.addWidget(self.pushButton_aqui, 0, 3, 1, 1)
        self.gridLayout_6.addWidget(self.frame_ModoPause, 1, 0, 1, 1)

        self.retranslateUi(SubVentanaMonitoreo)
        self.tabWidget_Monitoreo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaMonitoreo)

    def retranslateUi(self, SubVentanaMonitoreo):
        SubVentanaMonitoreo.setWindowTitle(_translate("SubVentanaMonitoreo", "Monitoreo de Señales", None))
        self.pushButton_Mapa.setToolTip(_translate("SubVentanaMonitoreo", "Ver Mapa", None))
        self.pushButton_Mapa.setStatusTip(_translate("SubVentanaMonitoreo", "Abrir Mapa de Ubicacion de Clientes", None))
        self.pushButton_CierreRapido.setToolTip(_translate("SubVentanaMonitoreo", "Cierre Rapido", None))
        self.pushButton_CierreRapido.setStatusTip(_translate("SubVentanaMonitoreo", "Cierre Rapido de Señales Masivamente", None))
        self.pushButton_Silenciar.setToolTip(_translate("SubVentanaMonitoreo", "Silenciar", None))
        self.pushButton_Silenciar.setStatusTip(_translate("SubVentanaMonitoreo", "Silenciar las Alertas del Monitoreo", None))
        self.pushButton_Pause.setToolTip(_translate("SubVentanaMonitoreo", "Pausar", None))
        self.pushButton_Pause.setStatusTip(_translate("SubVentanaMonitoreo", "Permite Pausar la Estacion (No Recibir mas Señales)", None))
        item = self.tableWidget_SenalesPorProcesar.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaMonitoreo", "#", None))
        item = self.tableWidget_SenalesPorProcesar.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaMonitoreo", "Cliente", None))
        item = self.tableWidget_SenalesPorProcesar.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaMonitoreo", "Evento", None))
        item = self.tableWidget_SenalesPorProcesar.horizontalHeaderItem(3)
        item.setText(_translate("SubVentanaMonitoreo", "Usuario / Zona", None))
        item = self.tableWidget_SenalesPorProcesar.horizontalHeaderItem(4)
        item.setText(_translate("SubVentanaMonitoreo", "Fecha", None))
        item = self.tableWidget_SenalesPorProcesar.horizontalHeaderItem(5)
        item.setText(_translate("SubVentanaMonitoreo", "Acciones", None))
        self.tabWidget_Monitoreo.setTabText(self.tabWidget_Monitoreo.indexOf(self.tab_SenalesPorProcesar), _translate("SubVentanaMonitoreo", "Señales por Procesar", None))
        item = self.tableWidget_SenalesPendientes.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaMonitoreo", "#", None))
        item = self.tableWidget_SenalesPendientes.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaMonitoreo", "Cliente", None))
        item = self.tableWidget_SenalesPendientes.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaMonitoreo", "Evento", None))
        item = self.tableWidget_SenalesPendientes.horizontalHeaderItem(3)
        item.setText(_translate("SubVentanaMonitoreo", "Usuario / Zona", None))
        item = self.tableWidget_SenalesPendientes.horizontalHeaderItem(4)
        item.setText(_translate("SubVentanaMonitoreo", "Fecha", None))
        item = self.tableWidget_SenalesPendientes.horizontalHeaderItem(5)
        item.setText(_translate("SubVentanaMonitoreo", "Acciones", None))
        self.tabWidget_Monitoreo.setTabText(self.tabWidget_Monitoreo.indexOf(self.tab_SenalesPendientes), _translate("SubVentanaMonitoreo", "Señales Pendientes", None))
        item = self.tableWidget_TodasLasSenales.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaMonitoreo", "#", None))
        item = self.tableWidget_TodasLasSenales.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaMonitoreo", "Cliente", None))
        item = self.tableWidget_TodasLasSenales.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaMonitoreo", "Evento", None))
        item = self.tableWidget_TodasLasSenales.horizontalHeaderItem(3)
        item.setText(_translate("SubVentanaMonitoreo", "Usuario / Zona", None))
        item = self.tableWidget_TodasLasSenales.horizontalHeaderItem(4)
        item.setText(_translate("SubVentanaMonitoreo", "Fecha", None))
        item = self.tableWidget_TodasLasSenales.horizontalHeaderItem(5)
        item.setText(_translate("SubVentanaMonitoreo", "Acciones", None))
        self.tabWidget_Monitoreo.setTabText(self.tabWidget_Monitoreo.indexOf(self.tab_TodasLasSenales), _translate("SubVentanaMonitoreo", "Todas las Señales", None))
        item = self.tableWidget_SenalesProcesadas.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaMonitoreo", "#", None))
        item = self.tableWidget_SenalesProcesadas.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaMonitoreo", "Cliente", None))
        item = self.tableWidget_SenalesProcesadas.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaMonitoreo", "Evento", None))
        item = self.tableWidget_SenalesProcesadas.horizontalHeaderItem(3)
        item.setText(_translate("SubVentanaMonitoreo", "Usuario / Zona", None))
        item = self.tableWidget_SenalesProcesadas.horizontalHeaderItem(4)
        item.setText(_translate("SubVentanaMonitoreo", "Observacion", None))
        item = self.tableWidget_SenalesProcesadas.horizontalHeaderItem(5)
        item.setText(_translate("SubVentanaMonitoreo", "Fecha Recepcion", None))
        item = self.tableWidget_SenalesProcesadas.horizontalHeaderItem(6)
        item.setText(_translate("SubVentanaMonitoreo", "Fecha Procesada", None))
        self.tabWidget_Monitoreo.setTabText(self.tabWidget_Monitoreo.indexOf(self.tab_SenalesProcesadas), _translate("SubVentanaMonitoreo", "Señales Procesadas", None))
        self.label_3.setText(_translate("SubVentanaMonitoreo", "para continuar", None))
        self.label.setText(_translate("SubVentanaMonitoreo", "Monitoreo se encuentra en modo PAUSE, presiona", None))
        self.pushButton_aqui.setText(_translate("SubVentanaMonitoreo", "aqui", None))

import recursos_rc
