# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSubVentanaEventos.ui'
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

class Ui_SubVentanaEventos(object):
    def setupUi(self, SubVentanaEventos):
        SubVentanaEventos.setObjectName(_fromUtf8("SubVentanaEventos"))
        SubVentanaEventos.resize(652, 432)
        SubVentanaEventos.setMinimumSize(QtCore.QSize(652, 432))
        SubVentanaEventos.setMaximumSize(QtCore.QSize(652, 432))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/Eventos.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubVentanaEventos.setWindowIcon(icon)
        SubVentanaEventos.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout_2 = QtGui.QGridLayout(SubVentanaEventos)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_4 = QtGui.QGroupBox(SubVentanaEventos)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.comboBox_Protocolos = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_Protocolos.setObjectName(_fromUtf8("comboBox_Protocolos"))
        self.gridLayout_3.addWidget(self.comboBox_Protocolos, 1, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.tableWidget_ListadeEventos = QtGui.QTableWidget(self.groupBox_4)
        self.tableWidget_ListadeEventos.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidget_ListadeEventos.setStyleSheet(_fromUtf8(""))
        self.tableWidget_ListadeEventos.setObjectName(_fromUtf8("tableWidget_ListadeEventos"))
        self.tableWidget_ListadeEventos.setColumnCount(3)
        self.tableWidget_ListadeEventos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ListadeEventos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ListadeEventos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ListadeEventos.setHorizontalHeaderItem(2, item)
        self.gridLayout_3.addWidget(self.tableWidget_ListadeEventos, 3, 0, 1, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_AgregarEvento = QtGui.QPushButton(self.groupBox_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/4-Icone-plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AgregarEvento.setIcon(icon1)
        self.pushButton_AgregarEvento.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_AgregarEvento.setFlat(True)
        self.pushButton_AgregarEvento.setObjectName(_fromUtf8("pushButton_AgregarEvento"))
        self.horizontalLayout_2.addWidget(self.pushButton_AgregarEvento)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 4, 0, 1, 2)
        self.label_7 = QtGui.QLabel(self.groupBox_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.lineEdit_Buscar = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_Buscar.setObjectName(_fromUtf8("lineEdit_Buscar"))
        self.gridLayout_3.addWidget(self.lineEdit_Buscar, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_DatosEvento = QtGui.QGroupBox(SubVentanaEventos)
        self.groupBox_DatosEvento.setObjectName(_fromUtf8("groupBox_DatosEvento"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_DatosEvento)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_DatosEvento)
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.radioButton_MonitoreoSi = QtGui.QRadioButton(self.groupBox_3)
        self.radioButton_MonitoreoSi.setObjectName(_fromUtf8("radioButton_MonitoreoSi"))
        self.gridLayout_5.addWidget(self.radioButton_MonitoreoSi, 0, 0, 1, 1)
        self.radioButton_MonitoreoNo = QtGui.QRadioButton(self.groupBox_3)
        self.radioButton_MonitoreoNo.setChecked(True)
        self.radioButton_MonitoreoNo.setObjectName(_fromUtf8("radioButton_MonitoreoNo"))
        self.gridLayout_5.addWidget(self.radioButton_MonitoreoNo, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 7, 3, 1, 6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 8, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox_DatosEvento)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 12, 2, 1, 4)
        self.label_9 = QtGui.QLabel(self.groupBox_DatosEvento)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 3)
        self.lineEdit_CodigoEvento = QtGui.QLineEdit(self.groupBox_DatosEvento)
        self.lineEdit_CodigoEvento.setObjectName(_fromUtf8("lineEdit_CodigoEvento"))
        self.gridLayout.addWidget(self.lineEdit_CodigoEvento, 1, 3, 1, 6)
        self.textEdit_Mensaje = QtGui.QTextEdit(self.groupBox_DatosEvento)
        self.textEdit_Mensaje.setMinimumSize(QtCore.QSize(0, 50))
        self.textEdit_Mensaje.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textEdit_Mensaje.setObjectName(_fromUtf8("textEdit_Mensaje"))
        self.gridLayout.addWidget(self.textEdit_Mensaje, 11, 0, 1, 9)
        self.comboBox_TipoEvento = QtGui.QComboBox(self.groupBox_DatosEvento)
        self.comboBox_TipoEvento.setObjectName(_fromUtf8("comboBox_TipoEvento"))
        self.gridLayout.addWidget(self.comboBox_TipoEvento, 3, 3, 1, 6)
        self.label_10 = QtGui.QLabel(self.groupBox_DatosEvento)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 10, 0, 1, 7)
        self.label_8 = QtGui.QLabel(self.groupBox_DatosEvento)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 3)
        self.comboBox_ProtocoloEvento = QtGui.QComboBox(self.groupBox_DatosEvento)
        self.comboBox_ProtocoloEvento.setObjectName(_fromUtf8("comboBox_ProtocoloEvento"))
        self.gridLayout.addWidget(self.comboBox_ProtocoloEvento, 2, 3, 1, 6)
        self.comboBox_Variables = QtGui.QComboBox(self.groupBox_DatosEvento)
        self.comboBox_Variables.setObjectName(_fromUtf8("comboBox_Variables"))
        self.gridLayout.addWidget(self.comboBox_Variables, 12, 7, 1, 2)
        self.label_5 = QtGui.QLabel(self.groupBox_DatosEvento)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 2)
        self.lineEdit_DescripcionEvento = QtGui.QLineEdit(self.groupBox_DatosEvento)
        self.lineEdit_DescripcionEvento.setMaxLength(100)
        self.lineEdit_DescripcionEvento.setObjectName(_fromUtf8("lineEdit_DescripcionEvento"))
        self.gridLayout.addWidget(self.lineEdit_DescripcionEvento, 4, 3, 1, 6)
        self.comboBox_GrupoEvento = QtGui.QComboBox(self.groupBox_DatosEvento)
        self.comboBox_GrupoEvento.setObjectName(_fromUtf8("comboBox_GrupoEvento"))
        self.gridLayout.addWidget(self.comboBox_GrupoEvento, 5, 3, 1, 6)
        self.label_4 = QtGui.QLabel(self.groupBox_DatosEvento)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_DatosEvento)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 3)
        self.label = QtGui.QLabel(self.groupBox_DatosEvento)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 6, 7, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_DatosEvento)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_DatosEvento)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 7, 0, 1, 1)
        self.spinBox_Prioridad = QtGui.QSpinBox(self.groupBox_DatosEvento)
        self.spinBox_Prioridad.setMinimum(1)
        self.spinBox_Prioridad.setMaximum(9)
        self.spinBox_Prioridad.setProperty("value", 9)
        self.spinBox_Prioridad.setObjectName(_fromUtf8("spinBox_Prioridad"))
        self.gridLayout.addWidget(self.spinBox_Prioridad, 6, 8, 1, 1)
        self.pushButton_ColorEvento = QtGui.QPushButton(self.groupBox_DatosEvento)
        self.pushButton_ColorEvento.setStyleSheet(_fromUtf8(""))
        self.pushButton_ColorEvento.setObjectName(_fromUtf8("pushButton_ColorEvento"))
        self.gridLayout.addWidget(self.pushButton_ColorEvento, 6, 3, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_GuardarEvento = QtGui.QPushButton(self.groupBox_DatosEvento)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_GuardarEvento.setIcon(icon2)
        self.pushButton_GuardarEvento.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_GuardarEvento.setFlat(True)
        self.pushButton_GuardarEvento.setObjectName(_fromUtf8("pushButton_GuardarEvento"))
        self.horizontalLayout.addWidget(self.pushButton_GuardarEvento)
        self.pushButton_BorrarEvento = QtGui.QPushButton(self.groupBox_DatosEvento)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/eraser-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_BorrarEvento.setIcon(icon3)
        self.pushButton_BorrarEvento.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_BorrarEvento.setFlat(True)
        self.pushButton_BorrarEvento.setObjectName(_fromUtf8("pushButton_BorrarEvento"))
        self.horizontalLayout.addWidget(self.pushButton_BorrarEvento)
        self.pushButton_Cancelar = QtGui.QPushButton(self.groupBox_DatosEvento)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/uncheck.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Cancelar.setIcon(icon4)
        self.pushButton_Cancelar.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Cancelar.setFlat(True)
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.horizontalLayout.addWidget(self.pushButton_Cancelar)
        self.gridLayout.addLayout(self.horizontalLayout, 13, 0, 1, 9)
        self.gridLayout_2.addWidget(self.groupBox_DatosEvento, 0, 1, 1, 1)

        self.retranslateUi(SubVentanaEventos)
        QtCore.QMetaObject.connectSlotsByName(SubVentanaEventos)

    def retranslateUi(self, SubVentanaEventos):
        SubVentanaEventos.setWindowTitle(_translate("SubVentanaEventos", "Administracion de Eventos", None))
        self.groupBox_4.setTitle(_translate("SubVentanaEventos", "Lista de Eventos", None))
        self.label_3.setText(_translate("SubVentanaEventos", "Protocolo:", None))
        self.comboBox_Protocolos.setToolTip(_translate("SubVentanaEventos", "Seleccione El Protocolo  ", None))
        item = self.tableWidget_ListadeEventos.horizontalHeaderItem(0)
        item.setText(_translate("SubVentanaEventos", "Cod Evento", None))
        item = self.tableWidget_ListadeEventos.horizontalHeaderItem(1)
        item.setText(_translate("SubVentanaEventos", "Descripcion", None))
        item = self.tableWidget_ListadeEventos.horizontalHeaderItem(2)
        item.setText(_translate("SubVentanaEventos", "Protocolo", None))
        self.pushButton_AgregarEvento.setToolTip(_translate("SubVentanaEventos", "Agregar Nuevo Evento  ", None))
        self.pushButton_AgregarEvento.setText(_translate("SubVentanaEventos", "Agregar", None))
        self.label_7.setText(_translate("SubVentanaEventos", "Buscar:", None))
        self.groupBox_DatosEvento.setTitle(_translate("SubVentanaEventos", "Datos del Evento", None))
        self.radioButton_MonitoreoSi.setToolTip(_translate("SubVentanaEventos", "<html><head/><body><p>Si Selecciona &quot; Si &quot; El Evento pasa a Señales por procesar y nesecitan</p><p> la Atencion del Operador.</p></body></html>", None))
        self.radioButton_MonitoreoSi.setText(_translate("SubVentanaEventos", "SI", None))
        self.radioButton_MonitoreoNo.setToolTip(_translate("SubVentanaEventos", "<html><head/><body><p>Si Selecciona &quot; No&quot; El Evento pasa al Log de Señales  y  no nesecitan</p><p>la Atencion del Operador.</p></body></html>", None))
        self.radioButton_MonitoreoNo.setText(_translate("SubVentanaEventos", "NO", None))
        self.label_11.setText(_translate("SubVentanaEventos", "Variables:", None))
        self.label_9.setText(_translate("SubVentanaEventos", "Grupo:", None))
        self.lineEdit_CodigoEvento.setToolTip(_translate("SubVentanaEventos", "Introdusca el Codigo del Evento  ", None))
        self.textEdit_Mensaje.setToolTip(_translate("SubVentanaEventos", "<html><head/><body><p>Variables Para La salida del Mensaje </p><p>de Texto</p></body></html>", None))
        self.comboBox_TipoEvento.setToolTip(_translate("SubVentanaEventos", "Seleccione El Tipo de Evento  ", None))
        self.label_10.setText(_translate("SubVentanaEventos", "Formato de Mesaje:", None))
        self.label_8.setText(_translate("SubVentanaEventos", "Descripcion:", None))
        self.comboBox_ProtocoloEvento.setToolTip(_translate("SubVentanaEventos", "Seleccione el Protocolo del Evento  ", None))
        self.label_5.setText(_translate("SubVentanaEventos", "Evento:", None))
        self.lineEdit_DescripcionEvento.setToolTip(_translate("SubVentanaEventos", "Descripcion a Mostrar Del Evento  ", None))
        self.comboBox_GrupoEvento.setToolTip(_translate("SubVentanaEventos", "Seleccione El Codigo De Alarma Del Evento", None))
        self.label_4.setText(_translate("SubVentanaEventos", "Tipo:", None))
        self.label_2.setText(_translate("SubVentanaEventos", "Protocolo:", None))
        self.label.setText(_translate("SubVentanaEventos", "Prioridad:", None))
        self.label_6.setText(_translate("SubVentanaEventos", "Color:", None))
        self.label_12.setText(_translate("SubVentanaEventos", "Monitoreo:", None))
        self.spinBox_Prioridad.setToolTip(_translate("SubVentanaEventos", "<html><head/><body><p>Seleccione La Prioridad del Evento </p><p>Ejemplo:</p><p>1 es Mayor Prioridad para la Atencion de dicho Evento ( Suiches de Panico, Emergencias Medicas, Etc)</p></body></html>", None))
        self.pushButton_ColorEvento.setToolTip(_translate("SubVentanaEventos", "Seleccione el Color a Mostrar Del Evento", None))
        self.pushButton_ColorEvento.setText(_translate("SubVentanaEventos", "...", None))
        self.pushButton_GuardarEvento.setToolTip(_translate("SubVentanaEventos", "Guardar Evento", None))
        self.pushButton_GuardarEvento.setText(_translate("SubVentanaEventos", "Guardar", None))
        self.pushButton_BorrarEvento.setToolTip(_translate("SubVentanaEventos", "Borrar Evento", None))
        self.pushButton_BorrarEvento.setText(_translate("SubVentanaEventos", "Borrar", None))
        self.pushButton_Cancelar.setToolTip(_translate("SubVentanaEventos", "Cancelar Edicion", None))
        self.pushButton_Cancelar.setText(_translate("SubVentanaEventos", "Cancelar", None))

import recursos_rc
