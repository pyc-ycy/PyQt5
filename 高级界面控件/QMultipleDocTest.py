# -*- coding:utf-8 -*-
# Time : 2019/08/27 下午 5:45 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : QMultipleDocTest.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    count = 0

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("Cascade")
        file.addAction("Tiled")
        file.triggered[QAction].connect(self.windowAction)
        self.setWindowTitle("MDI Demo")
        self.setWindowIcon(QIcon("./images/Python2.ico"))

    def windowAction(self, q):
        print("triggered")

        if q.text() == "New":
            MainWindow.count = MainWindow.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("SubWindow" + str(MainWindow.count))
            sub.setWindowIcon(QIcon("./images/Python2.ico"))
            self.mdi.addSubWindow(sub)
            sub.show()
        if q.text() == "Cascade":
            self.mdi.cascadeSubWindows()
        if q.text() == "Tiled":
            self.mdi.tileSubWindows()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
