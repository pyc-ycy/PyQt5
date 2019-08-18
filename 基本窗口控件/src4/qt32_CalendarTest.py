# -*- coding:utf-8 -*-
# Time : 2019/08/18 下午 2:43 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt32_CalendarTest.py 
# @software: PyCharm


import sys
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate


class CalendarExample(QWidget):
    def __init__(self):
        super(CalendarExample, self).__init__()
        self.cal = QCalendarWidget(self)
        self.label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 350)
        self.setWindowTitle("Calendar 例子")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.cal.setMinimumDate(QDate(1980, 1, 1))
        self.cal.setMaximumDate(QDate(3000, 1, 1))
        self.cal.setGridVisible(True)
        self.cal.move(20, 20)
        self.cal.clicked[QtCore.QDate].connect(self.showDate)
        date = self.cal.selectedDate()
        self.label.setText(date.toString("yyyy-MM-dd dddd"))
        self.label.move(20, 300)

    def showDate(self, date):
        self.label.setText(date.toString("yyyy-MM-dd dddd"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CalendarExample()
    win.show()
    sys.exit(app.exec_())
