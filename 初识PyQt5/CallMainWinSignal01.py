# -*- coding:utf-8 -*-
# Time : 2019/07/24 下午 2:50 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : CallMainWinSignal01.py 
# @software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from 初识PyQt5.MainWinSignal01 import Ui_Form01


class MyMainWindow(QMainWindow, Ui_Form01):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())