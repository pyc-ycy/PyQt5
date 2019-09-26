# -*- coding:utf-8 -*-
# Time : 2019/09/26 下午 5:09 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qssStyle01.py 
# @software: PyCharm

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class WindowDemo(QWidget):
    def __init__(self):
        super(WindowDemo, self).__init__()
        self.setWindowTitle('QSS Demo')
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(200, 100)
        btn1 = QPushButton(self)
        btn1.setText('按钮1')
        btn2 = QPushButton(self)
        btn2.setProperty('name', 'myBtn')
        btn2.setText('按钮2')

        vBox = QVBoxLayout()
        vBox.addWidget(btn1)
        vBox.addWidget(btn2)
        self.setLayout(vBox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WindowDemo()
    qssStyle = '''
        QPushButton[name="myBtn"]{
            background-color:red
        }
    '''
    win.setStyleSheet(qssStyle)
    win.show()
    sys.exit(app.exec_())
