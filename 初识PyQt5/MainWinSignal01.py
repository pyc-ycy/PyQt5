# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWinSignal01.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form01(object):
    def setupUi(self, Form01):
        Form01.setObjectName("Form01")
        Form01.resize(553, 401)
        self.closeWinBtn = QtWidgets.QPushButton(Form01)
        self.closeWinBtn.setGeometry(QtCore.QRect(170, 170, 93, 28))
        self.closeWinBtn.setObjectName("closeWinBtn")

        self.retranslateUi(Form01)
        self.closeWinBtn.clicked.connect(Form01.close)
        QtCore.QMetaObject.connectSlotsByName(Form01)

    def retranslateUi(self, Form01):
        _translate = QtCore.QCoreApplication.translate
        Form01.setWindowTitle(_translate("Form01", "Form"))
        self.closeWinBtn.setText(_translate("Form01", "关闭窗口"))
