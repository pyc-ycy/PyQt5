# -*- coding:utf-8 -*-
# Time : 2019/08/28 下午 3:56 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : timer02.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel("<font color=red size=128><b>Hello PyQt,窗口会在 10 秒后消失！</b></font>")
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    label.show()
    QTimer.singleShot(10000, app.quit)
    sys.exit(app.exec_())