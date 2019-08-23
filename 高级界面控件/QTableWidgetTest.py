# -*- coding:utf-8 -*-
# Time : 2019/08/23 上午 8:44 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : QTableWidgetTest.py 
# @software: PyCharm


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget 例子")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(400, 300)
        conLayout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(6)
        tableWidget.setColumnCount(3)
        conLayout.addWidget(tableWidget)
        tableWidget.setHorizontalHeaderLabels(['姓名  ', '性别', '体重(kg)'])
        tableWidget.setVerticalHeaderLabels(['行 1', '行 2', '行 3', '行 4', '行 5', '行 6'])
        newItem = QTableWidgetItem("张三")
        tableWidget.setItem(0, 0, newItem)
        newItem = QTableWidgetItem('男')
        tableWidget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem('160')
        tableWidget.setItem(0, 2, newItem)
        self.setLayout(conLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())
