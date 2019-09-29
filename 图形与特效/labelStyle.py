# -*- coding:utf-8 -*-
# Time : 2019/09/29 下午 8:44 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : labelStyle.py 
# @software: PyCharm


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class WinForm(QWidget):
    def __init__(self):
        super(WinForm, self).__init__()
        label1 = QLabel(self)
        label1.setToolTip('这是一个文本标签')
        label1.setStyleSheet("QLabel{border-image:url(./images/python.jpg);}")
        label1.setFixedWidth(476)
        label1.setFixedHeight(259)

        btn1 = QPushButton(self)
        btn1.setObjectName('btn1')
        btn1.setMaximumSize(48, 48)
        btn1.setMinimumSize(48, 48)
        style = '''
            #btn1{
                        border-radius: 4px;
                        background-image: url('./images/add.png');
                        }
             #btn1:Pressed{
                        background-image: url('./images/addhover.png');
             }
        '''
        btn1.setStyleSheet(style)

        vBox = QVBoxLayout()
        vBox.addWidget(label1)
        vBox.addStretch()
        vBox.addWidget(btn1)
        self.setLayout(vBox)
        self.setWindowTitle("Window Demo")
        self.setWindowIcon(QIcon("./images/Python2.ico"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
