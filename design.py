# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LibinputGesturesGUI(object):
    def setupUi(self, LibinputGesturesGUI):
        LibinputGesturesGUI.setObjectName("LibinputGesturesGUI")
        LibinputGesturesGUI.resize(372, 390)
        self.centralwidget = QtWidgets.QWidget(LibinputGesturesGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(100, 270, 161, 34))
        self.saveButton.setObjectName("saveButton")
        self.actionMenu = QtWidgets.QComboBox(self.centralwidget)
        self.actionMenu.setGeometry(QtCore.QRect(160, 60, 161, 31))
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
        self.actionLabel = QtWidgets.QLabel(self.centralwidget)
        self.actionLabel.setGeometry(QtCore.QRect(50, 60, 71, 31))
        self.actionLabel.setObjectName("actionLabel")
        self.fingersLabel = QtWidgets.QLabel(self.centralwidget)
        self.fingersLabel.setGeometry(QtCore.QRect(50, 130, 58, 18))
        self.fingersLabel.setObjectName("fingersLabel")
        self.fingersLine = QtWidgets.QSpinBox(self.centralwidget)
        self.fingersLine.setGeometry(QtCore.QRect(160, 120, 161, 32))
        self.fingersLine.setObjectName("fingersLine")
        self.keyboardLabel = QtWidgets.QLabel(self.centralwidget)
        self.keyboardLabel.setGeometry(QtCore.QRect(20, 200, 121, 18))
        self.keyboardLabel.setObjectName("keyboardLabel")
        self.keyboardLine = QtWidgets.QLineEdit(self.centralwidget)
        self.keyboardLine.setGeometry(QtCore.QRect(162, 190, 161, 32))
        self.keyboardLine.setObjectName("keyboardLine")
        LibinputGesturesGUI.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LibinputGesturesGUI)
        self.statusbar.setObjectName("statusbar")
        LibinputGesturesGUI.setStatusBar(self.statusbar)

        self.retranslateUi(LibinputGesturesGUI)
        QtCore.QMetaObject.connectSlotsByName(LibinputGesturesGUI)

    def retranslateUi(self, LibinputGesturesGUI):
        _translate = QtCore.QCoreApplication.translate
        LibinputGesturesGUI.setWindowTitle(_translate("LibinputGesturesGUI", "MainWindow"))
        self.saveButton.setText(_translate("LibinputGesturesGUI", "Save changes"))
        self.actionMenu.setItemText(0, _translate("LibinputGesturesGUI", "Swipe Up"))
        self.actionMenu.setItemText(1, _translate("LibinputGesturesGUI", "Swipe Down"))
        self.actionMenu.setItemText(2, _translate("LibinputGesturesGUI", "Swipe Left"))
        self.actionMenu.setItemText(3, _translate("LibinputGesturesGUI", "Swipe LeftUp"))
        self.actionMenu.setItemText(4, _translate("LibinputGesturesGUI", "Swipe LeftDown"))
        self.actionMenu.setItemText(5, _translate("LibinputGesturesGUI", "Swipe Right"))
        self.actionMenu.setItemText(6, _translate("LibinputGesturesGUI", "Swipe RightUp"))
        self.actionMenu.setItemText(7, _translate("LibinputGesturesGUI", "Swipe RightDown"))
        self.actionMenu.setItemText(8, _translate("LibinputGesturesGUI", "Pinch In"))
        self.actionMenu.setItemText(9, _translate("LibinputGesturesGUI", "Pinch Out"))
        self.actionMenu.setItemText(10, _translate("LibinputGesturesGUI", "Pinch Clockwise"))
        self.actionMenu.setItemText(11, _translate("LibinputGesturesGUI", "Pinch Anticlockwise"))
        self.actionLabel.setText(_translate("LibinputGesturesGUI", "Action"))
        self.fingersLabel.setText(_translate("LibinputGesturesGUI", "Fingers"))
        self.keyboardLabel.setText(_translate("LibinputGesturesGUI", "Keyboard shortcut"))

