# -*- coding:utf-8 -*-
# Time : 2019/08/29 下午 8:40 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : WebViewTest01.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('WebViewTest')
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()
        # 加载外部的 Web 页面
        self.browser.load(QUrl('https://me.csdn.net/qq_42896653'))
        self.setCentralWidget(self.browser)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
