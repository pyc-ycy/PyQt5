# -*- coding:utf-8 -*-
# Time : 2019/08/30 下午 9:27 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : WebViewJSTest02.py 
# @software: PyCharm


import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from 高级界面控件.MyShareObject import MyShareObject
from PyQt5.QtWebChannel import QWebChannel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QWidget()
    win.setWindowTitle('Web 页面中 JavaScript 与 QWebEngineView 交互示例')
    win.setWindowIcon(QIcon("./images/Python2.ico"))
    layout = QVBoxLayout()
    win.setLayout(layout)
    view = QWebEngineView()
    htmlUrl = 'http://192.168.3.105:8020/web/index.html'
    view.load(QUrl(htmlUrl))
    channel = QWebChannel()
    myObj = MyShareObject()
    channel.registerObject("bridge", myObj)
    view.page().setWebChannel(channel)
    layout.addWidget(view)
    win.show()
    sys.exit(app.exec_())
