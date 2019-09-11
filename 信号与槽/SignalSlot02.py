# -*- coding:utf-8 -*-
# Time : 2019/09/11 下午 3:52 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : SignalSlot02.py 
# @software: PyCharm

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import sys


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.setWindowTitle('内置信号和自定义槽函数')
        self.resize(330, 50)
        btn = QPushButton('关闭', self)
        btn.clicked.connect(self.btn_close)

    def btn_close(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
