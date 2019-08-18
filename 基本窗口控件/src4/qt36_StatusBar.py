# -*- coding:utf-8 -*-
# Time : 2019/08/18 下午 9:05 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt36_StatusBar.py 
# @software: PyCharm


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class StatusDemo(QMainWindow):
    def __init__(self, parent=None):
        super(StatusDemo, self).__init__(parent)
        self.setWindowTitle("状态栏示例")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        menuBar = self.menuBar()
        file = menuBar.addMenu("File")
        file.addAction("show")
        file.triggered[QAction].connect(self.processTrigger)
        self.setCentralWidget(QTextEdit())
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

    def processTrigger(self, q):
        if q.text() == "show":
            self.statusBar.showMessage(q.text() + " 菜单选项被点击了", 5000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = StatusDemo()
    demo.show()
    sys.exit(app.exec_())