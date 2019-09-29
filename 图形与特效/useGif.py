# -*- coding:utf-8 -*-
# Time : 2019/09/29 下午 8:01 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : useGif.py 
# @software: PyCharm


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.label = QLabel('', self)
        self.setFixedSize(128, 128)
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)
        self.movie = QMovie("./images/loading.gif")
        self.label.setMovie(self.movie)
        self.movie.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
