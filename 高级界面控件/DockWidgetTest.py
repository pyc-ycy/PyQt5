# -*- coding:utf-8 -*-
# Time : 2019/08/27 上午 10:34 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : DockWidgetTest.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class DockDemo(QMainWindow):
    def __init__(self, parent=None):
        super(DockDemo, self).__init__(parent)
        layout = QHBoxLayout()
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("Save")
        file.addAction("Quit")
        self.items = QDockWidget("Dock", self)
        self.listWidget = QListWidget()
        self.listWidget.addItem("item 1")
        self.listWidget.addItem("Item 2")
        self.listWidget.addItem("Item 3")
        self.items.setWidget(self.listWidget)
        self.items.setFloating(False)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)
        self.setLayout(layout)
        self.setWindowTitle("QDockWidget 例子")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        # self.resize(400, 200)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = DockDemo()
    win.show()
    sys.exit(app.exec_())