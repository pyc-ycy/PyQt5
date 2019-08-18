# -*- coding:utf-8 -*-
# Time : 2019/08/18 上午 8:37 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt29_Pixmap.py 
# @software: PyCharm


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QWidget()
    lab = QLabel()
    lab.setPixmap(QPixmap("./images/python.jpg"))
    vBox = QVBoxLayout()
    vBox.addWidget(lab)
    win.setLayout(vBox)
    win.setWindowTitle("QPixmap 例子")
    win.setWindowIcon(QIcon("./images/Python2.ico"))
    win.show()
    sys.exit(app.exec_())