# -*- coding:utf-8 -*-
# Time : 2019/08/26 下午 8:04 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : QStackedWidgetTest.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class StackedWidgetDemo(QWidget):
    def __init__(self):
        super(StackedWidgetDemo, self).__init__()
        self.setGeometry(300, 50, 10, 10)
        self.setWindowTitle('QStackedWidget 例子')
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.leftList = QListWidget()
        self.leftList.insertItem(0, '联系方式')
        self.leftList.insertItem(1, '个人信息')
        self.leftList.insertItem(2, '教育程度')
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack1UI()
        self.stack2UI()
        self.stack3UI()
        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)
        hBox = QHBoxLayout(self)
        hBox.addWidget(self.leftList)
        hBox.addWidget(self.Stack)
        self.setLayout(hBox)
        self.leftList.currentRowChanged.connect(self.display)

    def stack1UI(self):
        layout = QFormLayout()
        layout.addRow("姓名", QLineEdit())
        layout.addRow("地址", QLineEdit())
        self.stack1.setLayout(layout)

    def stack2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("男"))
        sex.addWidget(QRadioButton("女"))
        layout.addRow(QLabel("性别"), sex)
        layout.addRow("生日", QLineEdit())
        self.stack2.setLayout(layout)

    def stack3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("物理"))
        layout.addWidget(QCheckBox("高数"))
        self.stack3.setLayout(layout)

    def display(self, i):
        self.Stack.setCurrentIndex(i)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = StackedWidgetDemo()
    win.show()
    sys.exit(app.exec_())
