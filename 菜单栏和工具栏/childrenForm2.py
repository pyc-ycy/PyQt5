# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'childrenForm2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChildrenForm2(object):
    def setupUi(self, ChildrenForm2):
        ChildrenForm2.setObjectName("ChildrenForm2")
        ChildrenForm2.resize(440, 345)
        self.textEdit = QtWidgets.QTextEdit(ChildrenForm2)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 421, 331))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(ChildrenForm2)
        QtCore.QMetaObject.connectSlotsByName(ChildrenForm2)

    def retranslateUi(self, ChildrenForm2):
        _translate = QtCore.QCoreApplication.translate
        ChildrenForm2.setWindowTitle(_translate("ChildrenForm2", "Dialog"))
        self.textEdit.setPlaceholderText(_translate("ChildrenForm2", "我是子窗口的内容"))

