# -*- coding:utf-8 -*-
# Time : 2019/08/31 下午 3:50 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : AbsolutePositionTest.py 
# @software: PyCharm


import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class TestExample(QWidget):
    def __init__(self):
        super(TestExample, self).__init__()
        self.initUI()

    def initUI(self):
        lbl1 = QLabel('欢迎', self)
        lbl1.move(15, 10)
        lbl2 = QLabel('学习', self)
        lbl2.move(35, 40)
        lbl3 = QLabel('PyQt5 !', self)
        lbl3.move(55, 70)
        self.setGeometry(300, 300, 320, 120)
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.setWindowTitle("绝对布局示例")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = TestExample()
    demo.show()
    sys.exit(app.exec_())
