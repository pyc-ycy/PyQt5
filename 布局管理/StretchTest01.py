# -*- coding:utf-8 -*-
# Time : 2019/09/01 下午 2:51 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : StretchTest01.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class WinForm(QWidget):
    def __init__(self):
        super(WinForm, self).__init__()
        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        btn3 = QPushButton(self)
        btn1.setText('button 1')
        btn2.setText('button 2')
        btn3.setText('button 3')
        hBox = QHBoxLayout()
        # 设置伸缩量为 1
        hBox.addStretch(1)
        hBox.addWidget(btn1)
        hBox.addStretch(1)
        hBox.addWidget(btn2)
        hBox.addStretch(1)
        hBox.addWidget(btn3)
        hBox.addStretch(1)
        self.setLayout(hBox)
        self.setWindowTitle("addStretch Demo")
        self.setWindowIcon(QIcon("./images/Python2.ico"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
