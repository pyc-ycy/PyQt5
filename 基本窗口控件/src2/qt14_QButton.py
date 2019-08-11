# -*- coding:utf-8 -*-
# Time : 2019/08/11 下午 5:31 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt14_QButton.py 
# @software: PyCharm


import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class From(QDialog):
    def __init__(self, parent=None):
        super(From, self).__init__(parent)
        layout = QVBoxLayout()

        self.btn1 = QPushButton("Button1")
        self.btn1.setCheckable(True)
        self.btn1.toggle()
        self.btn1.clicked.connect(lambda: self.whichbtn(self.btn1))
        self.btn1.clicked.connect(self.btnState)
        layout.addWidget(self.btn1)

        self.btn2 = QPushButton('image')
        self.btn2.setIcon(QIcon("images/Python2.ico"))
        self.btn2.clicked.connect(lambda: self.whichbtn(self.btn2))
        layout.addWidget(self.btn2)
        self.setLayout(layout)

        self.btn3 = QPushButton("Disable")
        self.btn3.setEnabled(False)
        layout.addWidget(self.btn3)

        self.btn4 = QPushButton("&Download")
        self.btn4.setDefault(True)
        self.btn4.clicked.connect(lambda: self.whichbtn(self.btn4))
        layout.addWidget(self.btn4)
        self.setWindowTitle("Button Demo")

    def btnState(self):
        if self.btn1.isChecked():
            print("button pressed")
        else:
            print("button released")

    @staticmethod
    def whichbtn(btn):
        print("clicked button is " + btn.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    btnDemo = From()
    btnDemo.show()
    sys.exit(app.exec_())