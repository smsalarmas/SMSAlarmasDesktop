# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTDialogAgregarUsuario.ui'
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

class Ui_Dialog_AgregarUsuario(object):
    def setupUi(self, Dialog_AgregarUsuario):
        Dialog_AgregarUsuario.setObjectName(_fromUtf8("Dialog_AgregarUsuario"))
        Dialog_AgregarUsuario.resize(320, 600)
        Dialog_AgregarUsuario.setMinimumSize(QtCore.QSize(320, 600))
        Dialog_AgregarUsuario.setMaximumSize(QtCore.QSize(320, 600))
        Dialog_AgregarUsuario.setStyleSheet(_fromUtf8("QTableView {\n"
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
        self.gridLayout_2 = QtGui.QGridLayout(Dialog_AgregarUsuario)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox = QtGui.QGroupBox(Dialog_AgregarUsuario)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 15, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 16, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 9, 0, 1, 1)
        self.spinBox_MaximoSMSMensual = QtGui.QSpinBox(self.groupBox)
        self.spinBox_MaximoSMSMensual.setMaximum(99999)
        self.spinBox_MaximoSMSMensual.setProperty("value", 99999)
        self.spinBox_MaximoSMSMensual.setObjectName(_fromUtf8("spinBox_MaximoSMSMensual"))
        self.gridLayout.addWidget(self.spinBox_MaximoSMSMensual, 15, 1, 1, 1)
        self.lineEdit_CodigoUsuario = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_CodigoUsuario.setMaxLength(50)
        self.lineEdit_CodigoUsuario.setObjectName(_fromUtf8("lineEdit_CodigoUsuario"))
        self.gridLayout.addWidget(self.lineEdit_CodigoUsuario, 1, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 14, 0, 1, 1)
        self.lineEdit_Nombre = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Nombre.setMaxLength(50)
        self.lineEdit_Nombre.setObjectName(_fromUtf8("lineEdit_Nombre"))
        self.gridLayout.addWidget(self.lineEdit_Nombre, 3, 1, 1, 1)
        self.label_15 = QtGui.QLabel(self.groupBox)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout.addWidget(self.label_15, 17, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/18-Utilisateur.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout.addWidget(self.label_10)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.comboBox_Parentesco = QtGui.QComboBox(self.groupBox)
        self.comboBox_Parentesco.setObjectName(_fromUtf8("comboBox_Parentesco"))
        self.gridLayout.addWidget(self.comboBox_Parentesco, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.dateEdit_Nacimiento = QtGui.QDateEdit(self.groupBox)
        self.dateEdit_Nacimiento.setDate(QtCore.QDate(1900, 1, 1))
        self.dateEdit_Nacimiento.setMinimumDate(QtCore.QDate(1900, 1, 1))
        self.dateEdit_Nacimiento.setCalendarPopup(True)
        self.dateEdit_Nacimiento.setObjectName(_fromUtf8("dateEdit_Nacimiento"))
        self.gridLayout.addWidget(self.dateEdit_Nacimiento, 8, 1, 1, 1)
        self.lineEdit_Apellido = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Apellido.setMaxLength(50)
        self.lineEdit_Apellido.setObjectName(_fromUtf8("lineEdit_Apellido"))
        self.gridLayout.addWidget(self.lineEdit_Apellido, 4, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/29-Parametres.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_2.addWidget(self.label_11)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 13, 0, 1, 2)
        self.lineEdit_Clave = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Clave.setMaxLength(50)
        self.lineEdit_Clave.setObjectName(_fromUtf8("lineEdit_Clave"))
        self.gridLayout.addWidget(self.lineEdit_Clave, 5, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.comboBox_Reportes = QtGui.QComboBox(self.groupBox)
        self.comboBox_Reportes.setObjectName(_fromUtf8("comboBox_Reportes"))
        self.gridLayout.addWidget(self.comboBox_Reportes, 17, 1, 1, 1)
        self.lineEdit_Movil = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Movil.setMaxLength(50)
        self.lineEdit_Movil.setObjectName(_fromUtf8("lineEdit_Movil"))
        self.gridLayout.addWidget(self.lineEdit_Movil, 6, 1, 1, 1)
        self.lineEdit_Email = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Email.setMaxLength(60)
        self.lineEdit_Email.setObjectName(_fromUtf8("lineEdit_Email"))
        self.gridLayout.addWidget(self.lineEdit_Email, 7, 1, 1, 1)
        self.frame_2 = QtGui.QFrame(self.groupBox)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.radioButton_ActivadoSMS = QtGui.QRadioButton(self.frame_2)
        self.radioButton_ActivadoSMS.setIconSize(QtCore.QSize(16, 16))
        self.radioButton_ActivadoSMS.setAutoExclusive(True)
        self.radioButton_ActivadoSMS.setObjectName(_fromUtf8("radioButton_ActivadoSMS"))
        self.horizontalLayout_3.addWidget(self.radioButton_ActivadoSMS)
        self.radioButton_DesactivadoSMS = QtGui.QRadioButton(self.frame_2)
        self.radioButton_DesactivadoSMS.setChecked(True)
        self.radioButton_DesactivadoSMS.setObjectName(_fromUtf8("radioButton_DesactivadoSMS"))
        self.horizontalLayout_3.addWidget(self.radioButton_DesactivadoSMS)
        self.gridLayout.addWidget(self.frame_2, 14, 1, 1, 1)
        self.frame_3 = QtGui.QFrame(self.groupBox)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.radioButton_EmailActivado = QtGui.QRadioButton(self.frame_3)
        self.radioButton_EmailActivado.setObjectName(_fromUtf8("radioButton_EmailActivado"))
        self.horizontalLayout_4.addWidget(self.radioButton_EmailActivado)
        self.radioButton_EmailDesactivado = QtGui.QRadioButton(self.frame_3)
        self.radioButton_EmailDesactivado.setChecked(True)
        self.radioButton_EmailDesactivado.setObjectName(_fromUtf8("radioButton_EmailDesactivado"))
        self.horizontalLayout_4.addWidget(self.radioButton_EmailDesactivado)
        self.gridLayout.addWidget(self.frame_3, 16, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.pushButton_AgregarImagen = QtGui.QPushButton(self.groupBox)
        self.pushButton_AgregarImagen.setStyleSheet(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/picture-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AgregarImagen.setIcon(icon2)
        self.pushButton_AgregarImagen.setIconSize(QtCore.QSize(21, 24))
        self.pushButton_AgregarImagen.setAutoDefault(False)
        self.pushButton_AgregarImagen.setFlat(False)
        self.pushButton_AgregarImagen.setObjectName(_fromUtf8("pushButton_AgregarImagen"))
        self.gridLayout.addWidget(self.pushButton_AgregarImagen, 10, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.horizontalLayout_Image = QtGui.QHBoxLayout()
        self.horizontalLayout_Image.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout_Image.setObjectName(_fromUtf8("horizontalLayout_Image"))
        self.gridLayout.addLayout(self.horizontalLayout_Image, 9, 1, 4, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 3)
        self.pushButton_AgregarUsuario = QtGui.QPushButton(Dialog_AgregarUsuario)
        self.pushButton_AgregarUsuario.setStyleSheet(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/ico/guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AgregarUsuario.setIcon(icon3)
        self.pushButton_AgregarUsuario.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_AgregarUsuario.setAutoDefault(False)
        self.pushButton_AgregarUsuario.setFlat(True)
        self.pushButton_AgregarUsuario.setObjectName(_fromUtf8("pushButton_AgregarUsuario"))
        self.gridLayout_2.addWidget(self.pushButton_AgregarUsuario, 1, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 1, 0, 1, 1)

        self.retranslateUi(Dialog_AgregarUsuario)
        QtCore.QMetaObject.connectSlotsByName(Dialog_AgregarUsuario)
        Dialog_AgregarUsuario.setTabOrder(self.lineEdit_CodigoUsuario, self.comboBox_Parentesco)
        Dialog_AgregarUsuario.setTabOrder(self.comboBox_Parentesco, self.lineEdit_Nombre)
        Dialog_AgregarUsuario.setTabOrder(self.lineEdit_Nombre, self.lineEdit_Apellido)
        Dialog_AgregarUsuario.setTabOrder(self.lineEdit_Apellido, self.lineEdit_Clave)
        Dialog_AgregarUsuario.setTabOrder(self.lineEdit_Clave, self.lineEdit_Movil)
        Dialog_AgregarUsuario.setTabOrder(self.lineEdit_Movil, self.lineEdit_Email)
        Dialog_AgregarUsuario.setTabOrder(self.lineEdit_Email, self.dateEdit_Nacimiento)
        Dialog_AgregarUsuario.setTabOrder(self.dateEdit_Nacimiento, self.pushButton_AgregarImagen)
        Dialog_AgregarUsuario.setTabOrder(self.pushButton_AgregarImagen, self.radioButton_ActivadoSMS)
        Dialog_AgregarUsuario.setTabOrder(self.radioButton_ActivadoSMS, self.radioButton_DesactivadoSMS)
        Dialog_AgregarUsuario.setTabOrder(self.radioButton_DesactivadoSMS, self.spinBox_MaximoSMSMensual)
        Dialog_AgregarUsuario.setTabOrder(self.spinBox_MaximoSMSMensual, self.radioButton_EmailActivado)
        Dialog_AgregarUsuario.setTabOrder(self.radioButton_EmailActivado, self.radioButton_EmailDesactivado)
        Dialog_AgregarUsuario.setTabOrder(self.radioButton_EmailDesactivado, self.comboBox_Reportes)
        Dialog_AgregarUsuario.setTabOrder(self.comboBox_Reportes, self.pushButton_AgregarUsuario)
        Dialog_AgregarUsuario.setTabOrder(self.pushButton_AgregarUsuario, self.pushButton)
        Dialog_AgregarUsuario.setTabOrder(self.pushButton, self.pushButton_2)
        Dialog_AgregarUsuario.setTabOrder(self.pushButton_2, self.pushButton_3)
        Dialog_AgregarUsuario.setTabOrder(self.pushButton_3, self.pushButton_4)

    def retranslateUi(self, Dialog_AgregarUsuario):
        Dialog_AgregarUsuario.setWindowTitle(_translate("Dialog_AgregarUsuario", "Agregar Usuario", None))
        self.groupBox.setTitle(_translate("Dialog_AgregarUsuario", "Agregue la informacion del Usuario", None))
        self.label_8.setText(_translate("Dialog_AgregarUsuario", "Nacimiento", None))
        self.label_13.setText(_translate("Dialog_AgregarUsuario", "Maximo SMS Mensual", None))
        self.label_14.setText(_translate("Dialog_AgregarUsuario", "Estatus Alertas Email", None))
        self.label_9.setText(_translate("Dialog_AgregarUsuario", "Imagen", None))
        self.label_12.setText(_translate("Dialog_AgregarUsuario", "Estatus Alertas SMS", None))
        self.label_15.setText(_translate("Dialog_AgregarUsuario", "Reportes Email", None))
        self.label_10.setText(_translate("Dialog_AgregarUsuario", "Informacion del Usuario", None))
        self.label_3.setText(_translate("Dialog_AgregarUsuario", "Nombre", None))
        self.label.setText(_translate("Dialog_AgregarUsuario", "Codigo Usuario", None))
        self.label_11.setText(_translate("Dialog_AgregarUsuario", "Servicios", None))
        self.label_5.setText(_translate("Dialog_AgregarUsuario", "Clave", None))
        self.label_6.setText(_translate("Dialog_AgregarUsuario", "Movil", None))
        self.label_7.setText(_translate("Dialog_AgregarUsuario", "Email", None))
        self.radioButton_ActivadoSMS.setText(_translate("Dialog_AgregarUsuario", "Activado", None))
        self.radioButton_DesactivadoSMS.setText(_translate("Dialog_AgregarUsuario", "Desactivado", None))
        self.radioButton_EmailActivado.setText(_translate("Dialog_AgregarUsuario", "Activado", None))
        self.radioButton_EmailDesactivado.setText(_translate("Dialog_AgregarUsuario", "Desactivado", None))
        self.label_2.setText(_translate("Dialog_AgregarUsuario", "Parentesco", None))
        self.pushButton_AgregarImagen.setToolTip(_translate("Dialog_AgregarUsuario", "Agregar Imagen", None))
        self.pushButton_AgregarImagen.setText(_translate("Dialog_AgregarUsuario", "Agregar", None))
        self.label_4.setText(_translate("Dialog_AgregarUsuario", "Apellido", None))
        self.pushButton_AgregarUsuario.setToolTip(_translate("Dialog_AgregarUsuario", "Salvar Usuario", None))
        self.pushButton_AgregarUsuario.setText(_translate("Dialog_AgregarUsuario", "Agregar Usuario", None))

import recursos_rc
