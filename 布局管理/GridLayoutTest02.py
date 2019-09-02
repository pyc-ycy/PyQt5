# -*- coding:utf-8 -*-
# Time : 2019/09/02 下午 2:28 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : GridLayoutTest02.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.initUI()

    def initUI(self):
        name = QLabel('昵称')
        hobby = QLabel('兴趣爱好')
        signature = QLabel('个性签名')

        nameEdit = QLineEdit()
        hobbyEdit = QLineEdit()
        signatureEdit = QTextEdit()
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(name, 1, 0)
        grid.addWidget(nameEdit, 1, 1)
        grid.addWidget(hobby, 2, 0)
        grid.addWidget(hobbyEdit, 2, 1)
        grid.addWidget(signature, 3, 0)
        grid.addWidget(signatureEdit, 3, 1, 5, 1)
        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.setWindowTitle('个人信息完善')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
