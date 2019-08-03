# -*- coding:utf-8 -*-
# Time : 2019/08/03 上午 8:51 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt08_QLabel1.py 
# @software: PyCharm


from PyQt5.QtWidgets import *
import sys


class QLabelDemo(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel 标签快捷键的使用例子")
        nameLBl = QLabel('&Name', self)
        nameED1 = QLineEdit(self)
        nameLBl.setBuddy(nameED1)

        nameLB2 = QLabel('&Password', self)
        nameED2 = QLineEdit(self)
        nameLB2.setBuddy(nameED2)

        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLBl, 0, 0)
        mainLayout.addWidget(nameED1, 0, 1, 1, 2)

        mainLayout.addWidget(nameLB2, 1, 0)
        mainLayout.addWidget(nameED2, 1, 1, 1, 2)

        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    labelDemo = QLabelDemo()
    labelDemo.show()
    sys,exit(app.exec_())