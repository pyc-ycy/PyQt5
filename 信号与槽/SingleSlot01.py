# -*- coding:utf-8 -*-
# Time : 2019/09/10 下午 8:29 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : SingleSlot01.py 
# @software: PyCharm


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

if __name__ == "__main__":
    app = QApplication([])
    widget = QWidget()
    widget.setWindowTitle('内置信号示例')
    widget.setWindowIcon(QIcon("./images/Python2.ico"))
    widget.resize(350, 150)


    def showMSG():
        QMessageBox.information(widget, "信息提示框", "OK，弹出测试信息")


    btn = QPushButton("测试按钮", widget)
    btn.clicked.connect(showMSG)
    widget.show()
    sys.exit(app.exec_())
