# -*- coding:utf-8 -*-
# Time : 2019/09/28 上午 11:07 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : photoBackGround.py 
# @software: PyCharm


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowIcon(QIcon("images/Python2.ico"))
        self.setWindowTitle("paintEvent图片背景")
        self.resize(500, 350)

    def paintEvent(self, event):
        painter = QPainter(self)
        # pixmap = QPixmap("./images/雅男.jpg")
        pixmap = QPixmap("./images/8.png")
        painter.drawPixmap(self.rect(), pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
