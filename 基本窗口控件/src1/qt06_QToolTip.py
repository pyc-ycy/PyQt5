# -*- coding:utf-8 -*-
# Time : 2019/08/01 下午 3:49 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt06_QToolTip.py 
# @software: PyCharm

import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QApplication
from PyQt5.QtGui import QFont, QIcon


class WinForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip("这是一个<b>气泡提示</b>")
        self.setGeometry(200, 300, 400, 400)
        self.setWindowIcon(QIcon("Python2.ico"))
        self.setWindowTitle('气泡提示Demo')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())