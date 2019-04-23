# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(29, 29, 341, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.fingersLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.fingersLabel.setObjectName("fingersLabel")
        self.gridLayout.addWidget(self.fingersLabel, 2, 1, 1, 1)
        self.actionLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.actionLabel.setObjectName("actionLabel")
        self.gridLayout.addWidget(self.actionLabel, 1, 1, 1, 1)
        self.keyboardLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.keyboardLabel.setObjectName("keyboardLabel")
        self.gridLayout.addWidget(self.keyboardLabel, 3, 1, 1, 1)
        self.actionMenu = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.actionMenu.setObjectName("actionMenu")
        self.actionMenu.addItem("")
        self.actionMenu.setItemText(0, "")
        self.actionMenu.addItem("")
        self.actionMenu.addItem("")
        self.actionMenu.addItem("")
        self.actionMenu.addItem("")
        self.actionMenu.addItem("")
        self.actionMenu.addItem("")
        self.actionMenu.addItem("")
        self.actionMenu.addItem("")
        self.actionMenu.addItem("")
        self.actionMenu.addItem("")
        self.actionMenu.addItem("")
        self.actionMenu.addItem("")
        self.gridLayout.addWidget(self.actionMenu, 1, 2, 1, 1)
        self.fingersLine = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.fingersLine.setObjectName("fingersLine")
        self.gridLayout.addWidget(self.fingersLine, 2, 2, 1, 1)
        self.keyboardLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.keyboardLine.setObjectName("keyboardLine")
        self.gridLayout.addWidget(self.keyboardLine, 3, 2, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 4, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fingersLabel.setText(_translate("Form", "Fingers"))
        self.actionLabel.setText(_translate("Form", "Action"))
        self.keyboardLabel.setText(_translate("Form", "Keyboard shortcut"))
        self.actionMenu.setItemText(1, _translate("Form", "Swipe Up"))
        self.actionMenu.setItemText(2, _translate("Form", "Swipe Down"))
        self.actionMenu.setItemText(3, _translate("Form", "Swipe Left"))
        self.actionMenu.setItemText(4, _translate("Form", "Swipe LeftUp"))
        self.actionMenu.setItemText(5, _translate("Form", "Swipe LeftDown"))
        self.actionMenu.setItemText(6, _translate("Form", "Swipe Right"))
        self.actionMenu.setItemText(7, _translate("Form", "Swipe RightUp"))
        self.actionMenu.setItemText(8, _translate("Form", "Swipe RightDown"))
        self.actionMenu.setItemText(9, _translate("Form", "Pinch In"))
        self.actionMenu.setItemText(10, _translate("Form", "Pinch Out"))
        self.actionMenu.setItemText(11, _translate("Form", "Pinch Clockwise"))
        self.actionMenu.setItemText(12, _translate("Form", "Pinch Anticlockwise"))
        self.saveButton.setText(_translate("Form", "Save changes"))

