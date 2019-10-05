# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WeatherWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(715, 440)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ICON/images/Python2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 661, 321))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 41, 16))
        self.label.setObjectName("label")
        self.weatherComboBox = QtWidgets.QComboBox(self.groupBox)
        self.weatherComboBox.setGeometry(QtCore.QRect(90, 30, 151, 22))
        self.weatherComboBox.setObjectName("weatherComboBox")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.resultText = QtWidgets.QTextEdit(self.groupBox)
        self.resultText.setGeometry(QtCore.QRect(10, 70, 641, 241))
        self.resultText.setObjectName("resultText")
        self.queryBtn = QtWidgets.QPushButton(Form)
        self.queryBtn.setGeometry(QtCore.QRect(80, 380, 93, 28))
        self.queryBtn.setObjectName("queryBtn")
        self.clearBtn = QtWidgets.QPushButton(Form)
        self.clearBtn.setGeometry(QtCore.QRect(500, 380, 93, 28))
        self.clearBtn.setObjectName("clearBtn")

        self.retranslateUi(Form)
        self.queryBtn.clicked.connect(Form.queryWeather)
        self.clearBtn.clicked.connect(Form.clearResult)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "查询城市天气"))
        self.groupBox.setTitle(_translate("Form", "查询城市天气"))
        self.label.setText(_translate("Form", "城市"))
        self.weatherComboBox.setItemText(0, _translate("Form", "陆丰"))
        self.weatherComboBox.setItemText(1, _translate("Form", "天津"))
        self.weatherComboBox.setItemText(2, _translate("Form", "上海"))
        self.weatherComboBox.setItemText(3, _translate("Form", "北京"))
        self.queryBtn.setText(_translate("Form", "查询"))
        self.clearBtn.setText(_translate("Form", "清空"))


from 综合应用.getCityWeather import images_rc
