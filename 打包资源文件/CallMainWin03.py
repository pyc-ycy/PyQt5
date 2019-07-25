# -*- coding:utf-8 -*-
# Time : 2019/07/25 上午 9:23 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : CallMainWin03.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from 打包资源文件.MainWin03 import Ui_Form03


class MyMainWindow(QMainWindow, Ui_Form03):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
