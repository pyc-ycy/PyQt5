# -*- coding:utf-8 -*-
# Time : 2019/08/31 下午 8:17 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : HBoxLayoutTest.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle("水平布局示例")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        # self.resize(550, 400)
        hLayout = QHBoxLayout()
        hLayout.addWidget(QPushButton(str(1)))
        hLayout.addWidget(QPushButton(str(2)))
        hLayout.addWidget(QPushButton(str(3)))
        hLayout.addWidget(QPushButton(str(4)))
        hLayout.addWidget(QPushButton(str(5)))
        hLayout.setSpacing(0)
        self.setLayout(hLayout)
        # hLayout.addWidget(QPushButton(str(1)), 0, Qt.AlignTop)
        # hLayout.addWidget(QPushButton(str(2)), 0, Qt.AlignLeft | Qt.AlignTop)
        # hLayout.addWidget(QPushButton(str(3)))
        # hLayout.addWidget(QPushButton(str(4)), 0, Qt.AlignLeft | Qt.AlignBottom)
        # hLayout.addWidget(QPushButton(str(5)), 0, Qt.AlignLeft | Qt.AlignBottom)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
