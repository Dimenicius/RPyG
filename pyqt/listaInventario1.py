# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listaInventario.ui'
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
        Dialog.resize(764, 617)
        self.ID = QtGui.QLineEdit(Dialog)
        self.ID.setGeometry(QtCore.QRect(90, 30, 161, 32))
        self.ID.setText(_fromUtf8(""))
        self.ID.setObjectName(_fromUtf8("ID"))
        self.Description = QtGui.QLineEdit(Dialog)
        self.Description.setGeometry(QtCore.QRect(90, 190, 161, 32))
        self.Description.setText(_fromUtf8(""))
        self.Description.setObjectName(_fromUtf8("Description"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 40, 31, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 61, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 31, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 81, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 31, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 240, 41, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 280, 31, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.Value = QtGui.QLineEdit(Dialog)
        self.Value.setGeometry(QtCore.QRect(90, 230, 161, 32))
        self.Value.setText(_fromUtf8(""))
        self.Value.setObjectName(_fromUtf8("Value"))
        self.Name = QtGui.QLineEdit(Dialog)
        self.Name.setGeometry(QtCore.QRect(90, 70, 161, 32))
        self.Name.setText(_fromUtf8(""))
        self.Name.setObjectName(_fromUtf8("Name"))
        self.Type = QtGui.QComboBox(Dialog)
        self.Type.setGeometry(QtCore.QRect(90, 110, 161, 30))
        self.Type.setObjectName(_fromUtf8("Type"))
        self.Type.addItem(_fromUtf8(""))
        self.Type.addItem(_fromUtf8(""))
        self.Slot1 = QtGui.QComboBox(Dialog)
        self.Slot1.setGeometry(QtCore.QRect(90, 150, 161, 30))
        self.Slot1.setObjectName(_fromUtf8("Slot1"))
        self.Slot1.addItem(_fromUtf8(""))
        self.Slot1.addItem(_fromUtf8(""))
        self.Slot1.addItem(_fromUtf8(""))
        self.Slot1.addItem(_fromUtf8(""))
        self.Slot1.addItem(_fromUtf8(""))
        self.Slot2 = QtGui.QComboBox(Dialog)
        self.Slot2.setGeometry(QtCore.QRect(270, 150, 121, 30))
        self.Slot2.setObjectName(_fromUtf8("Slot2"))
        self.Slot2.addItem(_fromUtf8(""))
        self.Slot2.addItem(_fromUtf8(""))
        self.Selecionar = QtGui.QPushButton(Dialog)
        self.Selecionar.setGeometry(QtCore.QRect(270, 110, 90, 28))
        self.Selecionar.setObjectName(_fromUtf8("Selecionar"))
        self.Upload = QtGui.QPushButton(Dialog)
        self.Upload.setGeometry(QtCore.QRect(90, 270, 161, 28))
        self.Upload.setObjectName(_fromUtf8("Upload"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.Type, QtCore.SIGNAL(
            _fromUtf8("activated(QString)")), self.Selecionar.click)
        QtCore.QObject.connect(self.Slot2, QtCore.SIGNAL(
            _fromUtf8("activated(int)")), self.Slot1.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "ID", None))
        self.label_2.setText(_translate("Dialog", "Name", None))
        self.label_3.setText(_translate("Dialog", "Type", None))
        self.label_4.setText(_translate("Dialog", "Description", None))
        self.label_5.setText(_translate("Dialog", "Slot", None))
        self.label_6.setText(_translate("Dialog", "Value", None))
        self.label_8.setText(_translate("Dialog", "Img", None))
        self.Type.setItemText(0, _translate("Dialog", "Equipavel", None))
        self.Type.setItemText(1, _translate("Dialog", "Consumivel", None))
        self.Slot1.setItemText(0, _translate("Dialog", "Almuleto", None))
        self.Slot1.setItemText(1, _translate("Dialog", "Uma Mão", None))
        self.Slot1.setItemText(2, _translate("Dialog", "Duas Mãos", None))
        self.Slot1.setItemText(3, _translate("Dialog", "Armadura", None))
        self.Slot1.setItemText(4, _translate("Dialog", "Bota", None))
        self.Slot2.setItemText(0, _translate("Dialog", "Livre", None))
        self.Slot2.setItemText(1, _translate("Dialog", "Batalha", None))
        self.Selecionar.setText(_translate("Dialog", "Selecionar", None))
        self.Upload.setText(_translate("Dialog", "Upload", None))
