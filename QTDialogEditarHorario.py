# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTDialogEditarHorario.ui'
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

class Ui_Dialog_EditarHorarios(object):
    def setupUi(self, Dialog_EditarHorarios):
        Dialog_EditarHorarios.setObjectName(_fromUtf8("Dialog_EditarHorarios"))
        Dialog_EditarHorarios.resize(300, 250)
        Dialog_EditarHorarios.setMinimumSize(QtCore.QSize(300, 250))
        Dialog_EditarHorarios.setMaximumSize(QtCore.QSize(300, 250))
        Dialog_EditarHorarios.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout = QtGui.QGridLayout(Dialog_EditarHorarios)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog_EditarHorarios)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.comboBox_Dias = QtGui.QComboBox(self.groupBox)
        self.comboBox_Dias.setObjectName(_fromUtf8("comboBox_Dias"))
        self.comboBox_Dias.addItem(_fromUtf8(""))
        self.comboBox_Dias.addItem(_fromUtf8(""))
        self.comboBox_Dias.addItem(_fromUtf8(""))
        self.comboBox_Dias.addItem(_fromUtf8(""))
        self.comboBox_Dias.addItem(_fromUtf8(""))
        self.comboBox_Dias.addItem(_fromUtf8(""))
        self.comboBox_Dias.addItem(_fromUtf8(""))
        self.comboBox_Dias.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox_Dias)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.timeEdit_HoraApertura = QtGui.QTimeEdit(self.groupBox)
        self.timeEdit_HoraApertura.setTime(QtCore.QTime(8, 0, 0))
        self.timeEdit_HoraApertura.setObjectName(_fromUtf8("timeEdit_HoraApertura"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.timeEdit_HoraApertura)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.spinBox_ToleranciaApertura = QtGui.QSpinBox(self.groupBox)
        self.spinBox_ToleranciaApertura.setMaximum(1440)
        self.spinBox_ToleranciaApertura.setProperty("value", 15)
        self.spinBox_ToleranciaApertura.setObjectName(_fromUtf8("spinBox_ToleranciaApertura"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.spinBox_ToleranciaApertura)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.timeEdit_HoraCierre = QtGui.QTimeEdit(self.groupBox)
        self.timeEdit_HoraCierre.setTime(QtCore.QTime(18, 0, 0))
        self.timeEdit_HoraCierre.setObjectName(_fromUtf8("timeEdit_HoraCierre"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.timeEdit_HoraCierre)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_5)
        self.spinBox_ToleranciaCierre = QtGui.QSpinBox(self.groupBox)
        self.spinBox_ToleranciaCierre.setMaximum(1440)
        self.spinBox_ToleranciaCierre.setProperty("value", 15)
        self.spinBox_ToleranciaCierre.setObjectName(_fromUtf8("spinBox_ToleranciaCierre"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.spinBox_ToleranciaCierre)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtGui.QFormLayout.FieldRole, spacerItem)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtGui.QFormLayout.FieldRole, spacerItem1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 3)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        self.pushButton_Agregar = QtGui.QPushButton(Dialog_EditarHorarios)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Agregar.setIcon(icon)
        self.pushButton_Agregar.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_Agregar.setAutoDefault(False)
        self.pushButton_Agregar.setFlat(True)
        self.pushButton_Agregar.setObjectName(_fromUtf8("pushButton_Agregar"))
        self.gridLayout.addWidget(self.pushButton_Agregar, 1, 1, 1, 1)

        self.retranslateUi(Dialog_EditarHorarios)
        QtCore.QMetaObject.connectSlotsByName(Dialog_EditarHorarios)

    def retranslateUi(self, Dialog_EditarHorarios):
        Dialog_EditarHorarios.setWindowTitle(_translate("Dialog_EditarHorarios", "Editar Horario", None))
        self.groupBox.setTitle(_translate("Dialog_EditarHorarios", "Modifique la informacion del Horario", None))
        self.label.setText(_translate("Dialog_EditarHorarios", "Dia", None))
        self.comboBox_Dias.setItemText(0, _translate("Dialog_EditarHorarios", "Lunes", None))
        self.comboBox_Dias.setItemText(1, _translate("Dialog_EditarHorarios", "Martes", None))
        self.comboBox_Dias.setItemText(2, _translate("Dialog_EditarHorarios", "Miercoles", None))
        self.comboBox_Dias.setItemText(3, _translate("Dialog_EditarHorarios", "Jueves", None))
        self.comboBox_Dias.setItemText(4, _translate("Dialog_EditarHorarios", "Viernes", None))
        self.comboBox_Dias.setItemText(5, _translate("Dialog_EditarHorarios", "Sabado", None))
        self.comboBox_Dias.setItemText(6, _translate("Dialog_EditarHorarios", "Domingo", None))
        self.comboBox_Dias.setItemText(7, _translate("Dialog_EditarHorarios", "Feriados", None))
        self.label_2.setText(_translate("Dialog_EditarHorarios", "Hora Apertura", None))
        self.label_3.setText(_translate("Dialog_EditarHorarios", "Tolerancia Apertura", None))
        self.label_4.setText(_translate("Dialog_EditarHorarios", "Hora Cierre", None))
        self.label_5.setText(_translate("Dialog_EditarHorarios", "Tolerancia Cierre", None))
        self.pushButton_Agregar.setText(_translate("Dialog_EditarHorarios", "Modificar", None))

import recursos_rc
