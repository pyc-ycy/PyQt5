# -*- coding:utf-8 -*-
# Time : 2019/09/04 下午 8:52 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : QSplitterRest.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class WinForm(QWidget):
    def __init__(self):
        super(WinForm, self).__init__()
        self.initUI()

    def initUI(self):
        hBox = QHBoxLayout()
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.setWindowTitle("QSplitter Demo")
        self.setGeometry(300, 300, 300, 200)
        topLeft = QFrame()
        topLeft.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)
        splitter1 = QSplitter(Qt.Horizontal)
        textEdit = QTextEdit()
        splitter1.addWidget(topLeft)
        splitter1.addWidget(textEdit)
        splitter1.setSizes([100, 200])
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        hBox.addWidget(splitter2)
        self.setLayout(hBox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
