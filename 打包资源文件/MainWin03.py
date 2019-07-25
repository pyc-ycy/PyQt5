# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin03.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form03(object):
    def setupUi(self, Form03):
        Form03.setObjectName("Form03")
        Form03.resize(556, 456)
        self.label = QtWidgets.QLabel(Form03)
        self.label.setGeometry(QtCore.QRect(30, 10, 521, 431))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/pic/log1.jpg"))
        self.label.setObjectName("label")

        self.retranslateUi(Form03)
        QtCore.QMetaObject.connectSlotsByName(Form03)

    def retranslateUi(self, Form03):
        _translate = QtCore.QCoreApplication.translate
        Form03.setWindowTitle(_translate("Form03", "打包资源文件"))

import apprcc_rc
