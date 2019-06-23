# !/usr/bin/env python3.7
# encoding: utf-8
# Time : 2019/6/23 15:47 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : CallfirstMainWin.py 
# @software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from 初识PyQt5.firstMainWin import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
