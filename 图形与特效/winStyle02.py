# -*- coding:utf-8 -*-
# Time : 2019/09/23 下午 3:33 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : winStyle02.py 
# @software: PyCharm


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        # 设置窗口标志
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet('''background-color:blue;''')

    def showMaximized(self) -> None:
        desktop = QApplication.desktop()
        rect = desktop.availableGeometry()
        self.setGeometry(rect)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.showMaximized()
    sys.exit(app.exec_())
