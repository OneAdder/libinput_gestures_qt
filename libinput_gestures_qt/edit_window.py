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
        Form.resize(468, 196)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.fingersLabel = QtWidgets.QLabel(Form)
        self.fingersLabel.setObjectName("fingersLabel")
        self.gridLayout.addWidget(self.fingersLabel, 2, 1, 1, 1)
        self.actionLabel = QtWidgets.QLabel(Form)
        self.actionLabel.setObjectName("actionLabel")
        self.gridLayout.addWidget(self.actionLabel, 1, 1, 1, 1)
        self.actionMenu = QtWidgets.QComboBox(Form)
        self.actionMenu.setObjectName("actionMenu")
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
        self.fingersLine = QtWidgets.QSpinBox(Form)
        self.fingersLine.setObjectName("fingersLine")
        self.gridLayout.addWidget(self.fingersLine, 2, 2, 1, 1)
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 5, 2, 1, 1)
        self.shortcut_command = QtWidgets.QComboBox(Form)
        self.shortcut_command.setObjectName("shortcut_command")
        self.shortcut_command.addItem("")
        self.shortcut_command.addItem("")
        self.shortcut_command.addItem("")
        self.gridLayout.addWidget(self.shortcut_command, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)
        self.actionType = QtWidgets.QLabel(Form)
        self.actionType.setObjectName("actionType")
        self.gridLayout.addWidget(self.actionType, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fingersLabel.setText(_translate("Form", "Fingers"))
        self.actionLabel.setText(_translate("Form", "Gesture"))
        self.actionMenu.setItemText(0, _translate("Form", "Swipe Up"))
        self.actionMenu.setItemText(1, _translate("Form", "Swipe Down"))
        self.actionMenu.setItemText(2, _translate("Form", "Swipe Left"))
        self.actionMenu.setItemText(3, _translate("Form", "Swipe LeftUp"))
        self.actionMenu.setItemText(4, _translate("Form", "Swipe LeftDown"))
        self.actionMenu.setItemText(5, _translate("Form", "Swipe Right"))
        self.actionMenu.setItemText(6, _translate("Form", "Swipe RightUp"))
        self.actionMenu.setItemText(7, _translate("Form", "Swipe RightDown"))
        self.actionMenu.setItemText(8, _translate("Form", "Pinch In"))
        self.actionMenu.setItemText(9, _translate("Form", "Pinch Out"))
        self.actionMenu.setItemText(10, _translate("Form", "Pinch Clockwise"))
        self.actionMenu.setItemText(11, _translate("Form", "Pinch Anticlockwise"))
        self.saveButton.setText(_translate("Form", "Save changes"))
        self.shortcut_command.setItemText(0, _translate("Form", "Keyboard Shortcut"))
        self.shortcut_command.setItemText(1, _translate("Form", "Plasma action"))
        self.shortcut_command.setItemText(2, _translate("Form", "Command"))
        self.label.setText(_translate("Form", "Action"))
        self.actionType.setText(_translate("Form", "Keyboard Shortcut"))

