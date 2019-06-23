# !/usr/bin/env python3.7
# encoding: utf-8
# Time : 2019/6/23 17:23 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : CallMainWin01.py.py 
# @software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QWidget

from 初识PyQt5.MainWin01 import Ui_Form


class Widget1(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWidget = Widget1()
    myWidget.show()
    sys.exit(app.exec_())
