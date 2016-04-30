# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTDialogAgregarRonda.ui'
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

class Ui_Dialog_AgregarRonda(object):
    def setupUi(self, Dialog_AgregarRonda):
        Dialog_AgregarRonda.setObjectName(_fromUtf8("Dialog_AgregarRonda"))
        Dialog_AgregarRonda.resize(604, 467)
        Dialog_AgregarRonda.setMinimumSize(QtCore.QSize(0, 0))
        Dialog_AgregarRonda.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Dialog_AgregarRonda.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout = QtGui.QGridLayout(Dialog_AgregarRonda)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog_AgregarRonda)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.timeEdit_HoraFin = QtGui.QTimeEdit(self.groupBox)
        self.timeEdit_HoraFin.setObjectName(_fromUtf8("timeEdit_HoraFin"))
        self.gridLayout_2.addWidget(self.timeEdit_HoraFin, 2, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.spinBox_ToleranciaRonda = QtGui.QSpinBox(self.groupBox)
        self.spinBox_ToleranciaRonda.setMaximum(1440)
        self.spinBox_ToleranciaRonda.setObjectName(_fromUtf8("spinBox_ToleranciaRonda"))
        self.horizontalLayout_3.addWidget(self.spinBox_ToleranciaRonda)
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_3.addWidget(self.label_13)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 7, 0, 1, 1)
        self.comboBox_Dias = QtGui.QComboBox(self.groupBox)
        self.comboBox_Dias.setObjectName(_fromUtf8("comboBox_Dias"))
        self.gridLayout_2.addWidget(self.comboBox_Dias, 7, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 8, 0, 1, 1)
        self.comboBox_TipoRonda = QtGui.QComboBox(self.groupBox)
        self.comboBox_TipoRonda.setObjectName(_fromUtf8("comboBox_TipoRonda"))
        self.gridLayout_2.addWidget(self.comboBox_TipoRonda, 8, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.timeEdit_HoraInicio = QtGui.QTimeEdit(self.groupBox)
        self.timeEdit_HoraInicio.setCalendarPopup(False)
        self.timeEdit_HoraInicio.setObjectName(_fromUtf8("timeEdit_HoraInicio"))
        self.gridLayout_2.addWidget(self.timeEdit_HoraInicio, 1, 1, 1, 1)
        self.lineEdit_NombreRonda = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_NombreRonda.setMaxLength(50)
        self.lineEdit_NombreRonda.setObjectName(_fromUtf8("lineEdit_NombreRonda"))
        self.gridLayout_2.addWidget(self.lineEdit_NombreRonda, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.groupBox_Repetir = QtGui.QGroupBox(self.groupBox)
        self.groupBox_Repetir.setObjectName(_fromUtf8("groupBox_Repetir"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_Repetir)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_15 = QtGui.QLabel(self.groupBox_Repetir)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_4.addWidget(self.label_15, 3, 0, 1, 2)
        self.label_4 = QtGui.QLabel(self.groupBox_Repetir)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)
        self.timeEdit_RepetirHasta = QtGui.QTimeEdit(self.groupBox_Repetir)
        self.timeEdit_RepetirHasta.setCalendarPopup(False)
        self.timeEdit_RepetirHasta.setObjectName(_fromUtf8("timeEdit_RepetirHasta"))
        self.gridLayout_4.addWidget(self.timeEdit_RepetirHasta, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_Repetir)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.spinBox_IntervaloRonda = QtGui.QSpinBox(self.groupBox_Repetir)
        self.spinBox_IntervaloRonda.setMaximum(1440)
        self.spinBox_IntervaloRonda.setObjectName(_fromUtf8("spinBox_IntervaloRonda"))
        self.horizontalLayout.addWidget(self.spinBox_IntervaloRonda)
        self.label_7 = QtGui.QLabel(self.groupBox_Repetir)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.listWidget_CalculoRondas = QtGui.QListWidget(self.groupBox_Repetir)
        self.listWidget_CalculoRondas.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.listWidget_CalculoRondas.setObjectName(_fromUtf8("listWidget_CalculoRondas"))
        self.gridLayout_4.addWidget(self.listWidget_CalculoRondas, 4, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_Repetir, 10, 0, 1, 2)
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_2.addWidget(self.label_14, 9, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout_2.addWidget(self.checkBox, 9, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Dialog_AgregarRonda)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)
        self.listWidget_PuntosDisponibles = QtGui.QListWidget(self.groupBox_2)
        self.listWidget_PuntosDisponibles.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.listWidget_PuntosDisponibles.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget_PuntosDisponibles.setObjectName(_fromUtf8("listWidget_PuntosDisponibles"))
        self.gridLayout_3.addWidget(self.listWidget_PuntosDisponibles, 1, 0, 1, 1)
        self.listWidget_PuntosAsignados = QtGui.QListWidget(self.groupBox_2)
        self.listWidget_PuntosAsignados.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.listWidget_PuntosAsignados.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget_PuntosAsignados.setObjectName(_fromUtf8("listWidget_PuntosAsignados"))
        self.gridLayout_3.addWidget(self.listWidget_PuntosAsignados, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushButton_GuardarRonda = QtGui.QPushButton(Dialog_AgregarRonda)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_GuardarRonda.setIcon(icon)
        self.pushButton_GuardarRonda.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_GuardarRonda.setFlat(True)
        self.pushButton_GuardarRonda.setObjectName(_fromUtf8("pushButton_GuardarRonda"))
        self.horizontalLayout_4.addWidget(self.pushButton_GuardarRonda)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 2)

        self.retranslateUi(Dialog_AgregarRonda)
        QtCore.QMetaObject.connectSlotsByName(Dialog_AgregarRonda)

    def retranslateUi(self, Dialog_AgregarRonda):
        Dialog_AgregarRonda.setWindowTitle(_translate("Dialog_AgregarRonda", "Agregar Ronda", None))
        self.groupBox.setTitle(_translate("Dialog_AgregarRonda", "Agregue la Informacion de la Ronda", None))
        self.label_13.setText(_translate("Dialog_AgregarRonda", "Minutos", None))
        self.label_9.setText(_translate("Dialog_AgregarRonda", "Calendario:", None))
        self.label_2.setText(_translate("Dialog_AgregarRonda", "Tipo:", None))
        self.label_3.setText(_translate("Dialog_AgregarRonda", "Hora Inicio:", None))
        self.lineEdit_NombreRonda.setPlaceholderText(_translate("Dialog_AgregarRonda", "Nombre de la Ronda", None))
        self.label.setText(_translate("Dialog_AgregarRonda", "Nombre", None))
        self.label_10.setText(_translate("Dialog_AgregarRonda", "Hora Fin:", None))
        self.label_6.setText(_translate("Dialog_AgregarRonda", "Tolerancia:", None))
        self.groupBox_Repetir.setTitle(_translate("Dialog_AgregarRonda", "Auto Crear", None))
        self.label_15.setText(_translate("Dialog_AgregarRonda", "Calculo de Rondas a crear", None))
        self.label_4.setText(_translate("Dialog_AgregarRonda", "Repetir Hasta:", None))
        self.label_5.setText(_translate("Dialog_AgregarRonda", "Repetir cada:", None))
        self.label_7.setText(_translate("Dialog_AgregarRonda", "Minutos", None))
        self.label_14.setText(_translate("Dialog_AgregarRonda", "Repetir:", None))
        self.checkBox.setText(_translate("Dialog_AgregarRonda", "Repetir Ronda", None))
        self.groupBox_2.setTitle(_translate("Dialog_AgregarRonda", "Administracion de Puntos", None))
        self.label_8.setText(_translate("Dialog_AgregarRonda", "Puntos Disponibles", None))
        self.label_12.setText(_translate("Dialog_AgregarRonda", "Puntos Asignados a la Ronda", None))
        self.pushButton_GuardarRonda.setText(_translate("Dialog_AgregarRonda", "Guardar", None))

import recursos_rc
