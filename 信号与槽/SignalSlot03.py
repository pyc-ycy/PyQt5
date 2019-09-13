# -*- coding:utf-8 -*-
# Time : 2019/09/13 下午 8:37 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : SignalSlot03.py
# @software: PyCharm

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class WinForm(QWidget):
    button_clicked_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('自定义信号和内置槽函数示例')
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(330, 50)
        btn = QPushButton('关闭', self)
        # 连接信号与槽函数
        btn.clicked.connect(self.btn_clicked)
        self.button_clicked_signal.connect(self.close)

    def btn_clicked(self):
        self.button_clicked_signal.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
