# -*- coding:utf-8 -*-
# Time : 2019/09/21 下午 5:17 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : winStyle01.py 
# @software: PyCharm


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(400, 200)
        self.setWindowTitle("设置窗口样式示例")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        # 设置窗口无边框样式
        self.setWindowFlags(Qt.SubWindow)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(images/python.jpg);}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
