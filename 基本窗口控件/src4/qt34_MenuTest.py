# -*- coding:utf-8 -*-
# Time : 2019/08/18 下午 4:42 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt34_MenuTest.py 
# @software: PyCharm


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MenuDemo(QMainWindow):
    def __init__(self, parent=None):
        super(MenuDemo, self).__init__(parent)
        self.setWindowTitle("Menu 示例")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        layout = QHBoxLayout()
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        save = QAction("Save", self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)
        edit = file.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")
        quit = QAction("Quit", self)
        file.addAction(quit)
        file.triggered[QAction].connect(self.processTrigger)
        self.setLayout(layout)

    @staticmethod
    def processTrigger(q):
        print(q.text() + " is triggered")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MenuDemo()
    win.show()
    sys.exit(app.exec_())