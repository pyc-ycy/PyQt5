# !/usr/bin/env python3.7
# encoding: utf-8
# Time : 2019/6/23 15:10 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt_test.py 
# @software: PyCharm

import sys
from PyQt5 import QtWidgets, QtCore

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(260, 360)
widget.setWindowTitle("Hello PyQt5")
widget.show()
sys.exit(app.exec_())
