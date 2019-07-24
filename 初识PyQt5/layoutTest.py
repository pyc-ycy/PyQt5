# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layoutTest.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LayoutDemo(object):
    def setupUi(self, LayoutDemo):
        LayoutDemo.setObjectName("LayoutDemo")
        LayoutDemo.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(LayoutDemo)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(316, 141, 16, 109))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(447, 181, 93, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(62, 142, 16, 17))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_maxdrawdown = QtWidgets.QLabel(self.centralwidget)
        self.label_maxdrawdown.setGeometry(QtCore.QRect(60, 200, 60, 16))
        self.label_maxdrawdown.setObjectName("label_maxdrawdown")
        self.label_return = QtWidgets.QLabel(self.centralwidget)
        self.label_return.setGeometry(QtCore.QRect(62, 166, 30, 16))
        self.label_return.setObjectName("label_return")
        self.label_sharp = QtWidgets.QLabel(self.centralwidget)
        self.label_sharp.setGeometry(QtCore.QRect(60, 230, 63, 16))
        self.label_sharp.setObjectName("label_sharp")
        self.doubleSpinBox_maxdrawdown_min = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_maxdrawdown_min.setGeometry(QtCore.QRect(161, 192, 70, 21))
        self.doubleSpinBox_maxdrawdown_min.setObjectName("doubleSpinBox_maxdrawdown_min")
        self.doubleSpinBox_maxdrawdown_max = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_maxdrawdown_max.setGeometry(QtCore.QRect(238, 192, 70, 21))
        self.doubleSpinBox_maxdrawdown_max.setObjectName("doubleSpinBox_maxdrawdown_max")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(161, 142, 45, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(238, 142, 45, 16))
        self.label_2.setObjectName("label_2")
        self.doubleSpinBox_returns_min = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_returns_min.setGeometry(QtCore.QRect(161, 164, 70, 21))
        self.doubleSpinBox_returns_min.setObjectName("doubleSpinBox_returns_min")
        self.doubleSpinBox_returns_max = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_returns_max.setGeometry(QtCore.QRect(238, 164, 70, 21))
        self.doubleSpinBox_returns_max.setObjectName("doubleSpinBox_returns_max")
        self.doubleSpinBox_sharp_min = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_sharp_min.setGeometry(QtCore.QRect(161, 220, 70, 21))
        self.doubleSpinBox_sharp_min.setObjectName("doubleSpinBox_sharp_min")
        self.doubleSpinBox_sharp_max = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_sharp_max.setGeometry(QtCore.QRect(238, 220, 70, 21))
        self.doubleSpinBox_sharp_max.setObjectName("doubleSpinBox_sharp_max")
        LayoutDemo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LayoutDemo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        LayoutDemo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LayoutDemo)
        self.statusbar.setObjectName("statusbar")
        LayoutDemo.setStatusBar(self.statusbar)
        self.label_sharp.setBuddy(self.doubleSpinBox_sharp_min)

        self.retranslateUi(LayoutDemo)
        QtCore.QMetaObject.connectSlotsByName(LayoutDemo)

    def retranslateUi(self, LayoutDemo):
        _translate = QtCore.QCoreApplication.translate
        LayoutDemo.setWindowTitle(_translate("LayoutDemo", "MainWindow"))
        self.pushButton.setText(_translate("LayoutDemo", "开始"))
        self.label_maxdrawdown.setText(_translate("LayoutDemo", "最大回撤"))
        self.label_return.setText(_translate("LayoutDemo", "收益"))
        self.label_sharp.setText(_translate("LayoutDemo", "&sharp比"))
        self.label.setText(_translate("LayoutDemo", "最小值"))
        self.label_2.setText(_translate("LayoutDemo", "最大值"))

