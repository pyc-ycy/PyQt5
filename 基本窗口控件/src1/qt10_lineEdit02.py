# -*- coding:utf-8 -*-
# Time : 2019/08/03 下午 1:10 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt10_lineEdit02.py 
# @software: PyCharm


from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys


class lineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(lineEditDemo, self).__init__(parent)
        self.setWindowTitle("QLineEdit 例子")

        flo = QFormLayout()
        pIntLineEdit = QLineEdit()
        pDoubleLineEdit = QLineEdit()
        pValidatorLineEdit = QLineEdit()

        flo.addRow("整型:", pIntLineEdit)
        flo.addRow("浮点型:", pDoubleLineEdit)
        flo.addRow("字母和数字:", pValidatorLineEdit)

        pIntLineEdit.setPlaceholderText("整型")
        pDoubleLineEdit.setPlaceholderText("浮点型")
        pValidatorLineEdit.setPlaceholderText("字母和数字")

        # 整数范围：[1, 99]
        pIntValidator = QIntValidator(self)
        pIntValidator.setRange(1, 99)

        # 浮点型范围：[-360, 360], 精度：0.00
        pDoubleValidator = QDoubleValidator(self)
        pDoubleValidator.setRange(-360, 360)
        pDoubleValidator.setNotation(QDoubleValidator.StandardNotation)
        pDoubleValidator.setDecimals(2)

        # 字母和数字
        reg = QRegExp("[a-zA-Z0-9]+$")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)

        # 设置验证器
        pIntLineEdit.setValidator(pIntValidator)
        pDoubleLineEdit.setValidator(pDoubleValidator)
        pValidatorLineEdit.setValidator(pValidator)

        self.setLayout(flo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = lineEditDemo()
    win.show()
    sys.exit(app.exec_())