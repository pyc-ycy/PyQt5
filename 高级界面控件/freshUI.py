# -*- coding:utf-8 -*-
# Time : 2019/08/29 上午 11:23 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : freshUI.py 
# @software: PyCharm


import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle("实时刷新页面示例")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(400, 350)
        self.listFile = QListWidget()
        self.btnStart = QPushButton("开始")
        layout = QGridLayout()
        layout.addWidget(self.listFile, 0, 0, 1, 2)
        layout.addWidget(self.btnStart, 1, 1)
        self.btnStart.clicked.connect(self.slotAdd)
        self.setLayout(layout)

    def slotAdd(self):
        for i in range(10):
            str_n = 'File index{0}'.format(i)
            self.listFile.addItem(str_n)
            QApplication.processEvents()
            time.sleep(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())
