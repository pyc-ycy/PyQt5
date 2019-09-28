# -*- coding:utf-8 -*-
# Time : 2019/09/28 下午 2:17 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : unregular.py 
# @software: PyCharm


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.setWindowTitle("不规则窗口示例")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, 320, 450, QPixmap(r"./images/7.jpg"))
        painter.drawPixmap(330, 0, 320, 450, QBitmap(r"./images/7.jpg"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
