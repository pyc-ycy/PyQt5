# -*- coding:utf-8 -*-
# Time : 2019/08/16 下午 3:22 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt21_QMessageBox.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MyWindow(QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__()
        self.setWindowTitle("QMessageBox 例子")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(300, 100)
        self.myButton = QPushButton(self)
        self.myButton.setText("点击弹出消息对话框")
        self.myButton.clicked.connect(self.msg)

    def msg(self):
        reply = QMessageBox.information(self, "标题", "消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        print(reply)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
