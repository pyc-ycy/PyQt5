# -*- coding:utf-8 -*-
# Time : 2019/09/01 下午 2:38 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : VBoxLayoutTest.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('垂直布局示例')
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        vLayout = QVBoxLayout()
        vLayout.addWidget(QPushButton(str(1)))
        vLayout.addWidget(QPushButton(str(2)))
        vLayout.addWidget(QPushButton(str(3)))
        vLayout.addWidget(QPushButton(str(4)))
        vLayout.addWidget(QPushButton(str(5)))
        self.setLayout(vLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
