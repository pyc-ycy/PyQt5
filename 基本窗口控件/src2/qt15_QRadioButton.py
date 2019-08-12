# -*- coding:utf-8 -*-
# Time : 2019/08/12 上午 11:06 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt15_QRadioButton.py 
# @software: PyCharm


import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


class RadioDemo(QWidget):
    def __init__(self, parent=None):
        super(RadioDemo, self).__init__(parent)
        layout = QHBoxLayout()
        self.btn1 = QRadioButton("button1")
        self.btn1.setCheckable(True)
        self.btn1.toggled.connect(lambda: self.btnState(self.btn1))
        layout.addWidget(self.btn1)

        self.btn2 = QRadioButton("button2")
        self.btn2.toggled.connect(lambda: self.btnState(self.btn2))
        layout.addWidget(self.btn2)
        self.setLayout(layout)
        self.setWindowTitle("RadioButton Demo")
        self.setWindowIcon(QIcon("./images/Python2.ico"))

    @staticmethod
    def btnState(btn):
        if btn.text() == "button1":
            if btn.isChecked():
                print(btn.text() + " is selected")
            else:
                print(btn.text() + " is deselected")
        if btn.text() == "button2":
            if btn.isChecked():
                print(btn.text() + " is selected")
            else:
                print(btn.text() + " is deselected")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = RadioDemo()
    win.show()
    sys.exit(app.exec_())
