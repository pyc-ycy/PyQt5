# -*- coding:utf-8 -*-
# Time : 2019/09/03 下午 7:49 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : nestLayout01.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class WinForm(QWidget):
    def __init__(self):
        super(WinForm, self).__init__()
        self.setWindowTitle("Nested Layout Demo")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        # 全局布局（2 种）：水平
        wLayout = QHBoxLayout()
        # 局部布局（ 4 种）：水平、垂直、网格、表单
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

        # 创建四个 QWidget 类，用于放置四种子布局
        hwg = QWidget()
        vwg = QWidget()
        gwg = QWidget()
        fwg = QWidget()

        # 添加子布局
        hwg.setLayout(hLayout)
        vwg.setLayout(vLayout)
        gwg.setLayout(gLayout)
        fwg.setLayout(fLayout)
        wLayout.addWidget(hwg)
        wLayout.addWidget(vwg)
        wLayout.addWidget(gwg)
        wLayout.addWidget(fwg)

        # 添加全局布局
        self.setLayout(wLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
