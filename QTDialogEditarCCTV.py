# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTDialogEditarCCTV.ui'
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

class Ui_Dialog_EditarCCTV(object):
    def setupUi(self, Dialog_EditarCCTV):
        Dialog_EditarCCTV.setObjectName(_fromUtf8("Dialog_EditarCCTV"))
        Dialog_EditarCCTV.resize(419, 506)
        Dialog_EditarCCTV.setMinimumSize(QtCore.QSize(419, 506))
        Dialog_EditarCCTV.setMaximumSize(QtCore.QSize(419, 514))
        Dialog_EditarCCTV.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout_2 = QtGui.QGridLayout(Dialog_EditarCCTV)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_AgregarCCTV = QtGui.QPushButton(Dialog_EditarCCTV)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AgregarCCTV.setIcon(icon)
        self.pushButton_AgregarCCTV.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_AgregarCCTV.setFlat(True)
        self.pushButton_AgregarCCTV.setObjectName(_fromUtf8("pushButton_AgregarCCTV"))
        self.gridLayout_2.addWidget(self.pushButton_AgregarCCTV, 1, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(Dialog_EditarCCTV)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.lineEdit_IP = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_IP.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_IP.setObjectName(_fromUtf8("lineEdit_IP"))
        self.gridLayout.addWidget(self.lineEdit_IP, 6, 1, 1, 1)
        self.comboBox_Modelo = QtGui.QComboBox(self.groupBox)
        self.comboBox_Modelo.setObjectName(_fromUtf8("comboBox_Modelo"))
        self.gridLayout.addWidget(self.comboBox_Modelo, 5, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineEdit_Descripcion = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Descripcion.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_Descripcion.setObjectName(_fromUtf8("lineEdit_Descripcion"))
        self.gridLayout.addWidget(self.lineEdit_Descripcion, 2, 1, 1, 1)
        self.comboBox_ModoRegistro = QtGui.QComboBox(self.groupBox)
        self.comboBox_ModoRegistro.setObjectName(_fromUtf8("comboBox_ModoRegistro"))
        self.gridLayout.addWidget(self.comboBox_ModoRegistro, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_Tipo = QtGui.QComboBox(self.groupBox)
        self.comboBox_Tipo.setObjectName(_fromUtf8("comboBox_Tipo"))
        self.gridLayout.addWidget(self.comboBox_Tipo, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.comboBox_Marca = QtGui.QComboBox(self.groupBox)
        self.comboBox_Marca.setObjectName(_fromUtf8("comboBox_Marca"))
        self.gridLayout.addWidget(self.comboBox_Marca, 4, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.lineEdit_Puerto = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Puerto.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_Puerto.setObjectName(_fromUtf8("lineEdit_Puerto"))
        self.gridLayout.addWidget(self.lineEdit_Puerto, 7, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 9, 0, 1, 1)
        self.lineEdit_Usuario = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Usuario.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_Usuario.setObjectName(_fromUtf8("lineEdit_Usuario"))
        self.gridLayout.addWidget(self.lineEdit_Usuario, 8, 1, 1, 1)
        self.lineEdit_Clave = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Clave.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_Clave.setObjectName(_fromUtf8("lineEdit_Clave"))
        self.gridLayout.addWidget(self.lineEdit_Clave, 9, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)
        self.frame = QtGui.QFrame(self.groupBox)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.groupBox_RTSP = QtGui.QGroupBox(self.groupBox)
        self.groupBox_RTSP.setObjectName(_fromUtf8("groupBox_RTSP"))
        self.verticalLayoutRTSP = QtGui.QVBoxLayout(self.groupBox_RTSP)
        self.verticalLayoutRTSP.setObjectName(_fromUtf8("verticalLayoutRTSP"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_23 = QtGui.QLabel(self.groupBox_RTSP)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout.addWidget(self.label_23)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayoutRTSP.addLayout(self.horizontalLayout)
        self.horizontalLayout_CAM1 = QtGui.QHBoxLayout()
        self.horizontalLayout_CAM1.setObjectName(_fromUtf8("horizontalLayout_CAM1"))
        self.label_Camara = QtGui.QLabel(self.groupBox_RTSP)
        self.label_Camara.setObjectName(_fromUtf8("label_Camara"))
        self.horizontalLayout_CAM1.addWidget(self.label_Camara)
        self.lineEdit_Canal = QtGui.QLineEdit(self.groupBox_RTSP)
        self.lineEdit_Canal.setObjectName(_fromUtf8("lineEdit_Canal"))
        self.horizontalLayout_CAM1.addWidget(self.lineEdit_Canal)
        self.lineEdit_DescripcionCanal = QtGui.QLineEdit(self.groupBox_RTSP)
        self.lineEdit_DescripcionCanal.setObjectName(_fromUtf8("lineEdit_DescripcionCanal"))
        self.horizontalLayout_CAM1.addWidget(self.lineEdit_DescripcionCanal)
        self.pushButton_Agregar = QtGui.QPushButton(self.groupBox_RTSP)
        self.pushButton_Agregar.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_Agregar.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/4-Icone-plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Agregar.setIcon(icon1)
        self.pushButton_Agregar.setIconSize(QtCore.QSize(18, 18))
        self.pushButton_Agregar.setFlat(True)
        self.pushButton_Agregar.setObjectName(_fromUtf8("pushButton_Agregar"))
        self.horizontalLayout_CAM1.addWidget(self.pushButton_Agregar)
        self.verticalLayoutRTSP.addLayout(self.horizontalLayout_CAM1)
        self.tableWidget = QtGui.QTableWidget(self.groupBox_RTSP)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayoutRTSP.addWidget(self.tableWidget)
        self.gridLayout.addWidget(self.groupBox_RTSP, 10, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 3)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 2, 1, 1)

        self.retranslateUi(Dialog_EditarCCTV)
        QtCore.QMetaObject.connectSlotsByName(Dialog_EditarCCTV)
        Dialog_EditarCCTV.setTabOrder(self.lineEdit_Descripcion, self.lineEdit_IP)
        Dialog_EditarCCTV.setTabOrder(self.lineEdit_IP, self.lineEdit_Puerto)
        Dialog_EditarCCTV.setTabOrder(self.lineEdit_Puerto, self.pushButton_AgregarCCTV)

    def retranslateUi(self, Dialog_EditarCCTV):
        Dialog_EditarCCTV.setWindowTitle(_translate("Dialog_EditarCCTV", "Editar CCTV", None))
        self.pushButton_AgregarCCTV.setText(_translate("Dialog_EditarCCTV", "Guardar", None))
        self.groupBox.setTitle(_translate("Dialog_EditarCCTV", "Modifique la informacion de CCTV", None))
        self.label_6.setText(_translate("Dialog_EditarCCTV", "IP / DNS:", None))
        self.label.setText(_translate("Dialog_EditarCCTV", "Descripcion:", None))
        self.label_7.setText(_translate("Dialog_EditarCCTV", "Puerto:", None))
        self.label_3.setText(_translate("Dialog_EditarCCTV", "Tipo:", None))
        self.label_2.setText(_translate("Dialog_EditarCCTV", "Modo de Registro:", None))
        self.label_4.setText(_translate("Dialog_EditarCCTV", "Marca:", None))
        self.label_5.setText(_translate("Dialog_EditarCCTV", "Modelo:", None))
        self.label_9.setText(_translate("Dialog_EditarCCTV", "Clave:", None))
        self.label_8.setText(_translate("Dialog_EditarCCTV", "Usuario:", None))
        self.label_23.setText(_translate("Dialog_EditarCCTV", "Modificar Camaras RTSP", None))
        self.label_Camara.setText(_translate("Dialog_EditarCCTV", "Camara:", None))
        self.lineEdit_Canal.setPlaceholderText(_translate("Dialog_EditarCCTV", "Canal", None))
        self.lineEdit_DescripcionCanal.setPlaceholderText(_translate("Dialog_EditarCCTV", "Descripcion", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog_EditarCCTV", "Canal", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog_EditarCCTV", "Descripcion", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog_EditarCCTV", "Borrar", None))

import recursos_rc
