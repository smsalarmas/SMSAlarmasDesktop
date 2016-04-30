# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTDialogProcesarSenal.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(908, 570)
        Dialog.setMinimumSize(QtCore.QSize(900, 570))
        Dialog.setMaximumSize(QtCore.QSize(908, 590))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Monitoreo_Alertas2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("QTableView {\n"
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
""))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setStyleSheet(_fromUtf8("font: 75 bold 10pt \"Calibri\";"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setMargin(2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.formFrame_3 = QtGui.QFrame(self.groupBox)
        self.formFrame_3.setMaximumSize(QtCore.QSize(428, 16777215))
        self.formFrame_3.setObjectName(_fromUtf8("formFrame_3"))
        self.formLayout_2 = QtGui.QFormLayout(self.formFrame_3)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_6 = QtGui.QLabel(self.formFrame_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_Empresa = QtGui.QLabel(self.formFrame_3)
        self.label_Empresa.setStyleSheet(_fromUtf8("font: 75  10pt \"Calibri\";"))
        self.label_Empresa.setText(_fromUtf8(""))
        self.label_Empresa.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_Empresa.setWordWrap(True)
        self.label_Empresa.setObjectName(_fromUtf8("label_Empresa"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_Empresa)
        self.label = QtGui.QLabel(self.formFrame_3)
        self.label.setStyleSheet(_fromUtf8("font: 75 bold 10pt \"Calibri\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.label_NombreCuenta = QtGui.QLabel(self.formFrame_3)
        self.label_NombreCuenta.setStyleSheet(_fromUtf8("font: 75  10pt \"Calibri\";"))
        self.label_NombreCuenta.setText(_fromUtf8(""))
        self.label_NombreCuenta.setWordWrap(True)
        self.label_NombreCuenta.setObjectName(_fromUtf8("label_NombreCuenta"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.label_NombreCuenta)
        self.label_3 = QtGui.QLabel(self.formFrame_3)
        self.label_3.setStyleSheet(_fromUtf8("font: 75 bold 10pt \"Calibri\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_Fecha = QtGui.QLabel(self.formFrame_3)
        self.label_Fecha.setStyleSheet(_fromUtf8("font: 75  10pt \"Calibri\";"))
        self.label_Fecha.setText(_fromUtf8(""))
        self.label_Fecha.setObjectName(_fromUtf8("label_Fecha"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.label_Fecha)
        self.label_5 = QtGui.QLabel(self.formFrame_3)
        self.label_5.setStyleSheet(_fromUtf8("font: 75 bold 10pt \"Calibri\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_Evento = QtGui.QLabel(self.formFrame_3)
        self.label_Evento.setStyleSheet(_fromUtf8("font: 75  10pt \"Calibri\";"))
        self.label_Evento.setText(_fromUtf8(""))
        self.label_Evento.setScaledContents(False)
        self.label_Evento.setWordWrap(True)
        self.label_Evento.setObjectName(_fromUtf8("label_Evento"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.label_Evento)
        self.horizontalLayout_2.addWidget(self.formFrame_3)
        self.formFrame = QtGui.QFrame(self.groupBox)
        self.formFrame.setMaximumSize(QtCore.QSize(428, 16777215))
        self.formFrame.setObjectName(_fromUtf8("formFrame"))
        self.formLayout = QtGui.QFormLayout(self.formFrame)
        self.formLayout.setMargin(5)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_18 = QtGui.QLabel(self.formFrame)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_18)
        self.label_Telefono = QtGui.QLabel(self.formFrame)
        self.label_Telefono.setStyleSheet(_fromUtf8("font: 75  10pt \"Calibri\";"))
        self.label_Telefono.setText(_fromUtf8(""))
        self.label_Telefono.setWordWrap(True)
        self.label_Telefono.setObjectName(_fromUtf8("label_Telefono"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_Telefono)
        self.label_7 = QtGui.QLabel(self.formFrame)
        self.label_7.setStyleSheet(_fromUtf8("font: 75 bold 10pt \"Calibri\";"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_Direccion = QtGui.QLabel(self.formFrame)
        self.label_Direccion.setStyleSheet(_fromUtf8("font: 75  10pt \"Calibri\";"))
        self.label_Direccion.setText(_fromUtf8(""))
        self.label_Direccion.setWordWrap(True)
        self.label_Direccion.setObjectName(_fromUtf8("label_Direccion"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.label_Direccion)
        self.label_8 = QtGui.QLabel(self.formFrame)
        self.label_8.setStyleSheet(_fromUtf8("font: 75 bold 10pt \"Calibri\";"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_8)
        self.label_Referencia = QtGui.QLabel(self.formFrame)
        self.label_Referencia.setStyleSheet(_fromUtf8("font: 75  10pt \"Calibri\";"))
        self.label_Referencia.setText(_fromUtf8(""))
        self.label_Referencia.setWordWrap(True)
        self.label_Referencia.setObjectName(_fromUtf8("label_Referencia"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.label_Referencia)
        self.label_9 = QtGui.QLabel(self.formFrame)
        self.label_9.setStyleSheet(_fromUtf8("font: 75 bold 10pt \"Calibri\";"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_9)
        self.label_Estatus = QtGui.QLabel(self.formFrame)
        self.label_Estatus.setStyleSheet(_fromUtf8("font: 75  10pt \"Calibri\";"))
        self.label_Estatus.setText(_fromUtf8(""))
        self.label_Estatus.setObjectName(_fromUtf8("label_Estatus"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.label_Estatus)
        self.label_FechaEstatus = QtGui.QLabel(self.formFrame)
        self.label_FechaEstatus.setStyleSheet(_fromUtf8("font: 75  10pt \"Calibri\";"))
        self.label_FechaEstatus.setText(_fromUtf8(""))
        self.label_FechaEstatus.setObjectName(_fromUtf8("label_FechaEstatus"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.label_FechaEstatus)
        self.label_2 = QtGui.QLabel(self.formFrame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_2.addWidget(self.formFrame)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget_CierreSenal = QtGui.QTabWidget(Dialog)
        self.tabWidget_CierreSenal.setStyleSheet(_fromUtf8("font: 75 bold 10pt \"Calibri\";"))
        self.tabWidget_CierreSenal.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget_CierreSenal.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget_CierreSenal.setIconSize(QtCore.QSize(25, 25))
        self.tabWidget_CierreSenal.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_CierreSenal.setUsesScrollButtons(True)
        self.tabWidget_CierreSenal.setObjectName(_fromUtf8("tabWidget_CierreSenal"))
        self.tab_Cierre = QtGui.QWidget()
        self.tab_Cierre.setObjectName(_fromUtf8("tab_Cierre"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_Cierre)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_17 = QtGui.QLabel(self.tab_Cierre)
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_17.setStyleSheet(_fromUtf8("font: 75 bold 10pt \"Calibri\";"))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_3.addWidget(self.label_17, 0, 0, 1, 1)
        self.label_20 = QtGui.QLabel(self.tab_Cierre)
        self.label_20.setStyleSheet(_fromUtf8("font: 75 bold 10pt \"Calibri\";"))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_3.addWidget(self.label_20, 0, 2, 1, 1)
        self.tableWidget_TimeLine = QtGui.QTableWidget(self.tab_Cierre)
        self.tableWidget_TimeLine.setMinimumSize(QtCore.QSize(430, 0))
        self.tableWidget_TimeLine.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget_TimeLine.setObjectName(_fromUtf8("tableWidget_TimeLine"))
        self.tableWidget_TimeLine.setColumnCount(3)
        self.tableWidget_TimeLine.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_TimeLine.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_TimeLine.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_TimeLine.setHorizontalHeaderItem(2, item)
        self.gridLayout_3.addWidget(self.tableWidget_TimeLine, 1, 0, 1, 2)
        self.tableWidget_SenalesPendientes = QtGui.QTableWidget(self.tab_Cierre)
        self.tableWidget_SenalesPendientes.setMinimumSize(QtCore.QSize(430, 0))
        self.tableWidget_SenalesPendientes.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget_SenalesPendientes.setStyleSheet(_fromUtf8("font: 75  10pt \"Calibri\";"))
        self.tableWidget_SenalesPendientes.setObjectName(_fromUtf8("tableWidget_SenalesPendientes"))
        self.tableWidget_SenalesPendientes.setColumnCount(3)
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
        self.gridLayout_3.addWidget(self.tableWidget_SenalesPendientes, 1, 2, 1, 1)
        self.label_15 = QtGui.QLabel(self.tab_Cierre)
        self.label_15.setStyleSheet(_fromUtf8("font: 75 bold 10pt \"Calibri\";"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 2, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.tab_Cierre)
        self.label_16.setStyleSheet(_fromUtf8("font: 75 bold 10pt \"Calibri\";"))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_3.addWidget(self.label_16, 3, 0, 1, 1)
        self.textEdit_Comentarios = QtGui.QTextEdit(self.tab_Cierre)
        self.textEdit_Comentarios.setMaximumSize(QtCore.QSize(16777215, 45))
        self.textEdit_Comentarios.setStyleSheet(_fromUtf8("font: 75  10pt \"Calibri\";"))
        self.textEdit_Comentarios.setObjectName(_fromUtf8("textEdit_Comentarios"))
        self.gridLayout_3.addWidget(self.textEdit_Comentarios, 3, 1, 1, 2)
        self.comboBox_MensajesPredefinidos = QtGui.QComboBox(self.tab_Cierre)
        self.comboBox_MensajesPredefinidos.setStyleSheet(_fromUtf8("font: 75  10pt \"Calibri\";"))
        self.comboBox_MensajesPredefinidos.setObjectName(_fromUtf8("comboBox_MensajesPredefinidos"))
        self.gridLayout_3.addWidget(self.comboBox_MensajesPredefinidos, 2, 1, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_Procesar = QtGui.QPushButton(self.tab_Cierre)
        self.pushButton_Procesar.setMinimumSize(QtCore.QSize(90, 0))
        self.pushButton_Procesar.setStyleSheet(_fromUtf8("background-color: #428BCA;\n"
"color: rgb(255, 255, 255);"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/save (2).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Procesar.setIcon(icon1)
        self.pushButton_Procesar.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_Procesar.setObjectName(_fromUtf8("pushButton_Procesar"))
        self.horizontalLayout.addWidget(self.pushButton_Procesar)
        self.pushButton_Pendiente = QtGui.QPushButton(self.tab_Cierre)
        self.pushButton_Pendiente.setMinimumSize(QtCore.QSize(90, 0))
        self.pushButton_Pendiente.setStyleSheet(_fromUtf8("background-color:#E87E04;\n"
"color: rgb(255, 255, 255);"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/visibility1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Pendiente.setIcon(icon2)
        self.pushButton_Pendiente.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_Pendiente.setObjectName(_fromUtf8("pushButton_Pendiente"))
        self.horizontalLayout.addWidget(self.pushButton_Pendiente)
        self.pushButton_Cancelar = QtGui.QPushButton(self.tab_Cierre)
        self.pushButton_Cancelar.setMinimumSize(QtCore.QSize(90, 0))
        self.pushButton_Cancelar.setStyleSheet(_fromUtf8("background-color:#D91E18;\n"
"color: rgb(255, 255, 255);"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/cancel45.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Cancelar.setIcon(icon3)
        self.pushButton_Cancelar.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_Cancelar.setDefault(False)
        self.pushButton_Cancelar.setFlat(False)
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.horizontalLayout.addWidget(self.pushButton_Cancelar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.horizontalLayout, 4, 0, 1, 3)
        self.label_16.raise_()
        self.textEdit_Comentarios.raise_()
        self.tableWidget_TimeLine.raise_()
        self.comboBox_MensajesPredefinidos.raise_()
        self.label_20.raise_()
        self.label_17.raise_()
        self.label_15.raise_()
        self.tableWidget_SenalesPendientes.raise_()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_CierreSenal.addTab(self.tab_Cierre, icon4, _fromUtf8(""))
        self.tab_DatosCliente = QtGui.QWidget()
        self.tab_DatosCliente.setObjectName(_fromUtf8("tab_DatosCliente"))
        self.gridLayout_9 = QtGui.QGridLayout(self.tab_DatosCliente)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.groupBox_19 = QtGui.QGroupBox(self.tab_DatosCliente)
        self.groupBox_19.setObjectName(_fromUtf8("groupBox_19"))
        self.gridLayout_45 = QtGui.QGridLayout(self.groupBox_19)
        self.gridLayout_45.setObjectName(_fromUtf8("gridLayout_45"))
        self.tableWidget_Usuarios = QtGui.QTableWidget(self.groupBox_19)
        self.tableWidget_Usuarios.setStyleSheet(_fromUtf8("QTableView {\n"
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
""))
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
        self.gridLayout_45.addWidget(self.tableWidget_Usuarios, 0, 0, 1, 2)
        self.gridLayout_9.addWidget(self.groupBox_19, 0, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.tab_DatosCliente)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(350, 16777215))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.tableWidget_ContactosEmergencia = QtGui.QTableWidget(self.groupBox_4)
        self.tableWidget_ContactosEmergencia.setStyleSheet(_fromUtf8("font: 10pt \"Calibri\";"))
        self.tableWidget_ContactosEmergencia.setObjectName(_fromUtf8("tableWidget_ContactosEmergencia"))
        self.tableWidget_ContactosEmergencia.setColumnCount(3)
        self.tableWidget_ContactosEmergencia.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ContactosEmergencia.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ContactosEmergencia.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ContactosEmergencia.setHorizontalHeaderItem(2, item)
        self.gridLayout_7.addWidget(self.tableWidget_ContactosEmergencia, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_4, 0, 1, 2, 1)
        self.groupBox_13 = QtGui.QGroupBox(self.tab_DatosCliente)
        self.groupBox_13.setStyleSheet(_fromUtf8(""))
        self.groupBox_13.setObjectName(_fromUtf8("groupBox_13"))
        self.gridLayout_21 = QtGui.QGridLayout(self.groupBox_13)
        self.gridLayout_21.setObjectName(_fromUtf8("gridLayout_21"))
        self.tableWidget_Zonas = QtGui.QTableWidget(self.groupBox_13)
        self.tableWidget_Zonas.setStyleSheet(_fromUtf8("QTableView {\n"
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
""))
        self.tableWidget_Zonas.setObjectName(_fromUtf8("tableWidget_Zonas"))
        self.tableWidget_Zonas.setColumnCount(3)
        self.tableWidget_Zonas.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_Zonas.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Zonas.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Zonas.setHorizontalHeaderItem(2, item)
        self.gridLayout_21.addWidget(self.tableWidget_Zonas, 1, 1, 1, 2)
        self.gridLayout_9.addWidget(self.groupBox_13, 1, 0, 1, 1)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/listaClientes3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_CierreSenal.addTab(self.tab_DatosCliente, icon5, _fromUtf8(""))
        self.tab_Senales = QtGui.QWidget()
        self.tab_Senales.setObjectName(_fromUtf8("tab_Senales"))
        self.gridLayout_20 = QtGui.QGridLayout(self.tab_Senales)
        self.gridLayout_20.setObjectName(_fromUtf8("gridLayout_20"))
        self.groupBox_12 = QtGui.QGroupBox(self.tab_Senales)
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.gridLayout_19 = QtGui.QGridLayout(self.groupBox_12)
        self.gridLayout_19.setObjectName(_fromUtf8("gridLayout_19"))
        self.comboBox_FechaHistorialSenales = QtGui.QComboBox(self.groupBox_12)
        self.comboBox_FechaHistorialSenales.setObjectName(_fromUtf8("comboBox_FechaHistorialSenales"))
        self.gridLayout_19.addWidget(self.comboBox_FechaHistorialSenales, 0, 10, 1, 1)
        self.pushButton_BuscarAvanzado = QtGui.QPushButton(self.groupBox_12)
        self.pushButton_BuscarAvanzado.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/6-Loupe.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_BuscarAvanzado.setIcon(icon6)
        self.pushButton_BuscarAvanzado.setDefault(False)
        self.pushButton_BuscarAvanzado.setFlat(True)
        self.pushButton_BuscarAvanzado.setObjectName(_fromUtf8("pushButton_BuscarAvanzado"))
        self.gridLayout_19.addWidget(self.pushButton_BuscarAvanzado, 0, 8, 1, 1)
        self.dateEdit_FechaHasta = QtGui.QDateEdit(self.groupBox_12)
        self.dateEdit_FechaHasta.setEnabled(True)
        self.dateEdit_FechaHasta.setCalendarPopup(True)
        self.dateEdit_FechaHasta.setObjectName(_fromUtf8("dateEdit_FechaHasta"))
        self.gridLayout_19.addWidget(self.dateEdit_FechaHasta, 0, 5, 1, 1)
        self.label_FechaHistorialSenales = QtGui.QLabel(self.groupBox_12)
        self.label_FechaHistorialSenales.setObjectName(_fromUtf8("label_FechaHistorialSenales"))
        self.gridLayout_19.addWidget(self.label_FechaHistorialSenales, 0, 9, 1, 1)
        self.label_22 = QtGui.QLabel(self.groupBox_12)
        self.label_22.setEnabled(True)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_19.addWidget(self.label_22, 0, 6, 1, 1)
        self.comboBox_Eventos = QtGui.QComboBox(self.groupBox_12)
        self.comboBox_Eventos.setEnabled(True)
        self.comboBox_Eventos.setObjectName(_fromUtf8("comboBox_Eventos"))
        self.gridLayout_19.addWidget(self.comboBox_Eventos, 0, 7, 1, 1)
        self.tableWidget_Senales = QtGui.QTableWidget(self.groupBox_12)
        self.tableWidget_Senales.setStyleSheet(_fromUtf8("QTableView {\n"
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
""))
        self.tableWidget_Senales.setObjectName(_fromUtf8("tableWidget_Senales"))
        self.tableWidget_Senales.setColumnCount(4)
        self.tableWidget_Senales.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Senales.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Senales.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Senales.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Senales.setHorizontalHeaderItem(3, item)
        self.gridLayout_19.addWidget(self.tableWidget_Senales, 2, 0, 1, 13)
        self.label_12 = QtGui.QLabel(self.groupBox_12)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_19.addWidget(self.label_12, 0, 2, 1, 1)
        self.pushButton_SelectorBusqueda = QtGui.QPushButton(self.groupBox_12)
        self.pushButton_SelectorBusqueda.setObjectName(_fromUtf8("pushButton_SelectorBusqueda"))
        self.gridLayout_19.addWidget(self.pushButton_SelectorBusqueda, 0, 0, 1, 1)
        self.dateEdit_FechaDesde = QtGui.QDateEdit(self.groupBox_12)
        self.dateEdit_FechaDesde.setEnabled(True)
        self.dateEdit_FechaDesde.setCalendarPopup(True)
        self.dateEdit_FechaDesde.setObjectName(_fromUtf8("dateEdit_FechaDesde"))
        self.gridLayout_19.addWidget(self.dateEdit_FechaDesde, 0, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem2, 0, 11, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox_12)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_19.addWidget(self.label_14, 0, 4, 1, 1)
        self.gridLayout_20.addWidget(self.groupBox_12, 0, 0, 1, 1)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Ven_Rep_avtivaciones.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_CierreSenal.addTab(self.tab_Senales, icon7, _fromUtf8(""))
        self.tab_Camaras = QtGui.QWidget()
        self.tab_Camaras.setObjectName(_fromUtf8("tab_Camaras"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_Camaras)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.groupBox_11 = QtGui.QGroupBox(self.tab_Camaras)
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.gridLayout_38 = QtGui.QGridLayout(self.groupBox_11)
        self.gridLayout_38.setObjectName(_fromUtf8("gridLayout_38"))
        self.treeWidget_Camaras = QtGui.QTreeWidget(self.groupBox_11)
        self.treeWidget_Camaras.setObjectName(_fromUtf8("treeWidget_Camaras"))
        self.gridLayout_38.addWidget(self.treeWidget_Camaras, 0, 0, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox_11, 0, 0, 1, 1)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/CCTVICON.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_CierreSenal.addTab(self.tab_Camaras, icon8, _fromUtf8(""))
        self.tab_Mapas = QtGui.QWidget()
        self.tab_Mapas.setObjectName(_fromUtf8("tab_Mapas"))
        self.gridLayout_12 = QtGui.QGridLayout(self.tab_Mapas)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab_Mapas)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.gridLayout_14 = QtGui.QGridLayout(self.groupBox_7)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.gridLayout_12.addWidget(self.groupBox_7, 0, 0, 1, 1)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Maps.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_CierreSenal.addTab(self.tab_Mapas, icon9, _fromUtf8(""))
        self.tab_Foto = QtGui.QWidget()
        self.tab_Foto.setObjectName(_fromUtf8("tab_Foto"))
        self.gridLayout_13 = QtGui.QGridLayout(self.tab_Foto)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.horizontalLayout_Imagen = QtGui.QHBoxLayout()
        self.horizontalLayout_Imagen.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout_Imagen.setObjectName(_fromUtf8("horizontalLayout_Imagen"))
        self.gridLayout_13.addLayout(self.horizontalLayout_Imagen, 0, 0, 1, 1)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/picture-attach.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_CierreSenal.addTab(self.tab_Foto, icon10, _fromUtf8(""))
        self.tab_CierreRapido = QtGui.QWidget()
        self.tab_CierreRapido.setObjectName(_fromUtf8("tab_CierreRapido"))
        self.gridLayout_11 = QtGui.QGridLayout(self.tab_CierreRapido)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab_CierreRapido)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout_10 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.radioButton_SenalesSeleccionadas = QtGui.QRadioButton(self.groupBox_6)
        self.radioButton_SenalesSeleccionadas.setObjectName(_fromUtf8("radioButton_SenalesSeleccionadas"))
        self.gridLayout_10.addWidget(self.radioButton_SenalesSeleccionadas, 0, 0, 1, 1)
        self.radioButton_PorCodigodeEvento = QtGui.QRadioButton(self.groupBox_6)
        self.radioButton_PorCodigodeEvento.setObjectName(_fromUtf8("radioButton_PorCodigodeEvento"))
        self.gridLayout_10.addWidget(self.radioButton_PorCodigodeEvento, 1, 0, 1, 1)
        self.radioButton_PorCodigoAlarma = QtGui.QRadioButton(self.groupBox_6)
        self.radioButton_PorCodigoAlarma.setObjectName(_fromUtf8("radioButton_PorCodigoAlarma"))
        self.gridLayout_10.addWidget(self.radioButton_PorCodigoAlarma, 0, 2, 1, 1)
        self.radioButton_PorCliente = QtGui.QRadioButton(self.groupBox_6)
        self.radioButton_PorCliente.setObjectName(_fromUtf8("radioButton_PorCliente"))
        self.gridLayout_10.addWidget(self.radioButton_PorCliente, 0, 1, 1, 1)
        self.radioButton_TodasLasSenales = QtGui.QRadioButton(self.groupBox_6)
        self.radioButton_TodasLasSenales.setObjectName(_fromUtf8("radioButton_TodasLasSenales"))
        self.gridLayout_10.addWidget(self.radioButton_TodasLasSenales, 1, 1, 1, 1)
        self.gridLayout_11.addWidget(self.groupBox_6, 0, 0, 1, 4)
        self.label_10 = QtGui.QLabel(self.tab_CierreRapido)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_11.addWidget(self.label_10, 4, 0, 1, 1)
        self.textEdit_ComentarioCierreRapido = QtGui.QTextEdit(self.tab_CierreRapido)
        self.textEdit_ComentarioCierreRapido.setMaximumSize(QtCore.QSize(16777215, 50))
        self.textEdit_ComentarioCierreRapido.setStyleSheet(_fromUtf8("font: 75  10pt \"Calibri\";"))
        self.textEdit_ComentarioCierreRapido.setObjectName(_fromUtf8("textEdit_ComentarioCierreRapido"))
        self.gridLayout_11.addWidget(self.textEdit_ComentarioCierreRapido, 5, 0, 1, 3)
        self.pushButton_Procesar_2 = QtGui.QPushButton(self.tab_CierreRapido)
        self.pushButton_Procesar_2.setMinimumSize(QtCore.QSize(35, 35))
        self.pushButton_Procesar_2.setMaximumSize(QtCore.QSize(125, 35))
        self.pushButton_Procesar_2.setStyleSheet(_fromUtf8("background-color: #428BCA;\n"
"color: rgb(255, 255, 255);"))
        self.pushButton_Procesar_2.setIcon(icon1)
        self.pushButton_Procesar_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_Procesar_2.setFlat(False)
        self.pushButton_Procesar_2.setObjectName(_fromUtf8("pushButton_Procesar_2"))
        self.gridLayout_11.addWidget(self.pushButton_Procesar_2, 5, 3, 1, 1)
        self.tableWidget_SeleccionQueSenales = QtGui.QTableWidget(self.tab_CierreRapido)
        self.tableWidget_SeleccionQueSenales.setStyleSheet(_fromUtf8("QTableView {\n"
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
""))
        self.tableWidget_SeleccionQueSenales.setObjectName(_fromUtf8("tableWidget_SeleccionQueSenales"))
        self.tableWidget_SeleccionQueSenales.setColumnCount(3)
        self.tableWidget_SeleccionQueSenales.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SeleccionQueSenales.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SeleccionQueSenales.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_SeleccionQueSenales.setHorizontalHeaderItem(2, item)
        self.gridLayout_11.addWidget(self.tableWidget_SeleccionQueSenales, 1, 0, 1, 4)
        self.comboBox_MensajesPrefefinidosCierreRapido = QtGui.QComboBox(self.tab_CierreRapido)
        self.comboBox_MensajesPrefefinidosCierreRapido.setStyleSheet(_fromUtf8("font: 75  10pt \"Calibri\";"))
        self.comboBox_MensajesPrefefinidosCierreRapido.setObjectName(_fromUtf8("comboBox_MensajesPrefefinidosCierreRapido"))
        self.gridLayout_11.addWidget(self.comboBox_MensajesPrefefinidosCierreRapido, 3, 0, 1, 4)
        self.label_4 = QtGui.QLabel(self.tab_CierreRapido)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_11.addWidget(self.label_4, 2, 0, 1, 2)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/fastbue.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_CierreSenal.addTab(self.tab_CierreRapido, icon11, _fromUtf8(""))
        self.tab_Notas = QtGui.QWidget()
        self.tab_Notas.setObjectName(_fromUtf8("tab_Notas"))
        self.gridLayout_15 = QtGui.QGridLayout(self.tab_Notas)
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.groupBox_8 = QtGui.QGroupBox(self.tab_Notas)
        self.groupBox_8.setStyleSheet(_fromUtf8(""))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_8)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_9 = QtGui.QGroupBox(self.groupBox_8)
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.gridLayout_16 = QtGui.QGridLayout(self.groupBox_9)
        self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
        self.textEdit_NotaFija = QtGui.QTextEdit(self.groupBox_9)
        self.textEdit_NotaFija.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);\n"
"font: bold 18pt \"Calibri\";\n"
"color: rgb(255, 255, 255);"))
        self.textEdit_NotaFija.setReadOnly(True)
        self.textEdit_NotaFija.setObjectName(_fromUtf8("textEdit_NotaFija"))
        self.gridLayout_16.addWidget(self.textEdit_NotaFija, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_9, 0, 0, 1, 1)
        self.groupBox_10 = QtGui.QGroupBox(self.groupBox_8)
        self.groupBox_10.setMinimumSize(QtCore.QSize(430, 0))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.gridLayout_17 = QtGui.QGridLayout(self.groupBox_10)
        self.gridLayout_17.setObjectName(_fromUtf8("gridLayout_17"))
        self.label_11 = QtGui.QLabel(self.groupBox_10)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_17.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_FechaInicio = QtGui.QLabel(self.groupBox_10)
        self.label_FechaInicio.setText(_fromUtf8(""))
        self.label_FechaInicio.setObjectName(_fromUtf8("label_FechaInicio"))
        self.gridLayout_17.addWidget(self.label_FechaInicio, 0, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.groupBox_10)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_17.addWidget(self.label_19, 1, 0, 1, 1)
        self.label_FechaFin = QtGui.QLabel(self.groupBox_10)
        self.label_FechaFin.setText(_fromUtf8(""))
        self.label_FechaFin.setObjectName(_fromUtf8("label_FechaFin"))
        self.gridLayout_17.addWidget(self.label_FechaFin, 1, 1, 1, 1)
        self.textEdit_NotaTemp = QtGui.QTextEdit(self.groupBox_10)
        self.textEdit_NotaTemp.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);\n"
"font: bold 18pt \"Calibri\";\n"
"color: rgb(255, 255, 255);"))
        self.textEdit_NotaTemp.setReadOnly(True)
        self.textEdit_NotaTemp.setObjectName(_fromUtf8("textEdit_NotaTemp"))
        self.gridLayout_17.addWidget(self.textEdit_NotaTemp, 2, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_10, 0, 1, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox_8, 0, 0, 1, 1)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/note_text-edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_CierreSenal.addTab(self.tab_Notas, icon12, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget_CierreSenal, 2, 0, 1, 1)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_pic = QtGui.QPushButton(self.frame)
        self.pushButton_pic.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_pic.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_pic.setText(_fromUtf8(""))
        self.pushButton_pic.setIcon(icon10)
        self.pushButton_pic.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_pic.setAutoDefault(False)
        self.pushButton_pic.setFlat(True)
        self.pushButton_pic.setObjectName(_fromUtf8("pushButton_pic"))
        self.horizontalLayout_3.addWidget(self.pushButton_pic)
        self.pushButton_cam = QtGui.QPushButton(self.frame)
        self.pushButton_cam.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_cam.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_cam.setText(_fromUtf8(""))
        self.pushButton_cam.setIcon(icon8)
        self.pushButton_cam.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_cam.setAutoDefault(False)
        self.pushButton_cam.setDefault(False)
        self.pushButton_cam.setFlat(True)
        self.pushButton_cam.setObjectName(_fromUtf8("pushButton_cam"))
        self.horizontalLayout_3.addWidget(self.pushButton_cam)
        self.pushButton_key = QtGui.QPushButton(self.frame)
        self.pushButton_key.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_key.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_key.setText(_fromUtf8(""))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/key.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_key.setIcon(icon13)
        self.pushButton_key.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_key.setAutoDefault(False)
        self.pushButton_key.setFlat(True)
        self.pushButton_key.setObjectName(_fromUtf8("pushButton_key"))
        self.horizontalLayout_3.addWidget(self.pushButton_key)
        self.pushButton_clavemaster = QtGui.QPushButton(self.frame)
        self.pushButton_clavemaster.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_clavemaster.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_clavemaster.setText(_fromUtf8(""))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/lock yellow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_clavemaster.setIcon(icon14)
        self.pushButton_clavemaster.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_clavemaster.setAutoDefault(False)
        self.pushButton_clavemaster.setFlat(True)
        self.pushButton_clavemaster.setObjectName(_fromUtf8("pushButton_clavemaster"))
        self.horizontalLayout_3.addWidget(self.pushButton_clavemaster)
        self.pushButton_sms = QtGui.QPushButton(self.frame)
        self.pushButton_sms.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_sms.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_sms.setText(_fromUtf8(""))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/unnamed.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_sms.setIcon(icon15)
        self.pushButton_sms.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_sms.setAutoDefault(False)
        self.pushButton_sms.setFlat(True)
        self.pushButton_sms.setObjectName(_fromUtf8("pushButton_sms"))
        self.horizontalLayout_3.addWidget(self.pushButton_sms)
        self.pushButton_mail = QtGui.QPushButton(self.frame)
        self.pushButton_mail.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_mail.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_mail.setText(_fromUtf8(""))
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/mailbueno.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_mail.setIcon(icon16)
        self.pushButton_mail.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_mail.setAutoDefault(False)
        self.pushButton_mail.setFlat(True)
        self.pushButton_mail.setObjectName(_fromUtf8("pushButton_mail"))
        self.horizontalLayout_3.addWidget(self.pushButton_mail)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget_CierreSenal.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.pushButton_pic, self.pushButton_cam)
        Dialog.setTabOrder(self.pushButton_cam, self.tabWidget_CierreSenal)
        Dialog.setTabOrder(self.tabWidget_CierreSenal, self.comboBox_MensajesPredefinidos)
        Dialog.setTabOrder(self.comboBox_MensajesPredefinidos, self.textEdit_Comentarios)
        Dialog.setTabOrder(self.textEdit_Comentarios, self.pushButton_Procesar)
        Dialog.setTabOrder(self.pushButton_Procesar, self.pushButton_Pendiente)
        Dialog.setTabOrder(self.pushButton_Pendiente, self.pushButton_Cancelar)
        Dialog.setTabOrder(self.pushButton_Cancelar, self.tableWidget_TimeLine)
        Dialog.setTabOrder(self.tableWidget_TimeLine, self.tableWidget_SenalesPendientes)
        Dialog.setTabOrder(self.tableWidget_SenalesPendientes, self.tableWidget_Usuarios)
        Dialog.setTabOrder(self.tableWidget_Usuarios, self.tableWidget_ContactosEmergencia)
        Dialog.setTabOrder(self.tableWidget_ContactosEmergencia, self.tableWidget_Zonas)
        Dialog.setTabOrder(self.tableWidget_Zonas, self.comboBox_FechaHistorialSenales)
        Dialog.setTabOrder(self.comboBox_FechaHistorialSenales, self.pushButton_BuscarAvanzado)
        Dialog.setTabOrder(self.pushButton_BuscarAvanzado, self.dateEdit_FechaHasta)
        Dialog.setTabOrder(self.dateEdit_FechaHasta, self.comboBox_Eventos)
        Dialog.setTabOrder(self.comboBox_Eventos, self.tableWidget_Senales)
        Dialog.setTabOrder(self.tableWidget_Senales, self.pushButton_SelectorBusqueda)
        Dialog.setTabOrder(self.pushButton_SelectorBusqueda, self.dateEdit_FechaDesde)
        Dialog.setTabOrder(self.dateEdit_FechaDesde, self.treeWidget_Camaras)
        Dialog.setTabOrder(self.treeWidget_Camaras, self.radioButton_SenalesSeleccionadas)
        Dialog.setTabOrder(self.radioButton_SenalesSeleccionadas, self.radioButton_PorCodigodeEvento)
        Dialog.setTabOrder(self.radioButton_PorCodigodeEvento, self.radioButton_PorCodigoAlarma)
        Dialog.setTabOrder(self.radioButton_PorCodigoAlarma, self.radioButton_PorCliente)
        Dialog.setTabOrder(self.radioButton_PorCliente, self.radioButton_TodasLasSenales)
        Dialog.setTabOrder(self.radioButton_TodasLasSenales, self.textEdit_ComentarioCierreRapido)
        Dialog.setTabOrder(self.textEdit_ComentarioCierreRapido, self.pushButton_Procesar_2)
        Dialog.setTabOrder(self.pushButton_Procesar_2, self.tableWidget_SeleccionQueSenales)
        Dialog.setTabOrder(self.tableWidget_SeleccionQueSenales, self.comboBox_MensajesPrefefinidosCierreRapido)
        Dialog.setTabOrder(self.comboBox_MensajesPrefefinidosCierreRapido, self.textEdit_NotaFija)
        Dialog.setTabOrder(self.textEdit_NotaFija, self.textEdit_NotaTemp)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Cierre de Señal", None))
        self.groupBox.setTitle(_translate("Dialog", "Datos de la Cuenta", None))
        self.label_6.setText(_translate("Dialog", "Empresa:", None))
        self.label.setText(_translate("Dialog", "Nombre:", None))
        self.label_3.setText(_translate("Dialog", "Fecha:", None))
        self.label_5.setText(_translate("Dialog", "Evento:", None))
        self.label_18.setText(_translate("Dialog", "Telefono:", None))
        self.label_7.setText(_translate("Dialog", "Direccion:", None))
        self.label_8.setText(_translate("Dialog", "Referencia:", None))
        self.label_9.setText(_translate("Dialog", "Estatus:", None))
        self.label_2.setText(_translate("Dialog", "Fecha:", None))
        self.label_17.setText(_translate("Dialog", "Historial de la Senal", None))
        self.label_20.setText(_translate("Dialog", "Pendientes Cliente", None))
        item = self.tableWidget_TimeLine.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Fecha", None))
        item = self.tableWidget_TimeLine.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Observacion", None))
        item = self.tableWidget_TimeLine.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Operador", None))
        item = self.tableWidget_SenalesPendientes.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Seleccion", None))
        item = self.tableWidget_SenalesPendientes.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Fecha", None))
        item = self.tableWidget_SenalesPendientes.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Señal", None))
        self.label_15.setText(_translate("Dialog", "Mensaje Predefinido:", None))
        self.label_16.setText(_translate("Dialog", "Comentario:", None))
        self.pushButton_Procesar.setText(_translate("Dialog", "Procesar", None))
        self.pushButton_Pendiente.setText(_translate("Dialog", "Pendiente", None))
        self.pushButton_Cancelar.setText(_translate("Dialog", "Cancelar", None))
        self.tabWidget_CierreSenal.setTabText(self.tabWidget_CierreSenal.indexOf(self.tab_Cierre), _translate("Dialog", "Cierre", None))
        self.groupBox_19.setTitle(_translate("Dialog", "Lista de Usuarios", None))
        item = self.tableWidget_Usuarios.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID", None))
        item = self.tableWidget_Usuarios.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Nombre", None))
        item = self.tableWidget_Usuarios.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Parentesco", None))
        item = self.tableWidget_Usuarios.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Movil", None))
        item = self.tableWidget_Usuarios.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Clave", None))
        self.groupBox_4.setTitle(_translate("Dialog", "Numeros de Emergencia", None))
        item = self.tableWidget_ContactosEmergencia.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Numero", None))
        item = self.tableWidget_ContactosEmergencia.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Descripcion", None))
        item = self.tableWidget_ContactosEmergencia.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Observacion", None))
        self.groupBox_13.setTitle(_translate("Dialog", "Lista de Zonas", None))
        item = self.tableWidget_Zonas.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID", None))
        item = self.tableWidget_Zonas.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Descripcion", None))
        item = self.tableWidget_Zonas.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Ubicacion", None))
        self.tabWidget_CierreSenal.setTabText(self.tabWidget_CierreSenal.indexOf(self.tab_DatosCliente), _translate("Dialog", "Datos del Cliente", None))
        self.groupBox_12.setTitle(_translate("Dialog", "Lista de Señales", None))
        self.label_FechaHistorialSenales.setText(_translate("Dialog", "Fecha: ", None))
        self.label_22.setText(_translate("Dialog", "Eventos", None))
        item = self.tableWidget_Senales.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Evento", None))
        item = self.tableWidget_Senales.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Usuario/Zonas", None))
        item = self.tableWidget_Senales.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Fecha Recepcion", None))
        item = self.tableWidget_Senales.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Fecha Procesada", None))
        self.label_12.setText(_translate("Dialog", "Desde:", None))
        self.pushButton_SelectorBusqueda.setText(_translate("Dialog", "Busqueda Avanzada", None))
        self.label_14.setText(_translate("Dialog", "Hasta:", None))
        self.tabWidget_CierreSenal.setTabText(self.tabWidget_CierreSenal.indexOf(self.tab_Senales), _translate("Dialog", "Historial", None))
        self.groupBox_11.setTitle(_translate("Dialog", "Lista de Dispositivos de CCTV relacionados a la Cuenta", None))
        self.treeWidget_Camaras.headerItem().setText(0, _translate("Dialog", "Descripcion", None))
        self.treeWidget_Camaras.headerItem().setText(1, _translate("Dialog", "Tipo", None))
        self.treeWidget_Camaras.headerItem().setText(2, _translate("Dialog", "Modo", None))
        self.treeWidget_Camaras.headerItem().setText(3, _translate("Dialog", "Acciones", None))
        self.tabWidget_CierreSenal.setTabText(self.tabWidget_CierreSenal.indexOf(self.tab_Camaras), _translate("Dialog", "Camaras", None))
        self.groupBox_7.setTitle(_translate("Dialog", "Ubicacion del Cliente:", None))
        self.tabWidget_CierreSenal.setTabText(self.tabWidget_CierreSenal.indexOf(self.tab_Mapas), _translate("Dialog", "Mapas", None))
        self.tabWidget_CierreSenal.setTabText(self.tabWidget_CierreSenal.indexOf(self.tab_Foto), _translate("Dialog", "Foto", None))
        self.groupBox_6.setTitle(_translate("Dialog", "¿Que Señales?", None))
        self.radioButton_SenalesSeleccionadas.setText(_translate("Dialog", "Señales Seleccionadas", None))
        self.radioButton_PorCodigodeEvento.setText(_translate("Dialog", "Por Codigo de Evento", None))
        self.radioButton_PorCodigoAlarma.setText(_translate("Dialog", "Por Codigo de Alarma", None))
        self.radioButton_PorCliente.setText(_translate("Dialog", "Por Cliente", None))
        self.radioButton_TodasLasSenales.setText(_translate("Dialog", "Todas las Señales", None))
        self.label_10.setText(_translate("Dialog", "Comentario:", None))
        self.pushButton_Procesar_2.setText(_translate("Dialog", "Procesar Señales", None))
        item = self.tableWidget_SeleccionQueSenales.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Cliente", None))
        item = self.tableWidget_SeleccionQueSenales.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Señal", None))
        item = self.tableWidget_SeleccionQueSenales.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Fecha", None))
        self.label_4.setText(_translate("Dialog", "Mensajes Predefinido:", None))
        self.tabWidget_CierreSenal.setTabText(self.tabWidget_CierreSenal.indexOf(self.tab_CierreRapido), _translate("Dialog", "Cierre Rapido", None))
        self.groupBox_8.setTitle(_translate("Dialog", "Notas del Clientes", None))
        self.groupBox_9.setTitle(_translate("Dialog", "Nota Fija", None))
        self.groupBox_10.setTitle(_translate("Dialog", "Nota Temporal", None))
        self.label_11.setText(_translate("Dialog", "Fecha de Inicio:", None))
        self.label_19.setText(_translate("Dialog", "Fecha de Fin:", None))
        self.tabWidget_CierreSenal.setTabText(self.tabWidget_CierreSenal.indexOf(self.tab_Notas), _translate("Dialog", "Notas", None))
        self.pushButton_pic.setToolTip(_translate("Dialog", "Imagen Relacionada", None))
        self.pushButton_cam.setToolTip(_translate("Dialog", "Camaras Relacionadas", None))
        self.pushButton_key.setToolTip(_translate("Dialog", "Llave Cuenta", None))
        self.pushButton_clavemaster.setToolTip(_translate("Dialog", "Clave Master", None))
        self.pushButton_sms.setToolTip(_translate("Dialog", "Enviar SMS", None))
        self.pushButton_mail.setToolTip(_translate("Dialog", "Enviar Correo", None))

import recursos_rc
