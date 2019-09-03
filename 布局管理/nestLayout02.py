# -*- coding:utf-8 -*-
# Time : 2019/09/03 下午 8:23 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : nestLayout02.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class WinForm(QWidget):
    def __init__(self):
        super(WinForm, self).__init__()
        self.setWindowTitle('Nested Layout Demo')
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(700, 200)
        # 全局控件，用于承载全局布局
        wwg = QWidget(self)
        # 全局布局
        wl = QHBoxLayout(wwg)
        hLayout = QHBoxLayout()
        vLayout = QVBoxLayout()
        gLayout = QGridLayout()
        fLayout = QFormLayout()

        # 往局部布局添加控件
        hLayout.addWidget(QPushButton(str(1)))
        hLayout.addWidget(QPushButton(str(2)))
        vLayout.addWidget(QPushButton(str(3)))
        vLayout.addWidget(QPushButton(str(4)))
        gLayout.addWidget(QPushButton(str(5)), 0, 0)
        gLayout.addWidget(QPushButton(str(6)), 0, 1)
        gLayout.addWidget(QPushButton(str(7)), 1, 0)
        gLayout.addWidget(QPushButton(str(8)), 1, 1)
        fLayout.addWidget(QPushButton(str(9)))
        fLayout.addWidget(QPushButton(str(10)))
        fLayout.addWidget(QPushButton(str(11)))
        fLayout.addWidget(QPushButton(str(12)))

        # 将子布局添加到全局布局中
        wl.addLayout(hLayout)
        wl.addLayout(vLayout)
        wl.addLayout(gLayout)
        wl.addLayout(fLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
