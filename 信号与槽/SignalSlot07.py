# -*- coding:utf-8 -*-
# Time : 2019/09/16 下午 8:21 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : SignalSlot07.py 
# @software: PyCharm


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class WinForm(QWidget):
    def __init__(self):
        super(WinForm, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.setWindowTitle("信号与槽：连接滑块 LCD")
        self.setGeometry(300, 300, 350, 150)
        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal, self)
        vBox = QVBoxLayout()
        vBox.addWidget(lcd)
        vBox.addWidget(slider)
        self.setLayout(vBox)
        slider.valueChanged.connect(lcd.display)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
