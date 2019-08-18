# -*- coding:utf-8 -*-
# Time : 2019/08/18 下午 8:23 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt35_ToolBar.py 
# @software: PyCharm


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ToolBarDemo(QMainWindow):
    def __init__(self, parent=None):
        super(ToolBarDemo, self).__init__(parent)
        self.setWindowTitle("工具栏示例")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(300, 200)

        layout = QVBoxLayout()
        tb = self.addToolBar("File")
        new = QAction(QIcon("./images/new.png"), "new", self)
        tb.addAction(new)
        open = QAction(QIcon("./images/open.png"), "open", self)
        tb.addAction(open)
        save = QAction(QIcon("./images/save.png"), "save", self)
        tb.addAction(save)
        tb.actionTriggered[QAction].connect(self.toolBtnPressed)
        self.setLayout(layout)

    @staticmethod
    def toolBtnPressed(a):
        print("pressed tool button is ", a.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = ToolBarDemo()
    demo.show()
    sys.exit(app.exec_())
