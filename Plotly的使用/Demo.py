# -*- coding:utf-8 -*-
# Time : 2019/10/04 下午 8:12 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : Demo.py 
# @software: PyCharm


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.qWebEngine = QWebEngineView(self)
        self.qWebEngine.setGeometry(QRect(50, 20, 1200, 600))
        self.qWebEngine.load(QUrl.fromLocalFile('\plotly_html\if_hs300_bais.html'))
        self.setWindowTitle("Plotly Demo")
        self.setWindowIcon(QIcon("./images/Python2.ico"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())
