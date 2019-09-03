# -*- coding:utf-8 -*-
# Time : 2019/09/03 下午 4:15 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : formLayoutTest.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('FormLayout Demo')
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(400, 100)
        formLayout = QFormLayout()
        lbl1 = QLabel("姓名：")
        lineEdit1 = QLineEdit()
        lbl2 = QLabel("民族：")
        lineEdit2 = QLineEdit()
        lbl3 = QLabel("籍贯：")
        lineEdit3 = QLineEdit()
        formLayout.addRow(lbl1, lineEdit1)
        formLayout.addRow(lbl2, lineEdit2)
        formLayout.addRow(lbl3, lineEdit3)
        self.setLayout(formLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
