# -*- coding:utf-8 -*-
# Time : 2019/08/30 上午 8:50 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : WebViewTest02.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('加载并显示本地页面示例')
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.setGeometry(5, 30, 553, 330)
        self.browser = QWebEngineView()
        url = r'D:/users/lenovo/PyQt5/高级界面控件/index.html'
        self.browser.load(QUrl(url))
        self.setCentralWidget(self.browser)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
